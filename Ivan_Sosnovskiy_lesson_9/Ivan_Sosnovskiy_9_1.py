from time import sleep

class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def switch_light(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:  # обращение к 1 элементу списка
                sleep(7)
            elif i == 1:  # обращение ко 2 элементу списка
                sleep(2)
            elif i == 2:  # обращение к 3 элементу списка
                sleep(8)
            i += 1

t = TrafficLight()
t.switch_light()


