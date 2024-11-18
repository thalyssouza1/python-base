#!usr/bin/env python3
import os
import sys

 #LBYL - Look before you leap

if os.path.exists("names.txt"):
    print("O arquivo existe.")
    input("...") #race condition
    names = open("names.txt").readlines()
else: 
    print("[ERROR] File 'names.txt' not found.")
    sys.exit(1)

if len(names) >= 3:
    print(names[2])
else:
    print("[ERROR] Missing name in list.")
    sys.exit(1)
