# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)

import numpy as np
import pandas as pd
     
class MyTable:
    digit = None
        
    def get_table(self, digit, n):
        df = pd.DataFrame(digit, index=list(range(2009,2021)), columns=list(range(1,n+1)))
        print(df)
        print('Number of rows: ', len(df.index))
        print('Number of columns: ', n)

    
c1 = MyTable()
print(c1.get_table(1, 12))
c2 = MyTable()
print(c2.get_table(3, 9))

# Хех, хитро!)
# Ну, это не то что я ожидал, если честно) объект DataFrame и есть таблица из модудя pandas
# а так вариант например такой

class Table:
    
    def __init__(self,rows, cols):
        self.field = [ [None for _ in range(cols)] for _ in range(rows) ]
        self.rows = rows
        self.cols = cols
        
    def get_value(self, row, col):
        if  row in range(self.rows) and col in range(self.cols):
            return self.field[row][col]
        return
 
    def set_value(self, row, col,value):
        self.field[row][col] = value
    
    def n_rows(self):
        return self.rows
 
    def n_cols(self):
        return self.cols

matrix = Table(rows=10, cols=10)
print(matrix.n_cols())
print(matrix.get_value(2, 2))
matrix.set_value(2, 2, 'a')
print(matrix.get_value(2, 2))
