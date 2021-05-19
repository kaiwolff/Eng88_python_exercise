import time
from datetime import date
from datetime import datetime

now = date.today()
name = input("\nHello, what is your name? ")
birthday = input("\nThank you, please enter your birthday in format dd/mm: ")
age = int(input("\nThank you, and how old are you? "))

birthday_timed = datetime.strptime(birthday, "%d/%m") #this should turn the input string from birthday into a struct_time

if birthday_timed.month > now.month:
    birthyear = now.year - 1 - age


elif birthday_timed.month == now.month and birthday_timed.day >now.day:
    birthyear = now.year - 1 - age
    birthday_timed.year = birthyear


else:
    birthyear = now.year  - age
    birthday_timed.year = birthyear

#have to create new datetime for hours calculation as immutable
birth_month = birthday_timed.month
birth_day = birthday_timed.month
birthday_datetime = datetime(year = birthyear, month = birth_month, day = birth_day)
print(birthday_datetime)
print(now)
hours_alive = ((datetime.now() - birthday_datetime).total_seconds())/3600

print(f"OMG, you are {age} years old so you were born in {birthyear}")
print(f"You have been alive for about {int(hours_alive)} hours")



