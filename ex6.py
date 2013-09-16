import math
#ex 6.1

def compare(x,y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

#test functions
print(compare(4,6))
print(compare(6,6))
print(compare(4,3))

#ex 6.2  (this is  an exercise in incremental development.  what you see is the final product)

def hypotenuse(x,y):
    temp = math.sqrt(x**2 + y**2)
    return temp


print(hypotenuse(3,4))


#6.7
def fibonacci (n):
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + fibonacci (n-1)


#ex 6.5
def ack (m,n):
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m-1,1)
    return ack(m-1, ack(m,n-1))

print (ack(3,4))

#ex 6.6
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word [1:-1]


def is_palindrome(word):
    if len(word) <=1:
        return True 
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print(is_palindrome('poop'))
print(is_palindrome('alien'))
print(is_palindrome('racecar'))
print(is_palindrome('park'))

#ex 6.7

def is_power(a,b):
    if a == b:
        return True
    elif a%b == 0:
        return is_power(a/b, b)
    else:
        return False

print (is_power(3,5))
print (is_power(9,3))
print (is_power(9,2))

#ex 6.8
def gcd(a,b):
    if a < b:  #makes sure input is in the right order
        gcd(b,a)
        
    if b == 0:  #base case to eliminate devision by zero
        return a
        
    else:       #recursion step.  a%b happens after base to avoid division by zero
        r = a%b
        return gcd(b,r)

print(gcd(16,12))
print(gcd(13,26))
print(gcd(10,27))
        


