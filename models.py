from sqlalchemy import Column, Integer, Float, String,DateTime, ForeignKey, func, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


DATABASE_URL = f'postgresql://postgres:mypassword@localhost/postgres'
engine = create_engine(DATABASE_URL)

Base = declarative_base()

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    student_name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Groups', back_populates='student')
    grades = relationship('Grades', back_populates='student')

class Groups(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    group_name = Column(String, nullable=False)
    student = relationship('Students', back_populates='group')

class Teachers(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    teacher_name = Column(String, nullable=False)
    subjects = relationship('Subjects', order_by='Subjects.subject_name', back_populates='teacher')

class Subjects(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    subject_name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship('Teachers', back_populates='subjects')
    grades = relationship('Grades', back_populates='subject')

class Grades(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Float)
    date_of_grade = Column(DateTime, default=datetime.now)
    student = relationship('Students', back_populates='grades')
    subject = relationship('Subjects', back_populates='grades')

Base.metadata.create_all(engine)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()
