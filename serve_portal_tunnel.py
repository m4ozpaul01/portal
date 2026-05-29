#!/usr/bin/env python3
"""Serve PORTAL on port 8000 + SSH tunnel via localhost.run, auto-kill after 1 hour."""
import subprocess
import threading
import http.server
import socketserver
import re
import os
import time
import signal
import sys

PORT = 8000
DIRECTORY = "/home/paul/Desktop/PROJECTS/PORTAL"
TIMEOUT = 3600  # 1 hour
TUNNEL_URL_FILE = "/tmp/portal_tunnel_url.txt"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run_http_server():
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Serving PORTAL on port {PORT} from {DIRECTORY}")
            httpd.serve_forever()
    except Exception as e:
        print(f"HTTP Server Error: {e}")

def auto_kill():
    """Kill this script after TIMEOUT seconds."""
    for remaining in range(TIMEOUT, 0, -1):
        time.sleep(1)
    print(f"⏰ Tunnel expired after {TIMEOUT//60} minutes. Shutting down.")
    os.kill(os.getpid(), signal.SIGTERM)

def run_tunnel():
    print("Starting SSH tunnel via localhost.run...")
    cmd = ["ssh", "-o", "StrictHostKeyChecking=no", "-R", f"80:localhost:{PORT}", "nokey@localhost.run"]
    
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    
    tunnel_url = None
    try:
        for line in iter(process.stdout.readline, ''):
            print(f"[Tunnel] {line.strip()}")
            match = re.search(r"https://[a-zA-Z0-9-]+\.lhr\.life", line)
            if match and not tunnel_url:
                tunnel_url = match.group(0)
                print(f"\n{'='*60}")
                print(f"🌐 PORTAL TUNNEL ACTIVE: {tunnel_url}")
                print(f"⏱  Expires in: {TIMEOUT//60} minutes")
                print(f"{'='*60}")
                with open(TUNNEL_URL_FILE, "w") as f:
                    f.write(f"{tunnel_url}\n{TIMEOUT}\n")
    except Exception as e:
        print(f"Tunnel error: {e}")
    finally:
        process.terminate()
        process.wait()

if __name__ == "__main__":
    # Start auto-kill timer
    threading.Thread(target=auto_kill, daemon=True).start()
    
    # Start HTTP server
    server_thread = threading.Thread(target=run_http_server, daemon=True)
    server_thread.start()
    time.sleep(1)
    
    # Start tunnel (blocks until killed)
    run_tunnel()
