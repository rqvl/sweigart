# CommaCode.py - from Ch3
# rqvl@runbox.com

# define lists
spam = ['apples', 'bananas', 'tofu', 'cats']
eggs = []

def commaCode(ham):
    s = ''
    
    #no empty lists
    if len(ham) == 0:
        s = 'This list is empty.'
        return s
    
    #create string
    for i in range(len(ham)-1):
        s += ham[i] + ', '
    s += 'and ' + ham[-1] + '.'
    return s

#test cases
s = commaCode(spam)
print(s)

s = commaCode(eggs)
print(s)