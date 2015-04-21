#!/usr/bin/python

# huehuehue - A small commandline controller for Philips Hue Lights.
# By Anders Kusk - http://github.com/kusk/huehuehue
# The script is using phue - https://github.com/studioimaginaire/phue



import sys, getopt
from phue import Bridge

def set_state(ip, lamp, state):
	b = Bridge(ip)
	b.connect()
	b.set_light(check_lamp_id(lamp), 'on', check_state(state))
	print "At "+ip+" turning lamp #"+lamp+" "+state

def set_brightness(ip, lamp, brightness):
   b = Bridge(ip)
   b.connect()
   b.set_light(check_lamp_id(lamp), 'bri', brightness)

# Convert lamp number to int.
def check_lamp_id(id):
   if id.isdigit():
      return int(id)
   else:
      return id

# Convert on/off to true/false
def check_state(state):
   if state == 'on':
      return True
   else:
      return False

def check_state_reverse(state):
   if state == True:
      return 'On'
   else:
      return 'Off'


# Print a nice table of lamps with tab seperation
def print_lamps(ip):
   b = Bridge(ip)
   b.connect()
   print '\033[1mName\t\tState\t\tBrightness\033[0m'
   print '---------------------------------------------------------'
   lights = b.lights
   for l in lights:
      if len(l.name) < 5:
         print l.name + '\t\t' + check_state_reverse(l.on) + "\t\t" + str(l.brightness)
      elif len(l.name) > 5 and len(l.name) < 10:
         print l.name + '\t' + check_state_reverse(l.on) + "\t\t" + str(l.brightness)
      elif len(l.name) >= 10:
         print l.name + '\t' + check_state_reverse(l.on) + "\t\t" + str(l.brightness)


      


# main loop
def main(argv):
   ip = ''
   lamp = ''
   brightness = ''
   try:
       opts, args = getopt.getopt(argv,"hi:n:s:b:p:",["ip=","number=","state=","brightness=","print="])
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
      elif opt in ("-p", "--print"):
         print_lamps(ip)

if __name__ == "__main__":
   main(sys.argv[1:])