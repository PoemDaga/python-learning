from bs4 import BeautifulSoup

html = ("<!DOCTYPE html><html lang=\"en\"><head><title>Document</title></head><body><h3><b id=\"boldest\">Actor "
        "1</h3><p>10000</p><h3>Actor 2</h3><p>20000</p><h3>Actor 3</h3><p>30000</p></body></html>")
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())
print(soup.title)

print("-------------------")
tag_object = soup.body.h3
print(tag_object)
print("attrs: ", tag_object.b.attrs)
print("value: ", tag_object.string)

print("-------------------")
print(soup.p)
sibling_obj = tag_object.next_sibling
print(sibling_obj)
next1 = sibling_obj.next_sibling
print(next1)
next2 = next1.next_sibling
print(next2)
