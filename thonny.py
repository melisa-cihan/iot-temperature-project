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

# MQTT Broker Info Constants
ssid = 'Rechnernetze'
password = 'rnFIW625'
mqtt_server = '10.10.4.58'
mqtt_user = 'pi'
mqtt_pass = '1Himbeere'

#MQTT SetUp
client_id = ubinascii.hexlify(machine.unique_id())
topic_pub = b'sensors/inside/temperature'

# Sensor setup example
sensor = dht.DHT22(machine.Pin(4))

# Connect to MQTT Broker
def connect_mqtt():
    client = MQTTClient(client_id, mqtt_server, user=mqtt_user, password=mqtt_pass)
    client.connect()
    print('Connected to MQTT Broker')
    return client

def reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(5)
    machine.reset()

try:
    client = connect_mqtt()
except OSError as e:
    reconnect()
    
topic_sub = b'hello'
last_message = 0
message_interval = 5
counter = 0

