percent = 'процент'

for i in range(0, 21):
    if i == 0 or i >= 5:
        print(str(i) + ' ' + percent + 'ов')
    elif 2 <= i < 5:
        print(str(i) + ' ' + percent + 'а')
    else:
        print(str(i) + ' ' + percent)
