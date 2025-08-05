def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'bis2025/room625/temperature' and msg == b'received':
    print('ESP received hello message')

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()
  
_TEMP_SENSOR_PIN = 13

sensor = dht.DHT22(machine.Pin(_TEMP_SENSOR_PIN))
    
def get_temp_value():
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print(f"Temperature: {temperature:.2f} °C")
        print(f"Humidity: {humidity:.2f} %")
        return temperature, humidity
    except OSError as error:
        print("Error reading sensor:", error)
        return None, None

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    temp, hum = get_temp_value()
    if temp is not None and hum is not None:
        payload = {
            "temp": temp,
            "hum": hum,
            "client_id": ubinascii.hexlify(machine.unique_id()).decode('utf-8')}
        msg = json.dumps(payload)
        client.publish(topic_pub, msg.encode('utf-8'))
        print(f"Published: {msg}")
    time.sleep(5)
  except OSError as e:
    restart_and_reconnect()
    



