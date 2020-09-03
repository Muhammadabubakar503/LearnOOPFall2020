#printing table using while loop
print("...................")
print("Table using while loop")
print("...................")
num= int(input("enter table number : "))
y=int(input("enter the range : "))
i = 1
while i <= y:
        x = num*i
        print(num ,"*",i, "=", x)
        i = i + 1
#printing table using while loop
print("...................")
print("Table using for loop")
print("...................")
num= int(input("enter table number : "))
y=int(input("enter the range : "))
i=1
for i in range(1,y+1):
    x=num*i
    print(num, "*", i, "=", x)