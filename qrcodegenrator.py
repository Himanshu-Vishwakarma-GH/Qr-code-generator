import qrcode
import streamlit as st
from PIL import Image 

st.title("URL To QR Code Generator")

url= st.text_input("Enter The Url: ")
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

#st.image(img,caption="QR Code Generated Successfully")

download = st.button("Download QR Code")

if download:
  img.save("qrcode.png")
  st.success("QR Code downloaded successfully")
else:
  st.info("QR Code not downloaded")