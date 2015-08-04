
# This is a good candidate for dynamic style 
# I'll try to save previously calculated values in a hash
# using local functions as I don't think I'll need these again

# bad practice putting map here, but excusable 
dynamicMap = {2:2}
LIMIT = 1000000

def next_num(inNum):
    if inNum % 2 == 0:
        return inNum/2
    else:
        return (3*inNum)+1
        
def calc_collatz_size(inNum):
    if inNum not in dynamicMap:
        new = next_num(inNum)
        dynamicMap[inNum] = calc_collatz_size(new) + 1
    return dynamicMap[inNum]
    
def euler():
    best = 2
    for i in range(2,LIMIT+1): #I mess this up a lot, it's < not <=
        temp = calc_collatz_size(i)
        if temp > dynamicMap[best]:
            best = i
    print "Answer: %d" % best