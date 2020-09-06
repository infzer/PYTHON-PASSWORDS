import random
import time
import string
import os
import webbrowser

def clear():
       # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def contra():
    
    clear()
    print(menupass)
    
    gua = (input("YOU WANT TO SAVE THE PASSWORD ON TXT | Y = YES / N = NO | "))
    
    if gua == "Y":

        f=open("PASSWORD.txt","w", encoding='utf-8')

        opcionsepass = int (input("TYPE HOW LONG YOU WANT THE PASSWORD - "))
        for x in range(opcionsepass):
            y = ''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for _ in range(opcionsepass))
            f.write(y)
            print ("- - - - - - - - - - - - - - - - - - - - - - - - - ")
            print ("THE PASSWORD IS ----->",y)
            print ("- - - - - - - - - - - - - - - - - - - - - - - - - ")
        f.close()
        input("THANK YOU | IF YOU LIKE IT SHARE IT / PASSWORD SAVE AT THE RUTE OF THE PROGRAM IN PASSWORD.TXT   |   PRESS ENTER TO EXIT")
    
    if gua == "N":

        opcionsepass = int (input("TYPE HOW LONG YOU WANT THE PASSWORD - "))
        for x in range(opcionsepass):
            y = ''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for _ in range(opcionsepass))
        
        print ("- - - - - - - - - - - - - - - - - - - - - - - - - ")
        print ("THE PASSWORD IS ----->",y)
        print ("- - - - - - - - - - - - - - - - - - - - - - - - - ")

        input("THANK YOU | IF YOU LIKE IT SHARE IT    |   PRESS ENTER TO EXIT")

def email():
    # webbrowser.open_new
    clear()
    print(menuemail)
    print(opemail)
    ope=int(input("OPCION | "))
    
    if ope == 1:
        clear()
        print("-----------------------------------------------")
        print("YOUR PREDEFAULT NAVIGATOR IS GOING TO OPEN | ")
        print("-----------------------------------------------")
        time.sleep(3)
        webbrowser.open_new("http://www.yopmail.com")
        input("THANK YOU | IF YOU LIKE IT SHARE IT    |   PRESS ENTER TO EXIT")


    if ope == 2:
        clear()
        print("-----------------------------------------------")
        print("YOUR PREDEFAULT NAVIGATOR IS GOING TO OPEN | ")
        print("-----------------------------------------------")
        time.sleep(3)
        webbrowser.open_new("https://correotemporal.org/")
        input("THANK YOU | IF YOU LIKE IT SHARE IT    |   PRESS ENTER TO EXIT")

    if ope == 3:
        clear()
        print("-----------------------------------------------")
        print("YOUR PREDEFAULT NAVIGATOR IS GOING TO OPEN | ")
        print("-----------------------------------------------")
        time.sleep(3)
        webbrowser.open_new("https://temp-mail.org/es/")
        input("THANK YOU | IF YOU LIKE IT SHARE IT    |   PRESS ENTER TO EXIT")

    if ope == 4:
        clear()
        print("-----------------------------------------------")
        print("YOUR PREDEFAULT NAVIGATOR IS GOING TO OPEN | ")
        print("-----------------------------------------------")
        time.sleep(3)
        webbrowser.open_new("https://bupmail.com/es/")
        input("THANK YOU | IF YOU LIKE IT SHARE IT    |   PRESS ENTER TO EXIT")
   
    if ope == 5:
        clear()
        print("-----------------------------------------------")
        print("YOUR PREDEFAULT NAVIGATOR IS GOING TO OPEN | ")
        print("-----------------------------------------------")
        time.sleep(3)
        webbrowser.open_new("https://www.mohmal.com/es")
        input("THANK YOU | IF YOU LIKE IT SHARE IT    |   PRESS ENTER TO EXIT")

def google():
    clear()
    print('''
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                THIS SECTION IS UNDER

██████╗░███████╗██╗░░░██╗███████╗██╗░░░░░░█████╗░██████╗░███╗░░░███╗███████╗███╗░░██╗████████╗
██╔══██╗██╔════╝██║░░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝████╗░██║╚══██╔══╝
██║░░██║█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░██║░░██║██████╔╝██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░
██║░░██║██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░██║░░██║██╔═══╝░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░
██████╔╝███████╗░░╚██╔╝░░███████╗███████╗╚█████╔╝██║░░░░░██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░
╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝╚══════╝░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    ''')
    input("THANK YOU | IF YOU LIKE IT SHARE IT    |   PRESS ENTER TO EXIT")


menu = '''
----------------------------------------------------------------------
    	            STRONG PASSWORD GENERATOR 
                            MADE BY
            
▒█▀▀▄ ▀█▀ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀▀ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀▀ ▒█▀▀█ 
▒█░▒█ ▒█░ ░▀▀▀▄▄ ▒█░░░ ▒█░░▒█ ░▒█░░ ▒█▀▀▀ ░▀▀▀▄▄ ░▒█░░ ▒█▀▀▀ ▒█▄▄▀ 
▒█▄▄▀ ▄█▄ ▒█▄▄▄█ ▒█▄▄█ ▒█▄▄▄█ ░▒█░░ ▒█▄▄▄ ▒█▄▄▄█ ░▒█░░ ▒█▄▄▄ ▒█░▒█

                     ANTI BRUTEFORCE ATTAKS 
----------------------------------------------------------------------
'''

opciones = '''
    1 - GENERATE STRONG PASSWORD
    2 - GENERATE TEMPORAL EMAIL
    3 - GENERATE ACCOUNT FROM THIS SERVICES
'''

menupass = '''
------------------------------------------------------------------

▒█▀▀▄ ▀█▀ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀▀ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀▀ ▒█▀▀█ 
▒█░▒█ ▒█░ ░▀▀▀▄▄ ▒█░░░ ▒█░░▒█ ░▒█░░ ▒█▀▀▀ ░▀▀▀▄▄ ░▒█░░ ▒█▀▀▀ ▒█▄▄▀ 
▒█▄▄▀ ▄█▄ ▒█▄▄▄█ ▒█▄▄█ ▒█▄▄▄█ ░▒█░░ ▒█▄▄▄ ▒█▄▄▄█ ░▒█░░ ▒█▄▄▄ ▒█░▒█
            
                    PASSWORD GENERATOR MODE
------------------------------------------------------------------
'''



menuemail = '''
------------------------------------------------------------------

▒█▀▀▄ ▀█▀ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀▀ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀▀ ▒█▀▀█ 
▒█░▒█ ▒█░ ░▀▀▀▄▄ ▒█░░░ ▒█░░▒█ ░▒█░░ ▒█▀▀▀ ░▀▀▀▄▄ ░▒█░░ ▒█▀▀▀ ▒█▄▄▀ 
▒█▄▄▀ ▄█▄ ▒█▄▄▄█ ▒█▄▄█ ▒█▄▄▄█ ░▒█░░ ▒█▄▄▄ ▒█▄▄▄█ ░▒█░░ ▒█▄▄▄ ▒█░▒█
            
                        TEMPORAL EAMIL MODE
------------------------------------------------------------------
'''



opemail = '''
   IN THIS PART I TRY SOME OF THIS SO IF THEY PUT GOOD I DONT TRY IT BUT IT LOOK GOOD | SO TAKE CARE ABOUT IT 

   1 - yopmail (THIS MAIL IS PARCHED IN SOO MANY SITES SO PERSONALLY I THINK IS GOOD BUT YOU NEED LUCKY)
   2 - correotemporal.org (GOOD)
   3 - tempmail (GOOD)
   4 - bupmail (GOOD ?)
   5 - mohmal (GOOD ?)
---------------------------------------------------------------------------------------------------------------
'''


print(menu)
print(opciones)
op = int(input("OPCION | "))

if op == 1:
    contra()

if op == 2:
    email()

if op == 3:
    google()


