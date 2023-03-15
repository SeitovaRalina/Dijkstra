import math
i = math.inf
g = [[i, 5, i, i, i, 8],
     [i, i, 4, i, i, 3],
     [i, i, i, i, 3, i],
     [i, i, 4, i, i, i],
     [i, i, i, i, i, i],
     [i, i, i, 7, 4, i]]

g = [[i, 3, 1, 3, i, i],
     [3, i, 4, i, i, i],
     [1, 4, i, i, 7, 5],
     [3, i, i, i, i, 2],
     [i, i, 7, i, i, 4],
     [i, i, 5, 2, 4, i]]

g = [[i, 15, i, 23, 14, i, i, i, i],
     [15, i, 19, 16, 15, i, i, i, i],
     [i, 19, i, i, 14, 26, i, i, i],
     [23, 16, i, i, 25, i, 23, 20, i],
     [14, 15, 14, 25, i, 24, i, 27, 18],
     [i, i, 26, i, 24, i, i, i, i],
     [i, i, i, 23, i, i, i, 14, i],
     [i, i, i, 20, 27, i, 14, i, 18],
     [i, i, i, i, 18, i, i, 18, i]]
v = int(input('Введите номер стартовой вершины: ')) - 1 # она же далее текущая
n = len(g)
s = {v}
str = [i]*n  # последняя строка таблицы
res = [0]*n  # значения для каждой вершины
str[v], index, start = 0, 0, v
for nevazhno in range(n-1):
     mn = i
     for j in range(n):  # по всем вершинам
          if j not in s:  # если вершины нет среди использованных
               str[j] = min(str[j], str[v] + g[v][j])
               if mn > str[j]:
                    index = j  # поиск вершины с минимальным значением из неиспользованных
                    mn = str[j]
     v = index
     s.add(v)
     res[v] = str[v]

for i in range(n-1):
     if i != start:
          print(f'Мин. путь до вершины {i+1} равен: {res[i]}')