"""
Python program to calculate the sum of all the odd and even numbers within the given
range. (Suppose given range is 10)
"""
sum_odd=0
for i in range(1,11):
    if i%2 != 0:
        sum_odd+=i

print(sum_odd) 
