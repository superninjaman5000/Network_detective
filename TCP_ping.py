import socket

def tcp_ping(host, port, timeout=1):
    try:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((host, port))
            return True #if connection is successfull
        
    except (socket.timeout, ConnectionRefusedError):
        return False # if the connection failed
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    