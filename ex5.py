from math import *

#ex 3
print('a?\n')

a = int(userInput)
except ValueError:
   print("That's not an int!")
   
print('b?\n')

b = int(userInput)
except ValueError:
   print("That's not an int!")
   
print('c?\n')

c = int(userInput)
except ValueError:
   print("That's not an int!")
   
print('n?\n')

n = int(userInput)
except ValueError:
   print("That's not an int!")


def check_fermat(a,b,c,n):
    if a**n + b**n == c**n:
        print ("nope that doesn't work.")
    else:
        print ('Holy smokes, Fermat was wrong!')
    

check_fermat(a,b,c,n)

"""
             
#ex 4

x = input ('a?\n')
y = input ('b?\n')
z = input ('c?\n')

def is_greater(e,f,g):
    if e > f and e > g:
        GREATER=e
        OTHERS=f+g
        if GREATER < OTHERS:
            print ('Yes')
        else:
            print ('No')
    else:
       l = e
       m = f
       n = g
       is_greater (m, n, l)

    


def is_triangle(d,e,f):
    a = int(d)
    b = int(e)
    c = int(f)
    is_greater(a,b,c)
    

is_triangle(x,y,z)
"""
