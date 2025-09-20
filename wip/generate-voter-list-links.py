
import base64
import re
from urllib.parse import urlparse,parse_qs,urlencode,urlunparse

url = "https://ceowestbengal.nic.in/RollPDF/GetDraft?acId=108&key=QUMxMDhQQVJUMTM0LnBkZg=="
url = urlparse(url)
qs = parse_qs(url.query)
decoded_qs = base64.b64decode(qs["key"][0]).decode()
number = re.findall(r'(\d+)', decoded_qs)[-1]

def print_links(pdf_num,limit):
    for i in range(pdf_num - limit, pdf_num + limit + 1):
        # x = int(pdf_num) + limit
        pdf_name = f"AC108PART{str(i)}.pdf"
        qs["key"] = [base64.b64encode(pdf_name.encode()).decode()]
        new_query = urlencode(qs,doseq=True)
        updated_url = url._replace(query=new_query).geturl()
        print(f"{str(i)}: {updated_url}")

print_links(int(number),2)    



