#!/bin/python
""" starts aws ec2 instance """
import boto3     
import time

def status_instance(instid):
    ec2 = boto3.resource('ec2') 
    print(ec2.Instance(id='i-0458a7b3dfc1fcde4').state['Name'])
    ip = ec2.Instance(id=instid).public_ip_address
    print(f"public ip is: {ip}")

def main():
    id='i-0458a7b3dfc1fcde4'
    status_instance(id)

if __name__ == "__main__":
    main()

