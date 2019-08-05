#!/bin/bash
echo -n -e "$1" > /dev/ttyACM0
echo $1 >> /tmp/echo_secundaria.log
