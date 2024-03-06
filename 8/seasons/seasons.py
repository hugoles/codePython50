from datetime import date, datetime
import inflect
import sys

def seasons(s):
    try:
        datetime.strptime(s, '%Y-%m-%d')
        s = s.split('-')
        d = date(int(s[0]), int(s[1]), int(s[2]))
        today = date.today()
        lapse = today - d
        p = inflect.engine()
        m = int(lapse.total_seconds() / 60)
        phrase = p.number_to_words(m, andword="").capitalize()
        return phrase + ' minutes'
    except ValueError:
        sys.exit(1)

def main():
    print(seasons(input('Date of Birth: ')))

if __name__ == "__main__":
    main()
