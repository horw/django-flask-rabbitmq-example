#amqps://xxxxxxxx
import pika
params = pika.URLParameters('amqps://xxxxxxx')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method,properties, body):
    print('received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()
