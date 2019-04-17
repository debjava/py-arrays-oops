class Parent:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def addDesignation(self, desgn):
        self.designation = desgn

    def showParentDetails(self):
        print("parent in toString : ", self.__dict__)
