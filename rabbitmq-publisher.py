import pika
import json


def publish(msg):
  channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=json.dumps(msg),
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))


message1 = {"Message": "En un agujero en el suelo"}
message2 = {"Message": "vivía un hobbit"}
message3 = {"Message": "No un agujero humedo y sucio"}
message4 = {"Message": "Era un agujero Hobbit"}
message5 = {"Message": "y eso significa"}
message6 = {"Message": "comodidad"}

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.10.119', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

publish(message1)
publish(message2)
publish(message3)
publish(message4)
publish(message5)
publish(message6)

connection.close()
print(" [x] Messages Sent")
