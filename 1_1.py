duration = int(input())

if 60 < duration < 3600:
    m = duration // 60
    s = duration % 60
    print(f'{m} мин, {s} сек')
elif 3600 < duration < 86400:
    h = duration // 3600
    m = duration // 60 % 60
    s = duration % 60
    print(f'{h} ч, {m} мин, {s} сек')
elif 86400 <= duration < 31536000:
    d = duration // 86400
    h = (duration // 3600) % 60
    m = duration // 60 % 60
    s = duration % 60
    print(f'{d} сут, {h} ч, {m} мин, {s} сек')
elif duration >= 31536000:
    y = duration // 31536000
    d = duration // 86400 % 365
    h = duration // 3600 % 24
    m = duration // 60 % 60
    s = duration % 60
    print(f'{y} год, {d} сут, {h} ч, {m} мин, {s} сек')
else:
    print(f'{duration} сек')
