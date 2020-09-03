#LISTS
# "A list stores a series of items in a particular order.You access items using an index, or within a loop".

#Make a list
cars = ['Audi', 'BMW', 'Benz']

#Get the first item in a list
first_car = cars[0]
print(first_car)

#Get the last item in a list
last_bike = cars[-1]
print(last_bike)

#Exercises
#Lists

#Let us say your expense for every month are listed below,
#January -  2200 February - 2350 March -    2600 April -    2130 May -      2190

#Create a list to store these monthly expenses and using that find out,

#In Feb, how many dollars you spent extra compare to January?

#Find out your total expense in first quarter (first three months) of the year.

#Find out if you spent exactly 2000 dollars in any month

#June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

#You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this.

#Answer:

exp = [2200,2350,2600,2130,2190] #Created a List

# (a)
print("dollars you spent extra in February comparing to January",exp[1]-exp[0])

# (b)
print("total expense in first quarter (first three months) of the year",exp[0]+exp[1]+exp[2])


# (c)
var = 2000 in exp
print("Find out if you spent exactly 2000 dollars in any month",var)

# (d)
exp.append(1980) #Adding another Value to the List
print(exp)

# (e)
exp[3] = exp[3] - 200
exp[3]