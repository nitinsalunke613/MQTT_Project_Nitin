import pika
import pickle
from database import MongoDBHandler

class MQTTServer:
    def __init__(self, queue_name="mqtt_queue"):
        self.queue_name = queue_name
        self.mongo_handler = MongoDBHandler()

    def callback(self, body):
        message = pickle.loads(body)
        print(f"Received: {message}")
        self.mongo_handler.insert_message(message)

    def consume_messages(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=self.queue_name)
        channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)
        print("Incoming Messages...")
        channel.start_consuming()

if __name__ == "__main__":
    server = MQTTServer()
    server.consume_messages()
