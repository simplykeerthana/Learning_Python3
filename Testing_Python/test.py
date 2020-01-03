#testing in Python
# the importance of testing in programming is high
#write test unit cases

#main.py and test.py
#to check that everything in main.py works properly
 
 #unit test
 
import unittest
import main
 
class TestMain(unittest.TestCase):
     def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15) #we asserted the answer to be 15
        
     def test_do_stuff2(self):
        test_param = 'fadfafafadf'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError)) #we asserted the answer to be 15
     def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')
     def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')


if __name__ == '__main__':
    unittest.main()