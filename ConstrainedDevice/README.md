# ESP32 - Sensor Module

This directory contains the MicroPython code for the ESP32 device. The purpose of this device is to collect environmental sensor data and publish it via MQTT.

---

## 1. Features

* **Data Acquisition:** Continuously measures temperature and humidity using a **DHT22 sensor**
* **Automated Connectivity:** Manages its own Wi-Fi connection to the network and automatically attempts to reconnect upon failure
* **MQTT Communication:** Publishes sensor readings as a structured JSON payload to a specific MQTT topic
* **Robustness:** Includes a `try...except` block with a reset function to handle and recover from runtime errors
* **Unique Identification:** Generates a unique `client_id` from the device's MAC address to ensure traceability in the data

---

## 2. Technologies

This project uses the following hardware, software, and communication protocols:

* **Hardware:**
    * **ESP32:** The microcontroller running the code
    * **DHT22:** The connected sensor for environmental measurements
    * **Hygrometer Modul V1.2:** The connected sensor for measuring soil moisture
* **Software & Firmware:**
    * **MicroPython:** The firmware and programming language used on the ESP32
* **Libraries:**
    * `umqtt.simple`: A lightweight library for MQTT communication
    * `dht`: The library for interfacing with the DHT22 sensor
* **Protocols:**
    * **MQTT:** The messaging protocol used for data transmission
