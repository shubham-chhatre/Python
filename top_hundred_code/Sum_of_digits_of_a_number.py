def sum_of_digits(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Initialize a variable to store the sum
    digit_sum = 0
    
    # Iterate through each character in the string
    for digit in num_str:
        # Convert the character back to an integer and add it to the sum
        digit_sum += int(digit)
    
    return digit_sum

# Example usage:
number=int(input("enter the number\n"))
result = sum_of_digits(number)
print(f"The sum of digits in {number} is {result}")
