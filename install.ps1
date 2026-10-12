# ============================================================================
# DELTA-ATRAX-V2 - PowerShell Installation Script
# ============================================================================

#Requires -Version 5.1

[CmdletBinding()]
param(
    [switch]$SkipSystemDeps,
    [switch]$SkipVenv,
    [switch]$Force,
    [string]$InstallPath = $PSScriptRoot
)

# ============================================================================
# CONFIGURATION
# ============================================================================

$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"

$AppName = "DELTA-ATRAX-V2"
$AppVersion = "2.0.0"
$AppDir = $InstallPath
$VenvDir = Join-Path $AppDir "venv"
$PythonCmd = $null

# Colors
function Write-ColorOutput {
    param(
        [string]$Message,
        [string]$Color = "White"
    )
    Write-Host $Message -ForegroundColor $Color
}

function Write-Info { Write-ColorOutput "[INFO] $args" "Blue" }
function Write-Success { Write-ColorOutput "[SUCCESS] $args" "Green" }
function Write-Warning { Write-ColorOutput "[WARNING] $args" "Yellow" }
function Write-Error { Write-ColorOutput "[ERROR] $args" "Red" }

# ============================================================================
# BANNER
# ============================================================================

function Show-Banner {
    Write-Host ""
    Write-Host @"
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██████╗ ███████╗██╗  ████████╗ █████╗     █████╗ ████████╗██████╗  █████╗ ██╗  ██╗
║   ██╔══██╗██╔════╝██║  ╚══██╔══╝██╔══██╗   ██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚██╗██╔╝
║   ██║  ██║█████╗  ██║     ██║   ███████║   ███████║   ██║   ██████╔╝███████║ ╚███╔╝ 
║   ██║  ██║██╔══╝  ██║     ██║   ██╔══██║   ██╔══██║   ██║   ██╔══██╗██╔══██║ ██╔██╗ 
║   ██████╔╝███████╗███████╗██║   ██║  ██║   ██║  ██║   ██║   ██║  ██║██║  ██║██╔╝ ██╗
║   ╚═════╝ ╚══════╝╚══════╝╚═╝   ╚═╝  ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
║                                                                              ║
║                    DELTA-ATRAX-V2 - PowerShell Installer                     ║
║                         Author: Ian Carter Kulani, MSc                       ║
║                              Version: $AppVersion                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝
"@ -ForegroundColor Cyan
    Write-Host ""
}

# ============================================================================
# SYSTEM DETECTION
# ============================================================================

function Get-SystemInfo {
    Write-Info "Detecting system information..."
    
    $os = Get-CimInstance Win32_OperatingSystem
    $computer = Get-CimInstance Win32_ComputerSystem
    
    $info = @{
        OS = $os.Caption
        Version = $os.Version
        Architecture = $os.OSArchitecture
        ComputerName = $computer.Name
        TotalMemory = [math]::Round($computer.TotalPhysicalMemory / 1GB, 2)
        ProcessorCount = $computer.NumberOfLogicalProcessors
    }
    
    Write-Host "  OS: $($info.OS) ($($info.Architecture))" -ForegroundColor Gray
    Write-Host "  Version: $($info.Version)" -ForegroundColor Gray
    Write-Host "  Computer: $($info.ComputerName)" -ForegroundColor Gray
    Write-Host "  Memory: $($info.TotalMemory) GB" -ForegroundColor Gray
    Write-Host "  CPUs: $($info.ProcessorCount)" -ForegroundColor Gray
    
    return $info
}

function Test-Administrator {
    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

# ============================================================================
# PYTHON DETECTION
# ============================================================================

function Find-Python {
    Write-Info "Looking for Python 3.7+..."
    
    $pythonPaths = @(
        "py -3",
        "python3",
        "python",
        "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe",
        "$env:LOCALAPPDATA\Programs\Python\Python310\python.exe",
        "$env:LOCALAPPDATA\Programs\Python\Python39\python.exe",
        "$env:LOCALAPPDATA\Programs\Python\Python38\python.exe",
        "C:\Python311\python.exe",
        "C:\Python310\python.exe",
        "C:\Python39\python.exe",
        "C:\Python38\python.exe"
    )
    
    foreach ($path in $pythonPaths) {
        try {
            $version = & cmd /c "$path --version 2>&1"
            if ($version -match "Python (\d+)\.(\d+)\.(\d+)") {
                $major = [int]$Matches[1]
                $minor = [int]$Matches[2]
                
                if ($major -ge 3 -and $minor -ge 7) {
                    $script:PythonCmd = $path
                    Write-Success "Found $version at $path"
                    return $true
                }
            }
        }
        catch {
            continue
        }
    }
    
    Write-Error "Python 3.7+ not found!"
    Write-Info "Install from: https://www.python.org/downloads/"
    return $false
}

# ============================================================================
# CHOCOLATEY
# ============================================================================

function Install-Chocolatey {
    Write-Info "Checking for Chocolatey..."
    
    if (Get-Command choco -ErrorAction SilentlyContinue) {
        Write-Success "Chocolatey already installed"
        return $true
    }
    
    Write-Info "Installing Chocolatey..."
    
    try {
        Set-ExecutionPolicy Bypass -Scope Process -Force
        [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
        Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
        
        # Refresh PATH
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
        
        Write-Success "Chocolatey installed"
        return $true
    }
    catch {
        Write-Error "Failed to install Chocolatey: $_"
        return $false
    }
}

# ============================================================================
# SYSTEM DEPENDENCIES
# ============================================================================

function Install-SystemDependencies {
    Write-Info "Installing system dependencies..."
    
    if (-not (Install-Chocolatey)) {
        Write-Warning "Skipping system dependencies"
        return
    }
    
    $packages = @(
        "nmap",
        "curl",
        "wget",
        "netcat",
        "git",
        "vcredist-all"
    )
    
    foreach ($package in $packages) {
        Write-Info "Installing $package..."
        try {
            choco install $package -y --no-progress 2>&1 | Out-Null
            Write-Success "Installed $package"
        }
        catch {
            Write-Warning "Failed to install $package"
        }
    }
    
    Write-Success "System dependencies installed"
}

# ============================================================================
# VIRTUAL ENVIRONMENT
# ============================================================================

function New-VirtualEnvironment {
    Write-Info "Creating virtual environment..."
    
    if (Test-Path $VenvDir) {
        if ($Force) {
            Write-Info "Removing existing virtual environment..."
            Remove-Item -Path $VenvDir -Recurse -Force
        }
        else {
            Write-Warning "Virtual environment already exists"
            $response = Read-Host "Recreate? (y/n)"
            if ($response -eq "y") {
                Remove-Item -Path $VenvDir -Recurse -Force
            }
            else {
                return $true
            }
        }
    }
    
    try {
        & cmd /c "$PythonCmd -m venv `"$VenvDir`""
        Write-Success "Virtual environment created"
        return $true
    }
    catch {
        Write-Error "Failed to create virtual environment: $_"
        return $false
    }
}

# ============================================================================
# PYTHON DEPENDENCIES
# ============================================================================

function Install-PythonDependencies {
    Write-Info "Installing Python dependencies..."
    
    $pipPath = Join-Path $VenvDir "Scripts\pip.exe"
    
    if (-not (Test-Path $pipPath)) {
        Write-Error "pip not found in virtual environment"
        return $false
    }
    
    try {
        # Upgrade pip
        & $pipPath install --upgrade pip setuptools wheel 2>&1 | Out-Null
        
        $requirementsFile = Join-Path $AppDir "requirements.txt"
        
        if (Test-Path $requirementsFile) {
            Write-Info "Installing from requirements.txt..."
            & $pipPath install -r $requirementsFile
        }
        else {
            Write-Warning "requirements.txt not found. Installing core packages..."
            $corePackages = @(
                "colorama",
                "requests",
                "psutil",
                "cryptography",
                "paramiko",
                "scapy",
                "dnspython",
                "whois",
                "flask",
                "flask-socketio",
                "flask-cors",
                "discord.py",
                "telethon",
                "slack-sdk",
                "matplotlib",
                "numpy",
                "reportlab",
                "pillow",
                "qrcode"
            )
            & $pipPath install $corePackages
        }
        
        Write-Success "Python dependencies installed"
        return $true
    }
    catch {
        Write-Error "Failed to install Python dependencies: $_"
        return $false
    }
}

# ============================================================================
# DIRECTORIES
# ============================================================================

function New-DataDirectories {
    Write-Info "Creating data directories..."
    
    $directories = @(
        ".delta_atrax_v2",
        ".delta_atrax_v2\payloads",
        ".delta_atrax_v2\workspaces",
        ".delta_atrax_v2\scans",
        ".delta_atrax_v2\phishing_pages",
        ".delta_atrax_v2\captured_credentials",
        ".delta_atrax_v2\ssh_keys",
        ".delta_atrax_v2\keylogs",
        ".delta_atrax_v2\keylog_screenshots",
        ".delta_atrax_v2\malware",
        ".delta_atrax_v2\temp",
        ".delta_atrax_v2\logs",
        "delta_atrax_reports",
        "delta_atrax_reports\pdf_reports",
        "delta_atrax_reports\charts",
        "delta_atrax_reports\graphics",
        "config",
        "scripts",
        "docs",
        "backups"
    )
    
    foreach ($dir in $directories) {
        $fullPath = Join-Path $AppDir $dir
        if (-not (Test-Path $fullPath)) {
            New-Item -ItemType Directory -Path $fullPath -Force | Out-Null
        }
    }
    
    Write-Success "Directories created"
}

# ============================================================================
# CONFIGURATION
# ============================================================================

function New-Configuration {
    Write-Info "Creating default configuration..."
    
    $configDir = Join-Path $AppDir ".delta_atrax_v2"
    $configFile = Join-Path $configDir "config.json"
    
    if (-not (Test-Path $configFile)) {
        $config = @{
            version = $AppVersion
            auto_start = $false
            auto_block_enabled = $false
            scan_timeout = 30
            web = @{
                enabled = $true
                port = 5000
                host = "0.0.0.0"
            }
            keylogger = @{
                enabled = $false
                capture_clipboard = $true
            }
        }
        
        $config | ConvertTo-Json -Depth 10 | Set-Content -Path $configFile -Encoding UTF8
        Write-Success "Configuration created"
    }
    else {
        Write-Info "Configuration already exists"
    }
    
    # Create .env file
    $envFile = Join-Path $AppDir ".env"
    if (-not (Test-Path $envFile)) {
        $envContent = @"
# DELTA-ATRAX-V2 Environment Configuration

# Application
DELTA_ATRAX_HOME=$AppDir
DELTA_ATRAX_CONFIG=$configDir
DELTA_ATRAX_LOG_LEVEL=INFO

# Web Dashboard
DELTA_ATRAX_WEB_PORT=5000
DELTA_ATRAX_WEB_HOST=0.0.0.0

# Bot Tokens (Optional)
DISCORD_TOKEN=
TELEGRAM_TOKEN=
SLACK_TOKEN=

# Email/SMTP (Optional)
SMTP_SERVER=
SMTP_PORT=587
SMTP_USERNAME=
SMTP_PASSWORD=
"@
        Set-Content -Path $envFile -Value $envContent -Encoding UTF8
        Write-Success ".env file created"
    }
}

# ============================================================================
# LAUNCHER
# ============================================================================

function New-Launcher {
    Write-Info "Creating launcher script..."
    
    $launcherPath = Join-Path $AppDir "delta-atrax.ps1"
    
    $launcherContent = @"
# DELTA-ATRAX-V2 Launcher
Set-Location "`$PSScriptRoot"
& "`$PSScriptRoot\venv\Scripts\Activate.ps1"
python "`$PSScriptRoot\delta_atrax_v2.py" @args
"@
    
    Set-Content -Path $launcherPath -Value $launcherContent -Encoding UTF8
    Write-Success "PowerShell launcher created: delta-atrax.ps1"
    
    # Create batch launcher too
    $batchLauncher = Join-Path $AppDir "delta-atrax.bat"
    $batchContent = @"
@echo off
cd /d "%~dp0"
call venv\Scripts\activate.bat
python delta_atrax_v2.py %*
"@
    Set-Content -Path $batchLauncher -Value $batchContent -Encoding ASCII
    Write-Success "Batch launcher created: delta-atrax.bat"
}

# ============================================================================
# VERIFICATION
# ============================================================================

function Test-Installation {
    Write-Info "Verifying installation..."
    
    $pythonPath = Join-Path $VenvDir "Scripts\python.exe"
    
    if (-not (Test-Path $pythonPath)) {
        Write-Error "Python not found in virtual environment"
        return $false
    }
    
    # Check Python version
    $version = & $pythonPath --version
    Write-Success "Python: $version"
    
    # Check core packages
    $packages = @("colorama", "requests", "psutil", "flask")
    foreach ($pkg in $packages) {
        try {
            & $pythonPath -c "import $pkg" 2>&1 | Out-Null
            Write-Success "Package $pkg: OK"
        }
        catch {
            Write-Warning "Package $pkg: Missing"
        }
    }
    
    return $true
}

# ============================================================================
# MAIN
# ============================================================================

function Main {
    Show-Banner
    
    Write-Info "Starting installation..."
    Write-Host ""
    
    # System info
    $systemInfo = Get-SystemInfo
    Write-Host ""
    
    # Check admin
    if (Test-Administrator) {
        Write-Success "Running with administrator privileges"
    }
    else {
        Write-Warning "Not running as administrator. Some features may be limited."
    }
    Write-Host ""
    
    # Find Python
    if (-not (Find-Python)) {
        exit 1
    }
    Write-Host ""
    
    # Install system dependencies
    if (-not $SkipSystemDeps) {
        $response = Read-Host "Install system dependencies? (requires admin) (y/n)"
        if ($response -eq "y") {
            Install-SystemDependencies
        }
    }
    Write-Host ""
    
    # Create virtual environment
    if (-not $SkipVenv) {
        if (-not (New-VirtualEnvironment)) {
            exit 1
        }
    }
    Write-Host ""
    
    # Install Python dependencies
    if (-not (Install-PythonDependencies)) {
        exit 1
    }
    Write-Host ""
    
    # Create directories
    New-DataDirectories
    Write-Host ""
    
    # Create configuration
    New-Configuration
    Write-Host ""
    
    # Create launcher
    New-Launcher
    Write-Host ""
    
    # Verify
    Test-Installation
    Write-Host ""
    
    Write-Host "==========================================" -ForegroundColor Green
    Write-Host "  DELTA-ATRAX-V2 Installation Complete!   " -ForegroundColor Green
    Write-Host "==========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "To run the application:" -ForegroundColor Cyan
    Write-Host "  .\delta-atrax.ps1" -ForegroundColor Green
    Write-Host "  or" -ForegroundColor Gray
    Write-Host "  .\delta-atrax.bat" -ForegroundColor Green
    Write-Host ""
    Write-Host "Web Dashboard: http://localhost:5000" -ForegroundColor Cyan
    Write-Host ""
}

# Run
Main
