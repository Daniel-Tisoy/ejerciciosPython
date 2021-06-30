import string

morse = ['.- ', '-... ', '-.-. ', '-.. ', '. ', '..-. ', '--. ',
         '.... ', '.. ', '.--- ', '-.- ', '.-.. ', '-- ', '-. ', '--- ',
         '.--. ', '--.- ', '.-. ', '... ', '- ', '..- ', '...- ', '.-- ',
         '-..- ', '-.-- ', '--.. ']

abc = list(string.ascii_uppercase)

dict_morse = dict()
for i in range(len(abc)):
    dict_morse.setdefault(abc[i], morse[i])

dict_morse[' '] = '/ '
string_pru = 'We need help this is a mesagge in english'.upper()
translate = list()
for letra in string_pru:
    translate.append(dict_morse.get(letra))

print(''.join(translate))
