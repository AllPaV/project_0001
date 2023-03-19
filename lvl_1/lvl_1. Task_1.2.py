# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

import random
songs_three = random.sample(my_favorite_songs, k=3)
a1 = songs_three[0]
a2 = songs_three[1]
a3 = songs_three[2]
song_duration = round(a1[1] + a2[1] + a3[1])
print(f"Три песни звучат {song_duration} минут")

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# import random
seq = list(my_favorite_songs_dict.values())
random_songs = random.sample(seq, k=3)
b1 = random_songs[0]
b2 = random_songs[1]
b3 = random_songs[2]
song_duration_dict = round(b1 + b2 + b3)
print(f"Три песни звучат {song_duration_dict} минут")

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

#A
# random.sample(my_favorite_songs, k=3) и переменные   - см. выше в "A"
print(a1[0], a2[0], a3[0], sep=", ")

#B
seq_keys2 = list(my_favorite_songs_dict.keys())
random_songs_dict = random.sample(seq_keys2, k=3)
print(random_songs_dict)

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

import datetime
song_duration_pr = (a1[1] + a2[1] + a3[1])
time = datetime.time(00, song_duration, 00).strftime('%M:%S')
print(time, type(time))
