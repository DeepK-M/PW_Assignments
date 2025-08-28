# Pre-specified numbers
a, b, c = 12, 45, 30
# Using nested ternary operator
largest = a if (a > b and a > c) else (b if b > c else c)
print("The largest number is:", largest)

# Output:
#The largest number is: 45