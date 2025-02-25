from rabbitmq import RabbitMQ
import time

rabbitmq = RabbitMQ()
while True:
    time.sleep(1)
    message = 'Test message'
    rabbitmq.publish("message-queue",message)
    print(f"Sent message: {message}")
    time.sleep(1)
    rabbitmq.flush()
rabbitmq.close()
