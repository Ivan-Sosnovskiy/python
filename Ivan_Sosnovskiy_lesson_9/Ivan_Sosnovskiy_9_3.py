class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(b)}

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super(Worker, self).__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

p = Position('Ivan', 'Sosnovskiy', 'DI', 70000, 30000)
print(p.get_full_name(), p.get_total_income())

#  Получаю ошибку для встроенной функции 'super'
#  super() – это встроенная функция языка Python.
#  Она возвращает прокси-объект, который делегирует вызовы методов классу-родителю
#  (или собрату) текущего класса (или класса на выбор, если он указан, как параметр).
#  Основное ее применение и польза – получения доступа из класса наследника к методам класса-родителя
#  в том случае, если наследник переопределил эти методы.

#  Подскажите в чем ошибка ??