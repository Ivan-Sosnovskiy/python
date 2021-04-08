with open('nginx.txt', 'r', encoding='utf-8') as f:
    pars_list = []
    line = f.readline()
    while line:
        data = line.split()
        pars_list.append((data[0], data[5], data[6]))
        line = f.readline()
print(pars_list)

# я бы сам наверное не додумался что можно так просто распарсить,
# два вечера просидел пытаясь понять к чему привязать split, поиск закономерностей в строках, разная длина строк
# блин застрел башки :)




