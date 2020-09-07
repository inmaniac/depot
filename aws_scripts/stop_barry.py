#!/bin/python
""" stops aws ec2 instance """
import boto3     
import time

def stop_instance(instid):
    ec2 = boto3.resource('ec2') 
    status = ec2.instances.stop(InstanceIds=[instid]) 
    print("Starting instance: " + instid)
    while ec2.Instance(id='i-0458a7b3dfc1fcde4').state['Name'] != 'stopped':
        time.sleep(1)
        print(ec2.Instance(id='i-0458a7b3dfc1fcde4').state['Name'])
    print("Instance is stopped")

def main():
    id='i-0458a7b3dfc1fcde4'
    stop_instance(id)

if __name__ == "__main__":
    main()

