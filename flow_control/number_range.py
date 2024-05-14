def number_range(i):
    i = int(i)
    if 0 <= i <= 50:
        print(f'{i} is between 0 and 50')
    elif 51 <= i <= 100:
        print(f'{i} is between 51 and 100')
    elif i > 100:
        print(f'{i} is greater than 100')
    elif i < 0:
        print(f'{i} is less than 0')
    else:
        print(f'{i} is in some other range')
