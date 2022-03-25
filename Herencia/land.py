from Herencia.transport import Transport


class Land(Transport):

    def __init__(self, name, price, motor: bool) ->None:
        super().__init__(name, price)
        self.motor = motor

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def description(self):
        if self.motor:
            print('El vehiculo: {} tiene motor y un precio de {} bs'.format(self.name, self.price))
        else:
            print('El vehiculo: {} no tiene motor y su costo es de {} bs'.format(self.name, self.price))


