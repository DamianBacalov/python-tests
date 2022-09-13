
import pika


def callback(ch, method, properties, body):
    message = body.decode()
    print(" [x] Received %s" % message)

    ch.basic_ack(delivery_tag=method.delivery_tag)


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.10.119', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

print(" [x] Waiting messages")
channel.start_consuming()