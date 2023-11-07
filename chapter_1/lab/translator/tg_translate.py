from trnaslate import Translator
import re

new_lines = []

def translate_russian_to_ukrainian(word):
    translate = Translator(to_lang="uk")
    translation = translate.translate(word)
    return translation

with open('translatro/messages.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        thins = re.findall('<span aria-hidden="true">([^<]+)</span>', line)
        if len(thins) < 1 : continue
        new_lines.append(thins)
print(new_lines)