#!/usr/bin/python

# Small commandline controller for Philips Hue Lights using phue - https://github.com/studioimaginaire/phue



import sys, getopt
from phue import Bridge

def send_to_lamp(ip, lamp, state):
	b = Bridge(ip)
	b.connect()
	if state == 'on':
		onoff = True
	elif state == 'off':
		onoff = False
	b.set_light(int(lamp), 'on', bool(onoff))
	print "At "+ip+" turning lamp #"+lamp+" "+state

def main(argv):
   ip = ''
   lamp = ''
   try:
       opts, args = getopt.getopt(argv,"hi:n:s:",["ip=","number=","state="])
   except getopt.GetoptError:
      print 'test.py -i <ip> -n <lamp number> -s <on/off>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <ip> -n <lamp number>'
         sys.exit()
      elif opt in ("-i", "--ip"):
         ip = arg
      elif opt in ("-n", "--number"):
         lamp = arg
      elif opt in ("-s", "--state"):
      	state = arg
	send_to_lamp(ip, lamp, state)

if __name__ == "__main__":
   main(sys.argv[1:])
