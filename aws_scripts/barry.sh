#!/bin/bash
ip=$1
if [[ -z "$ip" ]]
then
    echo "Usage: $0 <ip>"
fi
ssh -i /home/sinman/.ssh/sinman-202009.pem ubuntu@$ip
