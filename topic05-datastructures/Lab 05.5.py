students= []
while True:
    student=input("Enter name student(or press Enter to stop): ")
    if student=="":
         break
    if student.isalpha():
        students_info={"name":student,"modules":[]} 
        
    else:
        print("Error.Enter only letter: ")

    while True:
        module=input("Enter module name(or press Enter to stop): ")
        grade=input(f"Enter grade for {module} (0-100): ")
        if module=="":
            break
        if grade=="":
            students_info["modules"].append({"courseName":module})
        else:
            grade=int(grade)
            if grade >=0 and grade <=100:
                students_info["modules"].append({"courseName":module,"grade":grade})
            else :
                print("Error.Enter grade between 0-100")
    students.append(students_info)

for student in students:
    print("\t{}".format(student["name"]))
    for module in student["modules"]:
        print("\t \t{} \t: {} %".format(module["courseName"],module["grade"]))



