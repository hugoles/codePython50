while  True:
    date  = input('Date: ').strip().title()

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    try:
        if date[0].isdigit():
            month, day, year = date.split(sep='/')
            month = int(month)
            day = int(day)
            if month <= 12 and day <= 31 and month >=1 and day >=1:
                print(f'{year}-{month:02}-{day:02}')
                break
        elif ',' in date:
            month, day, year = date.replace(',','').split(' ')
            day = int(day)
            month = months.index(month)+1
            if int(month) <= 12 and int(day) <= 31:
                print(f'{year}-{month:02}-{day:02}')
                break
    except:
        print()
        pass
