input = input("Greetings:").lower().strip()
array1 = input[0:5]
array2 = input[0]
if (array1 == 'hello'):
    print('$0')
elif (array2 == 'h' and input[0:5] != 'hello'):
    print('$20')
elif (input[0] != 'h' and input[0:5] != 'hello'):
    print('$100')
