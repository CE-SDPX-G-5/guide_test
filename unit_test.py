import unittest
import app

class ApptestCase(unittest.TestCase):
    def testint5(self):
        resp = app.next2(5)
        data = resp.get_json()
        self.assertEqual(data['msg'],7)

    def testintnext5(self):
        resp = app.next2(-5)
        data = resp.get_json()
        self.assertEqual(data['msg'],-3)

    def testfloat35(self):
        resp = app.next2('3.5')
        data = resp.get_json()
        self.assertEqual(data['msg'],5.5)

    def teststr(self):
        resp = app.next2('a')
        data = resp.get_json()
        self.assertEqual(data['msg'],'error')

if __name__ == "__main__":
    unittest.main()