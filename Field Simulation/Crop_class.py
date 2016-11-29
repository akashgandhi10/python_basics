import random
class Crop(object):
    """Crop light class"""
    #constructor
    def __init__(self, growth_rate, light_need, water_need):
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "seed"
        self._type = "generic"

    def needs(self):
        return {"light need": self._light_need, "water need": self._water_need}

    def report(self):
        return{"type": self._type, "status": self._status, "growth": self._growth, "days growing": self._days_growing}

    def _update_status(self):
        if self._growth > 15:
            self._status = "old"
        elif self._growth > 10:
            self._status = "mature"
        elif self._growth > 5:
            self._status = "young"
        elif self._growth > 0:
            self._status = "seedling"
        elif self._growth == 0:
            self._status = "seed"

    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()


def auto_grow(crop, days):
    for i in range(days):
        light = random.randint(1, 10)
        water = random.randint(1, 10)
        crop.grow(light, water)

def manual_grow(crop):
    valid =  False
    while not valid:
        try:
            light = int(input("Please enter a light value (1-10): "))
            if 1 <= light <= 10:
                valid = True
            else:
                print ("Please enter a valid light value between 1 to 10")
        except (ValueError, NameError):
            print ("Please enter a valid light value between 1 to 10")
    valid =  False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print ("Please enter a valid water value between 1 to 10")
        except (ValueError, NameError):
            print ("Please enter a valid water value between 1 to 10")
    crop.grow(light, water)

def display_menu():
    print ""
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit test program")
    print ""
    print("Please select a option from above menu")

def manage_crop(crop):
    print ("This is crop managment program")
    noexit = True
    while noexit:
        display_menu()
        option = input("Option Selected: ")
        print ""
        if option == 1:
            manual_grow(crop)
        elif option == 2:
            auto_grow(crop, 30)
        elif option == 3:
            print crop.report()
        elif option == 0:
            noexit = False
    print ("Thank you for using crop managment")

def main():
    #instatiate the class
    new_crop = Crop(1, 3, 4)
    manage_crop(new_crop)
    # print new_crop.needs()
    # print_messages()
    # print new_crop.report()
    # new_crop.grow(7, 7)
    # auto_grow(new_crop, 30)
    # manual_grow(new_crop)
    # print new_crop.report()

if __name__ == "__main__":
    main()
