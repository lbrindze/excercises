from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print (bob)

#ex 1

def square(t):
    for in in range(4):
        fd(t,100)
        lt(t)
        
square(bob)

#ex 2

def squarel(t, l):
    for in in range(4):
        fd(t,l)
        lt(t)

#ex 3
def polyline(t, n, length, angle):
    for i in range (n)
        fd(t, length)
        lt(t, angle)
        
def polygon(t,l,n):
    angle = 360/n
    polyline(t, n, l, angle)

#ex 4/5
def arc(t, r, angle):
    arc_length = 2*r*math.pi*abs(angle)/360
    n = int(arc_length/4)+1
    step_length = arc_length?n
    step_angle = float (angle)/n

def circle(t,r):
    arc(t, r, 360) 

    
    

wait_for_user()





