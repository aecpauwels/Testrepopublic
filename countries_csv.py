import csv
import os
import random

COUNTRIES = [
    "Russia", "Russia5", "Japan", "Canada", "India", "Germany",
    "Australia", "Mexico", "Egypt", "Norway", "Thailand", "Argentina",
    "Nigeria", "France", "Vietnam", "Chile", "Poland", "Morocco", "Peru",
    "Turkey", "Indonesia", "Ghana", "Portugal", "New Zealand",
]

CONTINENTS = ["Africa", "Asia", "Europe", "North America", "Oceania", "South America"]

HEADERS = [
    "Country", "Continent", "Population (M)", "Area (1000 km2)",
    "GDP (B USD)", "GDP per Capita (USD)", "Life Expectancy",
    "Literacy Rate (%)", "Unemployment (%)", "Urban Population (%)",
]

OUTPUT_DIR = r"C:\ClaudeFolderPythonTests\outputpath"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "countries.csv")


def random_row(country):
    population = round(random.uniform(1, 300), 1)
    gdp = round(random.uniform(10, 5000), 1)
    return [
        country,
        random.choice(CONTINENTS),
        population,
        round(random.uniform(50, 9000), 1),
        gdp,
        round(gdp * 1000 / population),
        round(random.uniform(55, 85), 1),
        round(random.uniform(60, 100), 1),
        round(random.uniform(2, 25), 1),
        round(random.uniform(20, 95), 1),
    ]


def main():
    rows = [random_row(country) for country in random.sample(COUNTRIES, 10)]

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(HEADERS)
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows x {len(HEADERS)} columns to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
