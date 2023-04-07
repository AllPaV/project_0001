'''Пункт 1. Создать таблицу'''

# import sqlite3
# connection = sqlite3.connect('students_hw.db')
# cursor = connection.cursor()
# query = """CREATE TABLE Students (
# Student_Id INTEGER NOT NULL PRIMARY KEY,
# Student_Name TEXT NOT NULL,
# School_Id INTEGER NOT NULL);
# """
# cursor.execute(query)
# connection.commit()
# connection.close()

''' Пункт 2. Наполнить таблицу'''
# import sqlite3
# connection = sqlite3.connect('students_hw.db')
# cursor = connection.cursor()
# query = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
# VALUES
# ('201', 'Иван', '1'),
# ('202', 'Петр', '2'),
# ('203', 'Анастасия', '3'),
# ('204', 'Игорь', '4');
# """
# cursor.execute(query)
# connection.commit()
# connection.close()

'''Пункт 3. Написать программу, с помощью которой по ID студента можно получать информацию
о школе и студенте.'''

import sqlite3

def get_connection():
    connection = sqlite3.connect('students_hw.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_student_info(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """SELECT * FROM Students WHERE Student_Id = ?"""
        cursor.execute(select_query,(student_id))
        records = cursor.fetchall()
        print("Данные по студентам")
        for row in records:
            print("ID студента: ", row[0])
            print("Имя студента: ", row[1])
            print("ID школы: ", row[2])
            # print("Название школы: ")
        cursor.execute(select_query)
        connection.commit()
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print('Ошибка в получении данных ', error)

print("Вывод информации по задаче:")
get_student_info(203)