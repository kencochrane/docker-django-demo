FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y cron
RUN mkdir -p /home/docker
WORKDIR /home/docker
ADD requirements.txt /home/docker
RUN pip install -r /home/docker/requirements.txt
ADD . /home/docker
