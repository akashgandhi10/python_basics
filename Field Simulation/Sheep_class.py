from Animal_class import *

class Sheep(Animal):
    """Sheep class"""

    #constructor
    def __init__(self, name):
        #call the parent class constructor with default values for sheep
        # growth_rate = 1, food_need = 4, water_need = 7
        super(Sheep, self).__init__(1, 4, 7, name)
        self._type = "Sheep"

    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "just borned" and water > self._water_need:
                self._weight += self._growth_rate * 1.5
            elif self._status == "young" and water > self._water_need:
                self._weight += self._growth_rate * 2.5
            else:
                self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()


def main():
    sheep_animal = Sheep()
    print sheep_animal.report()
    manual_grow(sheep_animal)
    print sheep_animal.report()
    manual_grow(sheep_animal)
    print sheep_animal.report()
    manual_grow(sheep_animal)
    print sheep_animal.report()


if __name__ == "__main__":
    main()
