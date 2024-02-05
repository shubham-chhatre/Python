def two_sum(num,target):
    num1=str(num)
    for i in num1:
        if num1[i]+num1[i+1]==target:
            return i,i+1
        else:
            return false
nu=int(input("enter the array:"))
tar=int(input("eenter the target:"))
result=two_sum(nu,tar)
