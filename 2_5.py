price = [15.99, 45.5, 100, 1799.99, 2.3, 458.48, 219.99, 649.99, 50, 300]

for i in price:
    r, k = str(f'{i:.2f}').split('.')
    print(f'{r} руб. {int(k):02d} коп.', end=', ')

print(f'\nID: {id(price)} - {price}')
price.sort()
print(f'ID: {id(price)} - {price}')

rev_price = sorted(price, reverse=True)
print(f'ID: {id(rev_price)} - {rev_price}')

print(f'{price[5:]}')
