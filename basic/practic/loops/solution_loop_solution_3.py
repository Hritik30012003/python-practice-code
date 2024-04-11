# Q reverse a string 
# Reverse a string using a loop.

input_str = "python" 

reversed_str = ""



for char in input_str:
    reversed_str = char + reversed_str

print(reversed_str)    

# Q Find the first non-repeated character
# Given a String , Find the first non-repeated character.

input_str = "teeteracdrtgh"

for char in input_str:
    print(char)
    if input_str. count(char) == 1:
        print("char is :",char)
        #break