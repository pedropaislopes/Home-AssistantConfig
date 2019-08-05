#!/bin/bash
mosquitto_pub -u mqtt_murguis -P 8183094 -t cmnd/auto_suite/SerialSend -m "$1"
echo $1 >> /tmp/echo_suite.log
