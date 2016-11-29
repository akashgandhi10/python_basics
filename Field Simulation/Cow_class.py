from Animal_class import *

class Cow(Animal):
    """A Cow Class"""
    #constructor
    def __init__(self, name):
        #call the parent class constructor with default values for cow
        super(Cow, self).__init__(1, 3, 6, name)
        # growth_rate = 1, food_need = 3, water_need = 6
        self._type = "Cow"
        # self.name = name


    #override grow method for subclass
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
    cow_animal = Cow("bc")
    print cow_animal.report()
    manual_grow(cow_animal)
    print cow_animal.report()
    manual_grow(cow_animal)
    print cow_animal.report()
    manual_grow(cow_animal)
    print cow_animal.report()

if __name__ == "__main__":
    main()
