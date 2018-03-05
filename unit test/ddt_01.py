# coding = utf-8
import ddt
import unittest

test_data = [{"username":"selenium群","pwd":"1234567"},
             {"username":"python群","pwd":"89376455"},
             {"username":"appium群","pwd":"12254497"}]

@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        print("end")

    @ddt.data(*test_data)
    def test_ddt(self,data):
        print(data)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test(test_ddt))

    runner = unittest.TextTestRunner()
    runner.run(suite)