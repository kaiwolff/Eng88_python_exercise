import time
from datetime import date
now = date.today()
name = input("\nHello, what is your name? ")
birthday = input("\nThank you, please enter your birthday in format dd/mm: ")
age = int(input("\nThank you, and how old are you? "))

birthday_timed = time.strptime(birthday, "%d/%m") #this should turn the input string from birthday into a struct_time

if birthday_timed[1] > now.month:
    print(f"OMG, you are {age} years old so you were born in {now.year - 1 - age}")

elif birthday_timed[1] == now.month and birthday_timed[2]:
    print(f"OMG, you are {age} years old so you were born in {now.year - 1 - age}")

else:
    print(f"OMG, you are {age} years old so you were born in {now.year  - age}")
