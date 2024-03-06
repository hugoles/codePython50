Due = 50
print(f'Amount Due: {Due}')
value = 0
while value < 50:
    coin = int(input('Insert Coin: '))
    if coin == 25 or coin == 10 or coin == 5:
        value += coin
        Due -= coin
        if Due > 0:
            print(f'Amount Due: {Due}')
    else:
        print(f'Amount Due: {Due}')
if value >= 50:
    Due = abs(Due)
    print(f'Change Owed: {Due}')




