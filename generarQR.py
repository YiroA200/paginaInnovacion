import qrcode

url = "https://YiroA200.github.io/paginaInnovacion"

qr = qrcode.make(url)
qr.save("qr_la_finestra.png")

print("qr generado")