import qrcode

# QR instance customizing the QRcode

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=8,
    border=3,
)

# Add data to the QR code
link = "https://www.youtube.com/watch?v=FOGRHBp6lvM"
qr.add_data(link)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="purple", back_color="white")

# Save image
img.save("my_qrcode.png")

# Display image
img.show()
