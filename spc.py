# import module
import os
import time
import random

#----------------------
#Gloable varable
cmd='mode 100,19'
one_spc=0x20
space=chr(one_spc)
cmd_clear='cls || clear'
def_ter_col='07'
card=['Ston','Paper','Scissor']
user_ans=int
comp_ans=int
user_point=int
comp_point=int
gvalu=int
#----------------------------
#Comp_valu_part finction
def comp_val_sel(user_ans):
    global comp_ans
    global user_point
    global comp_point

    
    comp_ran=random.randint(0,3)
    comp_ans=comp_ran
    if(comp_ans<user_ans):
        print('user win')
        time.sleep(2.5)
        wait_fun()
    elif(comp_ans>user_ans):
        print("comp win")
        time.sleep(2.5)
        wait_fun()
    else:
        print("draw match")
        time.sleep(2.5)
        wait_fun()
#-------------------------------------

#waithing time
def wait_fun():
    os.system(cmd_clear)
    for i in range(1,4,1):
        print(space*25+f'{i}')
        time.sleep(1)
        os.system(cmd_clear)


#----------------------------------

#game_area_functiom
def game_usr_fun(round_va):
    global user_ans
    global usr_sel
    global gvalu
    for i in range(0,round_va,1):
        os.system(cmd_clear)
        print("""
        1.Ston
        2.Paper
        3.Scissor
    """)
        try:
            usr_sel=int(input('>>>'))
            
        except:
            print('Enter the correct number')
            time.sleep(5)
            os.system(cmd_clear)
            exit()
        try:
            user_ans=usr_sel-1
            comp_val_sel(user_ans)
        except:
            print('enter correct value between (1,2,3)')
            time.sleep(3)
            os.system(cmd_clear)
            game_usr_fun()
            
    #final_out()
#-------------------------------------------------------

#menu function
def menu_cho(valu):
    global gvalu
    gvalu=valu
    if valu==0:
        help_menu()
    elif valu>0:
        game_usr_fun(valu)
    elif valu<0:
        print('exit')
    else:
        menu_cho(0)
    
#---------------------------------------------------
# Help mode
def help_menu():
    color=str
    os.system(cmd_clear)
    print('Enter 1 to Return the main menu')
    print('Enter 0 to change color mode ')
    help_mod_val=int(input(space*10+">>>"))
    if help_mod_val == 1:
        os.system(cmd_clear)
        main()
    elif help_mod_val == 0:
        os.system(cmd_clear)
        print(space*45+'Color mode')
        print(space*20+"""
    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White
              
Example: "fc" produces light red on bright white
""")
        color=str(input('>>>'))
        os.system(f'color {color}')
        print("""
Enter y to save
Enter d to back to default
    
""")
        save_col=str(input('>>>'))
        if save_col=='y':
            help_menu()
        elif save_col=='d':
            os.system(f'color {def_ter_col}')
            help_menu()
        else:
            help_menu()
        
        print("test condit for color")
        time.sleep(5)

# -------------------------      

#main finion 
def main():
    os.system(cmd)
    print(space*40+'Welcome To The Game')
    print('TO Exit the Game -> -1')
    print('TO Enter the Help -> 0')
    menu_valu=int(input(space*10+'>>>'))
    menu_cho(menu_valu)
    
#--------------------------------------------

#main funtion call
main()