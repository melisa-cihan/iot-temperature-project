# IoT-temperature-project
A project for the class Besondere Kapitel der Informatik in the study program Computer Science and Business Administration at the Hochschule für Technik und Wirtschaft Berlin.

## Requirements

https://github.com/melisa-cihan/iot-temperature-project/raw/main/art/Diagrams/Setup_Diagram.jpg

### Live temperature monitoring
- Implementation of a solution for real-time monitoring of room temperature.

### Web UI for access
- Provision of a web interface through which temperature values can be retrieved.

### Historical data and visualization
- Storage and display of past temperature values.
- Appropriate visualization of temperature trends (e.g., charts).

### Extensibility
- The system must be designed so that additional sensor types (e.g., CO₂ measurement, humidity) can be integrated in the future.
- Ability to directly correlate sensor values (e.g., temperature and CO₂ in one view).

### Security
- The room in which the values are measured is considered a “secure zone.”
- External communication (e.g., web UI) must be secure (e.g., encryption, authentication).

### MQTT broker as a means of communication
- An existing MQTT broker can be used for communication.

## Technologies Used
- Grafana
- InfluxDB
- MQTT
- Node-RED

## Project Structure
### Broker
- `mqtt://broker.f4.htw-berlin.de:1883`

### Constrained Devices
- [**ESP32 Code**](ConstrainedDevice/)

### IoT Gateway
- [**Gateway**](Gateway/)
    - Node-RED Flow (Sensors): The flow for sensor data is defined in [temp_hum_soilmoisture_flows.json](Gateway/temp_hum_soilmoisture_flows.json)
    - Node-RED Flow (Notifications): The flow for mobile push notifications is defined in [mobile_push_notification.json](Gateway/mobile_push_notification.json)

### Backend and Visualization
- [**Backend (Node-RED, InfluxDB)**](Backend/)
- [**Web UI (Grafana)**](WebUI/)
    - Grafana Dashboard: The exported Grafana dashboard JSON can be found at [Team8-Grafana.json](WebUI/Team8-Grafana.json)

### Documentation and Diagrams
- [**Diagrams**](Diagrams/)
    - System Architecture Overview: Find the architectural diagram in [Setup_Diagram.jpg](Diagrams/Setup_Diagram.jpg)
