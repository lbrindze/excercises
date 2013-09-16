string = ['a','b','c']

def permutations (string): #takes string and returns string list of all permutations
    length = len(string)
    perms = []
    if length <= 1:       #base case
        return string      
    elif length >= 2:                
        for i in range(length): #recursion down to second base.  Program runs fine up until length = 7 and then takes a looooooong time
            head = string[i]
            tail = string[0:i]+string[i+1::]
            print ("head", head)
            print ("tail", tail)
            for j in range(len(tail)):
                perm = head + permutations(tail)[j]
                print ("perm "+str(i)+":", perm)
                perms.append(perm)
                  
    return perms

def perms2 (string):
    ps = []
    if len(string)<=1:
        return string
    else:
        for perm in string:
            for i in range(len(string[1:])):
                ps.append([perm] + perms2(string[:i]+string[i+1:]))
    return ps

ps = perms2(string)           
print (ps)
print (len(ps))


""" This is an example found on stack overflow internet that uses generators
    which I don't yet have a working understanding of...


def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                #nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
"""
