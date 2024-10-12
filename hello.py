#!/usr/bin/env python3
"""Hello World multi linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Thalys Souza"
__license__ = "Unlicensed"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, world!"

if current_language =="pt_BR":
	msg = "Olá, mundo!"
elif current_language == "it_IT":
	msg = "Ciao, mondo!"
elif current_language == "es_SP":
	msg = "Hola, mundo!"
elif current_language == "fr_FR":
	msg = "Bonjour, monde!!"
	 
print(msg)