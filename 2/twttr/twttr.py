input = input('Input: ')
output = ''
for i in range(len(input)):
    if input[i].lower() in 'aeiou':
        continue
    output += input[i]
print(output)
