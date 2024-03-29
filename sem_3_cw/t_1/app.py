# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
# возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название
# факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.


from flask import Flask, render_template
from models import Student, db, Faculty

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')

@app.cli.command('add-date')
def add_date():
    for i in range(1, 6):
        faculty = Faculty(faculty_name = f'faculty_name{i}', )
        db.session.add(faculty)
    for i in range(1, 6):
        student = Student(name = f'name{i}', 
                          surname = f'surname{i}',
                          age = i,
                          group = 'A',
                          gender ='male',
                          faculty_id = i)
        db.session.add(student)
    db.session.commit()
    print('OK')

@app.route('/students/')
def all_students():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)
