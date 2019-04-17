from inheritance.Parent import Parent

class Child(Parent):

    def __init__(self, firstName, lastName , age):
        Parent.__init__(self,firstName,lastName)
        self.age = age

    def showChildDetails(self):
        print("Child toString : ", self.__dict__)

