#!/usr/bin/env python3
"""network_scan.py - Simple network discovery using system nmap."""
import argparse, subprocess, json, shlex
from datetime import datetime

def run_nmap(network):
    cmd = f"nmap -sn {shlex.quote(network)}"
    proc = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
    return proc.stdout

def scan_host_ports(ip):
    cmd = f"nmap -sS -Pn -T4 --top-ports 100 {ip}"
    proc = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
    return proc.stdout

def parse_nmap_hosts(nmap_output):
    hosts = []
    for line in nmap_output.splitlines():
        if line.startswith('Nmap scan report for'):
            parts = line.split()
            ip = parts[-1]
            hosts.append(ip)
    return hosts

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--network', required=True, help='Network in CIDR (e.g. 192.168.56.0/24)')
    parser.add_argument('--output', default='report.json', help='Output JSON file')
    args = parser.parse_args()

    nmap_out = run_nmap(args.network)
    hosts = parse_nmap_hosts(nmap_out)
    report = {'scan_time': datetime.utcnow().isoformat()+'Z', 'network': args.network, 'hosts': []}

    for host in hosts:
        ports_out = scan_host_ports(host)
        report['hosts'].append({'ip': host, 'raw_nmap': ports_out})

    with open(args.output, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"Report written to {args.output}")

if __name__ == '__main__':
    main()
