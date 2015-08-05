map = {
    0:"",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty",
    30:"thirty",
    40:"forty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety",
    100:"hundred",
    1000:"thousand"
}

def euler():
    total = 0
    for x in range(0,1001):
        temp = x%100
        if  0<temp<20:
            total += len(map[temp])
        elif 20<=temp<=99:
            temp = str(temp)
            total += len(map[int(temp[1])])
            total += len(map[int(temp[0]+"0")])
        if x>999:
            total += 3
            total += len(map[1000])
        elif x>99:
            if x%100 != 0:
                total += 3
            total += len(map[100])
            total += len(map[int(str(x)[0])])
    print "Answer: %d" % total
        
        
        
        
        
        
        