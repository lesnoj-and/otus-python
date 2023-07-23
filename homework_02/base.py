from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0) -> None:
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                return True
            else:
                raise LowFuelError

    def move(self, dist):
        need = self.fuel_consumption * dist
        if need > self.fuel:
            raise NotEnoughFuel
        else:
            self.fuel -= need
