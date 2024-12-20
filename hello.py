#!/usr/bin/env python3
"""Hello World multi linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Ou informe através do CLI argument '--lang'

Ou o usuário terá que digitar manualmente o idioma.

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Thalys Souza"
__license__ = "Unlicensed"

import os
import sys

arguments = {"lang": None, "count": 1,} 

for arg in sys.argv[1:]: 
    try:
        key, value = arg.split("=")
    except ValueError as e:
        #TODO logging
        print(f"[ERROR] {str(e)}")
        print("You need to use '='")
        print(f"You passed: {arg}")
        print("Try with --key=value")
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()

    #Validação
    if key not in arguments:
        print(f"Invalid option: '{key}'")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    #TODO usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language: ")

current_language = current_language[:5] # fatia para pegar os perimeiros 5 caracteres

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

# EAFP
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")   
    print(f"Language is invalid. Chosse from:{list(msg.keys())}")
    sys.exit(1)
    
print(msg[current_language] * int(arguments["count"]))
