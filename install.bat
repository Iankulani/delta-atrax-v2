@echo off
REM ============================================================================
REM DELTA-ATRAX-V2 - Windows Batch Installation Script
REM ============================================================================

setlocal EnableDelayedExpansion

REM Colors (limited in batch)
set "GREEN=[92m"
set "RED=[91m"
set "YELLOW=[93m"
set "BLUE=[94m"
set "CYAN=[96m"
set "NC=[0m"

REM Configuration
set "APP_NAME=DELTA-ATRAX-V2"
set "APP_DIR=%~dp0"
set "VENV_DIR=%APP_DIR%venv"
set "PYTHON_CMD="

REM ============================================================================
REM BANNER
REM ============================================================================

:print_banner
echo.
echo %CYAN%============================================================================%NC%
echo %CYAN%                                                                           %NC%
echo %CYAN%   DELTA-ATRAX-V2 - Installation Script                                    %NC%
echo %CYAN%   Ultimate Cybersecurity Platform                                         %NC%
echo %CYAN%   Author: Ian Carter Kulani, MSc                                         %NC%
echo %CYAN%   Version: 2.0.0                                                          %NC%
echo %CYAN%                                                                           %NC%
echo %CYAN%============================================================================%NC%
echo.
exit /b 0

REM ============================================================================
REM LOGGING
REM ============================================================================

:log_info
echo %BLUE%[INFO]%NC% %~1
exit /b 0

:log_success
echo %GREEN%[SUCCESS]%NC% %~1
exit /b 0

:log_warning
echo %YELLOW%[WARNING]%NC% %~1
exit /b 0

:log_error
echo %RED%[ERROR]%NC% %~1
exit /b 0

REM ============================================================================
REM FIND PYTHON
REM ============================================================================

:find_python
call :log_info "Looking for Python 3.7+..."

REM Try py launcher first
py -3 --version >nul 2>&1
if %errorlevel% equ 0 (
    set "PYTHON_CMD=py -3"
    for /f "tokens=2" %%i in ('py -3 --version 2^>^&1') do set "PY_VERSION=%%i"
    call :log_success "Found Python !PY_VERSION! via py launcher"
    exit /b 0
)

REM Try python3
python3 --version >nul 2>&1
if %errorlevel% equ 0 (
    set "PYTHON_CMD=python3"
    for /f "tokens=2" %%i in ('python3 --version 2^>^&1') do set "PY_VERSION=%%i"
    call :log_success "Found Python !PY_VERSION!"
    exit /b 0
)

REM Try python
python --version >nul 2>&1
if %errorlevel% equ 0 (
    set "PYTHON_CMD=python"
    for /f "tokens=2" %%i in ('python --version 2^>^&1') do set "PY_VERSION=%%i"
    call :log_success "Found Python !PY_VERSION!"
    exit /b 0
)

call :log_error "Python 3.7+ not found!"
call :log_info "Please install Python from https://www.python.org/downloads/"
call :log_info "Make sure to check 'Add Python to PATH' during installation."
exit /b 1

REM ============================================================================
REM CHECK ADMIN
REM ============================================================================

:check_admin
net session >nul 2>&1
if %errorlevel% equ 0 (
    set "IS_ADMIN=1"
    call :log_success "Running with administrator privileges"
) else (
    set "IS_ADMIN=0"
    call :log_warning "Not running as administrator. Some features may be limited."
)
exit /b 0

REM ============================================================================
REM INSTALL SYSTEM DEPENDENCIES
REM ============================================================================

:install_system_deps
call :log_info "Installing system dependencies..."

REM Check for Chocolatey
where choco >nul 2>&1
if %errorlevel% neq 0 (
    call :log_warning "Chocolatey not found. Installing..."
    powershell -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
    
    if !errorlevel! neq 0 (
        call :log_error "Failed to install Chocolatey"
        exit /b 1
    )
)

REM Install tools via Chocolatey
call :log_info "Installing networking tools..."
choco install -y nmap curl wget netcat wireshark 2>nul

call :log_info "Installing development tools..."
choco install -y git vcredist-all 2>nul

call :log_success "System dependencies installed"
exit /b 0

REM ============================================================================
REM CREATE VENV
REM ============================================================================

:create_venv
call :log_info "Creating virtual environment..."

if exist "%VENV_DIR%" (
    call :log_warning "Virtual environment already exists"
    set /p RECREATE="Recreate? (y/n): "
    if /i "!RECREATE!"=="y" (
        rmdir /s /q "%VENV_DIR%"
    ) else (
        exit /b 0
    )
)

%PYTHON_CMD% -m venv "%VENV_DIR%"
if %errorlevel% neq 0 (
    call :log_error "Failed to create virtual environment"
    exit /b 1
)

call :log_success "Virtual environment created"
exit /b 0

REM ============================================================================
REM INSTALL PYTHON DEPS
REM ============================================================================

:install_python_deps
call :log_info "Installing Python dependencies..."

call "%VENV_DIR%\Scripts\activate.bat"

python -m pip install --upgrade pip setuptools wheel

if exist "%APP_DIR%requirements.txt" (
    pip install -r "%APP_DIR%requirements.txt"
) else (
    call :log_warning "requirements.txt not found. Installing core packages..."
    pip install colorama requests psutil cryptography paramiko scapy dnspython whois flask flask-socketio flask-cors discord.py telethon slack-sdk matplotlib numpy reportlab pillow qrcode
)

if %errorlevel% neq 0 (
    call :log_error "Failed to install Python dependencies"
    exit /b 1
)

call :log_success "Python dependencies installed"
exit /b 0

REM ============================================================================
REM CREATE DIRECTORIES
REM ============================================================================

:create_directories
call :log_info "Creating data directories..."

mkdir "%APP_DIR%.delta_atrax_v2" 2>nul
mkdir "%APP_DIR%.delta_atrax_v2\payloads" 2>nul
mkdir "%APP_DIR%.delta_atrax_v2\workspaces" 2>nul
mkdir "%APP_DIR%.delta_atrax_v2\scans" 2>nul
mkdir "%APP_DIR%.delta_atrax_v2\phishing_pages" 2>nul
mkdir "%APP_DIR%.delta_atrax_v2\captured_credentials" 2>nul
mkdir "%APP_DIR%.delta_atrax_v2\ssh_keys" 2>nul
mkdir "%APP_DIR%.delta_atrax_v2\keylogs" 2>nul
mkdir "%APP_DIR%.delta_atrax_v2\keylog_screenshots" 2>nul
mkdir "%APP_DIR%.delta_atrax_v2\malware" 2>nul
mkdir "%APP_DIR%.delta_atrax_v2\temp" 2>nul
mkdir "%APP_DIR%.delta_atrax_v2\logs" 2>nul
mkdir "%APP_DIR%delta_atrax_reports" 2>nul
mkdir "%APP_DIR%delta_atrax_reports\pdf_reports" 2>nul
mkdir "%APP_DIR%delta_atrax_reports\charts" 2>nul
mkdir "%APP_DIR%config" 2>nul
mkdir "%APP_DIR%scripts" 2>nul
mkdir "%APP_DIR%docs" 2>nul
mkdir "%APP_DIR%backups" 2>nul

call :log_success "Directories created"
exit /b 0

REM ============================================================================
REM CREATE LAUNCHER
REM ============================================================================

:create_launcher
call :log_info "Creating launcher script..."

(
echo @echo off
echo cd /d "%%~dp0"
echo call "%VENV_DIR%\Scripts\activate.bat"
echo python "%APP_DIR%delta_atrax_v2.py" %%*
) > "%APP_DIR%delta-atrax.bat"

call :log_success "Launcher created: delta-atrax.bat"
exit /b 0

REM ============================================================================
REM MAIN
REM ============================================================================

:main
call :print_banner

call :log_info "Starting installation..."
echo.

call :find_python
if %errorlevel% neq 0 exit /b 1

call :check_admin

set /p INSTALL_DEPS="Install system dependencies? (requires admin) (y/n): "
if /i "!INSTALL_DEPS!"=="y" (
    call :install_system_deps
)

call :create_venv
if %errorlevel% neq 0 exit /b 1

call :install_python_deps
if %errorlevel% neq 0 exit /b 1

call :create_directories
call :create_launcher

echo.
call :log_success "=========================================="
call :log_success "  DELTA-ATRAX-V2 Installation Complete!   "
call :log_success "=========================================="
echo.
echo %CYAN%To run the application:%NC%
echo   %GREEN%delta-atrax.bat%NC%
echo   or
echo   %GREEN%venv\Scripts\activate && python delta_atrax_v2.py%NC%
echo.
echo %CYAN%Web Dashboard:%NC% http://localhost:5000
echo.

pause
exit /b 0

REM Run main
call :main
