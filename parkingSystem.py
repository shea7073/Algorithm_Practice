class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int):
        if carType == 1 and self.big >= 1:
            self.big = self.big - 1
            return True
        if carType == 2 and self.medium >= 1:
            self.medium -= 1
            return True
        if carType == 3 and self.small >= 1:
            self.small -= 1
            return True
        else:
            return False


obj = ParkingSystem(1, 1, 0)

p1 = obj.addCar(1)
p2 = obj.addCar(2)
p3 = obj.addCar(3)
p4 = obj.addCar(1)

print(p1, p2, p3, p4)
