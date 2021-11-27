# Python Lab Assignment 3
# Charlie Ding | 301159548

# week 6 begin

def week6_exercise_1():
    my_favorite_things="""
    watching TV
    going jog
    playing basketball
    """
    first_name ="Zhigang"
    last_name ="Ding"
    address ="richmond hill"
    info_charlie = first_name+ last_name+ " 's addresss is" + address
    print(info_charlie)

def week6_exercise_2():
    a_list_of_agile_software =['Scrum','XP','FDD','DSDM','ASD','LSD']

    a_list_of_agile_software.append('A brand new method')
    a_list_of_agile_software.remove('XP')
    left_list = a_list_of_agile_software[1:]

def week6_exercise_3():
    course_list=['comp100','comp120','comp213']
    print('you have enrolled in ',course_list[0])
    course_list.append('comp220')

# week 6 end

# week 8 begin

def week8_exercise_1():
    favorite_languages = {
        'jen': 'HTML',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'C#',
    }
    favorite_languages['phil'] = 'Python'
    favorite_languages['charlie']='Java'
    favorite_languages.pop('jen')
    for key in favorite_languages:
        print(key)
        print(favorite_languages[key])


def week8_exercise_2():
    student={}
    student['name']='Charlie'
    student['sbuject']='Software Engineering'
    student['semester']='semester one'
    student['grade'] ='A'
    student['lab'] ='A'


    for key in student:
        print(key)
        print('----')
        print(student[key])

# week 8 end

# week 9 begin

def week9_exercise_1(temperature):
    if temperature < 98:
        return 'Cold'
    elif temperature > 98:
        return 'Hot'
    return 'Normal'

def week9_exercise_2():
    agile_values = ['Individuals and interactions', 'Working software ', 'Customer collaboration ',
                    'Responding to change']
    for i in range(0,len(agile_values)):
        print(agile_values[i])


# week 9 end

# week 10 begin

def team_collaboration(name1,name2):
    print('I use [',name1,name2,'] software for team collaboration')

# global project id  for week 10 exercise 2
project_id = 1

def project(id):
    print('My global project id is',project_id)
    print('My internal project id is ', id)


team_collaboration('jira','git')
# week 10 end

# week 11 begin
import calendar
import  operator

def week11_exercise_1():
    year =2021
    mm =10
    print(calendar.month(year,mm))

def week11_exercise_2():
    print(
        operator.add(1,2))
    print(
        operator.sub(2,1) )
    print(
        operator.mul(1,2))
    print(
        operator.mod(10,2))
    print(
        operator.abs(-1))

week11_exercise_2()

# week 11 end

# week 12 begin

import os

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

def week12_exercise_1():

    os.mkdir('week12_ex_2')
    touch('week12_ex_2/test2.txt')
    touch('week12_ex_2/test3.txt')
    touch('week12_ex_2/test4.txt')
    os.remove('week12_ex_2/test2.txt')

    for f in os.listdir('week12_ex_2'):
        print(f)

import pandas as pd

def week12_exercise_2():
    data = {
        'subject_id': [1, 2, 3, 4],
        'student_name ': ['Joseph','Eva','Kevin','Joseph'],
        'courses':['software engineering','Artificial Intelligence','Gaming','Software engineering technician']
    }
    course_info = pd.DataFrame(data)
    print(course_info)


week12_exercise_2()

# week 12 end

# week 13 begin
def week13_exercise_1():
    if os.path.isfile('pi_digits.txt'):
        os.remove('pi_digits.txt')
    touch('pi_digits.txt')
    f = open('pi_digits.txt','w')
    f.write('-----------------------\n')
    f.close()
    f = open('pi_digits.txt','a')
    f.write('3.1415926535\n')
    f.write('8979323848\n')
    f.write('2643384379\n')
    f.write('-----------------------\n')
    f.close()

    f= open('pi_digits.txt','r')
    for line in f:
        print(line)


# week 13 end





