from requests import utils, api, get
import xml2df
import json
import xml
import xmlrpc
import pandas
import xmltodict3

response = get('http://www.cbr.ru/scripts/xml_daily.asp')  # ответв <xml>
respons_1 = get('https://www.cbr-xml-daily.ru/daily_json.js')  # ответ в json

response_dic_1 = json.loads(respons_1.content)  # ответ в json переводим в словарь

print(respons_1.status_code)
print(respons_1.content)
print(response_dic_1['Valute'])
print(response_dic_1["Date"])
#  print(response_dic_1["Valute"])


valute_dict = response_dic_1["Valute"]  # новая переменная(type = dict) ==
                                        # словарь и вложенные значения по ключу "Valute"
valute_dict_under = valute_dict.values()  # новая переменная(type = dict) == значения из словаря "valute_dict"

print(valute_dict_under)
print(valute_dict)

for key in valute_dict.keys():  # итерация по словарю == все ключи
    print(key)
for value in valute_dict.values():  # итерация по списку == все значения
    print(value)


def currensy_rates(string):
    if input(string) == key(valute_dict_under):
        print(type(value))

#  не смог нагуглить как получить конкретное значение по ключу из словаря в словаре








