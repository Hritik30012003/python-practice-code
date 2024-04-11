# Q Check if a number is prime.
# cheak if a number is prime.

number = 28

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
print(is_prime)   

# Q List uniqueness cheaker
# Cheak if all elements in a list are unique. if a duplicate is found, exit the loop and print the duplicate.
# items ["apple","banana", "orange", "apple", "mango"]

items = ["apple","banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate:",item)
        break
    unique_item.add(item)

