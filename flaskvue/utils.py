import cv2
from PIL import Image
from io import BytesIO
import base64
import numpy as np

def base64toCV2(img):
    code = base64.b64decode(img.split(',')[1])
    image_decoded = Image.open(BytesIO(code))

    img_array = np.asarray(image_decoded)

    return img_array

def CV2toBase64(img):
    convertedCV2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    CV2PIL = Image.fromarray(convertedCV2)

    modified_bin = BytesIO()
    CV2PIL.save(modified_bin, format="PNG")
    img_str = base64.b64encode(modified_bin.getvalue()).decode("utf-8")
    add_headers = "data:image/png;base64," + img_str

    return add_headers
