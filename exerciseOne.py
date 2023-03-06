class Student:

    def __init__(self, name, score):
        self. name = name
        self.score = score

    def imprinit(self):
        print("Name: " ,self.name)
        print("Score: " , self.score)

    def approved(self):
        if self.score >=11:
            print("The student is approved")
        else:
            print("Student is not approved")



StudentOne = Student("Percy",20)
StudentTwo = Student("Luis", 10)
StudentThree = Student("Carlos", 11)

StudentOne.imprinit()
StudentTwo.imprinit()
StudentThree.imprinit()

StudentOne.approved()
StudentTwo.approved()
StudentThree.approved()

