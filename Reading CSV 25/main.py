# with open("weather.csv") as f:
#     lst = f.readlines()

# print(lst)

# import csv

# with open("weather.csv") as f:
#     data = csv.reader(f)
#     temp = []
#     count = 0
#     for row in data:
#         count += 1
#         if count > 1:
#             temp.append(int(row[1]))
#         # print(row)

# print(temp)


# import pandas as pd

# data = pd.read_csv("weather.csv")
# print(data["temp"])
# temp = data["temp"]
# temp_list = temp.to_list()

# print(temp_list)
# print(f"Average of Temperature is {sum(temp_list)/len(temp_list)}")
# print(f"Average of Temperature is {temp.mean()}")
# print(f"Max of Temperature is {temp.max()}")
# print(f"Min of Temperature is {temp.min()}")


# print(data[data["temp"] == data["temp"].max()])



import pandas as pd

data = pd.read_csv("Squirrel.csv")

# print(data.head())
new_data = data["Primary Fur Color"].value_counts()
print(type(new_data))
new_data.to_csv("count_squarrel.csv")