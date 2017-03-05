import unittest
from bruch.Bruch import *

class AdditionalTests(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(9, 5)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(7, 10)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def addtest1(self):
        self.assertRaises(ZeroDivisionError, self.b2.__truediv__, Bruch(1, 0))

    def addtest2(self):
        self.b3 = self.b+1
        assert(self.b3 == Bruch(19, 5))

    def addtest3(self):
        self.b3 = self.b3 - self.b2
        assert(self.b3 == Bruch(-11, 10))

    def addtest4(self):
        self.b2 = Bruch(6, 10) * 5
        assert(self.b2 == 3)

    def addtest5(self):
        self.b2 = self.b / self.b3
        assert(self.b2 == Bruch(18, 7))