# https://leetcode.com/problems/design-parking-system/

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.car_type_map = {
            1: self.big,
            2: self.medium,
            3: self.small
        }

    def addCar(self, carType: int) -> bool:
        if not self.car_type_map[carType]:
            return False

        self.car_type_map[carType] -= 1
        return True


if __name__ == '__main__':
    p = ParkingSystem(1, 1, 0)
    print(p.addCar(1))
    print(p.addCar(2))
    print(p.addCar(3))
    print(p.addCar(1))
