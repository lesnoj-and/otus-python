from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo=10) -> None:
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, amount) -> None:
        if self.cargo + amount > self.max_cargo:
            raise CargoOverload("Overload!")
        else:
            self.cargo += amount

    def remove_all_cargo(self) -> int:
        weight = self.cargo
        self.cargo = 0
        return weight
