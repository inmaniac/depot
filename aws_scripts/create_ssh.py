#!/bin/python
""" starts aws ec2 instance """
import boto3     
import time
import subprocess

def start_instance(instid):
    ec2 = boto3.resource('ec2') 
    status = ec2.instances.start(InstanceIds=[instid]) 
    print("Starting instance: " + instid)
    while ec2.Instance(id='i-0458a7b3dfc1fcde4').state['Name'] != 'running':
        time.sleep(2)
        print(ec2.Instance(id='i-0458a7b3dfc1fcde4').state['Name'])
    ip = ec2.Instance(id=instid).public_ip_address
    print(f"public ip is: {ip}")
    return(ip)

def status_instance(instid):
    ec2 = boto3.resource('ec2')
    state = ec2.Instance(id='i-0458a7b3dfc1fcde4').state['Name']
    ip = -1
    if state == 'running':
        ip = ec2.Instance(id=instid).public_ip_address
    print(f"public ip is: {ip}")
    return ip

def create_ssh_script(keyfile,ipaddr,user='ubuntu'):
    sshstr=f"ssh -i {keyfile} {user}@{ipaddr}"
    with open('/home/sinman/ssh_barry.sh','wt') as sshf:
        sshf.write("#!/bin/bash\n")
        sshf.write(sshstr)
        sshf.write('\n')
    try:
        stat = subprocess.run(['/usr/bin/chmod','755','/home/sinman/ssh_barry.sh'])
        print("Created ssh_barry.sh script") 
    except:
        print("Couldn't create ssh_barry.sh script")

def main():
    keyfile='/home/sinman/.ssh/sinman-202009.pem'
    id='i-0458a7b3dfc1fcde4'
    ipaddr = status_instance(id)
    if ipaddr != -1:
        create_ssh_script(keyfile,ipaddr)

if __name__ == "__main__":
    main()

