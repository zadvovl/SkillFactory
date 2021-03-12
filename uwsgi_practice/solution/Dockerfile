FROM python:3.8

EXPOSE 5000

WORKDIR /usr/src/app

COPY requirements.txt ./

COPY uwsgi.ini ./ 

COPY ./src/ ./ 

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["uwsgi", "--ini", "./uwsgi.ini"]

#CMD [ "python", "./ml_server.py"]