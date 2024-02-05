def Pos_neg_num(a):
    if a>0:
        return 1
    elif a<0:
        return -1
    else:
        return 0
number=int(input("enter the number"))
result=Pos_neg_num(number)
if result==1:
    print("postive")
if result==-1:
    print("negative")
if result==0:
    print("either the the number is enter is zero or not valid")