# Practice Loops in Python

# Count positive numbers in list
num = [1, 3, -3, -3, 3, -4, -4, -6, -7, -2, -3, -4, -5, -23, 234, 34, -3, -3, -3]
positive_number_count = 0

for n in num:
    if n > 0:
        positive_number_count += 1

print("Count of Positive Numbers:", positive_number_count)

# Sum of even numbers
n = int(input("Enter the Number: "))
sum_even = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i

print("Sum is:", sum_even)

# Multiplication table printer
n1 = int(input("Enter the Number: "))
print("Table of:", n1)

for i in range(1, 11):
    if i == 5:
        continue
    print(n1, 'x', i, '=', n1 * i)

# Reverse a string
input_str = "Python"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str

print(reversed_str)

# Find first non-repetitive character
str_input = "teeter"

for char in str_input:
    if str_input.count(char) == 1:
        print("First non-repetitive char:", char)
        break

# Calculate factorial
number = 5
fact = 1

while number > 0:
    fact *= number
    number -= 1

print("Factorial:", fact)

# Validate input between 1-10
while True:
    number = int(input("Enter a Number between 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid Number, try again")

# Check if prime number
num = 28
is_prime = True

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break

print("Is Prime Number:", is_prime)

# Find duplicate items in list
items = ["apple", "banana", "orange", "apple", "mango"]
unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate:", item)
        break
    unique_item.add(item)

# Exponential backoff retry logic
import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "- Wait Time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
