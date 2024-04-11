passward = "fksdnj45"

#passward_length = len(passward)


if len(passward) < 6:
    strength = "Weak"
elif len(passward) <= 10:
    strength = "Medium"
else:
    strength = "strong"
print("Passward strength is:", strength)            