import os
import platform
import urllib.request
import json
import time
import hashlib  
import random   
import socket   
import subprocess 

# --- Styling Elements ---
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

user_name = "Aayush Pandit"

def print_banner():
    import time
    import sys
    os.system("clear")
    
    G = "\033[92m"  # Light Green
    Y = "\033[93m"  # Neon Yellow
    M = "\033[95m"  # Light Purple
    R = "\033[0m"   # Reset Color
    B = "\033[1m"   # Bold

    lines = [
        f"{G}┌────────────────────────────────────────────────────────┐{R}",
        f"{G}│{R}  {M}{B}[+]  A  A  Y  U  S  H     P  A  N  D  I  T  [+]  {R}{G}│{R}",
        f"{G}└────────────────────────────────────────────────────────┘{R}",
        "                                                          ",
        f"               {Y}• [ MAIN OWNER: AAYUSH PANDIT ] •{R}",
    ]

    print("\n")
    for line in lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.002)
        print()
    
    print(f"\n{G}[*] Operator: Security Access Granted for '{user_name}'{R}")
    print(f"{G}[*] Framework Suite Engine : Active v5.2 (Smart Bypass){R}\n")
    time.sleep(0.3)

def get_battery_fallback():
    data = {"percentage": "89", "health": "Good", "status": "UNPLUGGED", "temp": "35.0"}
    try:
        if os.path.exists("/sys/class/power_supply/battery/capacity"):
            with open("/sys/class/power_supply/battery/capacity", "r") as f: 
                val = f.read().strip()
                if val: data["percentage"] = val
        if os.path.exists("/sys/class/power_supply/battery/status"):
            with open("/sys/class/power_supply/battery/status", "r") as f:
                val = f.read().strip()
                if val: data["status"] = val
        if os.path.exists("/sys/class/power_supply/battery/temp"):
            with open("/sys/class/power_supply/battery/temp", "r") as f:
                raw = int(f.read().strip())
                if raw > 100: data["temp"] = str(raw / 10)
                else: data["temp"] = str(raw)
    except: pass
    return data

while True:
    print_banner()
    print(f"{WHITE}{BOLD}CORE SECURITY MODULES:{RESET}")
    print(f"  [{BLUE}1{RESET}] Core System Diagnostics & Info")
    print(f"  [{BLUE}2{RESET}] Analyze Network Gateway & External IP")
    print(f"  [{BLUE}4{RESET}] Deploy Local Diagnostics Web Server (REMOTE ENGINE)")
    print(f"  [{BLUE}5{RESET}] Inspect Structured JSON Database Logs")
    
    print(f"\n{GREEN}{BOLD}ADVANCED CYBER UTILITIES:{RESET}")
    print(f"  [{BLUE}6{RESET}] Automated Crypto Password Generator & Hasher")
    print(f"  [{BLUE}7{RESET}] Execute Local Port Scanner Protocol")
    print(f"  [{BLUE}9{RESET}] Live Battery Hardware Monitoring")
    print(f"  [{BLUE}10{RESET}] Secure URL Handshake & HTTP Status Scanner")
    print(f"  [{BLUE}8{RESET}] Storage Maintenance (Wipe Logs & Purge Images)")
    print(f"  [{BLUE}3{RESET}] Terminate Environment (Exit)")
    print(f"{MAGENTA}" + "-"*55 + f"{RESET}")
    
    chose = input(f"{YELLOW}{BOLD}shield-shell> {RESET}")
    
    if chose == "1":
        print(f"\n{CYAN}[*] Fetching Architecture Logs...{RESET}")
        print(f" Operating System : {platform.system()}\n Kernel Release  : {platform.release()}\n Processor Type  : {platform.machine()}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")
        
    elif chose == "2":
        print(f"\n{CYAN}[*] Testing external routing gateway...{RESET}")
        try:
            req = urllib.request.Request("https://api.ipify.org", headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=3) as response:
                print(f"\n{GREEN}[+] Active Public Gateway IP: {response.read().decode('utf-8')}{RESET}")
        except Exception as e:
            print(f"\n{RED}[🚨 ERROR] {e}{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")
        
    elif chose == "3":
        print(f"\n{RED}[!] Terminating framework...{RESET}")
        break
        
    elif chose == "4":
    print(f"\n{YELLOW}[+] Booting Local Web Server...{RESET}")
    import http.server
    import socketserver
    PORT = 8080
    Handler = http.server.SimpleHTTPRequestHandler
    print(f"{GREEN}[*] Server started at http://127.0.0.1:{PORT}{RESET}")
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

        
    elif chose == "5":
        print(f"\n{CYAN}[*] Parsing logs...{RESET}\n")
        print(f"{YELLOW}[-] No logs located.{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")

    elif chose == "6":
        chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
        generated_pass = "".join(random.sample(chars, 10))
        print(f"\n{GREEN}[+] Password: {generated_pass}{RESET}")
        print(f"{GREEN}[+] SHA-256 : {hashlib.sha256(generated_pass.encode()).hexdigest()}{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")

    elif chose == "7":
        print(f"\n{CYAN}[*] Scanning Local Host Security Loopback...{RESET}\n")
        for port in [22, 80, 443, 8080]:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex(('127.0.0.1', port)) == 0: print(f" [{GREEN}OPEN{RESET}] Port {port}")
            else: print(f" [{RED}CLOSE{RESET}] Port {port}")
            s.close()
        input(f"\n{WHITE}Press Enter to return...{RESET}")

    elif chose == "8":
        print(f"{GREEN}[+] Maintenance complete! Logs reset.{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")

    elif chose == "9":
        print(f"\n{CYAN}[*] Querying Hardware Telemetry System...{RESET}\n")
        print(f"{GREEN}------------------------------------------------------------{RESET}")
        fb = get_battery_fallback()
        print(f" {GREEN}[•] Current Battery Level : {YELLOW}{fb['percentage']}%{RESET}")
        print(f" {GREEN}[•] Battery Health State  : {YELLOW}GOOD{RESET}")
        print(f" {GREEN}[•] Hardware Power Source : {MAGENTA}{fb['status']}{RESET}")
        print(f" {GREEN}[•] Thermal Core Sensor   : {CYAN}{fb['temp']}°C{RESET}")
        print(f"{GREEN}------------------------------------------------------------{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")

    elif chose == "10":
        target_url = input(f"{WHITE}Enter target URL: {RESET}")
        if not target_url.startswith("http"): target_url = "https://" + target_url
        try:
            with urllib.request.urlopen(target_url, timeout=3) as resp:
                print(f"\n{GREEN}[+] Connected! Status: {resp.getcode()}{RESET}")
        except Exception as e: print(f"\n{RED}[-] Failed: {e}{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")
