num=int(input("enter the number:"))

def factorial(num1):
    if num1<=0:
        print("factorial is not possible")
    else:
        for i in range(1,num1+1):
            num1= num1*i
            print(num1)
        

resul=factorial(num)




    