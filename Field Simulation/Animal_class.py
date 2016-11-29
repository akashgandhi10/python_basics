import random
class Animal(object):
    """Animal food class"""
    #constructor
    def __init__(self, growth_rate, food_need, water_need, name):
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "born"
        self._type = "animal"
        self.name = name

    def needs(self):
        return {"food need": self._food_need, "water need": self._water_need}

    def report(self):
        return{"type": self._type, "name": self.name, "status": self._status, "growth": self._weight, "days growing": self._days_growing}

    def _update_status(self):
        if self._weight > 15:
            self._status = "old"
        elif self._weight > 10:
            self._status = "mature"
        elif self._weight > 5:
            self._status = "young"
        elif self._weight > 0:
            self._status = "just borned"
        elif self._weight == 0:
            self._status = "born"

    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()


def auto_grow(animal, days):
    for i in range(days):
        food = random.randint(1, 10)
        water = random.randint(1, 10)
        animal.grow(food, water)

def manual_grow(animal):
    valid =  False
    while not valid:
        try:
            food = int(input("Please enter a food value (1-10): "))
            if 1 <= food <= 10:
                valid = True
            else:
                print ("Please enter a valid food value between 1 to 10")
        except (ValueError, NameError):
            print ("Please enter a valid food value between 1 to 10")
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
    animal.grow(food, water)

def display_menu():
    print ""
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit test program")
    print ""
    print("Please select a option from above menu")

def manage_animal(animal):
    print ("This is animal managment program")
    noexit = True
    while noexit:
        display_menu()
        option = input("Option Selected: ")
        print ""
        if option == 1:
            manual_grow(animal)
        elif option == 2:
            auto_grow(animal, 30)
        elif option == 3:
            print animal.report()
        elif option == 0:
            noexit = False
    print ("Thank you for using animal managment")

def main():
    #instatiate the class
    new_animal = Animal(1, 3, 4)
    manage_animal(new_animal)
    # print new_animal.needs()
    # print_messages()
    # print new_animal.report()
    # new_animal.grow(7, 7)
    # auto_grow(new_animal, 30)
    # manual_grow(new_animal)
    # print new_animal.report()

if __name__ == "__main__":
    main()
