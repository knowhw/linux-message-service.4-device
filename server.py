import socket
# import datetime
import json

def handle_client(conn):
    # Use the connection within a context manager to ensure it's properly closed
    with conn:
        print("Connection established:", conn)
        while True:
            # Receive data from the client, up to 1024 bytes
            data = conn.recv(1024)
            # If no data is received, break out of the loop
            if not data:
                break
            print("data:", data.decode('utf-8'))
            # Prepare a response by encoding the received data
            response = f"{data}".encode('utf-8')
            # Send the response back to the client
            conn.sendall(response)
            # Break the loop after sending the response
            break
            
def main():
    # The socket is received via stdin when created by systemd
    s = socket.fromfd(0, socket.AF_INET, socket.SOCK_STREAM)
    while True:
        conn, addr = s.accept()
        handle_client(conn)

if __name__ == "__main__":
    main()

