import pandas as pd
import xml.etree.ElementTree as ET

tree = ET.parse("../data/sampleXML.xml")
root = tree.getroot()

columns = ["Name", "Age", "Email"]
df = pd.DataFrame(columns=columns)

for node in root:
    name = node.find("name").text
    age = node.find("age").text
    email = node.find("email").text
    print(name, age, email)

    # append to dataframe add new row
    new_df = pd.Series([name, age, email], columns)
    print("-------------------")
    print(new_df)
    print("-------------------")
# TODO: fix this
# print("df", df)
# concatinate = pd.concat([df, new_df], ignore_index=True)
# print("concatinate", concatinate.head())
# df = pd.concat([df, new_df], ignore_index=True)


print(df.head(2))
