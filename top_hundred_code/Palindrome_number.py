def palindrome(val):
    vai_str=str(val)
    
    reversed=vai_str[::-1]
    if reversed==vai_str:
        print("true")
    else:
        print("false")
value=input("enter the value\n")
result=palindrome(value)

