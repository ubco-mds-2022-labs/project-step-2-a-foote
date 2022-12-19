import unittest as ut
from test_person import TestSetupPerson
from test_course import TestSetupCourse
from test_deliverableviewer import Testnext7dates, TestDeliverableAll
from test_timemanager import Testfetchranks, Testtimemanagercal

def mdstm_suite():
    suite = ut.TestSuite()
    result = ut.TestResult()
    suite.addTest(ut.makeSuite(TestSetupPerson))
    suite.addTest(ut.makeSuite(TestSetupCourse))
    suite.addTest(ut.makeSuite(Testnext7dates))
    suite.addTest(ut.makeSuite(TestDeliverableAll))
    suite.addTest(ut.makeSuite(Testfetchranks))
    suite.addTest(ut.makeSuite(Testtimemanagercal))
    runner = ut.TextTestRunner()
    print(runner.run(suite))