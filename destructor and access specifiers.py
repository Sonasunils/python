# class Student:

#     def __init__(self):
#         print("Constructor Called")

#     def __del__(self):
#         print("Destructor Called")

# s1 = Student()
# del s1
# s2 = Student()





# Library Management System

# class Library:

#     def __init__(self, book_name, quantity):
#         self.book_name = book_name
#         self.quantity = quantity
#         print("Library Session Started")

#     def issue_book(self):

#         if self.quantity > 0:
#             self.quantity -= 1
#             print("Book Issued Successfully")

#         else:
#             print("Book Not Available")

#     def return_book(self):

#         self.quantity += 1
#         print("Book Returned Successfully")

#     def display_books(self):

#         print("\nBook Name:", self.book_name)
#         print("Available Quantity:", self.quantity)

#     def __del__(self):

#         print("Library Session Ended")


# # Main Program

# book = input("Enter Book Name: ")

# qty = int(input("Enter Quantity: "))

# l1 = Library(book, qty)


# while True:

#     print("\n===== LIBRARY MENU =====")
#     print("1. Issue Book")
#     print("2. Return Book")
#     print("3. Display Available Books")
#     print("4. Exit")

#     choice = int(input("Enter Choice: "))

#     if choice == 1:

#         l1.issue_book()

#     elif choice == 2:

#         l1.return_book()

#     elif choice == 3:

#         l1.display_books()

#     elif choice == 4:

#         print("Exiting...")
#         del l1
#         break

#     else:

#         print("Invalid Choice")



#access specifiers

class Demo:

    def __init__(self):

        self.name = "Public"

        self._age = 24

        self.__salary = 25000

    def display(self):

        print(self.name)

        print(self._age)

        print(self.__salary)

d1 = Demo()

print(d1.name)

print(d1._age)

# print(d1.__salary)

d1.display()

