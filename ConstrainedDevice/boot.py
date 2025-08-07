"""
This script runs automatically on the ESP32's startup and is responsible
for all initial setup and configuration.
Its primary tasks are to establish a Wi-Fi connection, define the MQTT client 
settings, and set up the global variables needed by the main application.
"""

import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
from machine import Pin, ADC
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
topic_pub_moisture = b'bis2025/soil/moisture'
topic_pub_distance = b'bis2025/ultrasonic/distance'

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


