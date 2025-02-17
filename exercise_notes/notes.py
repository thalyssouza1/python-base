#!usr/bin/env python3
""" Bloco de notas

$ notes.py new "Minha nota"
tag: tech
text:
Anotação geral sobre carreira de tecnologia.

$ notes.py read tech
...
...
"""
__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage.")
    print(f"You must specify a subcommand -> {cmds} + your desired title.")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command: {arguments[0]}")

if arguments[0] == "read": #leitura das notas
    for line in open(filepath): #abre o arquivo para leitura iterando linha por linha
        title, tag, text = line.split("\t") #divide a linha em 3 partes por \t e salva nas variáveis 
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()

if arguments[0] == "new":  # criação das notas
    try:
        title = arguments[1]
        text = [
            f"{title}",
            input("tag: ").strip(),
            input("text:\n").strip(),
        ]
    except IndexError:
        print("Error: Title is missing.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)
    
    #\t tsv = tab separated values
    with open(filepath, "a") as file_: #abre o arquivo para escrita
        file_.write("\t".join(text) + "\n")