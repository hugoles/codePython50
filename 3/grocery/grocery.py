grocery_dict = {}

try:
    while True:
        item = input().lower()
        grocery_dict[item] = grocery_dict.get(item, 0) + 1
except EOFError:
    for key, value in sorted(grocery_dict.items()):
        print(f"{value} {key.upper()}")
