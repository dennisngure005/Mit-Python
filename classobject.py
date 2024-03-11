# class is a  blue print of an object
# An object is an instance of a class

class person:
    # properties/Attributes/Characteristics
    age = 23
    name = "Bill"

    # Method/Function/Behaviour
    def talk(self):
        print("Person is talking")


teacher = person()
print(teacher.name)
print(teacher.age)

teacher.talk()
