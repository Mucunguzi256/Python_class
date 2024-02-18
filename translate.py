from translate import Translator

translator = Translator(to_lang='ja')
try:
    my_file = open('test.txt')
    text = my_file.read()
    translation = translator.translate(text)
    print(translation)
except FileNotFoundError as e:
    print('check file path again')
