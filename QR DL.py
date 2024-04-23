import qrcode

# URL del servidor donde está alojado el HTML
url_servidor = "https://tuusuario.github.io/holamundo.html"

# Generar el código QR que apunta a la URL del servidor
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(url_servidor)
qr.make(fit=True)

# Guardar el código QR como una imagen PNG
img = qr.make_image(fill_color="black", back_color="white")
img.save("codigo_qr_html_personalizado.png")

print("Código QR generado con éxito.")
