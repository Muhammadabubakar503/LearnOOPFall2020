#printing table using while loop
print("...................")
print("Table using while loop")
print("...................")
number= int(input("enter table number : "))
lower_range=int(input("enter the lower range : "))
upper_range=int(input("enter the upper range : "))

while lower_range <= upper_range :
    product = number*lower_range
    print(number ,"*",lower_range, "=", product)
    lower_range += 1
#printing table using while loop
print("...................")
print("Table using for loop")
print("...................")
number= int(input("enter table number : "))
lower_range=int(input("enter the lower range : "))
upper_range=int(input("enter the upper range : "))

for lower_range in range(lower_range,upper_range+1):
    product = number*lower_range
    print(number ,"*",lower_range, "=", product)
