#!/bin/bash

if [[ $(/usr/bin/id -u) -ne 0 ]]; then
  echo "You must run this script as root"
  exit
fi

yum install -y wireshark

echo "Starting tshark..."
nohup tshark -i any -t ad -n > tshark.out 2>&1 &
echo $! > tshark_pid.out

echo "Sleeping to collect data..."
sleep 300m

echo "Killing tshark process..."
kill -9 `cat tshark_pid.out`
rm tshark_pid.out

HOST_IP=`ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'`

echo "Parsing tshark output..."
cat tshark.out | grep -E "DNS .* Standard query response.*" | grep -oE ".*[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" | grep -oE "CNAME.*" > wireshark_dns_capture.out

python wireshark_dns_capture.py wireshark_dns_capture.out

echo "Done!"
