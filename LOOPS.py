#Loops
"for loop:"
#If we want to execute some action for every element present in some sequence
# (it may be string or collection)then we should go for for loop.

#Eg
#To Print Character represented in String
s = "Sachin Tendulkar"
for x in s:
    print(x)

#For loop
exp = [2310,5000,2500,4500,4500]
total = 0
for item in exp:
    total = total + item
print(total)

#Range Function
for i in range(1,101):
    print(i*i)


#print the total using range function
exp = [1000,2000,3000,4000,5000]
total = 0
for i in range(len(exp)):
    print("Month:",(i + 1),"Expense:",exp[i])
    total = total + exp[i]

print("Total Expenses of all Month is ",total)


#Find the Key
key_location = "Car"
location = ["Garage","Key Stand","Chair","Closet","Car"]
for i in location:
    if i==key_location:
        print("Key is found in:",i)
        break
    else:
        print("Key is not found in",i)


#print the sum of square of all numbers except even numbers
for i in range(1,6):
    if i%2==0:
        continue
    print(i*i)


#while loop
i = 1
while i<=5:
    print(i)
    i=i+1

#Using for loop figure out count for “heads”.

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for item in result:
    if item == "heads":
        count += 1
    print("Heads count: ", count)

#Your monthly expense list (from Jan to May)
#Write a program that asks you to enter an expense amount and program should tell youin which month that expense occurred.
# If expense is not found, then convey that as well
exp_list=[2340,2500,2100,3100,2980]
mon_list=["Jan","Feb","March","April","May"]
a=int(input("Enter the expense amount "))
for i in range(len(exp_list)):
    if a!=exp_list[i]:
        continue
    else:
        print("Expense of ",a,"occured in ",mon_list[i])
        break


#Write a program that prints following shape, (Hint: Use for loop inside another for loop)
#*
#**
#***
#****
#*****

for i in range(1,6):
 s = ' '
 for j in range(i):
     s += '*'
     print(s)