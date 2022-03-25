from Herencia.land import Land


class Car(Land):
    def __init__(self, name, price, motor, use_gas: bool) ->None:
        super().__init__(name, price, motor)
        self.use_gas = use_gas

    def use_gas(self):
        print(self.name)

    def description(self):
        if self.use_gas:
            print('El auto: {} tiene motor a gasolina y un precio de {} bs'.format(self.name, self.price))
        else:
            print('El auto: {} es electrico y su costo es de {} bs'.format(self.name, self.price))

