#Dictionary excercises

#ex11.1
def word_dict():
    fin = open("/Users/Paul/Documents/words.txt","r")
    words = dict()

    for lines in fin:
        word = lines.strip()
        words[word] = ''
    return words
#ex11.2

def histogram(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d

dic1 = histogram('tycoon')

#ex11.2

def print_hist(h):
    ks = h.keys()
    ks.sort()
    for c in ks:
        print c, h[c]

print_hist(dic1)

#ex11.3

def reverse_lookup(d, v):
    res = []
    for k in d:
        if d[k] == v:
            res.append(k)
    if res == []:
        raise ValueError
    else:
        return res
#ex11.4
    
def invert_dict(d):
    inverse = dict()
    for key, val in d.iteritems():
        setdefault(val, []).append(key)
    return inverse
#ex11.7
cache = {}

def ack (m,n):
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m-1,1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ack(m-1, ack(m, n-1))
        return cache[m, n]

#ex11.8
"""
weak form rsa takes input as number and exports number
keys gen could use revising
"""
import random
import fractions

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
    
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def key_gen(p,q):
    n = p*q
    n2 = (p-1)*(q-1)
    while True:
        e = random.randint(1,n2)
        if fractions.gcd(n2,e) == 1:
            break
    d = modinv(e, n2)

    return (long(e), long(d), long(n))
    
(e, d, n) = key_gen(4457, 5783)

def rsaencrypt(plain):
   cipher = pow(plain,e, n)
   return cipher

def rsadecrypt(cipher):
    plain = pow(cipher, d, n)
    return plain
"""
#ex11.9
"""
def has_duplicates2(xs):
    d = dict()
    for c in xs:
        if c in d:
            return True
        else:
            d[c] = ''
    return False

#ex11.10
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

    return str(cipher)


def make_word_dict():
    d = dict()
    fin = open("/Users/Paul/Documents/words.txt","r")
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    return d


def rotate_pair(word, word_dict):
    for i in range(1,14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print word, i, rotated

word_dict = make_word_dict()
"""
for word in word_dict:
    rotate_pair(word, word_dict)
"""
#ex11.11
#word_dict = word_dict()

def read_dictionary(filename='/Users/Paul/Documents/c06d.txt'):
    
    """read (filename) and build a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

phonetic = read_dictionary()

def homophones(a, b):
    """
    Checks to see if two words can be pronounced the same way
    """
    if a not in phonetic or b not in phonetic:
       return False

    return phonetic[a] == phonetic[b]

def word_check(word):
    """
    checks to see if word is in dictionary, then checks if homophones
    """
    word1 = word[1:]
    if word1 not in word_dict: return False
    if not homophones (word, word1): return False
    
    
    word2 = word[0] + word[2:]
    if word2 not in word_dict: return False
    if not homophones(word, word2): return False

    return True
    

def check_all_words():
    for word in word_dict:
        if word_check(word):
            print word

check_all_words()


    
