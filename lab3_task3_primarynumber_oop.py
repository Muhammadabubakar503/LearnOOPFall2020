#using for loop
print("................")
print("using for to check the prime number")
print("................")
number = int(input("enter number: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number" )
else:
    print(number, "is not a prime number")
#using while loop
print("................")
print("using while to check the prime number")
print("................")
number=int(input("enter number: "))
if number>1:
    i=2
    while i<=2:
        if number%2==0:
            print(number,"is not a prime number")
            break
        else:
            print(number,"is a prime number")
        i=i+1
else:
    print(number, "is not a prime number")