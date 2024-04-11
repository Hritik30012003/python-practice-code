# Q count positive numbers
#  Given a list of numbers, count how many are positive.
# number = [1,-2,3,-4,5,6,-7,-8,9,10]
positive_number_count = 0

numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
for num in numbers:
    if num > 0:
        positive_number_count += 1
print("Final count of positive number is:",positive_number_count)


# Q sum of even numbers
# calculate the sum of even numbers upto a given number n.

n= 100
sum_even = 45

for i in range(1, n+1):
    if i%2 == 0:
        sum_even += 1

print("Sum of even number is:", sum_even)        


# Q Multiplication Table Printer
# print the multiplication table for a given number upto 10. but skip the fifth iteration.

number = 3

for i in range (1, 11):
    if i == 5:
        continue  
    
    print(number, 'x', i, '=', number *i)