# iot-temperature-project
A project for the class Besondere Kapitel der Informatik in the study program Computer Science and Business Administration at the Hochschule für Technik und Wirtschaft Berlin.

## Requirements

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
- mqtt://broker.f4.htw-berlin.de:1883
### Constrained Devices
- ESP32
### IoT Gateway
- Raspberry Pi
