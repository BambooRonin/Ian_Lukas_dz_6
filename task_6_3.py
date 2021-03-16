from itertools import zip_longest

u = open('users.csv', 'r', encoding='utf-8')
h = open('hobby.csv', 'r', encoding='utf-8')
line_u_h = zip_longest((i.replace(',', ' ') for i in u), h, fillvalue=None)
d = {str(el[0]).strip(): (el[1].strip()) for el in line_u_h}

with open('task_6_3_text.txt', 'w', encoding='utf-8') as f:
    if 'None' in d:
        exit(1)
    else:
        f.write(str(d))
        print(d)
