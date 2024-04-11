# Validate input
# Keep asking the user for input until they enter a number between 1 and 10.

while True: 
    number = int(input("Enter value b/w 1 and 10"))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("invalid number, try again") 


# Q Check if a number is prime.
        # cheak if a number is prime.

number = 29

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
print(is_prime)        