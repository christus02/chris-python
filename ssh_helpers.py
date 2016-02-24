import pexpect

def ssh_login( ip, user = 'root', pas = 'root', prompt = '>', timeout = 30 ):
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
    

def exec_cmd(obj, cmd, prompt = '>', timeout = 30):
     obj.sendline(cmd)
     obj.expect(prompt)
     out = obj.before
     
     return(out);


#Main Program

#Provide IP address for Login
ip_address = ""
ses = ssh_login(ip_address)
out = exec_cmd(ses, "show version")
print out;

