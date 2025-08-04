# Imports
import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

# Constants
ssid = 'Rechnernetze'
password = 'rnFIW625'
mqtt_server = '10.10.4.58'
mqtt_user = 'pi'
mqtt_pass = '1Himbeere'

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'notification'
topic_pub = b'hello'
last_message = 0
message_interval = 5
counter = 0

