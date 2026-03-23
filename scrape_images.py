import urllib.request
from html.parser import HTMLParser
import ssl
import json

class ImgParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
    
    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.images.append(dict(attrs))

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://keroxdental.com/zirconia"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, context=ctx) as response:
        html = response.read().decode('utf-8')
        parser = ImgParser()
        parser.feed(html)
        results = []
        for img in parser.images:
            src = img.get('src', '')
            alt = img.get('alt', '')
            if 'http' not in src and src.startswith('/'):
                src = 'https://keroxdental.com' + src
            if 'http' not in src and src.startswith('./'):
                src = 'https://keroxdental.com' + src[1:]
            if 'ht' in src.lower() or 'ml' in src.lower() or 'zirc' in src.lower() or '3d' in src.lower():
                results.append({"src": src, "alt": alt})
        with open("C:\\projet antigravity\\scraped_images.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
except Exception as e:
    print(f"Error: {e}")
