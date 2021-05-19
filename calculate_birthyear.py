name = input("\nHello, what is your name? ")
age = int(input("\nThank you, what is your age? "))
current_year = 2021

birthday_happened = input("Has your birthday already happened this year? (y/n) ")

if birthday_happened.upper() == "Y":
    print(f"OMG, you are {age} years old so you born in {current_year - age}")
elif birthday_happened.upper() == "N":
    print(f"OMG, you are {age} years old so you born in {current_year - 1 - age}")
else:
    print("Unfortunately, I didn't recognise your answer. Please use y for yes, or n for no")