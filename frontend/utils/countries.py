def get_country_list():
    with open("./countries.txt", "r") as f:
        countries = [line.strip() for line in f if line.strip()]
    return sorted(countries)