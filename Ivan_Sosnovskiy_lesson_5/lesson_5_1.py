def odd_numbers(n):
    for number in range(1, n + 1, 2):
        yield number

gen = odd_numbers(15)

print(list(gen))






