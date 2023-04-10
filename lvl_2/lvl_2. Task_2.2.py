# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.


def quarter_of(month):
    months = {1:'январь', 2:'февраль', 3:'март', 4:'апрель', 5:'май', 6:'июнь', 7 :'июль', 8 : 'август', 9 :'сенябрь', 10 :'октябрь', 11 :'ноябрь', 12 :'декабрь'}
    w = {1:'первого', 2: 'второго', 3: 'третьего', 4: 'четвёртого'}
    if m < 1 or m > 12:
        return("Такого месяца нет! Вы ввели некорректное значение")
    elif m <= 3:
        w = w[1]
        return(f"Месяц {m} ({months[m]}) является частью {w} квартала")
    elif 4 <= m <= 6:
        w = w[2]
        return(f"Месяц {m} ({months[m]}) является частью {w} квартала")
    elif 7 <= m <= 9:
        w = w[3]
        return(f"Месяц {m} ({months[m]}) является частью {w} квартала")
    elif 10 <= m <= 12:
        w = w[4]
        return(f"Месяц {m} ({months[m]}) является частью {w} квартала")

m = int(input('Введите номер месяца: '))
print(quarter_of(m))

# Можно покороче
def quarter_of(month):
    q = {1: (1,3), 2:(4,6), 3:(7,9), 4:(10,12)}
    return [k for k,v in q.items() if v[0] <= month <= v[1]][0]
