import json

result_dict = {}

with open('users.csv', 'r', encoding='utf-8') as u, open('hobby.csv', 'r', encoding='utf-8') as h:
    u_line = u.readline().strip()
    h_line = h.readline().strip()
    while u_line:
        result_dict.update({u_line: h_line})
        u_line = u.readline().strip()
        h_line = h.readline().strip()

with open('users_hobby.json', 'w+', encoding='utf-8') as f:
    print(result_dict)
    json.dump(result_dict, f)


