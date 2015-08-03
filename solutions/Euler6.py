def euler():
    nums=[]
    for i in range(1,101):
        nums.append(i)
            
    t1=sum(nums)*sum(nums)

    for i in range(1,101):
        temp=nums[i-1]*nums[i-1]
        nums[i-1]=temp
         
    t2=sum(nums)

    print("Euler 6 answer:")
    print(t1-t2)