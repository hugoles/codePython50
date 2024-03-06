def main():
    while True:
        try:
            fraction = input('Fraction: ')
            convert(fraction)
            break
        except ZeroDivisionError:
            print("Error: Division by zero")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def convert(fraction):
    x, y = fraction.split('/')
    if not x.isdigit() or not y.isdigit():
        raise ValueError("Both must be integers")

    x = int(x)
    y = int(y)
    if x > y:
        raise ValueError("Numerator must be less than or equal to the denominator")

    if y != 0:
        percentage = (x / y) * 100
        gauge(percentage)
        return percentage
    else:
        raise ZeroDivisionError


def gauge(percentage):
    percentage = int(round(percentage))
    if percentage > 98:
        return 'F'
    elif percentage < 2:
        return 'E'
    else:
        return f'{percentage:.0f}%'


if __name__ == "__main__":
    main()
