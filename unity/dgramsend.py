import socket
import struct
import random
import array
import time
import logging
import sys

#ip = "172.26.2.235"
#ip = "172.26.2.171"
#ip = "172.26.2.132"
port = 9939

if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	random.seed()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	if (len(sys.argv) < 2):
		logging.error("Usage: {0} ip");
		sys.exit(1);
	ip = sys.argv[1];
	logging.info("Setting ip {0} port {1}".format(ip, port))
	
	while (1):
		
		datatosend = array.array("f")
		for i in range(10):
			datatosend.append(((float(random.random())) - 0.5) * 2.0)
			datatosend.append(((float(random.random())) - 0.5) * 2.0)
			datatosend.append(((float(random.random())) - 0.5) * 2.0)
		logging.debug("x{0} y{1} z{2}".format(datatosend[0], datatosend[1], datatosend[2]))
		s.sendto(datatosend.tostring(), (ip, port))
		
		time.sleep(0.25)
