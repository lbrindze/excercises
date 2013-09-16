#ex10.1

def nested_sum(lists):
    sums = []
    for each_list in lists:
        sums.append(sum(each_list))

    return sum(sums)

testa = [[1,2,3],[3,4],[5,6,7]]

print nested_sum(testa)

#ex10.2

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(lists):
    res = []
    for t in lists:
        res.append(capitalize_all(t))
    return res

testb = [['apples','oranges','olives'], ['fruit', 'first', 'finns'], ['plan', 'peace', 'ports']]

print capitalize_nested(testb)

#ex10.3

def culm_sum(ns):
    res = []
    sums = 0
    for i in ns:
        sums+=i
        res.append(sums)
    return res

testc = [1,2,3]
print culm_sum(testc)

#ex10.4
def middle(xs):
    res = xs[1:len(xs)-1]
    return res

x = [1,2,3,4,5,6]
print middle(x)

#ex10.5
def chop(xs):
    del xs[0]
    del xs[len(xs)-1]
    
#ex10.6
def is_sorted(ts):
    orig = ts[:]
    ts.sort()
    if ts == orig:
        return True
    else:
        return False

lista = [1,2,2]
listb = ['b','a']

print is_sorted(lista)
print is_sorted(listb)

#ex10.7
def is_anagrams(a, b):
    t = list(a)
    s = list(b)
    t.sort()
    s.sort()
    if t == s:
        return True
    else:
        return False

ang1 = 'babe'
ang2 = 'abbe'
ang3 = 'sole'
ang4 = 'lose'
ang5 = 'bob'
ang6 = 'sucks'

print is_anagrams(ang1,ang2)
print is_anagrams(ang3,ang4)    
print is_anagrams(ang5,ang6)

#ex10.8
import random

def has_duplicates(xs):
    s = xs[:]
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False 

def birthday_class_gen(n):
    bclass = []
    for i in range (n):
        b = random.randint(1,365)
        bclass.append(b)
    return bclass

def samplizer(bclas_size, samples):
    count = 0
    for i in range(samples):
        gs = birthday_class_gen(bclas_size)
        if has_duplicates(gs) == True:
            count+=1
    return count

num_sims = 1000
num_studs = 23
count = samplizer(num_studs, num_sims)
percent = float(count)/float(num_sims) * 100

print "After %d simulations" %num_sims
print "with %d students in each class" %num_studs
print "there were %d classes with at least one match" %count
print str(percent)+"% of classes had duplicates"

#ex10.9

def remove_duplicates(xs):
    res = []
    s = xs[:]
    s.sort()
    last = len(s)-1
    for i in range(last):
        if s[i] != s[i+1]:
            res.append(s[i])
    res.append(s[last]) #necisary last step or else final number is not included
    return res

#ex10.10
import time


def appendtest():
    words = open('/Users/Paul/Documents/words.txt', 'r')
    start = time.time()
    wlist = []
    for line in words.readlines():
        word = line.strip()
        wlist.append(word)
    elapsed = time.time()-start
    words.close()
    print wlist[34]
    print len(wlist)
    #return 'Appends Completed in: ' + str(elapsed)
    return wlist
"""
def concatest():
    words = open('/Users/Paul/Documents/words.txt', 'r')
    start = time.time()
    wlist = []
    for line in words.readlines():
        word = line.strip()
        wlist = wlist + [word]
    elapsed = time.time()-start
    words.close()
    print wlist[34]
    print len(wlist)
    return 'Concats Completed in: ' + str(elapsed)
"""

words = appendtest()
words.sort()

#ex10.11
"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from bisect import bisect_left


def in_bisect(word_list, word):
    i = bisect_left(word_list, word)
    if i != len(word_list) and word_list[i]==word:
        return True
    else:
        return False

#ex10.12


def reverse_pair(word_list, word):
    """Checks whether a reversed word appears in word_list.

    word_list: list of strings
    word: string
    """
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)
        
"""
if __name__ == '__main__':
    word_list = words
    
    for word in word_list:
        if reverse_pair(word_list, word):
            print word, word[::-1]"""

"""
def find_rp(vs):
    res = []
    for wo in vs:
        if in_bisect(words, vs[::-1]) == True:
            res.append(wo)
    print res

find_rp(words)
"""
#ex10.13

def interlock(word_list, word):
    """Checks whether a reversed word appears in word_list.

    word_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds) 
        

def interlock_general(word_list, word, n=3):
    """Checks whether a reversed word appears in word_list.

    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
    return True
        

if __name__ == '__main__':
    word_list = words
    
    for word in word_list:
        if interlock(word_list, word):
            print word, word[::2], word[1::2]

    for word in word_list:
        if interlock_general(word_list, word, 3):
            print word, word[0::3], word[1::3], word[2::3]
