#printing table using while loop
print("...................")
print("Table using while loop")
print("...................")
num= int(input("enter table number : "))

i = 1
while i <= 10:
        x = num*i
        print(x)
        i = i + 1
#printing table using while loop
print("...................")
print("Table using for loop")
print("...................")
num= int(input("enter table number : "))

i=1
for i in range(1,11):
    x=num*i
    print(x)