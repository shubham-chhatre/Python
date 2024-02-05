def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

# Input a number from the user
number = int(input("Enter a number: "))

if number < 1:
    print("Please enter a positive integer.")
else:
    factors = find_factors(number)
    print(f"Factors of {number}: {factors}")
