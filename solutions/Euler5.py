def euler():
    start=20*19
    check=False
    while check==False:
        if start%20==0 and start%19==0 and start%18==0 and start%17==0 and start%16==0 and start%15==0 and start%14==0 and start%13==0 and start%11==0:
            check=True
        else:
            start=start+20
    print("Euler 5 answer: %d") %start
