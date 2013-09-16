
# EXERCISE 3.3

def right_justify (s) :
	length = len(s)
	space = " "*(70 - length)
	poop = space + s
	print (poop)
	
# EXERCISE 3.4
def do_twice(f,v):
        f(v)
        f(v)


def print_spam():
	print ('spam')

do_twice(print,'spam')

def print_twice(s):
	do_twice(print(), s)


def do_four (f, v):
	do_twice(f,v)
	do_twice(f,v)


# EXERCISE 3.5


