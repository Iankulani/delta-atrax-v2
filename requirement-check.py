#!/usr/bin/env python3
"""
DELTA-ATRAX-V2 - Dependency Checker
====================================
Checks all required and optional dependencies for the platform.
"""

import sys
import subprocess
import importlib
from typing import Dict, List, Tuple, Optional
import platform
import shutil
import os

# Color handling
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLORS = True
except ImportError:
    COLORS = False

class Colors:
    if COLORS:
        PRIMARY = Fore.CYAN + Style.BRIGHT
        SUCCESS = Fore.GREEN + Style.BRIGHT
        WARNING = Fore.YELLOW + Style.BRIGHT
        ERROR = Fore.RED + Style.BRIGHT
        INFO = Fore.BLUE + Style.BRIGHT
        RESET = Style.RESET_ALL
    else:
        PRIMARY = SUCCESS = WARNING = ERROR = INFO = RESET = ""

# ============================================================================
# DEPENDENCY DEFINITIONS
# ============================================================================

REQUIRED_PACKAGES = {
    # Core
    'colorama': 'Color terminal output',
    'requests': 'HTTP library',
    'psutil': 'System monitoring',
    
    # Cryptography
    'cryptography': 'Cryptographic operations',
    
    # Networking
    'scapy': 'Packet manipulation',
    'dns': 'DNS resolution (dnspython)',
    'whois': 'WHOIS lookups',
    
    # SSH
    'paramiko': 'SSH client',
    
    # Web
    'flask': 'Web framework',
    'flask_socketio': 'WebSocket support',
    'flask_cors': 'CORS support',
    
    # Bot integrations
    'discord': 'Discord bot',
    'telethon': 'Telegram bot',
    'slack_sdk': 'Slack bot',
    
    # Visualization
    'matplotlib': 'Chart generation',
    'numpy': 'Numerical operations',
    
    # PDF
    'reportlab': 'PDF generation',
    
    # Database
    'sqlite3': 'SQLite database (built-in)',
    
    # Utilities
    'PIL': 'Image processing (Pillow)',
    'qrcode': 'QR code generation',
}

OPTIONAL_PACKAGES = {
    # Web scraping
    'selenium': 'Browser automation (WhatsApp)',
    'bs4': 'HTML parsing (BeautifulSoup)',
    'webdriver_manager': 'ChromeDriver management',
    
    # Document generation
    'docx': 'DOCX generation (python-docx)',
    
    # Data visualization
    'seaborn': 'Statistical visualization',
    'pandas': 'Data manipulation',
    
    # Keylogger
    'pynput': 'Keyboard monitoring',
    'pyautogui': 'Screenshot capture',
    'pyperclip': 'Clipboard access',
    
    # Google APIs
    'google.oauth2': 'Google authentication',
    'googleapiclient': 'Google API client',
    
    # URL shortening
    'pyshorteners': 'URL shortening',
    
    # Terminal formatting
    'rich': 'Rich terminal output',
    'tabulate': 'Table formatting',
}

SYSTEM_TOOLS = {
    # Networking
    'ping': 'ICMP ping utility',
    'nmap': 'Network scanner',
    'curl': 'HTTP client',
    'wget': 'File downloader',
    'nc': 'Netcat',
    'dig': 'DNS lookup',
    'traceroute': 'Network path tracing',
    
    # SSH
    'ssh': 'SSH client',
    
    # Security
    'whois': 'WHOIS client',
    'openssl': 'SSL/TLS toolkit',
    
    # Container
    'docker': 'Container platform',
}

# ============================================================================
# CHECK FUNCTIONS
# ============================================================================

def check_python_version() -> Tuple[bool, str]:
    """Check Python version compatibility."""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 7:
        return True, f"Python {version.major}.{version.minor}.{version.micro}"
    return False, f"Python {version.major}.{version.minor}.{version.micro} (requires 3.7+)"

def check_package(package_name: str) -> Tuple[bool, str]:
    """Check if a Python package is installed."""
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, '__version__', 'unknown')
        return True, version
    except ImportError:
        return False, "not installed"
    except Exception as e:
        return False, str(e)

def check_system_tool(tool_name: str) -> Tuple[bool, str]:
    """Check if a system tool is available."""
    path = shutil.which(tool_name)
    if path:
        try:
            result = subprocess.run([tool_name, '--version'], 
                                   capture_output=True, text=True, timeout=5)
            version = result.stdout.split('\n')[0][:50] if result.stdout else 'available'
        except:
            version = 'available'
        return True, version
    return False, "not found"

def check_directories() -> Tuple[bool, List[str]]:
    """Check/create required directories."""
    directories = [
        '.delta_atrax_v2',
        '.delta_atrax_v2/payloads',
        '.delta_atrax_v2/workspaces',
        '.delta_atrax_v2/scans',
        'delta_atrax_reports',
        'delta_atrax_reports/pdf_reports',
        'delta_atrax_reports/charts',
        '.delta_atrax_v2/phishing_pages',
        '.delta_atrax_v2/captured_credentials',
        '.delta_atrax_v2/ssh_keys',
        '.delta_atrax_v2/keylogs',
        '.delta_atrax_v2/keylog_screenshots',
        '.delta_atrax_v2/malware',
        '.delta_atrax_v2/temp',
    ]
    
    created = []
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            created.append(directory)
        except Exception as e:
            return False, [f"Failed to create {directory}: {e}"]
    
    return True, created

# ============================================================================
# MAIN CHECKER
# ============================================================================

def main():
    print(f"\n{Colors.PRIMARY}{'='*70}{Colors.RESET}")
    print(f"{Colors.PRIMARY}🦀 DELTA-ATRAX-V2 - Dependency Checker{Colors.RESET}")
    print(f"{Colors.PRIMARY}{'='*70}{Colors.RESET}\n")
    
    # System info
    print(f"{Colors.INFO}📋 System Information:{Colors.RESET}")
    print(f"   Platform: {platform.system()} {platform.release()}")
    print(f"   Machine: {platform.machine()}")
    print(f"   Processor: {platform.processor()}")
    
    # Python version
    py_ok, py_version = check_python_version()
    status = f"{Colors.SUCCESS}✅{Colors.RESET}" if py_ok else f"{Colors.ERROR}❌{Colors.RESET}"
    print(f"\n{Colors.INFO}🐍 Python Version:{Colors.RESET}")
    print(f"   {status} {py_version}")
    
    if not py_ok:
        print(f"\n{Colors.ERROR}❌ Python 3.7+ is required!{Colors.RESET}")
        sys.exit(1)
    
    # Required packages
    print(f"\n{Colors.INFO}📦 Required Python Packages:{Colors.RESET}")
    required_missing = []
    for package, description in REQUIRED_PACKAGES.items():
        installed, version = check_package(package)
        status = f"{Colors.SUCCESS}✅{Colors.RESET}" if installed else f"{Colors.ERROR}❌{Colors.RESET}"
        print(f"   {status} {package:<20} {version:<15} # {description}")
        if not installed:
            required_missing.append(package)
    
    # Optional packages
    print(f"\n{Colors.INFO}📦 Optional Python Packages:{Colors.RESET}")
    optional_missing = []
    for package, description in OPTIONAL_PACKAGES.items():
        installed, version = check_package(package)
        status = f"{Colors.SUCCESS}✅{Colors.RESET}" if installed else f"{Colors.WARNING}⚠️{Colors.RESET}"
        print(f"   {status} {package:<20} {version:<15} # {description}")
        if not installed:
            optional_missing.append(package)
    
    # System tools
    print(f"\n{Colors.INFO}🔧 System Tools:{Colors.RESET}")
    tools_missing = []
    for tool, description in SYSTEM_TOOLS.items():
        available, version = check_system_tool(tool)
        status = f"{Colors.SUCCESS}✅{Colors.RESET}" if available else f"{Colors.WARNING}⚠️{Colors.RESET}"
        print(f"   {status} {tool:<20} {version:<15} # {description}")
        if not available:
            tools_missing.append(tool)
    
    # Directories
    print(f"\n{Colors.INFO}📁 Required Directories:{Colors.RESET}")
    dirs_ok, dirs_result = check_directories()
    if dirs_ok:
        print(f"   {Colors.SUCCESS}✅ All {len(dirs_result)} directories ready{Colors.RESET}")
    else:
        for error in dirs_result:
            print(f"   {Colors.ERROR}❌ {error}{Colors.RESET}")
    
    # Summary
    print(f"\n{Colors.PRIMARY}{'='*70}{Colors.RESET}")
    print(f"{Colors.PRIMARY}📊 SUMMARY{Colors.RESET}")
    print(f"{Colors.PRIMARY}{'='*70}{Colors.RESET}")
    
    if required_missing:
        print(f"\n{Colors.ERROR}❌ Missing required packages: {len(required_missing)}{Colors.RESET}")
        print(f"   Install with: pip install {' '.join(required_missing)}")
        print(f"   Or: pip install -r requirements.txt")
    else:
        print(f"\n{Colors.SUCCESS}✅ All required packages installed!{Colors.RESET}")
    
    if optional_missing:
        print(f"\n{Colors.WARNING}⚠️ Missing optional packages: {len(optional_missing)}{Colors.RESET}")
        print(f"   Some features will be disabled.")
    
    if tools_missing:
        print(f"\n{Colors.WARNING}⚠️ Missing system tools: {', '.join(tools_missing)}{Colors.RESET}")
        print(f"   Install with your package manager.")
    
    # Exit code
    if required_missing:
        print(f"\n{Colors.ERROR}❌ Please install missing required packages.{Colors.RESET}\n")
        sys.exit(1)
    else:
        print(f"\n{Colors.SUCCESS}✅ DELTA-ATRAX-V2 is ready to run!{Colors.RESET}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
