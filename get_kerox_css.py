import urllib.request
import re
import ssl
from collections import Counter

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://keroxdental.com/css/style.css"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx) as r:
        css_content = r.read().decode('utf-8', errors='ignore')
        colors = re.findall(r'#[0-9a-fA-F]{6}', css_content)
        colors = [c.upper() for c in colors]
        print(f"Top colors in css: ", Counter(colors).most_common(10))
except Exception:
    pass

url2 = "https://keroxdental.com/style.css"
try:
    req = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx) as r:
        css_content = r.read().decode('utf-8', errors='ignore')
        colors = re.findall(r'#[0-9a-fA-F]{6}', css_content)
        colors = [c.upper() for c in colors]
        print(f"Top colors in root style.css: ", Counter(colors).most_common(10))
except Exception:
    pass
