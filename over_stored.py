nums=[]
num_input=input("Enter nums :")
nums_list=num_input.split(',')

for num in nums_list:
    if int(num)>100:
        nums.append("over")
    else:
        nums.append(num)

print(nums)