import random

def main():
    lvl = get_level()
    list1 = []
    list2 = []

    for _ in range(10):
        list1.append(generate_integer(lvl))
        list2.append(generate_integer(lvl))

    score = 0

    for i in range(10):
        errors = 0
        for _ in range(3):
            try:
                user_answer = int(input(f"{list1[i]} + {list2[i]} = "))
                result = list1[i] + list2[i]
            except ValueError:
                print('EEE')
                continue
            if user_answer == result:
                score += 1
                break
            else:
                print('EEE')
                errors += 1
                if errors == 3:
                    print(f'{list1[i]} + {list2[i]} = {result}')
                    break

    print(f'Score: {score}')

def get_level():
    while True:
        try:
            lvl = int(input('Level: '))
            if lvl in [1, 2, 3]:
                return lvl
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        lvl = random.randint(0, 9)
    elif level == 2:
        lvl = random.randint(10, 99)
    else:
        lvl = random.randint(100, 999)
    return lvl

if __name__ == "__main__":
    main()
