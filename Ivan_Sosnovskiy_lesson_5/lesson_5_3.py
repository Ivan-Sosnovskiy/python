tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б']# '10А', '10Б', '9А']


def get_gen(first_list, second_list):
    diff = len(first_list) - len(second_list)
    if diff > 0:
        second_list.extend([None for i in range(diff)])
    for t, k in zip(first_list, second_list):
        yield t, k

gen = get_gen(tutors, klasses)
print(type(gen))

print(gen)
print(type(gen))
print(list(gen))

