""" import random as omg_so_random
#part of modules
from random import choice,randint """
# import pyfiglet
# from termcolor import colored
# text = colored("hi there",color="red")
# #pyfiglet.figlet_format(text)
# with open('example.txt','w') as fileobject:
#     fileobject.write(colored("hi there",color="red"))
# print (text)
# print("hi am there")


# print("\033[0;37;40m Normal text\n")
# print("\033[2;37;40m Underlined text\033[0;37;40m \n")
# print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
# print("\033[3;37;40m Negative Colour\033[0;37;40m \n")
# print("\033[5;37;40m Negative Colour\033[0;37;40m\n")
# print("\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
# print("\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
# print("\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
# print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
# print("\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
# print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
# print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
# print("\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
# print("\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")



#module-dunder--plscheckout sayhi and saysup files
#---init--- checkout article and write here

# https://www.analyticsvidhya.com/blog/2021/05/30-useful-methods-from-python-os-module/

# import sys
import os
import sys
  
# print("This is the name of the program:", sys.argv[1])
  
# print("Argument List:", str(sys.argv))
# searchdir = "C:\\Users\\7330728\\Downloads"

# # for path,dir,files in os.walk(searchdir):
# #     print(path)
# #     # print(dir)
# #     for file in files:
# #         print(file)
# #         break


# print(os.getcwd())
# print(os.chdir('C:\\'))
# print(os.getcwd())


#files properties through os module

# os.stat(abs_path).st_size  - here we are printing size of file





#bytearray and bytes

# ba = bytearray.fromhex("AA55CC3301AA55CC330F234567")
# print(ba.reverse())
# #how to change the number to binary

# def decimalToBinary(n):
#     return "{0:b}".format(int(n))
# #2nd method
# print(f"{42:b}")

# print(bin(54).replace('0b',''))

# bytenum = (1024).to_bytes(2, 'big')
# print(bytenum)


#little endian and big endian

# print(sys.byteorder,sys.version,sys.path)


# import logging

# logger = logging.getLogger()

# logger.debug('debug info')

# import math,time

# delay = time.time()+60*60





#bit operators

# https://www.techiedelight.com/bit-hacks-part-3-playing-rightmost-set-bit-number/
# https://www.techiedelight.com/bit-hacks-part-4-playing-letters-english-alphabet/
