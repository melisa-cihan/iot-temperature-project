"""
This file contains the core application logic of the device, which runs in a continuous loop.
It is responsible for reading sensor data, formatting the data into a JSON payload,
and publishing it to the MQTT broker. It also includes the logic for error handling and device reconnection.
"""

def sub_cb(topic, msg):
  print((topic, msg))

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
_MOISTURE_SENSOR_PIN = 34

moisture_sensor = ADC(Pin(_MOISTURE_SENSOR_PIN))
sensor = dht.DHT22(machine.Pin(_TEMP_SENSOR_PIN))

#3.3V = 11DB
moisture_sensor.atten(ADC.ATTN_11DB)

def get_moisture_value():
    try:
        raw_moisture = moisture_sensor.read()
        max_moisture_value = 2685
        min_moisture_value = 1059
        moisture_percentage = ((max_moisture_value - raw_moisture) / (max_moisture_value - min_moisture_value)) * 100
        
        if moisture_percentage > 100: moisture_percentage = 100
        if moisture_percentage < 0: moisture_percentage = 0
        
        print(f"Soil Moisture: {moisture_percentage:.2f} % (Raw: {raw_moisture})")
        return moisture_percentage
    except Exception as e:
        print("Error reading moisture sensor:", e)
        return None

    
    
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
            "measurement": "sensor_data",
            "tags": {
                "client_id": ubinascii.hexlify(machine.unique_id()).decode('utf-8')
                },
            "fields": {
                "temp": temp,
                "hum": hum
                }
            }    
            
        msg = json.dumps(payload)
        client.publish(topic_pub, msg.encode('utf-8'))
        print(f"Published to {topic_pub}: {msg}")
    
    moisture = get_moisture_value()
    if moisture is not None:
        payload_moisture = {
            "measurement": "soil_moisture_sensor_data",
            "tags": {
                "client_id": ubinascii.hexlify(machine.unique_id()).decode('utf-8')
                },
            "fields": {
                "moisture": moisture
                }
            }
        msg_moisture = json.dumps(payload_moisture)
        client.publish(topic_pub_moisture, msg_moisture.encode('utf-8'))
        print(f"Published to {topic_pub_moisture}: {msg_moisture}")
        
        
    time.sleep(5)
  except OSError as e:
    restart_and_reconnect()
    



