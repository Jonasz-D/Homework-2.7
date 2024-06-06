from sqlalchemy import func, cast, Numeric
from sqlalchemy.sql.expression import desc
from models import session, Students, Groups, Teachers, Subjects, Grades


def select_1():
    top_students = session.query(Students.student_name, func.avg(Grades.grade).label('avg_grade')) \
        .join(Grades) \
        .group_by(Students.id) \
        .order_by(desc('avg_grade')) \
        .limit(5) \
        .all()
    print("1. 5 studentów z najwyższą średnią ocen ze wszystkich przedmiotów:")
    print(top_students)

def select_2():
    top_student_subject = session.query(Students.student_name, func.avg(Grades.grade).label('avg_grade')) \
        .join(Grades) \
        .join(Subjects) \
        .filter(Subjects.subject_name == 'Science') \
        .group_by(Students.id) \
        .order_by(desc('avg_grade')) \
        .first()
    print("2. Studnet z najwyższą średnią ocen z określonego przedmiotu:")
    print(top_student_subject)

def select_3():
    
    avg_grade_group = session.query(func.round(cast(func.avg(Grades.grade), Numeric), 2).label('avg_grade')) \
        .join(Subjects) \
        .filter(Subjects.subject_name == 'Science') \
        .scalar()
    print("3. Średni wynik w grupach dla określonego przedmiotu:")
    print(avg_grade_group)

def select_4():
    avg_all_grades_group = session.query(Groups.group_name, func.avg(Grades.grade)) \
        .select_from(Grades) \
        .join(Students) \
        .join(Groups) \
        .group_by(Groups.id) \
        .order_by(Groups.id) \
        .all()
    print('4. Średni wynik w grupie (w całej tabeli ocen):')
    print(avg_all_grades_group)

def select_5():
    subject_by_teachers = session.query(Subjects.subject_name, Teachers.teacher_name) \
        .select_from(Subjects) \
        .join(Teachers) \
        .filter(Teachers.teacher_name == 'David Leonard') \
        .all()
    print('5. Przedmioty, których uczy określony wykładowca:')
    print(subject_by_teachers)

def select_6():
    list_of_students_in_group = session.query(Groups.group_name, Students.student_name) \
        .join(Students) \
        .filter(Groups.group_name == 'Group 1') \
        .all()
    print('6. Lista studentów w określonej grupie:')
    print(list_of_students_in_group)

def select_7():
    grades_of_students_in_groups_by_subject = session.query(Groups.group_name, Students.student_name, Subjects.subject_name, Grades.grade) \
        .select_from(Grades) \
        .join(Students) \
        .join(Subjects) \
        .join(Groups) \
        .filter(Groups.group_name == 'Group 1') \
        .filter(Subjects.subject_name == 'Music') \
        .all()
    print('7. Oceny studentów w określonej grupie z danego przedmiotu:')
    print(grades_of_students_in_groups_by_subject)

def select_8():
    avg_grade_of_subjects_by_teacher = session.query(Teachers.teacher_name, func.avg(Grades.grade)) \
        .select_from(Teachers) \
        .join(Subjects) \
        .join(Grades) \
        .group_by(Teachers.teacher_name) \
        .filter(Teachers.teacher_name == 'David Leonard') \
        .all()
    print('8. Średnia ocena wystawiona przez określonego wykładowcę z jego przedmiotów:')
    print(avg_grade_of_subjects_by_teacher)


def select_9():
    list_of_subject_by_studnet = session.query(Students.student_name, Subjects.subject_name) \
        .select_from(Grades) \
        .join(Subjects) \
        .join(Students) \
        .filter(Students.student_name == 'Paul Conley') \
        .all()
    print("9. Lista przedmiotów zaliczonych przez danego studenta")
    print(list_of_subject_by_studnet)

def select_10():
    msg = "1. 5 studentów z najwyższą średnią ocen ze wszystkich przedmiotów:"
    list_of_subject_by_teacher_for_student = session.query(Subjects.subject_name) \
        .select_from(Grades) \
        .join(Subjects) \
        .join(Teachers) \
        .join(Students) \
        .filter(Students.student_name == 'Paul Conley', Teachers.teacher_name == 'David Leonard') \
        .group_by(Subjects.subject_name) \
        .all()
    print('10. Lista kursów prowadzonych przez określonego wykładowcę dla określonego studenta')
    print(list_of_subject_by_teacher_for_student)


if __name__ == '__main__':
    select_1()
    select_2()
    select_3()
    select_4()
    select_5()
    select_6()
    select_7()
    select_8()
    select_9()
    select_10()

















