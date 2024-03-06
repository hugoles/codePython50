input = input('camelCase: ')
output_string = ''
for i in range(len(input)):
    if input[i].isupper():
        output_string += '_' + input[i].lower()
    else:
        output_string += input[i]
print(output_string)

