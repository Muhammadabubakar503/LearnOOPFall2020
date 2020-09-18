#sepratee even and odd
def odd_even(j):
    even = []
    odd = []
    for i in j:

        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
        total_number = [even, odd]

    return total_number


h = list(range(1, 10))
print(odd_even(h))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# enter data in list
person_name=[]
person_age=[]
person=int(input("how many person in family? "))
list1=0
while list1 < person:
    person_name.append(input("enter name "))
    person_age.append(int(input("enter age ")))
    print(">>>>>>>>>>>>>>>>>>>>>>")
    print("record save")
    print(">>>>>>>>>>>>>>>>>>>>>>")

    list1=list1+1
print(person_name)
print(person_age)