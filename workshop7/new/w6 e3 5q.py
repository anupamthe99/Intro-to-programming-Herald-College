def list_to_int(numbers):
    return int(''.join(map(str, numbers)))
numbers = [11, 33, 50]
result = list_to_int(numbers)
print(result)
