from pyclasses.Person1 import Person1


class TestPerson1:

    @staticmethod
    def showValueFromPerson1():
        person = Person1("Deb", "Mishra")
        print("First Name : ", person.firstName)
        print("Last Name : ", person.lastName)


if __name__ == "__main__":
    TestPerson1.showValueFromPerson1()
