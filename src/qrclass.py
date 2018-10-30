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
        self.imagen_qr = self.qr.make_image(fill_color="blue", back_color="white")

    def generarQR(self,inf,size,br):
        self.size_qr = size
        self.border_qr = br
        self.qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = size, border = br,)
        self.info_qr = inf
        self.qr.add_data(inf)
        self.qr.make(fit=True)
        self.imagen_qr = self.qr.make_image(fill_color="blue", back_color="white")

    def getInfo(self):
        return self.info_qr

    def getSize(self):
        return self.size_qr

    def getBorder(self):
        return self.border_qr

    def getImageQR(self):
        return self.imagen_qr
