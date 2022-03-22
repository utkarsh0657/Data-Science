string1 = input('Enter a word: ')
string2 = ''
length = len(string1) - 1

while length >= 0:
    string2 = string2 + string1[length]
    length = length - 1
print(string2)