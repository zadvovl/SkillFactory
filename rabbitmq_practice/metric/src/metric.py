"""metric.py"""
import pika
import json
import sys
import pandas as pd
from sklearn.metrics import mean_squared_error

try:
	connection = pika.BlockingConnection(
	    pika.ConnectionParameters(host='rabbitmq'))
	channel = connection.channel()


	channel.queue_declare(queue='y_true')
	channel.queue_declare(queue='y_predict')

	def callback(ch, method, properties, body):
		print(f'Из очереди {method.routing_key} получено значение {json.loads(body)}')
		uid = list(json.loads(body).keys())[0]
		if uid:
		# proceed only if uid is available (meaning that we have a payload)
			if method.routing_key == 'y_predict':
				pred = list(json.loads(body).values())[0]
				with open('./results/predictions.txt', 'a') as file_object:
					file_object.write(f'{uid} {pred}'+'\n')
					#file_object.write('Some prediction value'+'\n')
				print('Successfully saved to predictions.txt')
			else:
				tr_val = list(json.loads(body).values())[0]
				with open('./results/true.txt', 'a') as file_object:
					file_object.write(f'{uid} {tr_val}'+'\n')
					#file_object.write('Some true value'+'\n')
				print('Successfully saved to true.txt')
			df_pred = pd.read_csv('./results/predictions.txt', delimiter=' ', header =None)
			df_true = pd.read_csv('./results/true.txt', delimiter=' ', header =None)
			df_pred.columns = ['uid','value']
			df_true.columns = ['uid','value']
			df_calc = pd.merge(df_true,df_pred,on='uid', suffixes=['_true','_pred'])
			rmse = mean_squared_error(df_calc['value_true'], df_calc['value_pred'], squared=False)
			print(f'RMSE: {rmse}')

	channel.basic_consume(
		queue='y_predict', on_message_callback=callback, auto_ack=True)

	channel.basic_consume(
		queue='y_true', on_message_callback=callback, auto_ack=True)

	print('...Ожидание сообщений, для выхода нажмите CTRL+C')
	channel.start_consuming()
	
except:
	print(f'Unexpected error: {sys.exc_info()[0]}')
	print('Не удалось подключиться к очереди')