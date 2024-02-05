num1=int(input("ente the number\n"))
def prime(num):
    num2=str(num)
    for i in range(2,num):
        if i%2!=0:
            print(i)
result=prime(num1)
