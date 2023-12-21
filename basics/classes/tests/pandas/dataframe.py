import pandas as pd

df = pd.read_csv("../data/existing-roles.csv")
print("head: ", df.head(2))
print("tail: ", df.tail(2))
print("-----------------------")
print("selecting a range of elements: ", df.iloc[3:5, 2])
print("-----------------------")
print(df.describe())  # Generates statistics summary of numeric columns in the DataFrame.
print("-----------------------")
print(df.info())  # Provides a summary of a DataFrame.

# dictionary can be read as dataframe
print("-----------------------")
dictionary = {'Car': 'Audi', 'Bike': 'Ducati', 'Plane': 'Boeing'}
new_df = pd.DataFrame(dictionary, index=[0])
print(new_df)

# create a new dataframe with one one or two columns
print("-----------------------")
new_df_selected_columns = df[['Role Description', 'Role Name']]
print(new_df_selected_columns)

# first row and first column
print("-----------------------")
first_row_first_column = new_df_selected_columns.iloc[0, 0]
print(first_row_first_column)

print("-----------------------")
print("Unique Role Names :: ", df['Role Name'].unique())

print("-----------------------")
print(df['Year of creation'] > 2000)
# create a new dataframe for selected rows
selected_rows = df[df['Year of creation'] > 2000]
print(selected_rows)
# write it in csv
selected_rows.to_csv("../data/selectedRoles.csv", index=False)

print("-----------------------")
# accessing specific element in dataframe
print(df.iloc[2])

print("-------------Filter Dataframe by condition----------")
# create a dataframe with age and salary
age = [23, 24, 25, 26, 27]
salary = [1000, 2000, 3000, 4000, 5000]
df = pd.DataFrame({'age': age, 'salary': salary})
print(df)

filtered_df = df[(df["age"] > 22) & (df["salary"] < 3000)]
print(filtered_df.head())

print("-------------Find Duplicates ----------")
age = [23, 24, 24, 26, 27]
salary = [1000, 2000, 2000, 4000, 5000]
df = pd.DataFrame({'age': age, 'salary': salary})
duplicate_rows = df[df.duplicated()]
print(duplicate_rows)

print("-------------Drop rows and columns ----------")
df.drop(["age"], axis=1, inplace=True)  # Will drop columns axis=1
print(df.head())
df.drop(index=[1, 3, 4], axis=0, inplace=True)  # Will drop rows
print(df.head())
