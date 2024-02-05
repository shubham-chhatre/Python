def prime_num_in_range(a,b):
    for i in range(a,b+1):
        if i%2!=0:
            print("prime numeber",i)
        elif i%2==0:
            print("not prime number",i)
start=int(input("start of range\n"))
end=int(input("end of range\n"))
result=prime_num_in_range(start,end)
print(result)