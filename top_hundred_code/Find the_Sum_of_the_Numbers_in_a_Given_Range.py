def sum_in_range(a,b):
    return sum(range(a,b+1))
#it will start form a but end before b therefore b+1 is used
start=int(input("enter the start of range\n"))
end=int(input("enter the end of range\n"))
result=sum_in_range(start,end)
print(result)