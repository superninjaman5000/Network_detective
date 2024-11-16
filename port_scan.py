#all in one network manger

# 665,535 ports in a host starting from 0
import socket
import time
import subprocess

# Function to scan ports
def port_scan(target):
    try:
        target_ip = socket.gethostbyname(target)
        print(f"Scanning host {target_ip}... please wait: \n")

        start = time.time()

        for port in range(1, 65536):
            try:
                # Create a new socket for each port
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(1)  # Timeout 
                    result = s.connect_ex((target_ip, port))  # Check connectivity
                    if result == 0:
                        print(f"Port {port} is open")
                    else:
                        print(f"Port {port} is closed")
            except KeyboardInterrupt:
                print("\nScan interrupted by user. Exiting...")
                break
                
        end = time.time()
        print(f"Scan took total {end - start:.2f} seconds \n")

    except socket.gaierror:
        print("Could not reach target, please try again.")
    except KeyboardInterrupt:
        print("\nScan canceled by user.")




