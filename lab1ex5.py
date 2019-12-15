"""даны формулы для вычислений и исходные данные:
   для цикла for
   для цикла while
   двойного цикла (while in for)
  надо разработать три циклические программы с одними и теми же расчетными формулами.
При наличии ошибок из-за некорректных исходных данных выполнить вычисления с другими числами
"""
# задание за 11.12.2019 №2 вариант 7
print('цикл for')
import numpy

i = (9, 1.4, 5)  # вместо -1.4 взяли положительное число 1.4 т.к нельзя извлечь корень из отриц. числа
t = 6.96 * (10 ** (-5))
x = 0.9
y = 2
for j in range(len(i)):
    z = t * (y ** 2) - numpy.sqrt(i[j] + x) * numpy.tan(y)
    g = numpy.sqrt((z ** 2) + (5 * z)) * numpy.log(y)
    print(g)

print('цикл while')
i = 1
while i <= 2:
    z = t * (y ** 2) - numpy.sqrt(i + x) * numpy.tan(y)
    r = numpy.sqrt((z ** 2) + (5 * z)) * numpy.log(y)
    i += 0.2
    print(r)

print('двойной цикл')
y = 2
x = (0.7, 1, 9)
t = 2
i = 0
for p in range(len(x)):
    print(p) # для проверки при каком значении x выполяется цикл while
    while t <= 3:
        z = t * (y ** 2) - numpy.sqrt(i + x[p]) * numpy.tan(y)
        b = numpy.sqrt((z ** 2) + (5 * z)) * numpy.log(y)
        t += 0.2
        print(b)


