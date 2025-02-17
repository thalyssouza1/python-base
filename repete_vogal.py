#!usr/bin/env python3

words = []
while True:
    word = input("Digite uma palavra ou [ENTER] para sair: ").strip()
    if not word:
        break

    final_word = ""
    for letter in word: 
        #TODO: Acrescentar letras com acentos usando função
        if letter.lower() in "aeiou":
            final_word += letter * 2
        else:
            final_word += letter
    words.append(final_word)

print(*words, sep="\n")