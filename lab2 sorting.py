import random
import datetime
import prettytable                  # пакет для таблицы
import matplotlib.pyplot as plt     # библиотека для графика

def InsertSort(A):
    # сортировка списка вставками
    N = len(A)
    for top in range(1, N):     # top-элемент, который вставляют. Начинаем с индекса 1, т.к. 0 элемент a priori отсортирован
        k = top                 # новая переменная
        while k > 0 and A[k-1] > A[k]:
            # k>0, чтобы не выйти за массив (-1 элемент);
            # пока отсортированный элемент больше top (сортировка справа налево, от больших к меньшим),
            A[k], A[k-1] = A[k-1], A[k]
            # отсортированный A[k-1] уступает место, сдвигаясь вправо
            k -= 1

def ChoiseSort(A):
    # сортировка списка выбором
    N = len(A)
    for position in range(0, N-1):
        for k in range (position+1,N):    # (position+1) для тех элементов, что правее
            if A[k] < A[position]:
               A[k], A[position] = A[position], A[k]



table = prettytable.PrettyTable(["Размер списка", "время сортировки вставками", "Время сортировки выбором"])
x=[]
y1=[]
y2=[]



for N in range(100,2001,100):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    #print(A)

    B = A.copy()
    # print(B)

    # InsertSort(A)
    print("---")
    # print(A)


    # ChoiseSort(B)
    print("---")
    # print(B)

    t1 = datetime.datetime.now()
    InsertSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Сортировка вставками" +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    ChoiseSort(B)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Сортировка выбором" +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds())])
print(table)

plt.plot(x, y1, "C6")        # x количество элементов, y время сортировки, C колор
plt.plot(x, y2, "C1")
plt.show()
