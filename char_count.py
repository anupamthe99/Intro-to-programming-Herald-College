pharase="Ram is a boy he studies in Herald college kathmandu kathmandu he is very popular among student in college".lower()

count_space=0
result={}
for char in pharase:
    # print(char)

    if char is " ":
        continue

    if char not in result:
        result[char]=1
    else:
        result[char]+=1

print(result)