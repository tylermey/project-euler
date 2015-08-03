def euler():
    best = 0
    for i in range(1,1000):
        for j in range(1,1000):
            temp=i*j
            revTemp=int("".join(list(reversed(str(temp)))))
            if temp==revTemp and temp>best:
                best=temp

    print "Euler 4 answer: %d" %best