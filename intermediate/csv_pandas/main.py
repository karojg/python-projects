# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data)

#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
#         print(temperatures)

# import pandas
# data = pandas.read_csv("weather_data.csv")

# print(data[data.temp])

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = data["Primary Fur Color"].value_counts()

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [color["Gray"], color["Cinnamon"], color["Black"]],
}

data_frame = pandas.DataFrame(data_dict, index=[1, 2, 3], columns=["Fur Color", "Count"])
print(data_frame)
data_frame.to_csv("squirrel_count.csv")
