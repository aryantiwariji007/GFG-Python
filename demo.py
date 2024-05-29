def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_digits == number

# User input
num = int(input("Enter a number: "))

# Check and display the result
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
