#!/bin/bash

crontab /home/docker/config/etc/crontab

/usr/sbin/cron -f
