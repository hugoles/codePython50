import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    n = ip.split('.')
    if len(n) == 4 or len(n) == 6:
        for i in n:
            if i.isnumeric():
                if not (0 <= int(i) <= 255):
                    return False
            else:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
