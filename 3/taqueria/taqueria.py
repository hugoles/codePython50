total = 0
while True:
    menu_dict = {
            "baja taco": 4.25,
            "burrito": 7.50,
            "bowl": 8.50,
            "nachos": 11.00,
            "quesadilla": 8.50,
            "super burrito": 8.50,
            "super quesadilla": 9.50,
            "taco": 3.00,
            "tortilla salad": 8.00
        }
    try:
        p1 = input('Item: ').lower()
    except EOFError:
            print('\n')
            break
    if p1 in menu_dict:
        value = menu_dict[p1]
        total += value
        print(f'Total: ${total:.2f}')

