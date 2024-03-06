import inflect

def main():
    names = []
    inf = inflect.engine()
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break
    names_list = inf.join((names))
    print('Adieu, adieu, to '+ names_list)

if __name__ == "__main__":
    main()
