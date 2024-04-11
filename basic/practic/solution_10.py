# Q Recomend a type of food based on the pet's species and age. (eg, Dog:<2 years-puppy food, Cat:>5 years - Senior cat food)

PetSpecies = "Dog"

Age = 1

if PetSpecies == "Dog" and Age < 3:
    Recommend = "puppy food"
elif PetSpecies == "Cat" and Age > 5:
    Recommend = "Senior Cat Food"
else:
    Recommend = "pls give me right input" 
print("food for your pet is:",Recommend)    