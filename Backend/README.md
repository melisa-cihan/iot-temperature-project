## Influx DB 2.0

### About
Buckets: In InfluxDB 2.0, data is stored in buckets. A bucket is a named location where time-series data is stored. It's similar to a database in traditional relational databases, but specifically designed for time-series data. 
Each bucket has a retention policy, defining how long data is kept.

Measurements: Within a bucket, data is organized into measurements. A measurement is analogous to a table in a relational database. For example, sensor_data is a measurement in your project.

Tags: Tags are key-value pairs that are indexed. They are used to store metadata that one can frequently query or filter by. Tags are crucial for efficient data retrieval in time-series data. 
In our project client_id is used as a tag.

Fields: Fields are key-value pairs that store the actual data values (e.g., sensor readings). Field values are not indexed, making them suitable for frequently changing data. In our project, temp and hum are fields.

API Tokens: InfluxDB 2.0 uses API Tokens for authentication and authorization. These tokens grant specific permissions (read, write, all) to buckets and other resources.

### 1. Bucket Creation in InfluxDB 2.0
Data in InfluxDB is stored in buckets, which are created via the web UI. A bucket name and retention policy must be defined, and this name must exactly match the "Bucket" field in the Node-RED InfluxDB Out node's server configuration.
We created a Bucket named "Team8".

### 2. API Token Generation
To authenticate and authorize the Node-RED flow to write data, an API Token must be generated in the InfluxDB 2.0 web UI. 
This token, which is granted write permissions for a specific bucket, must then be copied and pasted into the "Token" field of the Node-RED InfluxDB Out node's configuration.

### 3. Data Reception from Node-RED
The InfluxDB Out node in the Node-RED flow acts as a client, sending data to the InfluxDB API. The Change node restructures the incoming message, preparing the temp and hum values to be written as fields. 
Consequently, the InfluxDB Out node must be manually configured with the correct measurement and field names to properly ingest this data.

### Set-Up
The following Server was already established by our Professor:
URL: http://bis.f4.htw-berlin.de:8086
username: admin
password: