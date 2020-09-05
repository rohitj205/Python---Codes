#Let us say your expense for every month are listed below,
#January - 2200
#February - 2350
#March - 2600
#April - 2130
#May - 2190

#Create a list to store these monthly expenses and using that find out,
exp = [2200,2350,2600,2130,2190]

#1. In Feb, how many dollars you spent extra compare to January?
print("Q1.In Feb, how many dollars you spent extra compare to January?")
print("Dollars you spent extra compare to January:",exp[1]-exp[0])

#2. Find out your total expense in first quarter (first three months) of the year.
print("Q2.Find out your total expense in first quarter (first three months) of the year.")
print("Total expense in first quarter (first three months) of the year is",exp[0]+exp[1]+exp[2])

#3. Find out if you spent exactly 2000 dollars in any month.
print("Q3.Find out if you spent exactly 2000 dollars in any month.")
print("Did i spend $2000 in any month",2000 in exp )

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
print("Q4. Add June Month Exp")
exp.append(1980)
print(exp)

#5. You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
print("Q5.Make a correction to your monthly expense list")
print("Expenses after the Correction is",exp[3]-200)
print(exp)



#You have a list of your favourite marvel super heros.

heros=['spider man','thor','hulk','iron man','captain america']

#Using this find out,

#1. Length of the list
print("Q1.Length of the list")
print("Lenght of the List is",len(heros))

#2. Add 'black panther' at the end of this list
print("Q2. Add 'black panther' at the end of this list")
heros.append("Black Panther")
print('List Now:',heros)

#3. You realize that you need to add 'black panther' after 'hulk',
   #so remove it from the list first and then add it after 'hulk'
print(("Q3. You realize that you need to add 'black panther' after 'hulk',so remove it from the list first and then add it after 'hulk'"))
heros.remove('Black Panther')
heros.insert(3,"Black panther")
print("Now the list is like",heros)

#4. Now you don't like thor and hulk because they get angry easily :)
   #So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   #Do that with one line of code.
print("Q4.Remove Hulk and Thor and Replace it with Black Panther")
heros[1:3] = ['Doctor Strange']
print(heros)

#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
print(("Q5.Sort it in Alphabetical Order"))
heros.sort()
print(heros)


#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user
# using input() function

max = int(input("Enter a number"))
odd_numbers = [    ]

for i in range(max):
    if i%2 == 1:
        odd_numbers.append(i)

    print("Odd Numbers:",odd_numbers)


