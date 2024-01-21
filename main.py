import sqlite3
from faker import Faker
import random
from datetime import datetime

conn = sqlite3.connect('university.db')
c = conn.cursor()

# Таблицы
c.execute('''CREATE TABLE IF NOT EXISTS groups (group_id INTEGER PRIMARY KEY AUTOINCREMENT,
 group_name TEXT NOT NULL)''')

c.execute('''CREATE TABLE IF NOT EXISTS students (student_id INTEGER PRIMARY KEY AUTOINCREMENT, 
name TEXT NOT NULL, group_id INTEGER, FOREIGN KEY (group_id) REFERENCES groups (group_id))''')

c.execute('''CREATE TABLE IF NOT EXISTS teachers (teacher_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)''')

c.execute('''CREATE TABLE IF NOT EXISTS subjects (subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL, teacher_id INTEGER, FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id))''')

c.execute('''CREATE TABLE IF NOT EXISTS grades (grade_id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER,
 subject_id INTEGER, grade INTEGER, date_received DATE, FOREIGN KEY (student_id) REFERENCES students (student_id),
  FOREIGN KEY (subject_id) REFERENCES subjects (subject_id))''')

# Наполним базу
fake = Faker()

# Добавляем группы
for _ in range(3):
    c.execute("INSERT INTO groups (group_name) VALUES (?)", (fake.word(),))

# Добавляем преподов
for _ in range(5):
    c.execute("INSERT INTO teachers (name) VALUES (?)", (fake.name(),))

# Добавляем предметы
subjects = ['Mathematics', 'Physics', 'Literature', 'History', 'Biology']
for subject in subjects:
    teacher_id = random.randint(1, 5)
    c.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject, teacher_id))

# ученики + оценки
for _ in range(50):
    group_id = random.randint(1, 3)
    c.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (fake.name(), group_id))
    student_id = c.lastrowid
    for subject_id in range(1, 6):
        for _ in range(random.randint(5, 20)):
            grade = random.randint(1, 10)
            date_received = fake.date_between(start_date='-1y', end_date='today')
            c.execute("INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)", (student_id, subject_id, grade, date_received))


conn.commit()
conn.close()
