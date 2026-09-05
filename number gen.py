# random_math_demo.py

import random
import math

print("Random Number Demo")

# Generate a random number between 1 and 100
number = random.randint(1, 100)

print(f"Random number generated: {number}")

# Use modulo to determine if the number is even or odd
if number % 2 == 0:
    print("The num"
          "ber is even.")
else:
    print("The number is odd.")

# Use the math module to calculate the square root
square_root = math.sqrt(number)

print(f"Square root of {number}: {square_root:.2f}")