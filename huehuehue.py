#!/usr/bin/python

# huehuehue - A small commandline controller for Philips Hue Lights.
# By Anders Kusk - http://github.com/kusk/huehuehue
# The script is using phue - https://github.com/studioimaginaire/phue



import sys, getopt
from phue import Bridge

def set_state(ip, lamp, state):
	b = Bridge(ip)
	b.connect()
	if state == 'on':
		onoff = True
	elif state == 'off':
		onoff = False
	b.set_light(int(lamp), 'on', bool(onoff))
	print "At "+ip+" turning lamp #"+lamp+" "+state

def set_brightness(ip, lamp, brightness):
   b = Bridge(ip)
   b.connect()
   b.set_light(int(lamp), 'bri', brightness)


def main(argv):
   ip = ''
   lamp = ''
   brightness = '999'
   try:
       opts, args = getopt.getopt(argv,"hi:n:s:b:",["ip=","number=","state=","brightness="])
   except getopt.GetoptError:
      print 'test.py -i <ip> -n <lamp number> -s <on/off> -b <brightness 0-254>'
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
         set_state(ip, lamp, state)
      elif opt in ("-b", "--brightness"):
         brightness = arg
         set_brightness(ip, lamp, int(brightness))

if __name__ == "__main__":
   main(sys.argv[1:])