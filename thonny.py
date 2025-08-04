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
import dht
gc.collect()

# MQTT Broker Info Constants
ssid = 'Rechnernetze'
password = 'rnFIW625'
mqtt_server = '10.10.4.58'
mqtt_user = 'pi'
mqtt_pass = '1Himbeere'
mqtt_port = 1883

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

# Establish Wifi Connection
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
    pass
print('Connection successful')
print(station.ifconfig)



