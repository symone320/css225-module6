# Symone Mitchell
# August 15, 2026
# Problem 6: Calculate the factorial of a user-entered number
# and compare it with math.factorial()

import math

number = int(input("Enter a whole number: "))

factorial = 1

for value in range(1, number + 1):
    factorial = factorial * value

print("Calculated factorial:", factorial)
print("math.factorial result:", math.factorial(number))
