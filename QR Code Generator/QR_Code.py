import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=10)
qr.add_data("https://www.linkedin.com/in/harshmeena0645")
qr.make(fit=True)
img=qr.make_image(fill_color="white",back_color="blue")
img.save("Linkdin_QR_Code.png")