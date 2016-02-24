#Author: Raghul Christus
#Date  : 24-Feb-16
#Purpose : Helper Functions for SSH related functionalities

import pexpect

#Function to do a SSH Login
def ssh_login( ip, user = 'nsroot', pas = 'nsroot', prompt = '>', timeout = 30 ):
     cmd = "ssh " + str(user) + "@" + str(ip) 
     s = pexpect.spawn(cmd)
     s.expect
     i = s.expect (['yes/no', 'assword:'])
     if i == 0 :
         s.sendline('yes')
     elif i == 1 :
         s.sendline(pas)
     else :
         print "Unexpected Prompt\n"

     s.expect(prompt)
     return(s);

#Function to execute a command return output    
def exec_cmd(obj, cmd, prompt = '>', timeout = 30):
     obj.sendline(cmd)
     obj.expect(prompt)
     out = obj.before
     
     return(out);

