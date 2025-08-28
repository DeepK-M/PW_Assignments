# Simple Calculator

# Take two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Take operation input
print("Choose operation: +  -  *  /")
op = input("Enter operator: ")
# Perform operation
if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero not allowed!")
else:
    print("Invalid operator! Please use +, -, *, /")


# Example usage:
#Enter first number: 3
#Enter second number: 4
#Choose operation: +  -  *  /
#Enter operator: +
#Result: 7.0