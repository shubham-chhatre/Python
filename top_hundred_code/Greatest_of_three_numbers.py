def max_of_two(a,b):
    if a>b:
        return a 
    else:
        return b
def max_three(a,b,c):
    return max_of_two(a,max_of_two(b,c))
num1=int(input("enter the first number\n"))
num2=int(input("enter the second number\n"))
num3=int(input("enter the third number\n"))
result=max_of_two(num1,num2)
result2=max_three(num1,num2,num3)
print("the greater number\n",result)
print("the greater number\n",result2)