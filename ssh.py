#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
     
import pexpect
import sys
     
def ssh_cmd(username, ip, passwd, cmd): 
    ret = -1 
    ssh = pexpect.spawn('ssh %s@%s' % (username, ip))
    ssh.logfile=sys.stdout
    try:
        i = ssh.expect(['password:', 'continue connecting (yes/no)?', '$'], timeout=5)
        if i == 0 :
            print("asdfasf")
            ssh.sendline(passwd)
            ssh.expect('$')
            ssh.sendline(cmd)
        elif i == 1: 
            ssh.sendline('yes\n') 
            ssh.expect('password: ') 
            ssh.sendline(passwd) 
            ssh.sendline(cmd) 
            r = ssh.read() 
            print(r) 
            ret = 0
        elif i == 2:
            print('1234')
            ssh.sendline(cmd)
            r = ssh.read()
            print(r)
    except pexpect.EOF: 
        print("EOF") 
        ssh.close() 
        ret = -1 
    except pexpect.TIMEOUT: 
        print("TIMEOUT") 
        ssh.close() 
        ret = -2 
    return ret

#ssh_cmd('chs', '10.74.122.172', 'chs123!', 'ls')
ssh_cmd('wuji', '10.74.123.147', 'c', 'ls')

