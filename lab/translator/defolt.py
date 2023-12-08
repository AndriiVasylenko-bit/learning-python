from translate import Translator

def translate_russian_to_ukrainian(word):
    translator = Translator(to_lang="uk")
    translation = translator.translate(word)
    return translation

# Example usage
russian_word = "Привет"  # Replace with the word you want to translate
ukrainian_translation = translate_russian_to_ukrainian(russian_word)

print(f"Russian: {russian_word}")
print(f"Ukrainian: {ukrainian_translation}")