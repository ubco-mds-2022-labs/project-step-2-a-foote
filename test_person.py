import MDSTimeManager.setup.person as p
import unittest

# creating objects

# student1
stud1 = p.Student("Vimaljeet Singh", 25087913)
# student2
stud2 = p.Student("Alyssa Foote", 13712508)
# instructor1
instr1 = p.Instructor("Khalad Hasan","Wednesday: 12:30pm - 1:30pm", "Slack, Email, Appointment")
instr1.teaches = "Data 540: Scripting and Reporting, Data 533: Object Oriented Programming"
# instructor2
instr2 = p.Instructor("Emelie Gustaffson","Tuesday: 12:30pm - 01:00pm", "Slack")
instr2.teaches = "Data 543: Data Collection"
# instructor3
instr3 = p.Instructor("Jeff Andrews","Thursday: 3:30pm - 4:30pm", "Slack, Drop-in")
instr3.teaches = "Data 570: Resampling and Regularization"
# instructor4
instr4 = p.Instructor("Ladan Tazik","Wednesday: 01:30pm - 2:00pm", "Slack, Email")
instr4.teaches = "Data 581: Modelling and Simulation 2"

################################################################################################

class TestSetupPerson(unittest.TestCase):
    
    c = 1
    
    @classmethod
    def setUp(TestSetupPerson):
        print("\nStart Test", TestSetupPerson.c)
    
    @classmethod
    def tearDown(TestSetupPerson):
        print("\nEnd Test", TestSetupPerson.c)
        TestSetupPerson.c = TestSetupPerson.c + 1
    
    def test_students(self):
        self.assertEqual(stud1.name, "Vimaljeet Singh")
        self.assertIsNot(stud2.sID, 25087913)
        self.assertIn("Foote",stud2.name)
        self.assertTrue(stud2.sID==13712508)
        
    def test_instructors(self):
        self.assertIn("Emelie", instr2.name)
        self.assertNotIn("Appointment", instr4.comm)
        self.assertTrue(instr1.name=="Khalad Hasan")
        self.assertNotEqual(instr3.teaches, "Data 570: Resampling and Regularization")

unittest.main(argv=[''], verbosity=0, exit=False)