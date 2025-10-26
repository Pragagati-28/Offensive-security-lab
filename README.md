# Offensive Security Lab

**Project name:** offensive-security-lab

**Purpose:** Beginner-level lab to learn safe offensive security techniques: network discovery, vulnerability enumeration, and controlled exploit workflow demonstration using a purposely vulnerable VM (e.g., Metasploitable).

**Ethics & Legal:** Use only on systems you own or have explicit permission to test. Unauthorized hacking is illegal.

## Setup
1. Install VirtualBox (or VMware) and import two VMs:
   - Kali Linux (attacker)
   - Metasploitable2 or any intentionally vulnerable VM (target)
2. Ensure both VMs are on the same internal network (Host-only or NAT network) so testing remains local.
3. On Kali, install required tools: `nmap`, `python3`, `metasploit-framework` (optional), `net-tools`.

## Files
- `network_scan.py` — Run to discover hosts and services.
- `exploit_demo.sh` — Demo workflow (run only in lab). Edit TARGET_IP variable before running.
- `vuln_report.txt` — Example output report.

## How to run
1. Start both VMs and find the target IP (or let network_scan find it).
2. Run: `python3 network_scan.py --network 192.168.56.0/24 --output report.json`
3. Inspect `report.json` or `vuln_report.txt` and follow remediation suggestions.

## GitHub
- Create repo `offensive-security-lab` and set visibility to private initially.
- Add a `Screenshots/` folder with outputs.

## Disclaimer
This project is for educational purposes only. The author is not responsible for misuse.
