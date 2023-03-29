# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!

arr = input('Введите любое количество целых чисел: ').split(' ')
c = len(arr)
def minimum(arr):
    for i in range(c-1):
        for z in range(c-i-1):
            if arr[z] > arr[z+1]:
                arr[z], arr[z+1] = arr[z+1], arr[z]
    return arr[0]

def maximum(arr):
    for i in range(c-1):
        for z in range(c-i-1):
            if arr[z] > arr[z+1]:
                arr[z], arr[z+1] = arr[z+1], arr[z]
    return arr[-1]

print('Минимальное значение:', minimum(arr))
print('Максимальное значение:', maximum(arr))

