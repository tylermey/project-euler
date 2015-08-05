#brute force again, I'm going to have to get smarter eventually right?
def euler():
    day = 3 #tuesday
    total = 0
    for year in range(1901,2001):
        for month in range(1,13):
            if day == 1:
                    total += 1
            if month in [1,3,5,7,8,10,12]: #31
                day = (day+3)%7
            elif month in [4,6,9,11]: #30
                day = (day+2)%7
            # leap year
            elif year%4 == 0: #29
                day = (day+1)%7
            #not a leap year
            else: #28
                day = day
    print ("Euler 19 answer: %d") % total