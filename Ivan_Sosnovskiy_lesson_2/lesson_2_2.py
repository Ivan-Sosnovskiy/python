list_weather = ['В', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

list_weather_1 = []

for item in list_weather:
    is_number = False
    if item.isdigit():
        new_elem = f'{int(item):02}'
        is_number = True
        list_weather_1.append('"')
        list_weather_1.append(new_elem)
        list_weather_1.append('"')
    else:
        list_weather_1.append(item)

list_weather_2 = ' '.join(list_weather_1)
print(list_weather_2)
