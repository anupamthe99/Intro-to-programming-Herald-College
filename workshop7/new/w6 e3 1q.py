def filter_strings_with_a(strings):
    filtered_strings = []
    for string in strings:
        if 'a' in string:
            filtered_strings.append(string)
    return filtered_strings
strings = ['apple', 'banana', 'cat', 'dog']
filtered_strings = filter_strings_with_a(strings)
print(filtered_strings)
