# streamlit_qr_code.py

import streamlit as st
import qrcode
from PIL import Image
import io

# Set up the title for the Streamlit app
st.title("URL to QR Code Generator")

# Input field for the URL
url = st.text_input("Enter the URL to convert into a QR code:")

# Button to trigger QR code generation
if st.button("Generate QR Code"):
    if url:
        try:
            # Generate the QR code
            qr = qrcode.QRCode(
                version=1,  # controls the size of the QR Code
                error_correction=qrcode.constants.ERROR_CORRECT_L,  # default error correction
                box_size=10,  # size of each box in the QR code grid
                border=4,  # thickness of the border
            )
            qr.add_data(url)
            qr.make(fit=True)

            # Create an image from the QR code instance
            img = qr.make_image(fill="black", back_color="white")

            # Save the QR code image in memory as a BytesIO stream
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format="PNG")
            img_byte_arr = img_byte_arr.getvalue()

            # Display the QR code image in Streamlit
            st.image(img_byte_arr, caption="Your QR Code", use_column_width=True)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please enter a valid URL.")
