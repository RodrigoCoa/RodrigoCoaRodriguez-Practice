from Herencia.land import Land
from Herencia.transport import Transport
from Herencia.car import  Car
from Herencia.bicycle import Bicycle


if __name__=="__main__":
    trans1: Transport = Transport('Tren', 100)
    trans2: Transport = Land('Tractor', 4923, True)
    trans3: Transport = Car('Tesla', 4567, False, False)
    trans4: Transport = Bicycle('Plan3000', 65, False, True)

    trans_list = [trans1, trans2, trans3, trans4]

    for transp in trans_list:
        transp.description()





