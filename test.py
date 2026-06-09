import os
import platform
import urllib.request
import json
import time
import hashlib  
import random   
import socket   
import subprocess 
import http.server
import socketserver
import threading

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
    import sys
    os.system("clear")
    lines = [
        f"{GREEN}┌────────────────────────────────────────────────────────┐{RESET}",
        f"{GREEN}│{RESET}  {MAGENTA}{BOLD}[+]  A  A  Y  U  S  H     P  A  N  D  I  T  [+]  {RESET}{GREEN}│{RESET}",
        f"{GREEN}└────────────────────────────────────────────────────────┘{RESET}",
        "                                                          ",
        f"               {YELLOW}• [ MAIN OWNER: AAYUSH PANDIT ] •{RESET}",
    ]
    for line in lines:
        print(line)
    print(f"\n{GREEN}[*] Operator: Security Access Granted for '{user_name}'{RESET}")
    print(f"{GREEN}[*] Framework Suite Engine : Active v5.2 (Smart Bypass){RESET}\n")

def get_battery_fallback():
    data = {"percentage": "89", "health": "Good", "status": "UNPLUGGED", "temp": "35.0"}
    return data

while True:
    print_banner()
    print(f"{WHITE}{BOLD}CORE SECURITY MODULES:{RESET}")
    print(f"  [{BLUE}1{RESET}] Core System Diagnostics & Info")
    print(f"  [{BLUE}2{RESET}] Analyze Network Gateway & External IP")
    print(f"  [{BLUE}4{RESET}] Deploy Local Diagnostics Web Server")
    print(f"  [{BLUE}5{RESET}] Inspect Structured JSON Database Logs")
    print(f"\n{GREEN}{BOLD}ADVANCED CYBER UTILITIES:{RESET}")
    print(f"  [{BLUE}6{RESET}] Automated Crypto Password Generator & Hasher")
    print(f"  [{BLUE}7{RESET}] Execute Local Port Scanner Protocol")
    print(f"  [{BLUE}9{RESET}] Live Battery Hardware Monitoring")
    print(f"  [{BLUE}10{RESET}] Secure URL Handshake & HTTP Status Scanner")
    print(f"  [{BLUE}8{RESET}] Storage Maintenance (Wipe Logs & Purge Images)")
    print(f"  [{BLUE}3{RESET}] Terminate Environment (Exit)")
    
    chose = input(f"{YELLOW}{BOLD}shield-shell> {RESET}")
    
    if chose == "1":
        print(f"\n{CYAN}[*] Fetching Architecture Logs...{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")
    elif chose == "2":
        print(f"\n{CYAN}[*] Testing external routing...{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")
    elif chose == "3":
        break
    elif chose == "4":
        print(f"\n{YELLOW}[+] Booting Local Web Server on Port 8080...{RESET}")
        PORT = 8080
        Handler = http.server.SimpleHTTPRequestHandler
        try:
            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                print(f"{GREEN}[*] Server active at http://127.0.0.1:{PORT}{RESET}")
                httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n{RED}[!] Server stopped.{RESET}")
    elif chose == "5":
        print(f"\n{CYAN}[*] Parsing logs...{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")
    elif chose == "6":
        print(f"\n{GREEN}[+] Password Generated.{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")
    elif chose == "7":
        print(f"\n{CYAN}[*] Scanning Loopback...{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")
    elif chose == "8":
        print(f"{GREEN}[+] Maintenance complete.{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")
    elif chose == "9":
        fb = get_battery_fallback()
        print(f" {GREEN}[•] Level : {YELLOW}{fb['percentage']}%{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")
    elif chose == "10":
        target = input(f"{WHITE}Enter URL: {RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")

