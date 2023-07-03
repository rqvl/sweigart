# CommaCode.py - from Ch3
# rqvl@runbox.com

# define lists
spam = ['apples', 'bananas', 'tofu', 'cats']
eggs = []

def commaCode(list):
    s = ''
    
    #no empty lists
    if len(list) == 0:
        s = 'This list is empty.'
        return s
    
    #create string
    for i in range(len(list)-1):
        s += list[i]
        s += ', '
    s += ' and '
    s += list[-1]
    return s

#test cases
s = commaCode(spam)
print(s)

s = commaCode(eggs)
print(s)