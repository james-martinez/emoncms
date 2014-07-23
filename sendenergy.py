import serial, sys
import httplib

# Domain you want to post to: localhost would be an emoncms installation on your own laptop
# this could be changed to emoncms.org to post to emoncms.org
domain = "emoncms.org"

# Location of emoncms in your server, the standard setup is to place it in a folder called emoncms
# To post to emoncms.org change this to blank: ""
emoncmspath = ""

# Write apikey of emoncms account
apikey = "b742b99d9880b27ff50ce73b17c2e224"

# Node id youd like the emontx to appear as
nodeid = 1

conn = httplib.HTTPConnection(domain)


while 1:


        in0 = open('/sys/class/hwmon/hwmon0/device/in0_input', 'r')
        in0val = in0.read()
        in0.close()
        in1 = open('/sys/class/hwmon/hwmon0/device/in1_input', 'r')
        in1val = in1.read()
        in1.close()
        in2 = open('/sys/class/hwmon/hwmon0/device/in2_input', 'r')
        in2val = in2.read()
        in2.close()
        in3 = open('/sys/class/hwmon/hwmon0/device/in3_input', 'r')
        in3val = in3.read()
        in3.close()
        linestr = in0val.rstrip() + " " + in1val.rstrip() + " " + in2val.rstrip() + " " + in3val.rstrip()
        array = linestr.split(' ')
        csv = ",".join(array)
        print csv


  # Send to emoncms
  # For example using the first json type request above just add the apikey to the end like this:	http://emoncms.org/input/post.json?json={power:200}&apikey=xxxxxxxxxxxxxxxxxxx6
  # To use this module send a byte value csv string and the node id to: http://emoncms.org//node/set.json?nodeid=10&data=20,20,20,20
  # You can provide data using bulk mode	http://emoncms.org/input/bulk.json?data=[[0,16,1137],[2,17,1437,3164],[4,19,1412,3077]]
  # http://emoncms.org/input/api
  conn.request("GET", "/"+emoncmspath+"/input/post.json?apikey="+apikey+"&node="+str(nodeid)+"&csv="+csv)
  response = conn.getresponse()
  print response.read()
