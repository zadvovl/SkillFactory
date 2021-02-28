"""metric.py"""
import pika
import json

try:
	connection = pika.BlockingConnection(
	    pika.ConnectionParameters(host='rabbitmq'))
	channel = connection.channel()


	channel.queue_declare(queue='y_true')
	channel.queue_declare(queue='y_predict')

	def callback(ch, method, properties, body):
		print(f'Из очереди {method.routing_key} получено значение {json.loads(body)}')


	channel.basic_consume(
		queue='y_predict', on_message_callback=callback, auto_ack=True)

	channel.basic_consume(
		queue='y_true', on_message_callback=callback, auto_ack=True)

	print('...Ожидание сообщений, для выхода нажмите CTRL+C')
	channel.start_consuming()
	
except:
    print('Не удалось подключиться к очереди')