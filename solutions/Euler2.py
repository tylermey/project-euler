def euler():

    first=0
    second=0
    list=[]

    for i in range(1,35):
        if i<=1:
            next = i
            first=i
        else:
            next=first+second
            first=second
            second=next
            if second%2==0:
                list.append(second)
            
    ans = sum(list)
    print "Euler 2 answer: %d" %ans
    print "List of terms:"
    print list

