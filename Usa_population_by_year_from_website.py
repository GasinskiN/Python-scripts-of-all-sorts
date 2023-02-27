import requests
import json

url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
response = requests.get(url)
data = json.loads(response.text)
year_table = []
population_table = []
with open("file.txt", "w") as file:
    for x in range(0, 7):
        shallower_table = (data["data"][x])
        print(str(shallower_table["Year"]) + ": " + str(shallower_table["Population"]))
        file.writelines(str(shallower_table["Year"]) + ": " + str(shallower_table["Population"]) + "\n")
