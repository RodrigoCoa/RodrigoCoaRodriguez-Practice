from Herencia.land import Land


class Bicycle(Land):

    def __init__(self, name, price, motor, exercise_bike: bool) ->None:
        super().__init__(name, price, motor)
        self.exercise_bike = exercise_bike

    def exercise_bike(self):
        print(self.name)

    def description(self):
        if self.exercise_bike:
            print('La bicicleta: {} es a pedales y tiene un precio de {} bs'.format(self.name, self.price))
        else:
            print('La bicicleta: {} es electrica y tiene un precio de {} bs'.format(self.name, self.price))