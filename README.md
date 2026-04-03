# GhostTrack v1.0
Advanced Location Intelligence tool designed for authorized security research and OSINT investigations.
## Features
 * **Real-time Tracking**: Precise GPS coordinate capture with Google Maps integration.
 * **Auto-Tunneling**: Built-in Cloudflared support for public access without port forwarding.
 * **Device Fingerprinting**: Automatically logs IP address, Browser type, and Platform info.
 * **Persistent Logging**: All captured data is saved locally for post-analysis.
 * **Global Access**: Once installed, run the tool from any directory.
## Installation
 1. **Clone the repository**:
```bash
git clone https://github.com/alonebeast002/GhostTracker.git
cd GhostTrack

```
 2. **Run the installer**:
```bash
chmod +x setup.sh
./setup.sh

```
 3. **Apply changes**:
```bash
source ~/.bashrc  # Or source ~/.zshrc for Zsh

```
## Usage
**Start the tool**:
```bash
GhostTracker

```
**Monitor captured data**:
```bash
tail -f captured_locations.txt

```
## Project Structure
 * GhostTracker.py: Core server and exfiltration logic.
 * index.html: Frontend tracking interface.
 * setup.sh: Automated installation and alias config.
 * captured_locations.txt: Log file for captured data.
## Troubleshooting
 * **Command not found**: Run source ~/.bashrc or restart your terminal.
 * **Port busy**: Kill the process using lsof -i :8000 or change the port in the script.
 * **Tunnel failed**: Ensure you have an active internet connection and cloudflared is installed.
## Disclaimer
This software is developed for educational and authorized research purposes only. Unauthorized use of this tool to track individuals without their explicit consent is illegal and unethical. The developer assumes no liability for misuse or any damage caused by this program. Use responsibly and at your own risk.
**Developed by alonebeast002**
