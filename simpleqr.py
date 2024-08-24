import qrcode

url= input("Enter The Url: ")
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

print("QR Code Generated Successfully")

download = input("Do you want to download the QR Code? (y/n): ")
if download.lower() == "y":
  img.save("qrcode.png")
  print("QR Code downloaded successfully")
else:
  print("QR Code not downloaded")