pharase="Ram is a boy he studies in Herald college kathmandu kathmandu he is very popular among student in college"
word_count=0
result={}

phrase_list=pharase.lower().split()
# print(phrase_list)
# for word in phrase_list:
#     count=0
#     for w in phrase_list:
#         # print(w)
#         word_point=word 

#         if w==word_point:
#             count+=1
#     result[word]=count
# print(result)

for word in phrase_list:
    if word not in result:
        result[word]=1
    else:
        result[word]+=1
print(result)