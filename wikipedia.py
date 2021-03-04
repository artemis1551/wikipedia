# (C) Artemis
# MIT License

import wikipedia
import os
import time
from time import sleep

#UI
print("Wikipedia Search")
print("Made by Artemis1551")
lang = input("Language Code (ID, IN, DE) : ")
src = input("Search : ")
print(f'Searching for {src} with language code {lang}...')
sleep(2)

#Result
wikipedia.set_lang(lang)
print("Title :")
print(wikipedia.page(src).title)
print("Content :")
print(wikipedia.summary(src, sentences = 2))
print('\n')
print("Categories : ")
print(wikipedia.page(src).categories)