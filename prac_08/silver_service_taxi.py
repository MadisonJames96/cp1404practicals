from prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __int__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness

    def __str__(self):
        return"{} plus flagfall of ${:.2f}".format(super().__str__(),self.flagfall)