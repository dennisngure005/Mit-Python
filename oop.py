class person:
    def __init__(self,firstname,age,gender):
        self.firstname=firstname
        self.age=age
        self.gender=gender
    def details(self):
        print(self.firstname,"is studying")

teacher =person("Dennis",18,"male")
accountant =person("Virginia",18,"Female")
doctor =person("James",45,"Male")
print(teacher.firstname,teacher.age,teacher.gender)
print(accountant.firstname,accountant.age,accountant.gender)
print(doctor.firstname,doctor.age,doctor.gender)