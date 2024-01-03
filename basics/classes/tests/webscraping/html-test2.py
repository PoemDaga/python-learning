from bs4 import BeautifulSoup

html = "<table><tr><th>Pizza place</th><th>Orders</th><th>Slices</th></tr><tr><td>Domino's</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td>144</td></tr></table>"
table = BeautifulSoup(html, 'html.parser')
print(table.prettify())

table_row = table.find_all('tr')
print(type(table_row))
for row in table_row:
    print("row: ", row)
    cols = row.find_all('td')
    for col in cols:
        print(col.string)
