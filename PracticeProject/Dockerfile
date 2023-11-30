FROM ubuntu

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install Flask

WORKDIR /app
COPY . .
CMD [ "python3","-m","flask","run","--host=0.0.0.0"]
# FROM python:3.10.12-alpine3.15
# WORKDIR /app
# COPY . /app
# RUN pip install -r requirements.txt
# EXPOSE 3000
# CMD python ./sample.py