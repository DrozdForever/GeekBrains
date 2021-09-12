my_list = []
my_sum = 0

for i in range(1, 1000, 2):
    my_list.append(i ** 3)

for ind, n in enumerate(my_list):
    sum_one = 0
    while n:
        sum_one += n % 10
        n //= 10
    if sum_one % 7 == 0:
        my_sum += my_list[ind]
    my_list[ind] += 17

print(my_sum)

my_sum = 0

for ind, n in enumerate(my_list):
    sum_one = 0
    while n:
        sum_one += n % 10
        n //= 10
    if sum_one % 7 == 0:
        my_sum += my_list[ind]

print(my_sum)





