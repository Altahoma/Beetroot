input_str = 'Make a program that has some sentence a string on input and returns a dict containing all unique words ' \
            'as keys and the number of occurrences as values'.lower()
result = {}

for word in input_str.split():
    if word not in result:
        result[word] = 1
    else:
        result[word] += 1

print(result)
