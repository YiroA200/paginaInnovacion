import qrcode

url = "https://tu-dominio.com"

qr = qrcode.make(url)
qr.save("qr_la_finestra.png")

print("qr generado")