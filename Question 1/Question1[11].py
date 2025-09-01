print("Prime numbers between 2 and 100:")
for num in range(2, 101):  # numbers from 2 to 100
    is_prime = True        # assume number is prime  
    for i in range(2, num):  # check divisibility from 2 to num-1
        if num % i == 0:     # if divisible, not prime
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

# Sample Output:
#Prime numbers between 2 and 100:
#2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 