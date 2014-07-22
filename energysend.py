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

  # Read in line of readings from analog channel x
  in0=open("/sys/class/hwmon/hwmon0/device/in0_input","r")
  in0.close()
  
  in1=open("/sys/class/hwmon/hwmon0/device/in1_input","r")
  in0.close()
  
  linestr = in0.readline()

  # Remove the new line at the end
  linestr = linestr.rstrip()

  print linestr

  # Split the line at the whitespaces
  array = linestr.split(' ')

  # Create csv string
  csv = ",".join(array)

  # Send to emoncms
  conn.request("GET", "/"+emoncmspath+"/input/post.json?apikey="+apikey+"&node="+str(nodeid)+"&csv="+csv)
  response = conn.getresponse()
  print response.read()
