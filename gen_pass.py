import random, sys, pyperclip

length = 0

if len(sys.argv) < 2:
    length = 14    

else:
    length = int(sys.argv[1])

str = ''

for i in range(length):
    str += chr(random.randrange(32,127,1))

pyperclip.copy(str)
