class CitiesR:
    def __init__(self):
        self.cities_rainfalls = {}

    def is_element(self, city) -> bool:
        if city in self.cities_rainfalls:
            return True
        return False

    def add_key(self, key: str, value: int):
        self.cities_rainfalls[key] = value

    def add_value(self, key: str, value: int):
        self.cities_rainfalls[key] += value

    def __repr__(self) -> str:
        message = ""
        for i in self.cities_rainfalls.keys():
            message += i + ": " + str(self.cities_rainfalls[i]) + "\n"
        return message

def get_rainfall() -> CitiesR:
    cities_rainfall = CitiesR()
    while True:
        city = input().strip()
        if not city:
            break
        rainfall = int(input())
        if cities_rainfall.is_element(city):
            cities_rainfall.add_value(key=city, value=rainfall)
        else:
            cities_rainfall.add_key(key=city, value=rainfall)
    return cities_rainfall

print(get_rainfall())