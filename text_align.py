import os
rows, columns = os.popen('stty size', 'r').read().split()

str = 'Ashik'
print(str.rjust(int(columns), ' '))
