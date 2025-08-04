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

#MQTT SetUp
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'notification'
topic_pub = b'sensors/inside/temperature'

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

# Connect and Reconnect Functions
def connect_and_subscribe():
    global client_id, mqtt_server, topic_sub
    client = MQTTClient(client_id, mqtt_server, user=mqtt_user, password=mqtt_pass)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic_sub)
    print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
    return client

def restart_and_reconnect():
    print('Failed to connect to MQTT broker.
    Reconnecting...')
    time.sleep(10)
    machine.reset()

# Callback Funnction and Main Loop
def sub_cb(topic, msg):
    print((topic, msg))
    if topic == b'notification' and msg == b'received':
    print('ESP received hello message')
    try:
        client = connect_and_subscribe()
    except OSError as e:
        restart_and_reconnect()
    while True:
        try:
            client.check_msg()
            if (time.time() - last_message) > message_interval:
                msg = b'Hello #%d' % counter
                client.publish(topic_pub, msg)
                last_message = time.time()
                counter += 1
            except OSError as e:
                restart_and_reconnect()
    

