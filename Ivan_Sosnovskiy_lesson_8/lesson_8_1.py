import re


def email_parse(email):
    pattern = re.compile(r'[^@]+@[^@\.]+\.[^@\.]+')
    if (pattern.fullmatch(email)) is None:
        raise ValueError(f'Wrong email:{email} ! ')
    else:
        data = email.split('@')
        adress_voc = {'Username': data[0], 'Domain:': data[1]}
    return adress_voc


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))