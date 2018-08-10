
import pyperclip, re

numRegex = re.compile(r'\d+')
print(numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens'))
