total = 0
while True:
    num = int(input("Enter a number (negative to stop): "))
    if num < 0:    # stop when negative number is entered
        break
    total += num   # add only positive numbers
print("Sum of all positive numbers =", total)


# Example usage:
#Enter a number (negative to stop): 2
#Enter a number (negative to stop): 43
#Enter a number (negative to stop): 43
#Enter a number (negative to stop): -1
#Sum of all positive numbers = 88