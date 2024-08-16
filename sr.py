# In this code we are going to write program to make the os find and restart,shutdown
#r= restart
#s= shutdown
import os
import platform

#shutdown function
def shut_down():
    if platform.system()=='Windows':
        os.system('shutdown -s -f')
    elif platform.system()=='Linux' or platform.system()=='Darwin':
        os.system('shutdown -h now')
    else:
        print("Cant find the os ")

def re_start():
    if platform.system()=='Windows':
        os.system('shutdown -t 0 -r -f')
    elif platform.system()=='Linux' or platform.system()=='Darwin':
        os.system('reboot')
    else:
        print("Can't perform the re-boot")







#main code
input=input("Enter 'r' to shutdown\nEnter 's' to shutdown \n>>>").lower()

if(input=='r'):
    re_start()
elif(input=='s'):
    shut_down()
else:
    print('enter the correct string')

