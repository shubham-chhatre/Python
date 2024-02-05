def max_of_two(a,b):
    if a>b:
        return a 
    else:
        return b
num1=int(input("enter the first number\n"))
num2=int(input("enter the second number\n"))
result=max_of_two(num1,num2)
print("the greater number\n",result)