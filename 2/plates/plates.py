def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0:1].isalpha():
        return False
    if not 2 <= len(s) <= 6:
        return False
    fnum = True
    for i in s:
        if i == '0' and fnum == True:
            return False
        if i.isdigit():
            fnum = False
        if i.isalpha() and fnum ==  False:
            return False
        if not i.isalpha() and not i.isdigit():
            return False
    return True

main()
