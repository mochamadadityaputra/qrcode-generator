import qrcode

data = input("Enter text or URL: ").strip()
filename = input("Enter the filename (e.g., 'qrcode.png'): ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make()  # Add this line to generate the QR code matrix
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR code saved as {filename}")
