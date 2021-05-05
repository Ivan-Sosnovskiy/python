class Road:

    def __init__(self, lenght, widht):
        self._lenght = lenght
        self._widht = widht
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._lenght * self._widht * self.weight * self.height / 1000
        print(f'Для покрытия дорожного полотна длиной {self._lenght} м необходимо {asphalt_mass} т асфальта')

r = Road(5000, 20)
r.asphalt_mass()

