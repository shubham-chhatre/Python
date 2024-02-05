def find_hcf(a, b):
    if b == 0:
        return a
    else:
        return find_hcf(b, a % b)

# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Ensure that both numbers are positive
num1 = abs(num1)
num2 = abs(num2)

# Call the function to find the HCF
hcf = find_hcf(num1, num2)

# Output the HCF
print(f"The HCF of {num1} and {num2} is {hcf}")
