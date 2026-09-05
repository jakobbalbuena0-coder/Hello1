classGrades = { }

numberofClassestaken =int( input("How many classes did you take last semester? "))


for i in range(numberofClassestaken):
    classTaken = input("Enter a class name: ")
    grade = input("What grade did you get in " + classTaken + "? ")
    classGrades[classTaken] = grade

print("Here are your grades from the previous semester:")


for key in classGrades:
    print("In" , key, "you got a", classGrades[key])