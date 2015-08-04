from math import factorial
def euler():
    grid = [20,20]
    ans = factorial(grid[0]*2)/(factorial(grid[0])*factorial(grid[1]))
    print "Answer: %d" % ans