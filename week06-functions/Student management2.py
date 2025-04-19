# a different way or dealing with the users choice

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit):").strip()

    while moduleName != "":
        module = {}
        module["name"]= moduleName
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit):").strip()

    return modules   
def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= readModules()

    students.append(currentStudent)

def displayModules(modules):
    for module in modules:
        print(f"\t\t{module['name']}\t: {module['grade']}")

def doView(students):
    for student in students:
        print(f"Student: {student['name']}")
        displayModules(student["modules"])

def doNothing(dumby):
    pass

#the dict that maps a letter to function
choiceMap = {
    'a': doAdd,
    'v': doView,
    'q': doNothing # q is a valid choice
}

#main program
students = []
choice = displayMenu()
while(choice != 'q'):
    if choice in choiceMap:
        # run the function
        choiceMap[choice](students)
    else: # user did not enter something valid
        print("\n\nplease select either a,v or q")

    choice=displayMenu()
