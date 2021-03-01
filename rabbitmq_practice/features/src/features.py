import pika
import json
import numpy as np
import time
from sklearn.datasets import load_diabetes
import uuid
import sys

X, y = load_diabetes(return_X_y=True)

while True:
	try:
		uid = str(uuid.uuid1())	

		random_row = np.random.randint(0, X.shape[0]-1)

		feature_vector = json.dumps({uid:list(X[random_row])})
		correct_answer = json.dumps({uid:y[random_row]})

		connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
		channel = connection.channel()

		channel.queue_declare(queue='Features')
		channel.queue_declare(queue='y_true')

		channel.basic_publish(exchange='',
		                      routing_key='Features',
		                      body=feature_vector)
		print(f'Сообщение с вектором {feature_vector} признаков, отправлено в очередь')

		channel.basic_publish(exchange='',
		                      routing_key='y_true',
		                      body=correct_answer)

		print(f'Сообщение с правильным ответом {correct_answer}, отправлено в очередь')
		connection.close()
		time.sleep(5)
	except:
		print('Не удалось подключиться к очереди')
		print(f'Unexpected error: {sys.exc_info()[0]}')