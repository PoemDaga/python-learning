import pandas as pd

#
# #
# print("-----------------------")
# student_data = [
#     [1, 1.0],
#     [2, 1.0],
#     [3, None],
#     [None, 20]
# ]
#
# student_data2 = [
#     [11, 2.0],
#     [12, 1.0],
#     [13, None],
#     [14, 20]
# ]
# df = pd.DataFrame(student_data, columns=["student_id", "age"])
# df2 = pd.DataFrame(student_data2, columns=["student_id", "age"])
#
# frames = [df, df2]
# df3 = pd.concat(frames)
# print(df3)

# print(df.dtypes)
# df = df.astype({'age':int})
# print(df.dtypes)

# df['age'] = df['age'].fillna(0)
# print(df.head())

# df['age'] = df['age']*2

# df = df.rename(columns={"student_id": "yeah!", "age": "c"})
# print(df)

# print(len(df.axes[0]))
# print(len(df.axes[1]))
#
# print(len(df))
# #  count of row and count of columns
# print([len(df), len(df.columns)])
#
# print("-----------------------")
# # condition and column values to return
# var = df.loc[df['student_id'] > 2, ["age"]]
# print(var)
#
# print("-----------------------")
# df["bonus"] = df["age"] * 2
# print(df.head())
#
# print("------------------------------------")
# raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
#             'age': [20, 19, 22, 21],
#             'favorite_color': ['blue', 'blue', 'yellow', "green"],
#             'grade': [88, 92, 95, 70]}
# df = pd.DataFrame(raw_data, index=['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'])
# print(df)
#
# df.drop_duplicates(subset='favorite_color', keep="first", inplace=True)
# print(df.head())
#

# print("------------------------------------")
# raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
#             'age': [20, 19, 22, None],
#             'favorite_color': ['blue', None, 'yellow', "green"],
#             'grade': [88, 92, 95, 70]}
# df = pd.DataFrame(raw_data)
# #print(df)
#
# #df = df.df[df['favorite_color'].isnull()]
# df = df.dropna(subset=['favorite_color'])
# print(df.head())

# city_temp = [
#     ['Paris', 'January', 34],
#     ['Paris', 'Feb', 41],
#     ['Mumbai', 'January', 22],
#     ['Mumbai', 'Feb', 20]
# ]
# 
# df = pd.DataFrame(city_temp, columns=["city", "month", "temp"])
# print(df)
# 
# df = (df.pivot(columns="city", index="month", values='temp')
#       .astype(int)
#       .rename_axis(index=None, columns=None)
#       )  # {'temp': int})
# 
# print("---------")
# print(df)
# print("------------------------------------")
# 
# data = [
#     ['Umbrella', 417, 224, 379, 611],
#     ['SleepingBag', 800, 936, 93, 875]
# ]
# 
# df = pd.DataFrame(data, columns=['product', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'])
# 
# df = pd.melt(df, id_vars=['product'], value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
#              var_name='quarter', value_name='sales'
#              )
# print(df)

# # print("------------------------------------")
# data = [['Tatiana', 'Snake', 98, 464],
#         ['Khaled', 'Giraffe', 50, 41]]
# df = pd.DataFrame(data, columns=['name', 'species', 'age', 'weight'])
#
# df = df[df['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]
#
# print(df)

# print("------------------------------------")
# data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000],
#         ['Albania', 'Europe', 28748, 2831741, 12960000000],
#         ['Algeria', 'Africa', 2381741, 37100000, 188681000000],
#         ['Andorra', 'Europe', 468, 78115, 3712000000],
#         ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
#
# df = pd.DataFrame(data, columns=["name", 'continent', 'area', 'population', 'gdp'])
# # print(df)
#
# #df = df.groupby(by='continent').sum()
# print(df)
# df = df.loc[(df['population'] >= 25000000) | (df['area'] >= 3000000)][["name", 'area', 'population']]
#
# print(df)

# print("------------------------------------")

# customers = [
#     [1, 'John']
#     , [2, 'Pooh'],
#     [3, 'Divi']
# ]
# orders = [
#     [1, 1],
#     [2, 1],
#     [3, 2]
# ]
#
# customersDF = pd.DataFrame(customers, columns=["id", "name"])
# ordersDF = pd.DataFrame(orders, columns=["id", "customer_id"])
#
# df = pd.merge(customersDF, ordersDF, left_on='id', right_on='customer_id', how='left')
# df = df[df['customer_id'].isna()][['name']].rename(columns = {'name':'Customers'})
#
# print(df)


# print("------------------------------------")

# data = [
#     [1, 2], [2, 2], [3, 3], [3, 4], [2, 2]
# ]
#
# df = pd.DataFrame(data, columns=['author_id', 'viewer_id'])
# df = df[df['viewer_id'] == df['author_id']][['author_id']].rename(columns={"author_id": "id"}).sort_values('id', ascending=True).drop_duplicates()
# print(df)
