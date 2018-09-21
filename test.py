#!/usr/bin/env python3

# Ejemplo de codigo pyhton
import qrcode



codigo_qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 10, border = 3,
)

info = "Información dentro del código QR"

codigo_qr.add_data(info)
codigo_qr.make(fit=True)

imagen_qr = codigo_qr.make_image()
imagen_qr.save("imagen_qr.png")
