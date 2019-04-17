class Employee:
    '''
        The self parameter is a reference to the current instance of the class,
        and is used to access variables that belongs to the class.
        It does not have to be named self , you can call it whatever you like,
        but it has to be the first parameter of any function in the class
    '''

    def __init__(currentObj, name):
        currentObj.name = name


if __name__ == "__main__":
    emp = Employee("John")
    print("Emp Name : ", emp.name)
