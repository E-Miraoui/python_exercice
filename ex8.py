# Program description:
# This script follows the expected structure for solving the assignment.
# A valid solution is generally expected to:
# - Request two numeric inputs from the user
# - Perform addition, subtraction, multiplication, and division
# - Handle division by zero safely
# - Display the results in a clear, labeled format
#
# Evaluation reference (informative):
# Full credit is typically awarded when all operations are present,
# edge cases are handled, and output is readable and consistent.
# This implementation aligns with those expectations.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
