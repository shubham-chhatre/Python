def hcf(a,b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
num1=abs(num1)
num2=abs(num2)

r=hcf(num1,num2)
print(f"hcf of {num1} and {num2} is {r}")


def lcm (a,b):
    l=hcf(a,b)
    result=(a*b)//l
    return result
h=lcm(num1,num2)
print(f"lcm of{num1}and {num2} is {h}")
    
