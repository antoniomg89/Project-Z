# Ejemplo de codigo pyhton
import qrcode

def genQR(qr):
    codigo_qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 10, border = 3,
    )

    info = qr

    codigo_qr.add_data(info)
    codigo_qr.make(fit=True)

    imagen_qr = codigo_qr.make_image()
    #imagen_qr.save("imagen_qr.png")
    return info

def valQR(infoval):
    return infoval
