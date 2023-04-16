while True:
    password=input("Enter your password")

    upper=0
    lower=0
    digit=0
    for p in password:
        if p.isupper():
            upper+=1
        if p.islower():
            lower+=1
        if p.isdigit():
            digit+=1

    if len(password)>=8 and upper>=1 and lower>=1 and digit>=1:
        print("Password Created Successfully")
    else:
        print("Password should have atleast 1 upper ,1 lower and 1 digt along with 9 char")
        break
