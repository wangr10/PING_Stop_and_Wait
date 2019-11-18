# PingServer.py - from Kurose and Ross
# Modified by Prateek Kumar Singh

# We will need the following module to generate randomized lost packets
import random
import time
import sys
from socket import *

# Checking command line arguement
if (len(sys.argv) != 2):
    print("Required arguments: port")
    exit(0)
	
port = int(sys.argv[1])

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', port))
# Assign Loss and Delay parameters,(Delay = 100 means 100 milliseconds)
LOSS_RATE = 0.0
AVERAGE_DELAY = 0 
	
while True:
	# Generate random number in the range of 0 to 1
	rand = random.uniform(0, 1)

	# Receive the client packet along with the address it is coming from
	message, address = serverSocket.recvfrom(1024)

	# Print the received data.
	print(message)

	# Decide whether to reply, or simulate packet loss. If rand is less than LOSS_RATE, we consider the packet lost and do not respond
	if rand < LOSS_RATE:
	   print("Reply not sent.")
	   continue

	# Simulate network delay.
	delay = random.randint(0.0, 2*AVERAGE_DELAY)
	print(delay)
	time.sleep(delay/1000);

	# Otherwise, the server responds
	serverSocket.sendto(message, address)
	print("Reply sent.")
