#!/usr/bin/env python3

# Ejemplo de codigo pyhton
import qrcode



codigo = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 10, border = 3,
)

info = "Información dentro del código QR"

qr.add_data(info)
qr.make(fit=True)

imagen_qr = qr.make_image()
imgagen_qr.save("image.png")
