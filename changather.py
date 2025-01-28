#!/usr/bin/python3

import re
import sys
import socket
import ipaddress


def connection(IP, PORT):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(30)
            s.connect((IP, PORT))
            
            response = b""
            while True:
                data = s.recv(1024)
                if not data:
                    break
                response += data
            
            response_decoded = response.decode(errors="replace")
            if "pan-chan" in response_decoded:
                extracted_ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', response_decoded)
                return extracted_ips
    except socket.timeout:
        pass
    except socket.error:
        pass
    except Exception:
        pass
    return []


def main():
    if len(sys.argv) < 4:
        print(f"Usage: ./{sys.argv[0]} <IP> <PORT> <OUTPUT_FILE>")
        sys.exit(1)
    
    IP = sys.argv[1]
    PORT = sys.argv[2]
    OUTPUT_FILE = sys.argv[3]

    try:
        ipaddress.ip_address(IP)
    except ValueError as err:
        print(f"Invalid IP address: {err}")
        sys.exit(1)
    
    try:
        PORT = int(PORT)
        if not (1 <= PORT <= 65535):
            raise ValueError("Port must be between 1 and 65535")
    except ValueError as err:
        print(f"Invalid port: {err}")
        sys.exit(1)

    queue = [IP]
    visited = set()
    all_extracted_ips = []

    with open(OUTPUT_FILE, "w") as f:
        while queue:
            current_ip = queue.pop(0)
            if current_ip in visited:
                continue
            
            visited.add(current_ip)
            new_ips = connection(current_ip, PORT)

            for ip in new_ips:
                try:
                    ipaddress.ip_address(ip)
                    if ip not in visited:
                        queue.append(ip)
                        all_extracted_ips.append(ip)
                        f.write(f"{ip}\n")
                        print(f"\rLast IP: {ip} | Queue Length: {len(queue)}")
                except ValueError:
                    pass

    print("\n[STATS] Exploration complete.")
    print(f"Total unique IPs visited: {len(visited)}")
    print(f"All extracted IPs saved in: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
