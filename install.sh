#!/bin/bash
# ============================================================================
# DELTA-ATRAX-V2 - Bash Installation Script
# For Linux/macOS systems
# ============================================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# Configuration
APP_NAME="DELTA-ATRAX-V2"
APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${APP_DIR}/venv"
PYTHON_CMD=""

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

print_banner() {
    echo -e "${CYAN}"
    echo "╔══════════════════════════════════════════════════════════════════════════════╗"
    echo "║                                                                              ║"
    echo "║   ██████╗ ███████╗██╗  ████████╗ █████╗     █████╗ ████████╗██████╗  █████╗ ██╗  ██╗"
    echo "║   ██╔══██╗██╔════╝██║  ╚══██╔══╝██╔══██╗   ██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚██╗██╔╝"
    echo "║   ██║  ██║█████╗  ██║     ██║   ███████║   ███████║   ██║   ██████╔╝███████║ ╚███╔╝ "
    echo "║   ██║  ██║██╔══╝  ██║     ██║   ██╔══██║   ██╔══██║   ██║   ██╔══██╗██╔══██║ ██╔██╗ "
    echo "║   ██████╔╝███████╗███████╗██║   ██║  ██║   ██║  ██║   ██║   ██║  ██║██║  ██║██╔╝ ██╗"
    echo "║   ╚═════╝ ╚══════╝╚══════╝╚═╝   ╚═╝  ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝"
    echo "║                                                                              ║"
    echo "║                    DELTA-ATRAX-V2 - Installation Script                      ║"
    echo "║                         Author: Ian Carter Kulani, MSc                       ║"
    echo "║                              Version: 2.0.0                                  ║"
    echo "╚══════════════════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# ============================================================================
# SYSTEM DETECTION
# ============================================================================

detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
        if [ -f /etc/debian_version ]; then
            DISTRO="debian"
        elif [ -f /etc/redhat-release ]; then
            DISTRO="redhat"
        elif [ -f /etc/arch-release ]; then
            DISTRO="arch"
        elif [ -f /etc/alpine-release ]; then
            DISTRO="alpine"
        else
            DISTRO="unknown"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
        DISTRO="macos"
    else
        OS="unknown"
        DISTRO="unknown"
    fi
    
    log_info "Detected OS: ${OS} (${DISTRO})"
}

# ============================================================================
# PYTHON DETECTION
# ============================================================================

find_python() {
    log_info "Looking for Python 3.7+..."
    
    for cmd in python3.11 python3.10 python3.9 python3.8 python3.7 python3 python; do
        if command -v $cmd &> /dev/null; then
            version=$($cmd -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
            major=$(echo $version | cut -d. -f1)
            minor=$(echo $version | cut -d. -f2)
            
            if [ "$major" -ge 3 ] && [ "$minor" -ge 7 ]; then
                PYTHON_CMD=$cmd
                log_success "Found Python $version at $cmd"
                return 0
            fi
        fi
    done
    
    log_error "Python 3.7+ not found!"
    return 1
}

# ============================================================================
# SYSTEM DEPENDENCIES
# ============================================================================

install_system_deps() {
    log_info "Installing system dependencies..."
    
    case $DISTRO in
        debian)
            sudo apt-get update
            sudo apt-get install -y \
                python3 python3-pip python3-venv python3-dev \
                build-essential libssl-dev libffi-dev \
                nmap curl wget netcat-openbsd dnsutils \
                traceroute whois openssh-client \
                libxml2-dev libxslt1-dev zlib1g-dev \
                libjpeg-dev libpng-dev libfreetype6-dev \
                libopenblas-dev liblapack-dev gfortran \
                git tcpdump socat
            ;;
        redhat)
            sudo yum install -y \
                python3 python3-pip python3-devel \
                gcc openssl-devel libffi-devel \
                nmap curl wget nc bind-utils \
                traceroute whois openssh-clients \
                libxml2-devel libxslt-devel zlib-devel \
                libjpeg-turbo-devel libpng-devel freetype-devel \
                openblas-devel lapack-devel gcc-gfortran \
                git tcpdump socat
            ;;
        arch)
            sudo pacman -Sy --noconfirm \
                python python-pip python-virtualenv \
                base-devel openssl libffi \
                nmap curl wget gnu-netcat bind \
                traceroute whois openssh \
                libxml2 libxslt zlib \
                libjpeg-turbo libpng freetype2 \
                openblas lapack gcc-fortran \
                git tcpdump socat
            ;;
        alpine)
            sudo apk add --no-cache \
                python3 py3-pip python3-dev \
                gcc musl-dev openssl-dev libffi-dev \
                nmap curl wget netcat-openbsd bind-tools \
                traceroute whois openssh-client \
                libxml2-dev libxslt-dev zlib-dev \
                jpeg-dev libpng-dev freetype-dev \
                openblas-dev lapack-dev gfortran \
                git tcpdump socat
            ;;
        macos)
            if ! command -v brew &> /dev/null; then
                log_info "Installing Homebrew..."
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            fi
            
            brew update
            brew install \
                python3 \
                nmap curl wget netcat \
                bind traceroute whois \
                openssh libxml2 libxslt \
                jpeg libpng freetype \
                openblas lapack gcc \
                git tcpdump socat
            ;;
        *)
            log_warning "Unknown distribution. Please install dependencies manually."
            ;;
    esac
    
    log_success "System dependencies installed"
}

# ============================================================================
# INSTALLATION STEPS
# ============================================================================

create_venv() {
    log_info "Creating virtual environment..."
    
    if [ -d "$VENV_DIR" ]; then
        log_warning "Virtual environment already exists"
        read -p "Recreate? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm -rf "$VENV_DIR"
        else
            return 0
        fi
    fi
    
    $PYTHON_CMD -m venv "$VENV_DIR"
    log_success "Virtual environment created at $VENV_DIR"
}

install_python_deps() {
    log_info "Installing Python dependencies..."
    
    source "$VENV_DIR/bin/activate"
    pip install --upgrade pip setuptools wheel
    
    if [ -f "${APP_DIR}/requirements.txt" ]; then
        pip install -r "${APP_DIR}/requirements.txt"
    else
        log_warning "requirements.txt not found. Installing core packages..."
        pip install colorama requests psutil cryptography \
            paramiko scapy dnspython whois flask flask-socketio \
            flask-cors discord.py telethon slack-sdk \
            matplotlib numpy reportlab pillow qrcode
    fi
    
    log_success "Python dependencies installed"
}

create_directories() {
    log_info "Creating data directories..."
    
    mkdir -p "${APP_DIR}/.delta_atrax_v2"/{payloads,workspaces,scans,phishing_pages,captured_credentials,ssh_keys,keylogs,keylog_screenshots,malware,temp,logs}
    mkdir -p "${APP_DIR}/delta_atrax_reports"/{pdf_reports,charts,graphics}
    mkdir -p "${APP_DIR}/config"
    mkdir -p "${APP_DIR}/scripts"
    mkdir -p "${APP_DIR}/docs"
    mkdir -p "${APP_DIR}/backups"
    
    log_success "Directories created"
}

create_config() {
    log_info "Creating default configuration..."
    
    CONFIG_FILE="${APP_DIR}/.delta_atrax_v2/config.json"
    
    if [ ! -f "$CONFIG_FILE" ]; then
        cat > "$CONFIG_FILE" << 'EOF'
{
    "version": "2.0.0",
    "auto_start": false,
    "auto_block_enabled": false,
    "scan_timeout": 30,
    "web": {
        "enabled": true,
        "port": 5000,
        "host": "0.0.0.0"
    },
    "keylogger": {
        "enabled": false,
        "capture_clipboard": true
    }
}
EOF
        log_success "Default configuration created"
    else
        log_info "Configuration already exists"
    fi
}

create_env_file() {
    log_info "Creating .env file..."
    
    ENV_FILE="${APP_DIR}/.env"
    
    if [ ! -f "$ENV_FILE" ]; then
        cat > "$ENV_FILE" << 'EOF'
# DELTA-ATRAX-V2 Environment Configuration

# Application
DELTA_ATRAX_HOME=/app
DELTA_ATRAX_CONFIG=/app/.delta_atrax_v2
DELTA_ATRAX_LOG_LEVEL=INFO
DELTA_ATRAX_SECRET_KEY=

# Web Dashboard
DELTA_ATRAX_WEB_PORT=5000
DELTA_ATRAX_WEB_HOST=0.0.0.0

# Database
DELTA_ATRAX_DB_PATH=/app/.delta_atrax_v2/delta_atrax_v2.db

# Discord Bot
DISCORD_TOKEN=

# Telegram Bot
TELEGRAM_TOKEN=

# Slack Bot
SLACK_TOKEN=

# Email/SMTP
SMTP_SERVER=
SMTP_PORT=587
SMTP_USERNAME=
SMTP_PASSWORD=

# Redis
REDIS_PASSWORD=delta_redis_2024

# PostgreSQL
POSTGRES_USER=delta
POSTGRES_PASSWORD=delta_postgres_2024
POSTGRES_DB=delta_atrax
EOF
        log_success ".env file created"
    else
        log_info ".env file already exists"
    fi
}

create_launcher() {
    log_info "Creating launcher script..."
    
    LAUNCHER="${APP_DIR}/delta-atrax"
    
    cat > "$LAUNCHER" << EOF
#!/bin/bash
# DELTA-ATRAX-V2 Launcher

cd "\$(dirname "\${BASH_SOURCE[0]}")"
source "${VENV_DIR}/bin/activate"
python "${APP_DIR}/delta_atrax_v2.py" "\$@"
EOF
    
    chmod +x "$LAUNCHER"
    log_success "Launcher created at $LAUNCHER"
    
    # Create symlink in /usr/local/bin if root
    if [ "$EUID" -eq 0 ]; then
        ln -sf "$LAUNCHER" /usr/local/bin/delta-atrax
        log_success "Symlink created: /usr/local/bin/delta-atrax"
    fi
}

verify_installation() {
    log_info "Verifying installation..."
    
    source "$VENV_DIR/bin/activate"
    
    if python -c "import sys; sys.exit(0 if sys.version_info >= (3, 7) else 1)"; then
        log_success "Python version OK"
    else
        log_error "Python version check failed"
        return 1
    fi
    
    for pkg in colorama requests psutil; do
        if python -c "import $pkg" 2>/dev/null; then
            log_success "Package $pkg installed"
        else
            log_error "Package $pkg missing"
        fi
    done
    
    log_success "Installation verified"
}

# ============================================================================
# MAIN
# ============================================================================

main() {
    print_banner
    
    log_info "Starting installation..."
    
    detect_os
    find_python || exit 1
    
    # Ask for system deps
    read -p "Install system dependencies? (requires sudo) (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        install_system_deps
    fi
    
    create_venv
    install_python_deps
    create_directories
    create_config
    create_env_file
    create_launcher
    verify_installation
    
    echo
    log_success "=========================================="
    log_success "  DELTA-ATRAX-V2 Installation Complete!   "
    log_success "=========================================="
    echo
    echo -e "${CYAN}To run the application:${NC}"
    echo -e "  ${GREEN}./delta-atrax${NC}"
    echo -e "  or"
    echo -e "  ${GREEN}source venv/bin/activate && python delta_atrax_v2.py${NC}"
    echo
    echo -e "${CYAN}Web Dashboard:${NC} http://localhost:5000"
    echo
}

# Run
main "$@"
