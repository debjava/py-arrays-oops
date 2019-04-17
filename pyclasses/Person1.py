class Person1:

    ''' Constructor'''
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName


if __name__ == "__main__":
    person = Person1("DD", "Mishra")
    print(person.firstName + "<----->" + person.lastName)
