import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    try:
        match = re.search(r'\b\s*um[.,?!:]*\s*\b',s, re.IGNORECASE)
        if not match:
            sys.exit(1)
        matches = re.finditer(r'\b\s*um[.,?!:]*\s*\b', s, re.IGNORECASE)
        counter = sum(1 for _ in matches)
        return counter
    except:
        sys.exit(1)

if __name__ == "__main__":
    main()
