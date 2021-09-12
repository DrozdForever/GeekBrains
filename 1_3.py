b = 0

for i in range(102):
    percent = f'{i-1} {b}'
    if i % 10 == 1 and i % 100 != 11:
        b = 'процент'
        print(percent)
    elif 1 < i % 10 < 5 and not 11 < i % 100 < 15:
        b = 'процента'
        print(percent)
    else:
        b = 'процентов'
        print(percent)

