number_to_translate = input("Enter number (from 'one' to 'ten'): ")

dict_numbers = {"one": "один", "two": "два", "three": "три",
                "four": "четыре", "five": "пять", "six": "шесть",
                "seven": "семь", "eight": "восемь", "nine": "девять",
                "ten": "десять"}

#def numtranslate(number_to_translate):
for elem in dict_numbers.setdefault(number_to_translate, "None"):
    x = elem
    print(x.title())

# Не могу понять как закинуть это все в функцию.