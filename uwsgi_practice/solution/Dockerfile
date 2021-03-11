FROM nginx:latest as builder

WORKDIR /usr/src/app 

FROM python:3.8



COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./src/ . 

CMD [ "python", "./ml_server.py"]