import subprocess
import time
INTERFACES = [ 1, 2, 3,6, 7, 9, 10,11 ]
COUNT=[1,2,3,4,5,6,7,8,9,10,11]
DEVICES={ "ifInOctets": ".1.3.6.1.2.1.2.2.1.10", "ifInUcastPkts": ".1.3.6.1.2.1.2.2.1.11", "ifInNUcastPkts": "1.3.6.1.2.1.2.2.1.12", "ifOutOctets": "1.3.6.1.2.1.2.2.1.16", "ifOutUcastPkts": "1.3.6.1.2.1.2.2.1.17", "ifOutNUcastPkts": ".1.3.6.1.2.1.2.2.1.18"}
def snmpdxd():
	for devices in DEVICES:
		print (devices)
		print "//////////////////////////////////" 
		for interfaces in INTERFACES:
			command=["/usr/bin/snmpget",
              			 "-v", "2c",
              			 "-c", "public",
              			 "128.138.207.5:7777",
              			 "%s.%d" % (DEVICES[devices],interfaces)]
			output = subprocess.check_output(command)
               	 	output = output.split()
                	print output[-1]	           
	return
for i in COUNT:
	print (i)
	print "***************************"
	snmpdxd();
	time.sleep(600)
