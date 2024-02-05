def even_odd_number(a):
    if a%2==0:
        return "even"
    else:
        return "odd"

number=int(input("enter the number\n"))
result=even_odd_number(number)
print(result)