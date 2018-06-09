

import requests
from bs4 import BeautifulSoup


#url = 'http://www.kyobobook.co.kr/search/SearchCommonMain.jsp?vPstrCategory=TOT&vPstrKeyWord=%26%2351089%3B%26%2351008%3B%20%26%2353456%3B%26%2345769%3B&vPplace=top'
url = 'http://m.kyobobook.co.kr/digital/ebook/ebookContents.ink?item_position=1&barcode=4811506020012&class_code=&cate_code=EBOOK&returnUrl=%2Fdigital%2Febook%2FsearchList.ink&keyword=%EC%9E%91%EC%9D%80+%ED%83%90%EB%8B%89&type=&sort_type=1&sort_order=0&need_login=N&reviewLimit=0&barcodes=&refererUrl=%2Fdigital%2Febook%2FsearchList.ink%3Fcate_code%3DEBOOK%26keyword%3D%EC%9E%91%EC%9D%80+%ED%83%90%EB%8B%89&barcodes_temp=&gubun=&ser_product_yn=&listCateGubun=1&cate_gubun='
rsp = requests.get(url)
#print(rsp)
content = rsp.content
#print(content)
soup = BeautifulSoup(content, 'html.parser')

boundary = soup.find('div',{'class':"setBook_section"})
#print("type of boundary: {}".format(type(boundary))) # <class 'bs4.element.Tag'>

elems = boundary.find_all('p',{'class':'title'})
#print("type of elems: {}".format(type(elems))) # <class 'bs4.element.ResultSet'>
#print(elems.text)

rst = set()
for title in elems:
    book_title = title.text
    rst.add(book_title)

print("".join(rst))
