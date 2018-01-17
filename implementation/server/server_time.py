import time

server_time = time.time()

file = open('TIMESTAMP.DAT', 'r')
client_time = file.readline()
ct = float(client_time) 

diff = server_time - ct

if(diff > 200.00):
	print 0
else: 
	print 1

