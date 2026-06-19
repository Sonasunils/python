#single inheritance

# Base class
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")

# # Derived class
# class Child(Parent):
#     def func2(self):
#         print("This function is in child class.")

# # Driver code
# obj = Child()
# obj.func1()
# obj.func2()

#multiple inheritance

# Base class 1
# class Mother:
#     mothername = ""

#     def mother(self):
#         print(self.mothername)

# # Base class 2
# class Father:
#     fathername = ""

#     def father(self):
#         print(self.fathername)

# # Derived class
# class Son(Mother, Father):
#     def parents(self):
#         print("Father :", self.fathername)
#         print("Mother :", self.mothername)

# # Driver code
# s1 = Son()
# s1.fathername = "RAM"
# s1.mothername = "SITA"
# s1.mother()
# s1.parents()

#multilevel inheritance
# Base class
# class Grandfather:
#     def __init__(self, grandfathername):
#         self.grandfathername = grandfathername

# # Intermediate class
# class Father(Grandfather):
#     def __init__(self, fathername, grandfathername):
#         self.fathername = fathername
#         # Call the constructor of Grandfather
#         Grandfather.__init__(self, grandfathername)

# # Derived class
# class Son(Father):
#     def __init__(self, sonname, fathername, grandfathername):
#         self.sonname = sonname
#         # Call the constructor of Father
#         Father.__init__(self, fathername, grandfathername)

#     def print_name(self):
#         print('Grandfather name :', self.grandfathername)
#         print('Father name :', self.fathername)
#         print('Son name :', self.sonname)

# # Driver code
# s1 = Son('Prince', 'Rampal', 'Lal mani')
# print(s1.grandfathername)
# s1.print_name()


#Hierarchical Inheritance

# Base class
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")

# # Derived class 1
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1.")

# # Derived class 2
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2.")

# # Driver code
# object1 = Child1()
# object2 = Child2()

# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()


#hybrid inheritance


# Base class
# class School:
#     def func1(self):
#         print("This function is in school.")

# # Derived class 1 (Single Inheritance)
# class Student1(School):
#     def func2(self):
#         print("This function is in student 1.")

# # Derived class 2 (Another Single Inheritance)
# class Student2(School):
#     def func3(self):
#         print("This function is in student 2.")

# # Derived class 3 (Multiple Inheritance)
# class Student3(Student1, School):
#     def func4(self):
#         print("This function is in student 3.")

# # Driver code
# obj = Student3()
# obj.func1()
# obj.func2()


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def display_name(self):
#         print("Name:", self.name)

# class Student(Person):
#     def study(self):
#         print("Student is studying")

# class Teacher(Person):
#     def teach(self):
#         print("Teacher is teaching")

# s = Student("Rahul")
# s.display_name()
# s.study()

# t = Teacher("Anita")
# t.display_name()
# t.teach()

# class Employee:
#     def emp_info(self):
#         print("Employee Details")

# class Developer(Employee):
#     def code(self):
#         print("Writing Code")

# class Tester(Employee):
#     def test(self):
#         print("Testing Software")

# class TeamLead(Developer, Tester):
#     def manage(self):
#         print("Managing Team")

# t = TeamLead()

# t.emp_info()
# t.code()
# t.test()
# t.manage()