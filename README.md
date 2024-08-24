# QR Code Generator

This repository contains two Python scripts for generating QR codes:

- `qrcodegenrator.py`: Generates QR codes from URLs using a Streamlit GUI.
- `simpleqr.py`: A simple QR code generator without a GUI.

## Requirements

Install the required packages:
```sh
pip install qrcode[pil] streamlit
```

## Usage
### qrcodegenrator.py
   
   You can try the hosted version of this script here:
   https://urltoqrcode.streamlit.app/
   
   1.Run The Script
   
    streamlit run qrcodegenrator.py 
    
   2.Open the provided URL in your browser.
   
   3.Enter the URL and click “Download QR Code”.

<br>

### simpleqr.py
   
   1.Run The Script
   
    python simpleqr.py 
    
   2.Enter the URL when prompted.
   
   3.The QR code will be saved as `qrcode.png`


## License
Licensed under the MIT License.
