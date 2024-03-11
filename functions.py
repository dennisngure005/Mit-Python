# Inbuilt functions
number = max(89, 70, 59, 13)
print(number)
x = min(78, 45, 34, 1)
print(x)
z = pow(2, 3)
print(z)


# User defined functions
def name():
    print("node")


name()  # Calling a function


def student():
    name = "Dennis"
    age = 18
    course = "MIT"
    print(name, age, course)


student()


# parameters/variables and arguments/values
def students(name, age, course):
    print(name, age, course)


students("Vincent", 18, "MIT")
students("James", 18, "Cybersecurity")
students("Virginia", 19, "MIT")
students("Grace", 17, "MIT")
students("Dennis", 18, "MIT")
students("Collins", 17, "cybersecurity")


# create a user defined function
# called employees. It should display
# details of five employees.parameters are
# fullname, age, gender, position, salary

def employees(fullname, age, gender, position, salary):
    print(fullname, age, gender, position, salary)


employees("James Makori", 19, "Male", "Manager", "Ksh80,000")
employees("Grace Wamahiu", 17, "female", "CEO", "Ksh70,000")
employees("Virginia Wangoi", 18, "Female", "Accountant", "Ksh65,000")
employees("Dennis Nganga", 18, "Male", "P.A", "Ksh55,000")
employees("Chris Njuguna", 20, "Male", "Clerk", "Ksh35,000")
