# Q1  Age group Catogarization
# Classify a person's age group: Child( <13), Teenager(13-19), Adult(20-59), Senior(60+)

age = 65

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult") 
else:
    print("Senior")       
          
 # Q2 Movie Ticket Pricing
    # Movie tickets are priced based on age: $12 for adults (18 and over),$8 for children. Everyone gets a $2 discount on Wednesday.

    age = 10
    day = "Wednesday"

    price = 12 if age >= 18 else 8

    if day == "Wednesday":
        price = price - 2
        #price -= 2 

    print("Ticket price for you is $",price) 

    # Q3 Grade Calculator
    # Assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(below 60).

    score =78 

    if score >= 90:
        Grade = "A"
    elif score >= 80:
        Grade = "B"
    elif score >= 70:
        Grade = "C"
    elif score >= 60:
        Grade = "D"
    else:
        Grade = "F"

    print("Grade: ", Grade)        
    

    
