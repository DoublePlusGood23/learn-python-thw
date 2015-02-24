
def loopin(n, nums, incro):
    i = 0
    while i < n:
        print "At the top is %d" % i
        nums.append(i)

        i += incro
        print "Numbers now: ", nums
        print "At the bottom i is %d" % i
    
print "The numbers: "

numbers = []

loopin(50,numbers, 3)
