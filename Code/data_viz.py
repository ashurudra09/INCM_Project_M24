"""
Testing out data analysis and visualization using pandas library
"""
import matplotlib.pyplot as plt
import pandas as pd

# df = pd.read_csv("../datasets/iris.csv")
#
# # print(df.describe())    # general description of dataframe (only numerical data)
# # print(df.head(5))   # first n rows of dataframe
# # print(df.tail(5))   # last n rows of dataframe
# # print(df.iloc[:5,1:])   # prints certain subset of rows and columns (ranged arguments)
# # print(df.loc[:6,"species"]) # prints by column name
# print(df.groupby("species").mean().head())  # groups all unique elements of column 'species' together, takes means of data in other columns accordingly
#
# # Separating petal length and petal width data by species
# pl_setosa = df["petal_length"][df["species"] == "setosa"]
# pl_versicolor = df["petal_length"][df["species"] == "versicolor"]
# pl_virginica = df["petal_length"][df["species"] == "virginica"]
#
# pw_setosa = df["petal_width"][df["species"] == "setosa"]
# pw_versicolor = df["petal_width"][df["species"] == "versicolor"]
# pw_virginica = df["petal_width"][df["species"] == "virginica"]
#
# # Create scatter plot for petal length vs petal width
# plt.figure(figsize=(10, 6))
# plt.scatter(pl_setosa, pw_setosa, color="blue", marker="o", label="Setosa")
# plt.scatter(pl_versicolor, pw_versicolor, color="green", marker="s", label="Versicolor")
# plt.scatter(pl_virginica, pw_virginica, color="red", marker="^", label="Virginica")
#
# # Labels and legend
# plt.xlabel("Petal Length (cm)")
# plt.ylabel("Petal Width (cm)")
# plt.title("Petal Length vs Petal Width by Species")
# plt.legend()
# plt.show()

df = pd.read_csv("../datasets/penguins.csv")

print(df.head())
print(df.columns)

print(df.describe())
