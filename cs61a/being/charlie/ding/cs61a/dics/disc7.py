from datetime import date
class Student(object):
    students =0
    def __init__(self,name,staff):
        self.name = name
        self.understanding =0
        Student.students +=1
        print("There are now ", Student.students, "students")
        staff.add_student(self)
    def visit_office_hours(self,staff):
        staff.assist(self)
        print("Thanks," + staff.name)


class Professor:
    def __init__(self,name,school=''):
        self.name = name
        self.students ={}
        self.school= school

    def update_shcool(self,school):
        self.school = school

    def add_student(self,student):
        self.students[student.name] = student

    def assist(self,student):
        student.understanding +=1
        self.school.add_log(LogAssist(self.name,student.name))


class LogAssist(object):
    def __init__(self,staff_name, student_name):
        self.time = date.today()
        self.staff_name = staff_name
        self.student_name = student_name

    def __str__(self):
        reslut=''
        reslut = str(self.time) +' - '+ self.staff_name +'->'+ self.student_name
        return reslut



class School:
    def __init__(self,name):
        self.professors = []
        self.name = name
        self.log_assist={}

    def add_professor(self,professor):
        self.professors.append(professor)
        professor.update_shcool(self)

    def get_all_students(self):
        students =[]
        for pro in self.professors:
            students.extend(pro.students)
        return students

    def add_log(self,log_assist):
        if self.log_assist.__contains__(log_assist.staff_name):
            self.log_assist[log_assist.staff_name].append(log_assist)
        else:
            self.log_assist[log_assist.staff_name] = [log_assist]

    def present_assist_log(self):
        report=''
        for key in self.log_assist:
            lst = self.log_assist[key]
            temp = key+": ["
            for item in lst:
                temp = temp + '|'+ str(item)
            temp = temp +" ]"
            report = report + temp

        return report



def test_date():
    print(date.isocalendar(date.today()))

test_date()

def some_test_init():

    richmond_rose = School('Richmond Rose')

    professor_fiona = Professor('Fiona')
    professor_charlie = Professor('Charlie')

    student_daniel = Student('Daniel', professor_fiona)
    student_joz = Student('Joz', professor_fiona)
    student_lucy = Student('Lucy', professor_fiona)

    student_jim = Student('Jim', professor_charlie)
    student_rosa = Student('Rosa', professor_charlie)
    student_nigola = Student('Nigola', professor_charlie)

    richmond_rose.add_professor(professor_charlie)

    richmond_rose.add_professor(professor_fiona)

    # test 1 professor assist students:
    professor_charlie.assist(student_jim)
    professor_fiona.assist(student_daniel)
    professor_fiona.assist(student_daniel)
    professor_fiona.assist(student_daniel)
    professor_fiona.assist(student_daniel)

    professor_charlie.assist(student_daniel)

    print(richmond_rose.present_assist_log())




def present_student_of_professor(professor,student1):
    # print(professor.students[student1])
    object1 = professor.students[student1]

    print(object1.understanding)


some_test_init()

class MinList:
    """ A list that can only pop the smallest element"""
    def __init__(self):
        self.items= []
        self.size =0

    def append(self,item):
        """ Appends an item to the MinList"""
        self.items.append(item)
        self.size = self.size +1
        return self

    def pop(self):
        """ Removes and returns the smallest item from the MinList"""
        index_min,i,pre=0,0,self.items[0]
        while i<= self.size-1:
            temp = self.items[i]
            if temp < pre:
                pre = temp
                index_min = i
            i = i+1
        self.items[index_min]=False
        new_items =[]
        for item in self.items:
            if item:
                new_items.append(item)
        self.items =new_items
        self.size = len(new_items)
        return pre

def test_MinList():
    minlist = MinList()
    minlist.append(10).append(12).append(6).append(3).append(-10).append(-2)
    for _ in range(1,7):
        print(minlist.pop())



test_MinList()