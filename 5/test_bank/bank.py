

def main():
    input("Greetings:")
    val = value(greeting)
    print(val)

def value(greeting):
    greeting = greeting.lower().strip()
    array1 = greeting[0:5]
    array2 = greeting[0]
    if (array1 == 'hello'):
        return 0
    elif (array2 == 'h' and greeting[0:5] != 'hello'):
        return 20
    elif (greeting[0] != 'h' and greeting[0:5] != 'hello'):
        return 100

if __name__ == "__main__":
    main()
