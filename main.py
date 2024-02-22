from colorama import Fore 
import sys 
import time 
colors=[Fore.RED,Fore.GREEN,Fore.BLUE,Fore.YELLOW,Fore.MAGENTA,Fore.LIGHTRED_EX,Fore.LIGHTMAGENTA_EX,Fore.BLACK,Fore.CYAN,Fore.RESET]
scythe_ascii_art=f'''
{colors[-3]}
         ____________________________      
        /_                           \ 
           \ ________________________ \ 
            |__|                     \/
            |__|                 
            |__|       
            | {colors[-2]}○{colors[-3]}|
            |__|
            |__|
            |__|
            | {colors[-2]}○{colors[-3]}|
            |__|
            |__|
            |__|
            | {colors[-2]}○{colors[-3]}|
            |{colors[5]}__{colors[-3]}|
            |{colors[5]}\/{colors[-3]}|
            |{colors[5]}__{colors[-3]}|
            |{colors[5]}\/{colors[-3]}|
            |{colors[5]}__{colors[-3]}|
            |{colors[5]}\/{colors[-3]}|
            ||{colors[0]}-{colors[-3]}|
            ||{colors[0]}-{colors[-3]}|
            ||{colors[0]}-{colors[-3]}|
            \__/'''
print(scythe_ascii_art)