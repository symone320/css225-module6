# Symone Mitchell
# August 15, 2026
# Problem 5: Convert radians to degrees
# and compare the result with math.degrees()

import math

radians = float(input("Enter a value in radians: "))

calculated_degrees = radians * 180 / math.pi

print("Calculated degrees:", calculated_degrees)
print("math.degrees result:", math.degrees(radians))
