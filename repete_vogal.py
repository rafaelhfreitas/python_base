#!/usr/bin/env python

# vowels = ["a", "e", "i", "o", "u"]
list_words = []

while True:
    word = input("Type a word (or press Enter to quit):").strip()
    if not word:
        print(*list_words, sep="\n")
        # for word in list_words:
        #     print(word)
        break
    new_word = ""
    for letter in word:
        new_word += letter * 2 if letter.lower() in "aeiou" else letter
        # if letter.lower() in "aeiou":
        #     new_word += letter * 2
        # else:
        #     new_word += letter

    list_words.append(new_word)
