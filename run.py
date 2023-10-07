

# Define your data as provided
data = {
    "Country Name": ["Angola", "Argentina", "Armenia", "Australia", "Ireland"],
    "Country Code": ["AGO", "ARG", "ARM", "AUS", "IRL"],
    "2019": [2142.238757, 9963.672506, 4828.505178, 54941.43418, 80927.07467],
    "2020": [1603.993477, 8496.424142, 4505.867364, 51720.37076, 85420.19086],
    "2021": [1953.533757, 10636.1202, 4966.513471, 60443.10916, 100172.0793]
}

year_2020_data = {
    "Country Name": data["Country Name"],
    "GDP 2020": data["2020"]
}
print("Data for 2020:")
print(year_2020_data)

mean_gdp_2019 = sum(data["2019"]) / len(data["2019"])
mean_gdp_2020 = sum(data["2020"]) / len(data["2020"])
mean_gdp_2021 = sum(data["2021"]) / len(data["2021"])
print("Mean GDP for 2019:", mean_gdp_2019)
print("Mean GDP for 2020:", mean_gdp_2020)
print("Mean GDP for 2021:", mean_gdp_2021)

print("Country Name\tCountry Code\t2019\t\t2020\t\t2021")
for i in range(len(data["Country Name"])):
    print(f"{data['Country Name'][i]}\t\t{data['Country Code'][i]}\t\t{data['2019'][i]}\t{data['2020'][i]}\t{data['2021'][i]}")


