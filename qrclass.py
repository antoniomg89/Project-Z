import random
import qrcode

class servQR:
    def __init__(self):
        self.info_qr = 'Constructor'
        self.size_qr = 10
        self.border_qr = 4
        self.qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 10, border = 4,)
        self.qr.add_data('Constructor')
        self.qr.make(fit=True)
        self.imagen_qr = self.qr.make_image()

    def generarQR(self,inf,size,br):
        self.size_qr = size
        self.border_qr = br
        self.qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = size, border = br,)
        self.info = inf
        self.qr.add_data(info)
        self.qr.make(fit=True)
        self.imagen_qr = self.qr.make_image()

    def getInfo(self):
        return self.info_qr

    def getSize(self):
        return self.size_qr

    def getBorder(self):
        return self.border_qr

    def getImageQR(self):
        return self.imagen_qr
