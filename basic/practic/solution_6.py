# Q Choose a mode of transportation based on the distance(eg, <3 km:Walk, 3-15 km: Bike,>15km:Car)

Distance = 100


if Distance < 3:
    transport = "Walk"
elif Distance < 15:
    transport = "Bike"
else:
    transport = "Car"

print("Ai recomends you the transport of: ",transport)        

# Q Customize a coffee order: "small", "medium", "large" with an option for "Extra shot" of espresso.

order_size = "Medium"
extra_shot = False 

if extra_shot:
    coffee = order_size + "coffee with an extra shot"
else:
    coffee = order_size + "coffee"
print("Order:", coffee)        