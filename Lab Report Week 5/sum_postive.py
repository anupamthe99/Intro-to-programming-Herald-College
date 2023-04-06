"""
Prompts the user to enter any number of positive and negative integer values, then
displays the number of each type that were entered, sum the positive number (use break
and continue concept).
"""

list_number=[]

total_number=int(input("Enter how many number you want to use :"))

for i in range(1,total_number+1):
    number=int(input("Enter the number :"))
    list_number.append(number)

print(list_number)
total_neg=0
total_sum=0
total_zero=0
sum_postive=0
# for number in list_number:
#     if number<0:
#         total_neg+=1
#     elif number>0:
#         total_sum+=1
#         sum_postive+=number
#     elif number==0:
#         total_zero+=1

# print(f"You have enterd {total_neg} negtaive number ,{total_zero} zero ,and {total_sum} positive number\n")

# print(f"The sum of all the positive number is {sum_postive}")


"""

using break and continue 

"""
"""
this will only sum the postive integer
"""
for number in list_number:
    if number<0:
        break
    elif number>0:
        total_sum+=1
        sum_postive+=number
        continue
    elif number==0:
        break

print(sum_postive)

