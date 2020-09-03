#IF..ELSE , ELIF  STATEMENTS
#If statements are used to test for particular conditions and respond appropriately

#A simple if test
age = int(input("Enter your Age?")) #We have added "Input function" to get the value, and its stored in age variable.


#Input Function.
#Your programs can prompt the user for input. All input is stored as a string.usinh "input()"

if age >= 18: #Now "if" statement checks the condition
    print("You can vote!")  #and prints the output
else: #if the condition doesn't match with first comdition it comes to else
    print("Sorry! ") #and prints the default value or given value

#if - elif - else statements

age = int(input("What is your Age?"))
if age < 4:
    ticket_price = 0
    print(ticket_price)
elif age < 18:
    ticket_price = 10
    print(ticket_price)
else:
    ticket_price = 15
    print(ticket_price)


#Exercises

#Write a program that uses following list of cities per country,USA,UK,INDIA
#a.Write a program that asks user to enter a city name and it should tell you whichcountry it belongs to
#b.Write a program that asks user to enter two cities and tell you if they both are insamecountry or not"

usa = ["Atlanta","New York","Baltimore","Chicago"]
uk = ["London","Bristol","Cardiff"]
india = ["New Delhi","Mumbai","Bengaluru"]

city = input("Enter the Name of the City:")
if city in usa:
    print("This City is in USA")
elif city in uk:
    print("This City is in UK")
elif city in india:
    print("This City is in INDIA")
else:
    print("Sorry, We Couldn't Find this city")

city1 = input("Enter City1")
city2 = input("Enter city2")

if city1 in usa and city2 in usa:
    print("Both cities are in USA")
elif city1 in uk and city2 in uk:
    print("Both cities are in uk")
elif city1 in india and city2 in india:
    print("Both cities are in India")
else:
    print("They don't belong to same country")













