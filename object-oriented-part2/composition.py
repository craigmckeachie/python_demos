class Vehicle:

    def lock_the_doors(self):
        pass

    def unlock(self):
        pass


class Engine:

    def start(self):
        pass

    def stop(self):
        pass


class Car(Vehicle):

    def __init__(self):
        # composition - "has a" engine
        self._engine = Engine()

    def start(self):
        self.lock_the_doors()
        self._engine.start()


car = Car()
car.start()
