import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    try:
        if not re.search(r'\bto\b', s, re.IGNORECASE) or (' AM' not in s and ' PM' not in s):
            raise ValueError

        match = re.search(r"^([0-9]+):?([0-9]+)?\s*(A?P?M)\s*to\s*([0-9]+):?([0-9]+)?\s*(A?P?M)$", s, re.IGNORECASE)
        if match:
            hour1, minute1, turn1, hour2, minute2, turn2 = match.groups()

            if minute1 is None:
                minute1 = "00"
            if minute2 is None:
                minute2 = "00"

            if 'PM' in turn2.upper() and hour2 != '12':
                hour2 = str(int(hour2) + 12)

            if 'PM' in turn1.upper() and hour1 != '12':
                hour1 = str(int(hour1) + 12)

            if 'AM' in turn2.upper() and hour2 == '12':
                hour2 = '00'

            if 'AM' in turn1.upper() and hour1 == '12':
                hour1 = '00'

            if not (0 <= int(minute1) <= 59) or not (0 <= int(minute2) <= 59):
                raise ValueError

            print_fixed = f'{int(hour1):02d}:{int(minute1):02d} to {int(hour2):02d}:{int(minute2):02d}'
            return print_fixed
        else:
            raise ValueError
    except ValueError:
        raise ValueError


if __name__ == "__main__":
    main()
