class Transport:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def description(self):
        print('El vehiculo: {} tiene un precio de {} bs'.format(self.name, self.price))
