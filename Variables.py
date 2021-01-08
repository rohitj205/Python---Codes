#Variable and Strings.

#Variables are used to store values.
#A String is a series of characters, surrounded by single or double quotes

#Printing Hello world
print("Hello world!")

#Printing Msg with a variable
msg = "Hey! This is My First Program in Python"
print(msg)

#Concatenation (combining strings)
first_name = 'Sachin'
last_name = 'Tendulkar'
full_name = first_name + ' ' + last_name
print(full_name)

#Strings
my_string = "Sachin Tendulkar is known as the GOD of Cricket."

#to print a substring, for eg. print "Sachin" from the String
print(my_string[0:6]) #this method is known as slicing

#to print a substring from last line for eg. Print "Cricket"
print(my_string[-8:]) #this method is known as slicing

#print only "God of Cricket" from the String
print(my_string[33:])

#Numbers
#Calculating Total
Apple = 50
Mango = 50
total = (Apple + Mango)
print(total)

#Exercises with Variables and String.
#(1) Find out an area of a triangle whose base is 15 meter and height is 22 meter. The
# mathematical equation for an area of a triangle is: Area = ½*Base*Height
base=15
height=22
area=1/2*(base*height)
print("Answer for 1:","The Area is",area)

#(2)You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar.
# Find out using python, how many dollars is the shopkeeper going to give you back?
num_packets=9
cost_per_packet=1.49
total_cost=num_packets*cost_per_packet
money_paid=20
cash_back=money_paid-total_cost
print("Answer for 2:","Money you will get on returned is:",cash_back)


#(3)The bathroom of your home is an exact square. You want to replace tiles in it. Length of this bathroom is 5.5 feet.
# How many square foot of tiles you need to buy? Equation for an area of a square is: Area = Length to the power of 2. Find it out using python.
length=5.5
area=length**2
print("Answer for 3",area)

#strings

#(1) Create a string variable to store this text "Earth revolves around the sun",
#(a) Print substring “revolves”
#(b) Print substring “sun” using negative index
s="Earth revolves around the sun"
print('Answer for 1a:',s[6:14])
print("Answer for 1b:",s[-3:])

#(2) Create a string variable to store this text "Earth revolves around the “sun”" and print it

s='Earth revolves around the “sun”'
print("Answer for 2",s)

#(3) Create three string variables with values “I love eating“, “veggies”, “fruits”
#(a) Print “I love eating veggies and fruits” (Hint: Use + operator)
s1="I love eating"
s2="veggies"
s3="fruits"
print("Answer for 3a:",s1+" " +s2+" and "+s3)

#(b) Create fourth variable to store number of fruits you eat everyday.
# #Say for example you eat 2 fruits everyday, in that case print “I love eating 2 fruits everyday”
num_fruits=2
print("Answer for 3b.",s1+" "+str(num_fruits)+" "+s3+" everyday")
