import pika
import json


message = {
  "Report": [
    {
      "object": "Datacenters",
      "alarm": "vSphere Health detected new issues in your environment",
      "severity": "red",
      "time": "2022-08-30T20:01:49.609Z",
      "vcenter": "endpoint1.corp.com"
    }
  ],
  "Component": "vcenter",
  "User": "Administrator",
  "Name": "Alertas de vSphere",
  "Result": "ERROR",
  "DateTime": "2022-09-08 10-00",
  "Message": "Something is wrong"
}

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.10.119', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=json.dumps(message),
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
connection.close()
print(" [x] Message Sent")
