from Crop_class import *

class Potato(Crop):
    """A Potato Class"""
    #constructor
    def __init__(self):
        #call the parent class constructor with default values for cow
        super(Potato, self).__init__(1, 3, 6)
        # growth_rate = 1, light_need = 3, water_need = 6
        self._type = "Potato"

    #override grow method for subclass
    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status == "young" and water > self._water_need:
                self._growth += self._growth_rate * 2.5
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()


def main():
    potato_crop = Potato()
    print potato_crop.report()
    manual_grow(potato_crop)
    print potato_crop.report()
    manual_grow(potato_crop)
    print potato_crop.report()
    manual_grow(potato_crop)
    print potato_crop.report()

if __name__ == "__main__":
    main()
