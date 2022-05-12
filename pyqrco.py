import qrcode 
import PIL
from PIL import Image 

qr=qrcode.QRCode(version=1,error_correction= qrcode.constants.ERROR_CORRECT_H,box_size=8,border=3)
qr.add_data("https://www.prakharshukla.org/")
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="white")
img.save("prakhar_werbsite.png")