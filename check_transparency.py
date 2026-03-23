from urllib.request import Request, urlopen
from PIL import Image
import io

url = "https://keroxdental.com/img/products/zirconia/zircostar-3dml-bg.png"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urlopen(req) as response:
        img_data = response.read()
        img = Image.open(io.BytesIO(img_data))
        print(f"Format: {img.format}, Mode: {img.mode}, Size: {img.size}")
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            print("Image has transparency capabilities.")
            # Check if any pixel is actually transparent
            if img.mode == 'RGBA':
                extrema = img.getextrema()
                if extrema[3][0] < 255:
                    print("Image contains transparent pixels!")
                else:
                    print("Alpha channel is fully opaque.")
except Exception as e:
    print(f"Error: {e}")
