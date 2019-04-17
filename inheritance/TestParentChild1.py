from inheritance.Child import Child
from inheritance.Parent import Parent


def checkParentDetails():
    parent = Parent("DD", "Mishra")
    parent.addDesignation("Engineer")
    parent.showParentDetails()

def checkChildDetails():
    child = Child("John","Abraham", 23)
    child.addDesignation("Actor")
    child.showParentDetails()
    print("----------------Child details-------------")
    child.showChildDetails()

checkParentDetails()
checkChildDetails()