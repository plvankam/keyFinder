#!/usr/bin/python 


class Chord(object):
    a = [1,0,0,0,1,0,0,1,0,0,0,0]
    retArray = []

    def __init__(self,arr=None,num=0):
        print arr

                

    def keyTranspose(num):
        # use slicing method as to not copy identity of a
        tmp = a[:]
        # empty retArray allows us to start over each time
        # we call the function 
        retArray = []
        # print "In keyTranspose({})".format(num)
        for i in range(num):
            # pop end of a array off into retArray
            retArray.append(tmp.pop())
            # print "retArray[{}] = {}".format(i,retArray[i])
        # reverse so as to arrange in proper order from .pop() methods
        retArray.reverse()
        for i in range(len(tmp)):
            # append retArray with remaing elements of array a
            retArray.append(tmp[i])

if __name__ == "__main__": 
    bVal = True
    count = 0
    a = raw_input("how many chord do you have?")
    print "a = ",a
    if count < a:
        print "a = ", a
        print "{} < {}  is ".format(count,a), count < a
        raw_input("press enter to continue")
        count += 1
        print "count = " ,count
        raw_input("press enter to continue")
        c = Chord([1,2,3])
