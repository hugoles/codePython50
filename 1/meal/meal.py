def main():
    time = input('What time is it? ')
    x = convert(time)
    if x >= 7 and x <= 8:
        print('breakfast time')
    if x >= 12 and x <= 14:
        print('lunch time')
    if x >= 18 and x <= 20:
        print('dinner time')
def convert(time):
    time = time.split(':')
    y = float(time[0])
    z = time[1][0:2]
    z = float(z)/60
    return y+z

if __name__ == "__main__":
    main()
