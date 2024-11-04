import random

# Declares a bunch of variables
NPCNumber = 0
MaxAge = 0
MinAge = 5
age = 0
Money = 0
Height = 0
inches = 0

# A lot of names and useful information in lists which is used later to generate random names and characteristics
MaleNames = ["James", "Michael", "Robert", "John", "David", "William", "Richard", "Joseph", "Thomas", "Christopher"]
FemNames = ["Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Karen"]
Names = ["Elon", "Bill", "James", "Michael", "Robert", "John", "David", "William", "Richard", "Joseph", "Thomas", "Christopher", "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Karen"]
LastNames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzales", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Musk", "Gates"]
MiddleNames = ["A.", "B.", "C.", "D.", "E.", "F.", "G.", "H.", "J.", "K.", "L.", "M.", "N.", "O.", "P.", "Q.", "R.", "S.", "T.", "V.", "W."]
Characteristics = ["Brave", "Idiotic", "Short Tempered", "Genius", "Cowardly", "Loving", "Stylish", "Rich", "Stereotypical", "Gregarious", "Anxious", "Unique", "Always Tired", "Goofy", "Chef", "Sporty", "Artistic", "Accountability", "Authentic", "Bold", "Compassionate", "Creative", "Decisive", "Diligent", "FEAR OF THE LORD", "Faithful", "Generous", "Gentle", "Integrous", "Kind", "Knowledgable", "Generous", "Meek", "Loyal", "Optimistic", "Reasonable", "Resourceful", "Righteous", "Weird", "Bald", "Peculiar"]

print('\/ Welcome to NPC Generator 3000! \/ \n')

# Checks whether the user wants to determine any variables
# Keeps asking until the answer is "Yes" or "No"
trueRandom = input("Would you like to determine anything for the NPCs? (Yes/No): ")
while (trueRandom != "Yes") and (trueRandom != "No"):
    print("\nNot an understood answer - Try 'Yes' or 'No'\n")
    trueRandom = input("Would you like to determine anything for the NPCs? (Yes/No): ")

# asks user for values if they want to enter them
if trueRandom == "Yes":
# Will keep asking for minumum and maximum age variables until they are logical
    while MaxAge < MinAge:
        while True:
            try:
                MinAge = int(input("Enter Minimum Age: "))
            except ValueError:
                print("\nNot an integer\n")
            else:
                break
        while True:
            try:
                MaxAge = int(input("Enter Maximum Age: "))
            except ValueError:
                print("\nNot an integer\n")
            else:
                break
    
    Gender =  input("Enter Gender (Male/Female): ")

  # If gender is not "Male" or "Female", keep asking for new input
    while (Gender != "Male") and (Gender != "Female"):
        print("\nNot an understood gender - Try 'Male' or 'Female'\n")
        Gender = input("Enter Gender (Male/Female): ")

# Asks for the number of NPCs until it is a positive integer
while True:
    try:
        NPCNumber = int(input("Enter number of NPCs: "))
        if NPCNumber < 0:
            print("\nNumber cannot be negative\n")
            continue
    except ValueError:
        print("\nNot an integer\n")
    else:
        break  

# If the user entered variables, this code runs using them
if trueRandom == "Yes":
    for i in range(NPCNumber):
        
        age = random.randint(MinAge,MaxAge) 

      # Chooses names based on age and gender
        if age > 5:
            if Gender == "Male":
                print(f"\nName: {random.choice(MaleNames)} {random.choice(MiddleNames)} {random.choice(LastNames)}")
            elif Gender == "Female":
                print(f"\nName: {random.choice(FemNames)} {random.choice(MiddleNames)} {random.choice(LastNames)}")
        else:
            if Gender == "Male":
                print(f"\nName: Baby {random.choice(MaleNames)}")
            elif Gender == "Female":
                print(f"\nName: Baby {random.choice(FemNames)}")
      
        print(f"Age: {age}")

      # Chooses random characteristics 
        print(f"Characteristics: {random.choice(Characteristics)}, {random.choice(Characteristics)}, {random.choice(Characteristics)}")

      # Chooses height based on age
        inches = random.randint(1,11)
        if age < 3:
            feet = random.randint(0,2)
            
        elif age < 10:
            feet = random.randint(2,4)
        else:
            feet = random.randint(4,6)
        print(f"Height: {feet}'{inches}")

      # Chooses inheritance based on age
        if age < 10:
            inheritance = random.randint(1,999)
        elif age < 20:
            inheritance = random.randint(100,9999)
        elif age < 50:
            inheritance = random.randint(1000,99999)
        else:
            inheritance = random.randint(10000,999999) 
        print(f"Inheritance: {inheritance}$")

# If the user didn't enter variables, this code runs
else:
    for i in range(NPCNumber):

  
        age = random.randint(0,100)

      # chooses name based on age
        if age > 5:
            print(f"\nName: {random.choice(MaleNames)} {random.choice(MiddleNames)} {random.choice(LastNames)}")
        else:
            print(f"\nName: Baby {random.choice(Names)}")
        
        print(f"Age: {age}")

      # Chooses characteristics
        print(f"Characteristics: {random.choice(Characteristics)}, {random.choice(Characteristics)}, {random.choice(Characteristics)}")

      # Bases height on age
        inches = random.randint(1,11)
        if age < 3:
            feet = random.randint(0,2)
            
        elif age < 10:
            feet = random.randint(2,4)
        else:
            feet = random.randint(4,6)
        print(f"Height: {feet}'{inches}")

      # Bases inheritance on age
        if age < 10:
            inheritance = random.randint(1,999)
        elif age < 20:
            inheritance = random.randint(100,9999)
        elif age < 50:
            inheritance = random.randint(1000,99999)
        else:
            inheritance = random.randint(10000,999999) 
        print(f"Inheritance: {inheritance}$")
        
