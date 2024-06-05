import faker
from random import choices
from models import Students, Groups, Teachers, Subjects, Grades, session

NUMBER_OF_STUDENTS = 40
NUMBER_OF_GROUPS = 3
NUMBER_OF_SUBJECTS = 7
NUMBER_OF_TEACHERS = 4
NUMBER_OF_GRADES_PER_STUDENT = 20
LIST_OF_SUBJETS = ['Math', 'Art', 'English', 'Music', 'History', 'Science', 'Geography', 'Physical education']


def generate_data(number_of_students, number_of_groups, number_of_subjects, 
                       number_of_teachers, list_of_subjects, number_of_grades_per_student):

    fake_data = faker.Faker()

    groups = []
    for group_num in range(number_of_groups):
        group_name = f'Group {group_num + 1}'
        group = Groups(group_name=group_name)
        groups.append(group)
        session.add(group)

    teachers = []
    for _ in range(number_of_teachers):
        teacher = Teachers(teacher_name = fake_data.name())
        teachers.append(teacher)
        session.add(teacher)

    students = []
    for _ in range(number_of_students):
        student = Students(student_name=fake_data.name(), group=choices(groups)[0])
        students.append(student)
        session.add(student)

    subjects = []
    for subject_num in range(number_of_subjects):
        teacher = choices(teachers)[0]
        subject_name = list_of_subjects[subject_num]
        subject = Subjects(subject_name=subject_name, teacher=teacher)
        subjects.append(subject)
        session.add(subject)

    #creating a list of grades
    grades = []
    grade_value = 2
    while grade_value <= 6:
        grades.append(grade_value)
        grade_value += 0.5

    for student in students:
        num_of_grade = 0
        while num_of_grade < number_of_grades_per_student:
            grade = Grades(student=student, subject=choices(subjects)[0], grade=choices(grades)[0])
            session.add(grade)
            num_of_grade += 1
    
    session.commit()


if __name__ == '__main__':
    generate_data(NUMBER_OF_STUDENTS, NUMBER_OF_GROUPS, NUMBER_OF_SUBJECTS, NUMBER_OF_TEACHERS, LIST_OF_SUBJETS, NUMBER_OF_GRADES_PER_STUDENT)
    
   