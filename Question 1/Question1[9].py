# Input a whole number
num = int(input("Enter a whole number: "))
print(f"Factors of {num} are:")
i = 1
while i <= num:
    if num % i == 0:   # if i divides num completely
        print(i, end=" ")
    i += 1


# Example Input/Output
#Enter a whole number: 12
#Factors of 12 are:
#1 2 3 4 6 12 