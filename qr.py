import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image

# URL directa a tu hoja de vida
cv_url = "https://ingpmas92.github.io/Mi_CV/CV-PAOLA%20M%20ARGUELLES%20S-ING%20DE%20SISTEMAS.pdf"

# Generar el QR
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(cv_url)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')

# Guardar la imagen del QR
qr_image_path = "qr_code.png"
img.save(qr_image_path)

# Crear el PDF con el QR
pdf_path = "cv_qr_code.pdf"
c = canvas.Canvas(pdf_path, pagesize=letter)
width, height = letter

# Agregar el QR al PDF
c.drawImage(qr_image_path, width / 2 - 50, height / 2 - 50, width=100, height=100)

# Agregar texto opcional
c.drawString(width / 2 - 80, height / 2 + 60, "Escanea el código QR para ver mi hoja de vida")

# Guardar el PDF
c.save()

print("PDF generado con éxito.")