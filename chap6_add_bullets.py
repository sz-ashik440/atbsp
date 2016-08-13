import pyperclip

text = pyperclip.paste()
#print(text)
str = text.split('\n')

for index in range(len(str)):
    str[index] = '* ' + str[index]

text = '\n'.join(str)

pyperclip.copy(text)
