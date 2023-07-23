from homework_02.base import Vehicle


class Car(Vehicle):
    def __init__(self, brand, model, year) -> None:
        super().__init__(brand, model, year)
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine
