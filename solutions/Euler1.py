def euler():
    y=0
    for x in range(1000):
        if x%3==0 or x%5==0:
            y += x
			
    print ("Euler 1 answer: %d") % y
