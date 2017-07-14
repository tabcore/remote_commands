#!/usr/bin/python
import os
import sys
import paramiko

with open('/tmp/pass','r') as file:
        user_name = ''
        secret = file.read().splitlines()[0]
user_name = ''

def ssh_command(user, host,'):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=host,username=user,password=secret)
            std_in, std_out, std_err = ssh.exec_command(sys.argv[3])
            for line in std_out.readlines():
                print line
            for line in std_err.readlines():
                print line
        except :
            print "Authentication failed."
if len(sys.argv) <= 3:
    print 'USAGE: remote_service -c <hostname> command'
else:
    if sys.argv[1] == '-c':
        ssh_command(user_name, sys.argv[2])
