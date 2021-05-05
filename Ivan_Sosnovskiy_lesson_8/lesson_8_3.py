def args_type(func):
    def logger(*args, **kwargs):
        for arg in args:
            print(f'{str(arg)}: {type(args)}')
    return logger


@args_type
def calc_cube(*args, **kwargs):
    result_list = []
    for num in args:
        result_list.append(num ** 3)


calc_cube(33)

#  не совсем понимаю почему в ответе получаю: кортеж !?
