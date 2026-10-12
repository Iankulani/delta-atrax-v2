# ============================================================================
# DELTA-ATRAX-V2 - Dockerfile
# Multi-stage build with Alpine Linux
# ============================================================================

# ==================== STAGE 1: BUILDER ====================
FROM python:3.11-alpine AS builder

LABEL maintainer="Ian Carter Kulani, MSc"
LABEL description="DELTA-ATRAX-V2 - Ultimate Cybersecurity Platform"
LABEL version="2.0.0"

# Install build dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    linux-headers \
    libffi-dev \
    openssl-dev \
    cargo \
    rust \
    make \
    cmake \
    git \
    py3-pip \
    python3-dev \
    libxml2-dev \
    libxslt-dev \
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    libpng-dev \
    openblas-dev \
    lapack-dev \
    gfortran \
    libjpeg-turbo-dev \
    tiff-dev \
    lcms2-dev \
    tk-dev \
    tcl-dev

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip and install wheel
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Copy requirements first for better caching
COPY requirements.txt /tmp/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# ==================== STAGE 2: RUNTIME ====================
FROM python:3.11-alpine AS runtime

LABEL maintainer="Ian Carter Kulani, MSc"
LABEL description="DELTA-ATRAX-V2 - Ultimate Cybersecurity Platform"
LABEL version="2.0.0"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app \
    PATH="/opt/venv/bin:$PATH" \
    DELTA_ATRAX_HOME=/app \
    DELTA_ATRAX_CONFIG=/app/.delta_atrax_v2

# Install runtime dependencies
RUN apk add --no-cache \
    # Networking tools
    iputils \
    nmap \
    nmap-scripts \
    curl \
    wget \
    netcat-openbsd \
    bind-tools \
    traceroute \
    mtr \
    whois \
    openssl \
    openssh-client \
    tcpdump \
    socat \
    # System utilities
    bash \
    coreutils \
    findutils \
    grep \
    sed \
    gawk \
    procps \
    htop \
    # Python runtime
    python3 \
    py3-pip \
    # Libraries for matplotlib
    freetype \
    libpng \
    openblas \
    libjpeg-turbo \
    tiff \
    lcms2 \
    tk \
    # Additional
    ca-certificates \
    tzdata \
    && rm -rf /var/cache/apk/*

# Set timezone
ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Create app directory
WORKDIR /app

# Create non-root user
RUN addgroup -g 1000 delta && \
    adduser -u 1000 -G delta -s /bin/bash -D delta

# Copy application files
COPY delta_atrax_v2.py /app/
COPY requirements.txt /app/
COPY requirement-check.py /app/

# Create necessary directories
RUN mkdir -p /app/.delta_atrax_v2/{payloads,workspaces,scans,phishing_pages,captured_credentials,ssh_keys,keylogs,keylog_screenshots,malware,temp,logs} \
    /app/delta_atrax_reports/{pdf_reports,charts,graphics} \
    /app/scripts \
    /app/docs

# Copy scripts if they exist
COPY scripts/ /app/scripts/ 2>/dev/null || true

# Create entrypoint script
RUN echo '#!/bin/bash\n\
set -e\n\
\n\
echo "🦀 Starting DELTA-ATRAX-V2..."\n\
echo "================================"\n\
\n\
# Check dependencies\n\
python3 /app/requirement-check.py || true\n\
\n\
# Run the application\n\
exec python3 /app/delta_atrax_v2.py "$@"\n\
' > /app/entrypoint.sh && chmod +x /app/entrypoint.sh

# Set ownership
RUN chown -R delta:delta /app

# Switch to non-root user
USER delta

# Expose ports
# 5000 - Web Dashboard
# 8080 - Phishing Server
# 4444 - C2 Callback
# 8081 - API Server
EXPOSE 5000 8080 4444 8081

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python3 -c "import sys; sys.exit(0)" || exit 1

# Volume for persistent data
VOLUME ["/app/.delta_atrax_v2", "/app/delta_atrax_reports"]

# Default command
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["--interactive"]
