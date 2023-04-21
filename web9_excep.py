def divide(a,b):
    if b==0:
        raise ValueError("Value can not be 0")
    
    result=a/b
    return result

try:
    result=divide(1,0)
    print(result)
except ValueError as e:
    print(e)