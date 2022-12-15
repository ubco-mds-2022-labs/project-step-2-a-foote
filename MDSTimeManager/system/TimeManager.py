import MDSTimeManager.system.deliverableviewer as dv
import MDSTimeManager.setup.course as c
import MDSTimeManager.system.TimeManager as tm 
import MDSTimeManager.system.deliverableviewer as dv
import datetime 

def userinput(Courses):
    
    t=0
    next7deliverables = dv.DeliverableSearch(Courses)
    
    print("\nPlease choose a rank for the following courses out of (1,2,3) with 3 being most difficult.")
    for course in Courses:
        print(f"For {course}: ")
        rank = input()
        while rank not in ["1","2","3"]:
            print("Having a hard time following basic instructions? \nChoose from ranks 1, 2 or 3 only")
            rank = input()
        course.rank = rank
    weektime = input("How much time is available in the next 7 days for studies (in hours)? ")
    while (not weektime.isnumeric()):
        print("\nInput should be a number.")
        weektime = input("\nHow much time is available in the next 7 days for studies (in hours)? ")
    weektime = float(weektime)
    w = weektime
    if len(next7deliverables) > 0 and (any(isinstance(asslab, c.AssignLab) for asslab in next7deliverables) or any(isinstance(proj, c.Project) for proj in next7deliverables)):
        print("\nHow much time (in hours) you think you will take for the following:\n")
    for deliverable in next7deliverables:
        if isinstance(deliverable,c.AssignLab) or isinstance(deliverable,c.Project) :
            print(f"For {deliverable}")
            time = input()
            while (not time.isnumeric()):
                print("\nInput should be a number.")
                time = input()
            time = float(time)
            t = t + time
            weektime = weektime - time
            deliverable.dur = time
        else:
            continue
    if t > w:
        return 0
    else:
        print(f"\n\nTime left after assignments and labs: {weektime:.2f} hours\n")
        return weektime

def fetchranks(course_list):
    totalranks = 0.0
    for course in course_list:
        totalranks = totalranks + float(course.rank)
    return totalranks 
    
def timemanagercal(timeavailable, course_list):
    if timeavailable <= 0:
        print("\nTime alloted for studying is less than the time you will work on deliverables.\n")
        print("Study time cannot be recommended.\n")
    else:
        studytime = 0.0
        tr = fetchranks(course_list)
        for course in course_list:
            cr = float(course.rank)
            studytime = (cr/tr)*timeavailable
            print(f"Recommended study time for {course} is {studytime:.2f} hours ({studytime*60:1.0f} mins)")