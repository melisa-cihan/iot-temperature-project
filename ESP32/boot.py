import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
import dht
import ubinascii
esp.osdebug(None)
import gc
gc.collect()
import json

ssid = 'Rechnernetze'
password = 'rnFIW625'
mqtt_server = 'broker.f4.htw-berlin.de'

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'notification'
topic_pub = b'bis2025/room625/temperature'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())