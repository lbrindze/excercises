"""
fruit = 'banana'


#ex 8.1
def reverse (strs):
    index = len(strs)-1
    while index >=0:
        letter = strs[index]
        print (letter)
        index = index - 1       
        
reverse (fruit)

#ex 8.2
prefixes = 'JKLMNOPQ'
suffix = 'ack'

def duck(pres):
    if pres == 'O' or pres == 'Q':
        pres = pres + 'u'
    return(pres)

for letter in prefixes:
        print (str(duck(letter)) + suffix)

#ex 8.4

def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

#ex8.5

def char_count(word,char):
    count = 0
    for letter in word:
        if letter == char:
            count += 1
    print (count)
    
char_count('banana', 'a')
char_count('banana', 'b')
char_count('banana', 'n') 

#ex8.6
def char_count_trav(word, char):
    count = 0
    index = find(word, letter, 0)
    while index !=-1:
        count += 1
        index = find(word, letter, index)
        print(index)
    return count

#ex8.7
'bananas'.count('a')

#ex8.10
def is_palindrome(word):
    return word == word[::-1]
"""

#ex8.12
def uconvert(n,m):
    n = ((n-97)+m)%26 + 97
    return n
    

def rotate_word(strings, n):
    strings = strings.lower()
    cipher = ''
    
    for i in strings:
        ntext = ord(i)
        ctext = uconvert(ntext, n)
        cipher += chr(ctext)

    return str(cipher) + "\n"
        
print(rotate_word ("cheer", 7))
print(rotate_word ("melon", -10))
print(rotate_word ("agave", 13))
print(rotate_word ("Ubj pna lbh gryy na rkgebireg sebz na vagebireg ng AFN", 13))
