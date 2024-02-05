def sum_of_natural_numbers(n):
    if n < 1:
        return "Invalid input. Please provide a positive integer."
    else:
        return sum(range(1, n + 1))

# Example usage:
n = 10
result = sum_of_natural_numbers(n)
print(f"The sum of natural numbers up to {n} is {result}")
