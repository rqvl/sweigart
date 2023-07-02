# CommaCode.py - from Ch3
# rqvl@runbox.com

# define a list
spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(list):
    s = ''
    for i in range(len(list)-1):
        s += list[i]
        s += ', '
    s += ' and '
    s += list[-1]
    
    return s

s = commaCode(spam)
print(s)
