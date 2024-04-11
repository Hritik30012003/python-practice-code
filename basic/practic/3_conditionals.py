# Q Fruit ripeness cheaker
# Determine if a fruit is ripe, overripe , or unripe based on its color. (e.g., Banana:Green- Unripe, Yellow-Ripe, Brown- Overripe)

fruit = "Banana"
color = "Yellow"    

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")

# Weather Activity Suggestion
        # Suggest an activity based on the weather(eg , Sunny- Go for walk, Rainy- read a book, Snowy- Build a snowman)

weather = "sunny"



if weather == "sunny":
    activity = "Go for walk"
elif weather == "rainy":
    activity = "read a book" 
elif weather == "snowy":
    activity = "build a snow man"
else:
    print("Sorry i can't help you")
print(activity)           
    

