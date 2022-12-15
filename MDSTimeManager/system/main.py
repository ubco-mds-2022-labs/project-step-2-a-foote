def execute():
    import MDSTimeManager.setup.course as c
    import MDSTimeManager.system.deliverableviewer as dv
    import MDSTimeManager.system.TimeManager as tm
    
    # Course 1
    Data533 = c.Course("Object Oriented Programming","Khalad Hasan","3",1)
    Data533Quiz = c.Quiz("Data533: Quiz", "12/20", "Incomplete", "Lecture 1 to Lecture 8", "MCQ, Short Answers on paper")
    Data533Lab1 = c.AssignLab("Data533: Lab 1", "12/05", "Complete", "", "", subloc="git classroom repo, link in Canvas")
    Data533Project = c.Project("Data 533: Project- Time Manager","12/22",milestones="no milestones",repo="MyRepo.git")
    # How to assign deliverables to a course object
    Data533.deliverables = Data533Quiz
    Data533.deliverables = Data533Lab1
    Data533.deliverables = Data533Project

    # Course 2
    Data543 = c.Course("Data Collection","Emelie Gustaffson","3",1)
    Data543Quiz1 = c.Quiz("Data543: Quiz 1", "12/5", "Complete", "Lecture 1 to Lecture 4", "MCQ, Short Answers and R programming")
    Data543Quiz2 = c.Quiz("Data543: Quiz 2", "12/19", "Incomplete", "Lecture 5 to Lecture 8", "MCQ and R programming")
    Data543Assignment1 = c.AssignLab("Data543: Assignment 1", "12/12", "Complete", "", "", subloc="Canvas" )
    Data543Assignment2 = c.AssignLab("Data543: Assignment 2", "12/16","Incomplete" , "", "", subloc="Canvas" )
    Data543.deliverables = Data543Quiz1
    Data543.deliverables = Data543Quiz2
    Data543.deliverables = Data543Assignment1
    Data543.deliverables = Data543Assignment2

    # Course 3
    Data571 = c.Course("Resampling and Regularization","Jeff Andrews","3",3)
    Data571Quiz1 = c.Quiz("Data571: Quiz 1", "12/7", "Complete", "Lecture 1 to Lecture 3", "MCQ and Short Answers")
    Data571Quiz2 = c.Quiz("Data571: Quiz 2", "12/21", "Incomplete", "Lecture 4 to Lecture 6", "MCQ and Short Answers")
    Data571Assignment1 = c.AssignLab("Data571: Assignment 1", "12/5", "Complete", "","",subloc="Canvas" )
    Data571Assignment2 = c.AssignLab("Data571: Assignment 2", "12/19", "Incomplete","","",subloc="Canvas" )
    Data571.deliverables = Data571Quiz1
    Data571.deliverables = Data571Quiz2
    Data571.deliverables = Data571Assignment1
    Data571.deliverables = Data571Assignment2

    # Course 4
    Data581 = c.Course("Modelling and Simulation","Ladan Tazik","3",1)
    Data581Quiz1 = c.Quiz("Data 581: Quiz 1", "12/6", "Complete", "Lecture 1 to Lecture 3", "MCQ and Short Answers")
    Data581Quiz2 = c.Quiz("Data 581: Quiz 2", "12/20", "Incomplete", "Lecture 4 to Lecture 7", "MCQ and Short Answers")
    Data581Lab1 = c.AssignLab("Data 581: Lab 1", "12/1", "Complete", "","",subloc="Canvas" )
    Data581Lab2 = c.AssignLab("Data 581: Lab 2", "12/8", "Complete", "","",subloc="Canvas" )
    Data581Lab3 = c.AssignLab("Data 581: Lab 3", "12/15", "Incomplete", "","",subloc="Canvas" )
    Data581.deliverables = Data581Quiz1
    Data581.deliverables = Data581Quiz2
    Data581.deliverables = Data581Lab1
    Data581.deliverables = Data581Lab2
    Data581.deliverables = Data581Lab3

    Courses = [Data533, Data543, Data571, Data581]
        
    print("Welcome to the MDSTimeManager! \n\nPlease note:\nPresently this tool is strictly for use by MDS Okanagan students in Block 3 of 2022. \nFuture versions of this package will expand for use in all blocks for both MDS Vancouver and Okanagan students.")
    
    while True:
        
        print(("\n\nEnter one of the following options:\n"
       "1    : Use the deliverableviewer and see upcoming or all due dates\n"
       "2    : Use the timemanagercalc and get study time recommendations\n"
       "x    : Quit the session"))
        
        usrinput = input()
        
        if usrinput == "x":
            print("\nYour MDSTimeManger session is over. Have a good day :)")
            break 
        
        if usrinput == "1":
            print("\n")
            print(("\n\nEnter one of the following options:\n"
       "a    : View deliverables due in the next 7 days\n"
       "b    : View all deliverables"))
            usrinput = input()
            if usrinput == "a":
                print("\n")
                next7deliverables = dv.DeliverableSearch(Courses)
                dv.DeliverableViewer(next7deliverables)
            elif usrinput == "b":
                print("\n")
                dv.DeliverableAll(Courses)
            else:
                print("Invalid input, please try again.")
        elif usrinput == "2":
            print("\n")
            availabletime = tm.userinput(Courses)
            tm.timemanagercal(availabletime, Courses)
        
        else:
            print("\n")
            print("Invalid input, please try again.")