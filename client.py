from device import state
# import device
import time
import datetime
import socket
import json


# Get the device data
data = state.devices()

# Get the current date and time
dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
test_p = dict
# 2024-08-27 12:34:56 INFO sda1: fstype=vfat, label=null, uuid=4A35-C66D, mountpoint=/media/linux/4A35-C66D, mounted=false, plugged=true
# 2024-08-27 12:34:56 INFO mmcblk1p1: fstype=vfat, label=null, uuid=6335-3364, mountpoint=/media/linux/6335-3364, mounted=true, plugged=true
test_p = data
# Add the current datetime to each device entry if necessary
# for item in test_p: test_p[item]['dt'] = dt

# Server information
host = 'localhost'
port = 2443

# Create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Convert the JSON message to a string format
data = json.dumps(test_p)

try:
    # Connect to the server
    client_socket.connect((host, port))
    
    # Send the JSON message
    client_socket.sendall(data.encode('utf-8'))
    
    # Receive the response from the server
    response = client_socket.recv(1024)
    print('response:', response.decode('utf-8'))

finally:
    # Close the socket
    client_socket.close()

