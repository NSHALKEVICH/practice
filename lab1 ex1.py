# задача: ввести три числа m, n, p и посчитать количество отрицательных чисел
m = float(input())
n = float(input())
p = float(input())
col_neg = 0
if m < 0:
    col_neg += 1
if n < 0:
    col_neg += 1
if p < 0:
    col_neg += 1
print('количество отрицательных чисел равно', col_neg)
