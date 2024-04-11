# if it is raining, then i will bring umbrella. Will i bring an umbrellaif it is not raining?



raining = "NO"

if raining == "yes":
    Recommend = "Umbrella"
else:
    Recommend = "you don't need Umbrella"
print("AI recommend you:",Recommend)


# if the traffic light is red, then i will stop, what will i do if the traffic light is green?

traffic_light = "red"
if traffic_light == "red":
    Recommend = "Wait"
elif traffic_light == "green":
    Recommend = "go"
else:
    Recommend = "give me valid input"
print("AI recommend you for your safty:",Recommend) 

# Q if a triangle has three equal sides, then it is equilateral. is a triangle with three unequal sides equilateral?

triangle_side = 4

if triangle_side == 3:
    Recommend = "equilateral"
else:
    Recommend = "not equilateral" 
print("I recommend you it is:",Recommend)       