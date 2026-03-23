import urllib.request
import re
import ssl
from collections import Counter

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://keroxdental.com/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, context=ctx) as response:
        html = response.read().decode('utf-8')
        css_links = re.findall(r'<link[^>]*rel="[a-z-]*stylesheet"[^>]*href="([^"]+)"', html)
        print("CSS Links:", css_links)
        for link in css_links:
            if link.startswith('/'):
                link = 'https://keroxdental.com' + link
            if 'http' not in link: continue
            
            try:
                req2 = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req2, context=ctx) as r2:
                    css_content = r2.read().decode('utf-8', errors='ignore')
                    colors = re.findall(r'#[0-9a-fA-F]{6}', css_content)
                    colors = [c.upper() for c in colors]
                    print(f"Top 5 colors in {link.split('/')[-1]}:", Counter(colors).most_common(5))
            except Exception as e:
                pass
except Exception as e:
    print(e)
