from sys import argv

with open('bakery.csv', 'r+', encoding='utf-8') as f_r:
    pos, val = argv[1:]
    for line in range(int(pos) - 1):
        n = f_r.readline()
    f_r.seek(f_r.tell())
    f_r.write(f'{val + " " * len(n) }\n')
