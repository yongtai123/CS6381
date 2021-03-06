
# Make sure you run this file at the first step for every unit tests.

from Broker import Broker

import time
import argparse   # for command line parsing

def parseCmdLineArgs ():
	# parse the command line
	parser = argparse.ArgumentParser ()
	# add optional arguments
	parser.add_argument("-b", "--brokers", type=str, help='all brokers ip address')
	parser.add_argument("-i", "--ip", type=str, help='self ip address')
	# parse the args
	args = parser.parse_args()
	return args

if __name__ == '__main__':
	args = parseCmdLineArgs()
	brokerIPs = args.brokers
	ip = args.ip
	brokerIPs = brokerIPs.split('-')
	broker = Broker(brokerIPs, ip, '5556', '5557', '5558', '5559', '6000', '6001', '6002', '6003')

	broker.handler()
	while True:
		pass
