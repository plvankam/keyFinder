#!/usr/bin/python 

a = [1,0,0,0,1,0,0,1,0,0,0,0]
retArray = []

def keyTranspose(num):
    # declare global to interract with a
    global a
    # declare global to access array outside of function
    global retArray
    # use slicing method as to not copy identity of a
    tmp = a[:]
    # empty retArray allows us to start over each time
    # we call the function 
    retArray = []
    # print "In keyTranspose({})".format(num)
    for i in range(num):
        # pop ent of a array off into retArray
        retArray.append(tmp.pop())
        # print "retArray[{}] = {}".format(i,retArray[i])
    # reverse so as to arrange in proper order from .pop() methods
    retArray.reverse()
    for i in range(len(tmp)):
        # append retArray with remaing elements of array a
        retArray.append(tmp[i])

# we are making an array for each key based up the key of A major
#------------------------------------------------------------
#                   TO DO: 
# Later on we can go about manipulating matrices in order to represent 
# minor, 7, 9... etc.  
#------------------------------------------------------------
#------------------------------------------------------------

print a
keyTranspose(1)
asharp = retArray
bflat = asharp
print asharp
keyTranspose(2)
b= retArray
cflat = b
print b
keyTranspose(3)
c = retArray
bsharp = c
print c 
keyTranspose(4)
csharp = retArray
dflat = csharp
print csharp
keyTranspose(5)
d = retArray
print d 
keyTranspose(6)
dsharp = retArray
eflat = dsharp
print dsharp
keyTranspose(7)
e = retArray
fflat = e
print e 
keyTranspose(8)
f= retArray
esharp = f
print f 
keyTranspose(9)
fsharp = retArray
gflat = fsharp
print fsharp 
keyTranspose(10)
g = retArray
print g 
keyTranspose(11)
gsharp = retArray
aflat = gsharp
print gsharp 


