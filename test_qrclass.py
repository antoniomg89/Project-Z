import unittest
import qrcode

from qrclass import servQR

class TestservQR(unittest.TestCase):
    def setUp(self):
        self.qr = servQR()
        #self.qr_test_img = qrcode.make('Constructor')

    def test_object_OK(self):
        self.assertIsInstance(self.qr,servQR, "Object OK")

    #def test_getImageQR_correctly(self):
        #self.assertEqual(self.qr.getImageQR(),self.qr_test_img, "Image OK")

    def test_getInfo_correctly(self):
        self.assertIsInstance(self.qr.getInfo(),str, "Info OK")

    def test_getBorder_correctly(self):
        self.assertIsInstance(self.qr.getBorder(),int, "Border OK")

    def test_getSize_correctly(self):
        self.assertIsInstance(self.qr.getSize(),int, "Size OK")

if __name__ == '__main__':
    unittest.main()
