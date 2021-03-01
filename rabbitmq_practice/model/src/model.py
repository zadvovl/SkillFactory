"""model.py"""
import pika
import json
import pickle
import numpy as np
import sys

with open('myfile.pkl', 'rb') as pkl_file:
    regressor = pickle.load(pkl_file)

try:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='Features')
    channel.queue_declare(queue='y_predict')

    def callback(ch, method, properties, body):
        uid = list(json.loads(body).keys())[0]
        features = list(json.loads(body).values())[0]

        print(f'Получен вектор признаков {features} с уникальным id {uid}')

        pred = regressor.predict(np.array(features).reshape(1, -1))

        print('I am here!!!')

        channel.basic_publish(exchange='',
                              routing_key='y_predict',
                              body=json.dumps({uid:list(pred[0])}))   
        print(f'Предсказание {pred[0]} отправлено в очередь y_predict c уникальным id {uid}')


    channel.basic_consume(
        queue='Features', on_message_callback=callback, auto_ack=True)

    print('...Ожидание сообщений, для выхода нажмите CTRL+C')
    channel.start_consuming()

except:
    print('Не удалось подключиться к очереди')
    print(f'Unexpected error: {sys.exc_info()[0]}')