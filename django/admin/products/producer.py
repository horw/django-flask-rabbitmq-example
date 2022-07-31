#amqps://hqntvffm:XgWOZMrf7P4xs7A0I9ml57LVndxH3uqC@chimpanzee.rmq.cloudamqp.com/hqntvffm
import pika, json
params = pika.URLParameters('amqps://xxxxxxx')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
