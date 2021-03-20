position = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']

for i in position:
    words = i.split(' ')
    same_name = words[-1]
    print(f'Привет, {same_name.capitalize()}!')
