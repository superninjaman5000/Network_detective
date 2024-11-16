#main
import socket
import time
from port_scan import port_scan
from TCP_ping import tcp_ping

def main():
    while True:

        print("\nwelcome to Network Detective")
        print("1. Port Scan")
        print("2. TCP Ping")
        print("3. Vulnerability Scan (Coming Soon)")
        print("4. Exit")



        choice = input("Please select an option:  ")

        if choice == "1":
            #port scan function
            target = input(" Please enter the target IP or domain you wish to scan: \n")
            port_scan(target)

        elif choice == "2":
            #tcp ping function
            target = input("Enter the target IP or domain for testing: \n")
            port = int(input("Enter the Targets port for TCP ping: \n"))
            if tcp_ping(target, port):
                print(f"Host {target} is reachable on port {port} ")
            else:
                print(f"Host{target} is not reachable on {port}.")

        elif choice == "3":
            print("Vulnerability scanning please wait")

        elif choice == "4":
            print ("exiting the program")
            break
        else:
                # Handle invalid input
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()



