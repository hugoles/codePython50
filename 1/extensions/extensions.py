input = input('File name: ').lower().strip()
if (input.endswith(('.gif', '.png', '.jpeg', '.jpg'))):
    type = input[-3:]
    if type == 'peg' or type == 'jpg':
        print('image/jpeg')
    else:
        print(f'image/{type}')
elif (input.endswith(('.pdf', '.zip'))):
    type = input[-3:]
    print(f'application/{type}')
elif (input.endswith('.txt')):
    print('text/plain')
else:
    print('application/octet-stream')
