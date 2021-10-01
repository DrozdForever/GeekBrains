import collections

with open('pars_logs.txt', 'w', encoding='utf-8') as p:
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        content = (f'{line.split()[0]} {line.split()[5][1:]} {line.split()[6]}' for line in f)
        for i in content:
            print(i, file=p)

with open('pars_logs.txt', 'r', encoding='utf-8') as f:
    my_dict = collections.Counter()

    for i in f:
        i = i.split()[0]
        my_dict[i] += 1

    ip, count = my_dict.most_common(1)[0][0], my_dict.most_common(1)[0][1]
    print(f'IP спаммера: {ip}\nКол-во отправленных запросов: {count}')
    