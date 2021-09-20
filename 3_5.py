from random import choice, randrange

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью', 'летом', 'зимой']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий', 'невероятный']


def get_jokes(n, repeat=False):
    """
    Функция, возвращающая n рандомных шуток, собранных из трёх списков

    param n: кол-во шуток
    param repeat: флаг уникальности шуток(выкл. по умолчанию)
    return: список случайных шуток

    """
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    jokes = []
    list_min = min(no, adv, adj)

    while n and len(list_min):
        num = randrange(len(list_min))
        if repeat:
            jokes.append(f'{no.pop(num)} {adv.pop(num)} {adj.pop(num)}')
        else:
            jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        n -= 1
    return jokes


print(get_jokes(10))
