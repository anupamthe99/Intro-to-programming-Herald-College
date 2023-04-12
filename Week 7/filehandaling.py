

# with open('file.txt','w') as f:
#     f.write("hey")

# with open('file.txt','a')as f:
#     f.write("added new line too")


# # def read_file():
# #     file=open('file.txt','r')
# #     print(file.read()) 
# #     file.close()

# # read_file()

# if __name__ =="__main__":
#     read_file()



with open('file.txt','r') as f:
    print(f"Single line{f.readline()}")
    print(f"Multiple lines:{f.readlines()}/n")
    print(f.read())

with open('file1.txt','w') as f:
    print(f.write("Hello ,good morning"))

with open('file1.txt','a') as f:
    print(f.write("Hello ,good morning\n .Go have breakfast"))

