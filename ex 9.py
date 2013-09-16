fin = open('/Users/Paul/Documents/words.txt')

word = fin.readline()
line = word.strip()

#ex9.1
"""
for line in fin:
    word1 = line.strip()
    if len(word1)>=20:
        print (word1)
"""

#ex 9.2 no 'e's
def has_no_e(worde):
    for char in worde:
        if 'e' in worde or 'E' in worde:
            return False
        else:
            return True

def percent(n):
    print (str(n))
    n = (n/113809) * 100
    print(str(n) + "% of words comply")


def avoids1():
    index = 0
    for line in fin:
        word = line.strip()
        if has_no_e(word) == True:
            index += 1
    return index

#ex 9.3 avoid fun
#forbidden = input ("input characters:")


def avoids(words, forbid):
    for j in forbid:
        for char in words:



            if j in words:
                return False
                break
    return True 
            
def wordretreive():
    index = 0
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden) == True:
            index += 1
    return index

#9.4  use only
#inputs = input("insert Characters: ")

def use_only (word, char):
    for k in word:
        if not(k in char):
            return False
            break
    return True

#9.5
"""
another solution for uses all could implement use_only since it is really just the reverse of use_only
ie:

def uses_all (word, char):
    return uses_only(char, word)

"""

def uses_all (word, char):
    for k in char:
        if not(k in word):
            return False
            break
    return True
"""
there are 598 words that contain all the vowels
and only 42 contain all the vowels including y
"""

#9.6
def is_abecedarian(word):
    word = word.lower()
    j = word[0]
    for i in word:
        if i>=j:
                result = True
                j = i
        else:
                result = False
                break
    return result


#ex 9.7

def three_consec(word):
    if len(word) < 6:
        return False
    if word[0] == word[1] and word[2] == word [3] and word[4] == word[5]:
        return True
    return three_consec(word[1:])
"""
for line in fin:
    word1 = line.strip()
    if three_consec(word1) == True:
        print (word1) """

#ex 9.8

def is_palindrome(word):
    return word == word[::-1]

def regulate(number):
    stn = str(number)
    if len(stn) < 6:
        stn = ('0'*(6 - len(stn))+stn)
    return stn

def puzzler(n):
    if is_palindrome(regulate(n+3)) == True:
        if is_palindrome(regulate(n+2)[1:5]) == True:
            if is_palindrome(regulate(n+1)[1:]) == True:
                if is_palindrome(regulate(n)[2:]) == True:
                    print (n)
    


for x in range(999999):
    puzzler(x)


""" allen's solution:
This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

    http://www.cartalk.com/content/puzzler/transcripts/200803


def has_palindrome(i, start, len):
    return True if the integer i, when written as a string,
    contains a palindrome with length (len), starting at index (start).
    
    s = str(i)[start:start+len]
    return s[::-1] == s
    
def check(i):
    check whether the integer (i) has the properties described
    in the puzzler
    
    return (has_palindrome(i, 2, 4)   and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6))

def check_all():
    enumerate the six-digit numbers and print any that satisfy the
    requirements of the puzzler

    i = 100000
    while i <= 999999:
        if check(i):
            print i
        i = i + 1

print 'The following are the possible odometer readings:'
check_all()
print


"""

#ex 9.9 taken from Allen B. Downey's solution
def str_fill(i, len):
    """return the integer (i) written as a string with at least
    (len) digits"""
    return str(i).zfill(len)


def are_reversed(i, j):
    """ return True if the integers i and j, written as strings,
    are the reverse of each other"""
    return str_fill(i,2) == str_fill(j,2)[::-1]


def num_instances(diff, flag=False):
    """returns the number of times the mother and daughter have
    pallindromic ages in their lives, given the difference in age.
    If flag==True, prints the details."""
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff
        if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
            count = count + 1
            if flag:
                print (daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count
    

def check_diffs():
    """enumerate the possible differences in age between mother
    and daughter, and for each difference, count the number of times
    over their lives they will have ages that are the reverse of
    each other."""
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print (diff, n)
        diff = diff + 1

print ('diff  #instances')
check_diffs()

print()
print ('daughter  mother')
num_instances(18, True)




