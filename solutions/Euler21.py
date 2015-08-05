from supportFunctions import find_divisors
map = {};
# using a set so it edits out all duplicates
# key: sum, value: number
def divisor_sum(inNum):
    return sum(find_divisors(inNum))
def euler():
    ans = []
    for x in range(1,10001):
        map[x] =  divisor_sum(x)
    for x in range (1,10001):
        currSum = map[x]
        if currSum in map:
            if map[currSum] == x and currSum != x:
                ans.append(x)
    print ("Euler 21 answer: %d") % sum(set(ans))