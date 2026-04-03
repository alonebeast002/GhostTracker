# GhostTrack v1.0
Advanced Location Intelligence tool designed for security research and OSINT.
## Features
 * Real-time GPS tracking with Google Maps integration.
 * Automated Cloudflared tunneling for public access.
 * Device fingerprinting (IP, Browser, Platform).
 * Persistent logging of captured data to text files.
 * Global command access from any directory.
## Installation
 1. Clone the repository:
```bash
git clone https://github.com/alonebeast002/GhostTracker.git
cd GhostTrack

```
 2. Run the setup script:
```bash
chmod +x setup.sh
./setup.sh

```
 3. Launch the tool from anywhere:
```bash
GhostTracker

```
## Requirements
 * Python 3.x
 * Cloudflared binary
 * Internet connection
## Project Structure
 * GhostTracker.py: Core logic and server.
 * index.html: Frontend tracking interface.
 * setup.sh: Installation and alias configuration.
 * captured_locations.txt: Log file for data.
**Disclaimer**
This tool is developed for educational purposes and authorized security testing only. Using this software to track individuals without their explicit consent is illegal and unethical. The developer assumes no liability for misuse or damage caused by this program. Use at your own risk.
