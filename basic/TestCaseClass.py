import unittest


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Test class is started, AQA with Python. Python is cool!")

    @classmethod
    def tearDownClass(cls):
        print('Test run is finished for class: {}'.format(cls.__name__))

    def setUp(self):
        print('Check {} has started.'.format(self._testMethodName))

    @unittest.skip("Skip this test!")
    def test_something(self):
        self.assertIn(1, [2, 1, 4])

    def test_1(self):
        a = b = 1
        self.assertIs(a, b, "Compare references failed")

    def test_2(self):
        a = [1, 5, 7]
        b = [1, 5, 7]
        self.assertEqual(a, b, "Compare content of two lists - failed")


if __name__ == '__main__':
    unittest.main()
