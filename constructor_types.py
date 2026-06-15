#default constructor

# class Employee:
#     def __init__(self):
#         print("Employee object created")

#     def display(self):
#         print("Welcome Employee")

# e1 = Employee()
# e1.display()


#parameterized constructor


# class Student:
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no

#     def display(self):
#         print("Name:", self.name)
#         print("Roll No:", self.roll_no)

# s1 = Student("Arun", 101)
# s1.display()



#copy constructor


class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

m1 = Mobile("Samsung", 30000)

# Copy constructor
m2 = Mobile(m1.brand, m1.price)


print("Original Object")
m1.display()

print("\nCopied Object")
m2.display()