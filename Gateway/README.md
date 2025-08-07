# Node-RED

## Use Case
Node-RED is deployed on a Raspberry Pi, acting as a gateway and data processor for the IoT Network.

## FLOW-Diagram
MQTT In --> JSON --> function 1 --> Rules --> InfluxDB --> debug 1

## 1. MQTT In Node
Purpose: This node is the entry point for sensor data. It subscribes to a specific MQTT topic to receive messages from the ESP32 device.

Topic: bis2025/room625/temperature

Receives: A raw JSON string containing temperature and humidity readings, along with a client ID.

Sends: The received JSON string as msg.payload to the next node.

## 2. JSON Node
Purpose: This node, as configured, is set to "convert to JSON string" (json zeichenfolge). While the incoming message is already a string, this node effectively acts as 

Receives: A JSON string from the MQTT In node.

Sends: The same JSON string as msg.payload to the function 1 node.

## 3. Function Node
Purpose: This node is designed to process the JavaScript object from the JSON node. The function of this node is to prepare the message payload for the next step.

Receives: The structured JavaScript object from the JSON node.

Sends: A modified JavaScript object to the Change (Rules) node.

## 4. Change Node - Rules
Purpose: This node performs a critical data transformation, restructuring the msg.payload into a new format. It extracts specific values and discards others, preparing the data for the InfluxDB Out node.

### Rules Applied:
1. Move msg.payload.fields.temp to msg.payload.temp
2. Move msg.payload.fields.hum to msg.payload.hum
3. Delete msg.payload.fields
4. Delete msg.payload.tags
5. Delete msg.payload.measurement
   
Receives: A JavaScript object from the function 1 node.

Sends: A new JavaScript object to the InfluxDB Out node with a flattened structure

## 5. InfluxDB Out Node
Purpose: This node takes the transformed data and writes it into the InfluxDB 2.0 database.

Configuration: The node is configured to connect to InfluxDB 2.0 instance. Given the data transformation in the Change node, the InfluxDB Out node's properties for measurement, fields, and tags
must be manually specified, as they are no longer dynamically available in the payload.

Receives: The transformed JavaScript object from the Change (Rules) node.

Sends: The message to the Debug node upon a successful write operation.

## 6. Debug Node
Purpose: This node is used for monitoring and troubleshooting the flow.

Configuration: Displays the entire message object that passes through it.

Receives: The message object after it has been processed by the InfluxDB Out node.


Sends: The message content to the Node-RED debug sidebar, allowing for inspection of the data at the end of the pipeline.

## Start & Stop Node-RED
Since Node-RED is deployed on our Raspberry Pi you need to follow these steps to start Node-RED:

1. Connecto to the Raspberry Pi via SSH:
`ssh pi@10.10.4.58`
2. Start Node-RED: `node-red-start`  
3. open http://10.10.4.58:1880 (Note: doesn't work in Chrome, use Safari)
4. Stop Node-RED: `node-red-stop` 





