import pandas as pd

data = pd.read_csv("One_Plus_Phones_With_Missing.csv")

# print(data.head())

data["Rating"] = 2 * data["Rating"]

data.to_csv("One_Plus_Phones_With_Missing.csv", index=False)