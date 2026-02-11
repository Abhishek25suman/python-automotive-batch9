import qrcode
from PIL import Image

# 🔗 Your GitHub Pages Link
project_link = "https://abhishek25suman.github.io/python-automotive-batch9/"

# Create QR Code with high quality settings
qr = qrcode.QRCode(
    version=None,  # Auto size
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=12,  # Controls size of QR
    border=4,  # Border thickness
)

qr.add_data(project_link)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save image
img.save("57152_ABHISHEK_SUMAN_Project_QR.png")

print("✅ Professional QR Code Generated Successfully!")