# 1) Создать переменную типа String
a = 'Liza'

# 2) Создать переменную типа Integer
b = 22

# 3) Создать переменную типа Float
c = 3.5

# 4) Создать переменную типа Bytes
d = bytes('Hello, Liza', 'UTF-8')

# 5) Создать переменную типа List
e = [a, d, c, d]

# 6) Создать переменную типа Tuple
i = tuple('Hello')

# 7) Создать переменную типа Set
q = set('Liza')

# 8. Создать переменную типа Frozen set
w = frozenset('Edward')

# 9) Создать переменную типа Dict
r = dict(sa='1', ra='2', ta='3')

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)
print(type(i), i)
print(type(q), q)
print(type(w), w)
print(type(r), r)

# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
li = 'Liza'
ya = 'Yaroslav'
liya = li + ya

print(li, ' + ', ya)


# 12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
qw = 12947
wq = 23456

summ = qw + wq
print(summ)

# 13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
divide = qw / wq
print(divide)

# 14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
multi = qw * wq
print(multi)

# 15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
dividerest = qw // wq
print(dividerest)

# 16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
rest = qw % wq
print(rest)

# 17) (7 + 12)  3 + 7 * 4 - 44 / 2  4 расставить точки так чтобы получилось 6884.25. Вывести в консоль.
equal = (7 + 12) ** 3 + 7 * 4 - 44 / 2 ** 4

print(equal)
