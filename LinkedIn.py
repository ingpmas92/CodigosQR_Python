import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image

# URLs
cv_url = "https://ingpmas92.github.io/Mi_CV/CV-PAOLA%20M%20ARGUELLES%20S-ING%20DE%20SISTEMAS.pdf"
linkedin_url = "http://linkedin.com/in/paola-arguelles-salazar-b90471259"

# Generar el QR para la hoja de vida
cv_qr = qrcode.QRCode(version=1, box_size=10, border=5)
cv_qr.add_data(cv_url)
cv_qr.make(fit=True)
cv_img = cv_qr.make_image(fill='black', back_color='white')
cv_image_path = "cv_qr_code.png"
cv_img.save(cv_image_path)

# Generar el QR para LinkedIn
linkedin_qr = qrcode.QRCode(version=1, box_size=10, border=5)
linkedin_qr.add_data(linkedin_url)
linkedin_qr.make(fit=True)
linkedin_img = linkedin_qr.make_image(fill='black', back_color='white')
linkedin_image_path = "linkedin_qr_code.png"
linkedin_img.save(linkedin_image_path)

# Crear el PDF con ambos QRs
pdf_path = "cv_and_linkedin_qr_code.pdf"
c = canvas.Canvas(pdf_path, pagesize=letter)
width, height = letter

# Agregar el QR de la hoja de vida al PDF
c.drawImage(cv_image_path, width / 2 - 50, height / 2 + 50, width=100, height=100)
c.drawString(width / 2 - 60, height / 2 + 160, "Escanea el código QR para ver mi hoja de vida")

# Agregar el QR de LinkedIn al PDF
c.drawImage(linkedin_image_path, width / 2 - 50, height / 2 - 100, width=100, height=100)
c.drawString(width / 2 - 70, height / 2 - 10, "Escanea el código QR para ver mi LinkedIn")

# Guardar el PDF
c.save()

print("PDF generado con éxito y guardado como cv_and_linkedin_qr_code.pdf.")