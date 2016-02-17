# docker-django-demo
Demo Django application using docker

The goal of this demo, is to mimic a real life production application where there are
multiple parts.


There are 5 parts to this demo app:
- Web container
- Worker container
- Cron container
- redis container
- postgresql container


# Docker-compose
To get started, you need to do the following.

1. install docker-toolbox

https://www.docker.com/products/docker-toolbox

2. create a new docker virtual machine called `demo`

$ docker-machine create --driver virtualbox demo

3. Setup your shell

$ eval "$(docker-machine env demo)"

4. Clone this repo somewhere.

$ git clone https://github.com/kencochrane/docker-django-demo.git

5. docker compose up the env.

$ docker-compose up -d

6. The first time, you need to setup the database, by running this command.

$ docker-compose run web python /home/docker/dockerdemo/manage.py migrate

7. Find out the IP, and connect from browser.

$ docker-machine ip demo
