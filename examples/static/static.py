import sys
import os
import network
import socket
import ure
import time

from utime import sleep

SSID = 'wifi_ssid'
PASSWD = 'WIFI_PASSWORD'

print('Connecting to WiFi Network Name:', SSID)
wlan = network.WLAN(network.STA_IF)
wlan.active(True) # power up the WiFi chip
print('Waiting for wifi chip to power up...')
sleep(3) # wait three seconds for the chip to power up and initialize
wlan.connect(SSID, PASSWD)
print('Waiting for access point to log us in.')
sleep(2)
if wlan.isconnected():
  print('Success! We have connected to your access point!')
  print('Try to ping the device at', wlan.ifconfig()[0])
else:
  print('Failure! We have not connected to your access point!  Check your credentials.')

from microdot import Microdot, send_file
app = Microdot()


@app.route('/')
async def index(request):
    return send_file('/static/index.html')


@app.route('/static/<path:path>')
async def static(request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('lib/static/' + path)


app.run(debug=True)
