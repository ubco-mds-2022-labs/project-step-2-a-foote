import datetime

def next7dates():
    """
    The function returns the next 7 dates (DD) from the current date.
    
    Input:
    The function does not require any inputs and can be called directly.
    
    Output:
    If today is December, 12: the output will be a list: ['13','14','15','16','17','18','19']
    """
    datelist=[]
    for i in range(0,7):
        datelist.append(str((datetime.datetime.now()+datetime.timedelta(i)).day))
    return datelist

def DeliverableViewer(deliverable_list):
    print("Deliverables due in the next 7 days are:\n")
    for deliverable in deliverable_list:
        print(deliverable)
    print("\n")

def DeliverableSearch(course_list):
    lst = []
    for course in course_list:
        for deliverable in course.deliverables:
            if (deliverable.date.split("/")[1] in next7dates()):
                lst.append(deliverable)
    return lst
                
def DeliverableAll(course_list):
    for course in course_list:
        for deliverable in course.deliverables:
            print(f"{deliverable.dname},{deliverable.date}")
       

     
   