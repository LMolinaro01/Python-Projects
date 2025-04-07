n = 5

for i in range(n):
    print('-' * (n - i - 1) + (str(n - i) + '-') * i + str(n - i) + '-' * (n - i - 1))
