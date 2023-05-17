peoples = [
    {
        "name": "shyam",
        "age": 19
    },
    {
        "name": "hari",
        "age": 12
    },
    {
        "name": "jim",
        "age": 15
    },
    {
        "name": "ram",
        "age": 34
    },
]

voter_list=[]

for people in peoples:
    if people["age"]>=18:
        voter_list.append({"name":people["name"],"age":people["age"]})
print(voter_list)
