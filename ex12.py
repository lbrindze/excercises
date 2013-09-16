#ex 12.1

def sum_all(*args): return sum(*args)
    
sumnums = (1,2,3,4,5,5,23,6,32,4,65,82,3,64,19,92)

print sum_all(sumnums)

#ex 12.2
import random

def sort_by_length(words):
    t = []
    for word in words:
        rand = random.random()
        t.append((len(word), rand, word))

    t.sort(reverse=True)
            

    res = []
    for length, rand, word in t:
        res.append(word)

    return res


print sort_by_length(["hello", "my", "name", "is", "the", "great", "gatsby"])

#ex 12.3
def histogram(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d

def most_frequent(text):
    hist = make_histogram(text)
    t = []
    for x, freq in hist.iteritems():
        t.append(x, freq)

    t.sort(reverse = True)

    res = []
    for x, freq in t:
        res.append(x)
    return res


#ex 12.4
def word_dict():
    fin = open("/Users/Paul/Documents/words.txt","r")
    words = dict()

    for lines in fin:
        word = lines.strip()
        words[word] = ''
    return words
