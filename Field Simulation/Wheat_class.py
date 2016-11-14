from Crop_class import *

class Wheat(Crop):
    """Wheat class"""

    #constructor
    def __init__(self):
        #call the parent class constructor with default values for sheep
        # growth_rate = 1, light_need = 4, water_need = 7
        super(Wheat, self).__init__(1, 4, 7)
        self._type = "Wheat"

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
    wheat_crop = Wheat()
    print wheat_crop.report()
    manual_grow(wheat_crop)
    print wheat_crop.report()
    manual_grow(wheat_crop)
    print wheat_crop.report()
    manual_grow(wheat_crop)
    print wheat_crop.report()


if __name__ == "__main__":
    main()
