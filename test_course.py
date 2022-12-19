import unittest
import MDSTimeManager.setup.course as c
import datetime 

########################################################################################################################

# Creating objects

# Course 1
Data533 = c.Course("Object Oriented Programming","Khalad Hasan","3",1)
Data533Project = c.Project("Data 533: Project- Time Manager","12/22", milestones="no milestones",repo="MyRepo.git")

# Course 2
Data543 = c.Course("Data Collection","Emelie Gustaffson","3",1)
Data543Quiz1 = c.Quiz("Data543: Quiz 1", "12/5", "Complete", "Lecture 1 to Lecture 4", "MCQ, Short Answers and R programming")
Data543Quiz2 = c.Quiz("Data543: Quiz 2", "12/19", "Incomplete", "Lecture 5 to Lecture 8", "MCQ and R programming")
Data543Assignment1 = c.AssignLab("Data543: Assignment 1", "12/12", "Complete", "", "", subloc="Canvas" )
Data543Assignment2 = c.AssignLab("Data543: Assignment 2", "12/16","Incomplete" , "", "", subloc="Canvas" )

# Course 3
Data571 = c.Course("Resampling and Regularization","Jeff Andrews","3",3)
Data571Quiz1 = c.Quiz("Data571: Quiz 1", "12/7", "Complete", "Lecture 1 to Lecture 3", "MCQ and Short Answers")
Data571Quiz2 = c.Quiz("Data571: Quiz 2", "12/21", "Incomplete", "Lecture 4 to Lecture 6", "MCQ and Short Answers")
Data571Assignment1 = c.AssignLab("Data571: Assignment 1", "12/5", "Complete", "","",subloc="Canvas" )
Data571Assignment2 = c.AssignLab("Data571: Assignment 2", "12/19", "Incomplete","","",subloc="Canvas" )


# Course 4
Data581 = c.Course("Modelling and Simulation","Ladan Tazik","3",1)
Data581Quiz1 = c.Quiz("Data 581: Quiz 1", "12/6", "Complete", "Lecture 1 to Lecture 3", "MCQ and Short Answers")
Data581Quiz2 = c.Quiz("Data 581: Quiz 2", "12/20", "Incomplete", "Lecture 4 to Lecture 7", "MCQ and Short Answers")
Data581Lab1 = c.AssignLab("Data 581: Lab 1", "12/1", "Complete", "","",subloc="Canvas" )
Data581Lab2 = c.AssignLab("Data 581: Lab 2", "12/8", "Complete", "","",subloc="Canvas" )
Data581Lab3 = c.AssignLab("Data 581: Lab 3", "12/15", "Incomplete", "","",subloc="Canvas" )

Courses = [Data533, Data543, Data571, Data581]

########################################################################################################################

class TestSetupCourse(unittest.TestCase):
    
    c = 1
    
    @classmethod
    def setUp(TestSetupCourse):
        print("\nStart Test", TestSetupCourse.c)
    
    @classmethod
    def tearDown(TestSetupCourse):
        print("\nEnd Test", TestSetupCourse.c)
        TestSetupCourse.c = TestSetupCourse.c + 1
    
    def test_deliverables(self):
        self.assertEqual(Data543Quiz1.dname, "Data543: Quiz 1")
        self.assertIsNot(Data581Quiz2.dname, "Data 581: Quiz 1")
        self.assertIn("Time Manager",Data533Project.dname)
        self.assertTrue(Data571Quiz1.date=="12/7")
        
    def test_course(self):
        self.assertIn("Jeff", Data571.instructor)
        self.assertNotIn("Data Colection", Data543.cname)
        self.assertTrue(Data571.block=="3")
        self.assertEqual(Data533.cname, "Object Oriented Programming")

unittest.main(argv=[''], verbosity=0, exit=False)