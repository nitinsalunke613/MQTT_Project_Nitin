# MQTT_Project_Nitin
This project demonstrates an IoT-like client-server system for real-time MQTT message processing using Python. The client generates random status messages and sends them to a RabbitMQ queue. The server consumes these messages, processes them, and stores the data in MongoDB. Additionally, the server provides a REST API to retrieve status counts based on a time range.

Key Features

Client:

Publishes MQTT messages to RabbitMQ every second.
Each message contains:
A random status value (0-6).
A timestamp in ISO 8601 format.
Uses pickle for efficient message serialization.

Server:

Consumes messages from RabbitMQ.
Stores the processed data in a MongoDB database.
Offers a REST API endpoint (via FastAPI) to retrieve status counts within a specific time range.


Technologies Used
Python: Core programming language.
RabbitMQ: Message broker for reliable message queuing.
MongoDB: Database for storing and querying status data.
FastAPI: Framework for creating the REST API.
Pickle: Python module for data serialization.
