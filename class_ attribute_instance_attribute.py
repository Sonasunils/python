# ==========================
# 1. Mobile Phone Information
# ==========================

# class Mobile:
#     def set_data(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Price:", self.price)

# print("\n--- Mobile Information ---")

# m1 = Mobile()
# m1.set_data("Samsung", "A54", 35000)
# m1.display()


# ==========================
# 2. Library Book Management
# ==========================

# class Book:
#     def set_data(self, name, author, pages):
#         self.name = name
#         self.author = author
#         self.pages = pages

#     def display(self):
#         print("Book:", self.name)
#         print("Author:", self.author)
#         print("Pages:", self.pages)

# print("\n--- Library Book Management ---")

# b1 = Book()
# b1.set_data("Python Basics", "John", 250)
# b1.display()


# # ==========================
# # 3. Online Food Order
# # ==========================

# class FoodOrder:
#     def set_data(self, customer, item, quantity):
#         self.customer = customer
#         self.item = item
#         self.quantity = quantity

#     def bill(self):
#         total = self.quantity * 120

#         print("Customer:", self.customer)
#         print("Food Item:", self.item)
#         print("Quantity:", self.quantity)
#         print("Total Bill:", total)

# print("\n--- Online Food Order ---")

# o1 = FoodOrder()
# o1.set_data("Arun", "Burger", 3)
# o1.bill()


# # ===================================
# # 4. Netflix Subscription
# # (Class & Instance Attribute)
# # ===================================

# class NetflixUser:
#     subscription_plan = "Premium"

#     def set_data(self, name, profiles):
#         self.name = name
#         self.profiles = profiles

#     def display(self):
#         print("Name:", self.name)
#         print("Profiles:", self.profiles)
#         print("Plan:", NetflixUser.subscription_plan)

# print("\n--- Netflix Subscription ---")

# u1 = NetflixUser()
# u1.set_data("Anu", 4)
# u1.display()


# # ===================================
# # 5. School Bus System
# # (Class & Instance Attribute)
# # ===================================

# class SchoolBus:
#     school_name = "ABC Public School"

#     def set_data(self, name, stop, route):
#         self.name = name
#         self.stop = stop
#         self.route = route

#     def display(self):
#         print("School:", SchoolBus.school_name)
#         print("Student:", self.name)
#         print("Bus Stop:", self.stop)
#         print("Route:", self.route)

# print("\n--- School Bus System ---")

# s1 = SchoolBus()
# s1.set_data("Rahul", "Town", 1)
# s1.display()


# # ===================================
# # 6. Hospital Patient Records
# # (Class & Instance Attribute)
# # ===================================

# class Patient:
#     hospital_name = "City Hospital"

#     def set_data(self, name, age, disease):
#         self.name = name
#         self.age = age
#         self.disease = disease

#     def display(self):
#         print("Hospital:", Patient.hospital_name)
#         print("Patient:", self.name)
#         print("Age:", self.age)
#         print("Disease:", self.disease)

# print("\n--- Hospital Patient Records ---")

# p1 = Patient()
# p1.set_data("Meera", 40, "Diabetes")
# p1.display()


# class Student:

#     # def __init__(self, name, age):
#     #     self.name = name
#     #     self.age = age
#     def set_data(self,name,age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# s1 = Student()
# s1.set_data("anu",67)
# # s2=Student()

# s1.display()
# # s2.display()

# class Room:

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         print("Area =", self.length * self.width)

# r1 = Room(10, 5)

# r1.area()



# class Bank:

#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance = self.balance + amount

#     def show_balance(self):
#         print("Balance =", self.balance)

# b1 = Bank(5000)

# b1.deposit(2000)

# b1.show_balance()


# class Employee:

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display(self):
#         print("Employee:", self.name)
#         print("Salary:", self.salary)

# e1 = Employee("Anu", 35000)

# e1.display()