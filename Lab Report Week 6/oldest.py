list_age=[]
for i in range(4):
    age=int(input("Enter yours age:"))
    list_age.append(age)

oldest_age=list_age[0]
for age in list_age:
    if age>oldest_age:
        oldest_age=age

print(f"The oldest age amongs four people is {oldest_age}")
