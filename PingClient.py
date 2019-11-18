import socket
import sys
import time
from socket import *

if (len(sys.argv) != 3):
    print("Required arguments: hostname and port number")
    exit(0)

hostname = sys.argv[1]
port = int(sys.argv[2])

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientsocket = socket(AF_INET, SOCK_DGRAM)

# Set the timeout value to 1 second. If socket does not get any response
# from the Server in 1 second, it will go into Exception.
clientsocket.settimeout(1)
# Create a Byte(String) variable to store the Ping Data (Not necessary)
dataRecv = ""

# Set the sequence number to 0 and plus 4 after each successful ping operation
seq_num = 0
# Create a list to store the statistics of transmission
RTT=[]
time_taken = 0.0 
start_time = 0.0     
packets_recv = 0 

print("PING %s, %d" % (hostname, port))

while (True):
	start_time = time.time()
	seq_num += 1
	data = bytes(56)
	clientsocket.sendto(data,(hostname, port))
	try:
		dataRecv, address = clientsocket.recvfrom(1024)
		# calculate the estimate RTT
		time_taken = time.time() - start_time
		RTT.append(time_taken)
		packets_recv += 4
		print ( "PING %s %d %.3f seconds" % (hostname, packets_recv, time_taken))
	except Exception:
		print ( "PING %s %d LOST" % (hostname, packets_recv))
	# after sending 5 ping requests, break out from the while loop
	if(seq_num == 5):
		break 


# Statistics processing(help to visualize the data)
packet = seq_num
packets_lost = packet - (packets_recv / 4)
lost_percent = ((float(packets_lost) / packet) * 100)
lost_percent = int(lost_percent)
print("\nPing statistics for %s" % (hostname))
print("Packets: Sent=%d, Received=%d, Lost=%d (%d%% Loss)" % (packet, packets_recv, packets_lost, lost_percent))
print("The Minimum RTT is: %.3f seconds" % (min(RTT)))
print("The Maximum RTT is: %.3f seconds" % (max(RTT)))
print("The Average RTT is: %.3f seconds" % (sum(RTT) / (packets_recv / 4)))