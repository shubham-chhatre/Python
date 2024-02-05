def prime_number(num):
    if num==0 or num==1:
        return "not prime"
    if num%2!=0:
        return "prime"
    return "not prme"
num1=int(input("enter the number\n"))
result=prime_number(num1)
print(result)