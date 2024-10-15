n = int(input('Введите целое число: '))

def escape_from_trap(n):
    if n < 3 or n > 20:
        return print('Неправильное число')

    password = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return f'{n} - {password}\nПароль верен!'


result = escape_from_trap(n)
print(result)