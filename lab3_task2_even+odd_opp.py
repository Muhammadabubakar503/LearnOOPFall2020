#taking number from the user checking even or odd

print("................")
print("check the number is even or odd")
print("................")
number=int(input("enter your number: "))
if number%2==0:
    print(number,"is even")
else:
    print(number,"is odd")

#using for loop
print("................")
print("using for to check the number")
print("................")
lower_range=int(input("enter starting number: "))
upper_range=int(input("enter end starting: "))
for lower_range in range (lower_range,upper_range+1):
    if lower_range%2==0:
        print(lower_range,"is even")
    else:
        print(lower_range, "is odd")
#using while loop
print("................")
print("using while to check the number")
print("................")
lower_range=int(input("enter the starting point: "))
upper_range=int(input("enter the end point: "))
while lower_range<=upper_range:
    if lower_range%2==0:
        print(lower_range, "is even")
    else:
        print(lower_range,"is odd")
    lower_range=lower_range+1
