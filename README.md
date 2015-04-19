# huehuehue
![huehuehue](http://maep.dk/img/huehuehue.gif)

huehuehue - A small commandline controller for Philips Hue Lights.

By Anders Kusk - http://github.com/kusk/huehuehue

The script is working by using phue - https://github.com/studioimaginaire/phue

For now the script is very basic and can only turn a specific light on and off.

You have to authorize the client with the hub by pressing the Connect-button.

# Syntax
Set state(on/off)
python huehuehue.py -i <ip> -n <lamp number> -s <on/off>

Set brightness
python huehuehue.py -i <ip> -n <lamp number> -b <1-254>
