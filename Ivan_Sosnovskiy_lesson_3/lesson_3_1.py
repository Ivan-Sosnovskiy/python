number_to_translate = input("Enter number (from 'one' to 'ten'): ")

dict_numbers = {"one": "один", "two": "два", "three": "три",
                "four": "четыре", "five": "пять", "six": "шесть",
                "seven": "семь", "eight": "восемь", "nine": "девять",
                "ten": "десять"}

#def numtranslate(number_to_translate):
for elem in dict_numbers.setdefault(number_to_translate, "None"):
    x = elem
    print(x)

# Не могу понять как закинуть это все в функцию.











   # x = dict_numbers.get(number_to_translate)
    #print(x)






    #dict_numbers.values()






