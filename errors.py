#!usr/bin/env python3
import os
import sys

 #EAFP - Easier to ask for forgiveness than permission

try:
    names = open("names.txt").readlines() #FileNotFoundError
except FileNotFoundError as e: 
    print(f"{str(e)}")
    sys.exit(1)
    # TODO: usar retry
else:
    print("Sucesso!!") #else nao é obrigatorio e vai ser executado caso nao tenha erro
finally:
    print("Execute isso sempre!") #finally sempre vai ser executado

try:
    print(names[2])
except:
    print("[ERROR] Missing name in list.")
    sys.exit(1)
