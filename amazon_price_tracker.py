import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

URL = """https://www.amazon.com/Orient-Bambino-Japanese-Automatic-Stainless/dp/B01MTS5BFN/ref=sxin_15_ac_d_rm?ac_md=0-0-
b3JpZW50IGJhbWJpbm8%3D-ac_d_rm_rm_rm&content-id=amzn1.sym.b09913c7-88ee-4b06-b977-3fd4ebd29a25%3Aamzn1.sym.b09913c7-88ee
-4b06-b977-3fd4ebd29a25&crid=2CWTBHJ3JSTAW&cv_ct_cx=orient+bambino&keywords=orient+bambino&pd_rd_i=B01MTS5BFN&pd_rd_r=7b
efd3a6-292b-40e6-9c9e-96affa48e4dc&pd_rd_w=H9qge&pd_rd_wg=oyKPX&pf_rd_p=b09913c7-88ee-4b06-b977-3fd4ebd29a25&pf_rd_r=KZ4
6XHVHGF7PYA4TV154&qid=1673225707&sprefix=orient+bambin%2Caps%2C302&sr=1-1-7d9bfb42-6e38-4445-b604-42cab39e191b"""

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)
data = response.text

soup = BeautifulSoup(data, 'html.parser')
price = soup.find(name='span', class_=["a-price a-text-price a-size-medium apexPriceToPay"]).getText()
real_price = price.split("$")[1]

product_name = soup.find(name='span', id='productTitle', class_="a-size-large product-title-word-break").getText().strip()
now = str(datetime.now())

filename = 'prices.txt'

if os.path.exists(filename):
    with open(filename, 'a') as f:
        f.write(f"{now[:19]}, {product_name}, {real_price}\n")
else:
    # File does not exist
    with open(filename, 'w') as f:
        f.write(f"{now[:19]}, {product_name}, {real_price}\n")

