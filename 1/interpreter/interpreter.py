x, y, z = input("Expression: ").split(' ')
if y == '+':
    output = float(x)+float(z)
elif y == '-':
    output = float(x)-float(z)
elif y == '*':
    output = float(x)*float(z)
elif y == '/' and z != '0':
    output = float(x)/float(z)

print(output)
