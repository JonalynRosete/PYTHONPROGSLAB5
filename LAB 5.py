def classify_age(age):
    if age < 0:
        print("Invalid age, please enter a positive number.")
    elif age <=12:
        print("You are a child.")
    elif age <=19:
        print("You are a teen.")
    elif age <=54:
        print("You are an adult.")
    else:
        print("You are a senior.")
        
while True:
    age = int(input("Enter your age."))
    classify_age(age)
        
           
        
        