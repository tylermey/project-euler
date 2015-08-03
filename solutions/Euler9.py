from math import sqrt

def euler():
    c=0
    for a in range(1,1000):
        for b in range(1,1000):
            temp = (a*a)+(b*b)
            c = sqrt(temp)
            if (a+b+c)==1000 and a<b<c:
                print("Euler 9 answer: %d") %int(a*b*c)
        

