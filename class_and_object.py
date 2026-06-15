# 1. Student Management

# Why OOP? A student has data (name, roll no) and actions (display details).

# class Student:
#     name = "Arun"
#     roll_no = 101

#     def display(self):
#         print("Name:", self.name)
#         print("Roll No:", self.roll_no)

# s1 = Student()
# s1.display()


# Concept: Student is a class. s1 is an object representing one student.

# # 2. Bank Account

# # Why OOP? Each bank account has its own balance and operations.

# class BankAccount:
#     balance = 5000

#     def deposit(self):
#         self.balance += 1000
#         print("Balance after deposit:", self.balance)

# account = BankAccount()
# account.deposit()

# # Concept: An object represents a real bank account.

# # 3. Fan

# # Why OOP? A fan can be ON or OFF.

# class Fan:
#     status = "OFF"

#     def turn_on(self):
#         self.status = "ON"
#         print("Fan is", self.status)

# f1 = Fan()
# f1.turn_on()

# # Concept: Objects can store state and perform actions.

# # 4. Mobile Phone

# # Why OOP? A mobile phone can make calls.

# class Mobile:
#     brand = "Samsung"

#     def call(self):
#         print("Calling from", self.brand)

# m1 = Mobile()
# m1.call()

# # 5. Car

# # Why OOP? A car can start and stop.

# class Car:
#     brand = "Toyota"

#     def start(self):
#         print(self.brand, "Car Started")

# c1 = Car()
# c1.start()


# # 6. Employee

# # Why OOP? Employees have details and can work.

# class Employee:
#     name = "Anu"
#     department = "HR"

#     def work(self):
#         print(self.name, "is working in", self.department)

# e1 = Employee()
# e1.work()

# # 7. Library Book

# # Why OOP? Books can be issued.

# class Book:
#     title = "Python Basics"

#     def issue(self):
#         print(self.title, "issued successfully")

# b1 = Book()
# b1.issue()

# # Better Example: Why Multiple Objects
# class Student:
#     def display(self, name, mark):
#         print("Name:", name)
#         print("Mark:", mark)

# s1 = Student()
# s2 = Student()

# s1.display("Arun", 85)
# s2.display("Anu", 92)
# # Explanation

# # Without OOP:

# # student1_name = "Arun"
# # student1_mark = 85

# # student2_name = "Anu"
# # student2_mark = 92

# # With OOP:

# # class Student:
# #     ...

# # You create as many student objects as needed. This makes the code organized and reusable.


# # workout qn 1 :Create a class Student with attributes name and mark. Create two objects and display their details.


# # What is a Class?
# # What is an Object?
# # Why Objects are created from a Class?
# # How one Class can represent many real-world entities.



# # 1. Student Details (Class Attribute)
# # Concept:

# # All students belong to the same institution, so the institution name can be a class attribute.

# class Student:
#     college = "LBS Skill Centre"   # Class Attribute

#     def display(self):
#         print("College:", Student.college)

# s1 = Student()
# s1.display()


# # Creating a class
# # Creating an object
# # Accessing a class attribute

# # 2. Student Details (Instance Attributes)
# # Concept:
# # Each student has different details.

# class Student:
#     def set_data(self, name, age):
#         self.name = name      # Instance Attribute
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# s1 = Student()
# s1.set_data("Arun", 20)

# s2 = Student()
# s2.set_data("Anu", 21)

# s1.display()
# s2.display()

# # self.name and self.age belong to individual objects.
# # Different objects store different values.
# # 3. Employee Salary Calculator
# # Concept:

# # Class attribute + Instance attribute together.

# class Employee:
#     company = "ABC Technologies"    # Class Attribute

#     def set_data(self, name, basic):
#         self.name = name
#         self.basic = basic

#     def salary(self):
#         hra = self.basic * 0.10
#         total = self.basic + hra

#         print("Company:", Employee.company)
#         print("Employee:", self.name)
#         print("Salary:", total)

# e1 = Employee()
# e1.set_data("Rahul", 25000)

# e2 = Employee()
# e2.set_data("Anu", 30000)

# e1.salary()
# e2.salary()

# # 4. Bank Account
# # Concept:

# # Objects represent real bank accounts.

# class BankAccount:
#     bank_name = "State Bank"   # Class Attribute

#     def create_account(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Updated Balance:", self.balance)

# acc1 = BankAccount()

# acc1.create_account("Arun", 5000)
# acc1.deposit(1000)


# # Count how many objects are created.

# class Student:
#     count = 0      # Class Attribute

#     def add_student(self, name):
#         self.name = name
#         Student.count += 1

#     def display(self):
#         print("Student:", self.name)
#         print(self.count)

# s1 = Student()
# s1.add_student("Arun")
# s1.display()

# s2 = Student()
# s2.add_student("Anu")
# s2.display()

# s3 = Student()
# s3.add_student("Rahul")
# s3.display()

# print("Total Students:", Student.count)



# class Room:
#     height = 10      # Class Attribute (same for all rooms)

#     def set_data(self, length, width):
#         self.length = length
#         self.width = width

#     def display(self):
#         perimeter = 2 * (self.length + self.width)

#         print("Length:", self.length)
#         print("Width:", self.width)
#         print("Height:", Room.height)
#         print("Perimeter:", perimeter)
#         print()

# bedroom = Room()
# bedroom.set_data(12, 8)

# kitchen = Room()
# kitchen.set_data(15, 10)

# bedroom.display()
# kitchen.display()


class BankAccount:
    # Setup account details without __init__
    def create_account(self, owner, account_number, initial_balance=0.0):
        self.owner = owner
        self.account_number = account_number
        self.balance = initial_balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ₹{amount}. New Balance: ₹{self.balance}")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive.")

    # Display current balance
    def display_balance(self):
        print(f"Account Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₹{self.balance}")
# --- Execution Example ---

# 1. Create a blank object
account = BankAccount()

# 2. Explicitly initialize the object attributes
account.create_account(owner="Rahul Sharma", account_number="987654321", initial_balance=5000.0)

# 3. Perform banking operations
account.display_balance()
account.deposit(1500.0)
account.withdraw(2000.0)
account1 = BankAccount()

# 2. Explicitly initialize the object attributes
account1.create_account(owner="sona", account_number="987654322", initial_balance=8000.0)

# 3. Perform banking operations
account1.display_balance()
account1.deposit(1500.0)
account1.withdraw(2000.0)
account.withdraw(3000.0)