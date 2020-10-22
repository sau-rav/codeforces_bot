import sys
import subprocess 
import os
from decouple import config

IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE')

proc = subprocess.Popen(["ping", IP_NETWORK],stdout=subprocess.PIPE)
while True:
	line = proc.stdout.readline()
	if not line:
		break
	#the real code does filtering here
	connected_ip = line.decode('utf-8').split()[3][0:-1]
	print('{} got connected to the router'.format(connected_ip))

