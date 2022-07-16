class province_freedonia:
    def __init__(self, name):
        self.name = name
        self.provinces = {'Chico': 0.5,
                          'Goucho': 0.7,
                          'Harpo': 0.5,
                          'Zeppo': 0.4}
        self.tax = self._main_tax_assign()

    def _main_tax_assign(self):
        return self.provinces[self.name]

    def calculate_tax(self, amount, hour):
        return self.tax * amount * hour/24


def calculate_tax(amount: float, province: str, hour: int):
    prov = province_freedonia(province)
    return prov.calculate_tax(amount, hour) + amount
