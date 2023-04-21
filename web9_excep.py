def divide(a,b):
    if b==0:
        raise ValueError("Value can not be 0")
    
    result=a/b
    return result

try:
    result=divide(1,2)
    print(result)
except ValueError as e:
    print(e)
else:
    print("run when there is no error")
finally:
    print("at last")

