import qrcode
import streamlit as st
from PIL import Image 
from io import BytesIO

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

# Save the image to a BytesIO object
buffer = BytesIO()
buffer.seek(0)

 # Provide a download button
st.download_button(
        label="Download QR Code",
        data=buffer,
        file_name="qrcode.png",
        mime="image/png"
    )
