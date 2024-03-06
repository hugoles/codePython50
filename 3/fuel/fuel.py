while True:
    try:
        x, y = input('Fraction: ').split('/')
        if not x.isdigit() or not y.isdigit():
            raise ValueError("Both must be integers")

        x = int(x)
        y = int(y)
        if x > y:
            raise ValueError("Numerator must be less than or equal to the denominator")

        if y != 0:
            output = (x / y) * 100
            output = int(round(output))
            if output > 98:
                print('F')
            elif output < 2:
                print('E')
            else:
                print(f'{output}%')
        else:
            raise ZeroDivisionError

        break

    except ValueError as ve:
        print(f"Error: {ve}")
    except ZeroDivisionError:
        print("Error: Division by zero")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
