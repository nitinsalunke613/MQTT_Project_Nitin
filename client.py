import pika
import pickle
import time
from utils import generate_status

class MQTTClient:
    def __init__(self, queue_name="mqtt_queue"):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)

    def publish_status(self):
        while True:
            status = generate_status()
            message = {"status": status, "timestamp": time.time()}
            self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=pickle.dumps(message))
            print(f"Sent: {message}")
            time.sleep(1)

if __name__ == "__main__":
    client = MQTTClient()
    client.publish_status()
