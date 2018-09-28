# Ejemplo de codigo pyhton
import generaQR

def test_genQR():
    assert generaQR.genQR('información') == 'información'

def test_valQR():
    info = generaQR.valQR('validarinformacion')
    assert type(info) is str
