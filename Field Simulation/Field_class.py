from Cow_class import *
from Sheep_class import *
from Potato_class import *
from Wheat_class import *

class Field(object):
    """Simulate a field that can contain animals and crops"""

    #constructor
    def __init__(self, max_animals, max_crops):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops

    def plant_crop(self, crop):
        if len(self._crops) <= self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False

    def add_animal(self, animal):
        if len(self._animals) <= self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False

    def harvest_crop(self, poistion):
        return self._crops.pop(poistion)

    def remove_animal(self, poistion):
        return self._animals.pop(poistion)

    def report_content(self):
        crop_report = []
        animal_report = []
        for crop in self._crops:
            crop_report.append(crop.report())
        for animal in self._animals:
            animal_report.append(animal.report())
        return {"Crops": crop_report, "Animals": animal_report}

    def report_needs(self):
        light = 0
        water = 0
        food = 0
        for crop in self._crops:
            needs = crop.needs()
            if needs["light need"] >  light:
                light = needs["light need"]
            if needs["water need"] >  water:
                water = needs["water need"]
        for animal in self._animals:
            needs = animal.needs()
            food += needs["food need"]
            if needs["water need"] > water:
                water = needs["water need"]
        return {"food": food, "light": light, "water": water}

    def grow(self, light, water, food):
        if len(self._crops) > 0:
            for crop in self._crops:
                crop.grow(light, water)
        if len(self._animals) > 0:
            food_required = 0
            for animal in self._animals:
                needs =  animal.needs()
                food_required += needs["food need"]
            if food > food_required:
                additional_food = food - food_required
                food = food_required
            else:
                additional_food = 0
            for animal in self._animals:
                needs = animal.needs()
                feed = needs["food need"]
                if food >= needs["food need"]:
                    food -= needs["food need"]
                    # feed = needs["food need"]
                if additional_food > 0:
                    additional_food -= 1
                    feed += 1
                animal.grow(feed, water)


def display_crop(crops_list):
    print""
    print("The following crops are in the field:")
    pos = 1
    for crop in crops_list:
        print ("{0:>2} .{1}".format(pos, crop.report()))
        pos += 1


def display_animal(animals_list):
    print""
    print("The following animals in the field:")
    pos = 1
    for animal in animals_list:
        print ("{0:>2} .{1}".format(pos, animal.report()))
        pos += 1


def select_crop(lenght_list):
    valid = False
    while not valid:
        selected = int(input("please select a crop: "))
        if selected in range(1, lenght_list + 1):
            valid = True
        else:
            print ("please enter a valid option")
    return selected - 1


def select_animal(lenght_list):
    valid = False
    while not valid:
        selected = int(input("please select a animal: "))
        if selected in range(1, lenght_list + 1):
            valid = True
        else:
            print ("please enter a valid option")
    return selected - 1


def harvest_crop_from_field(field):
    display_crop(field._crops)
    selected_crop =  select_crop(len(field._crops))
    return field.harvest_crop(selected_crop)


def remove_animal_from_field(field):
    display_crop(field._animals)
    selected_animal =  select_animal(len(field._animals))
    return field.remove_animal(selected_animal)


def auto_grow(field, days):
    for day in range(days):
        light = random.randint(1, 10)
        food =  random.randint(1, 10)
        water =  random.randint(1, 10)
        field.grow(light, water, food)


def manual_grow(field):
    valid = False
    while not valid:
        try:
            light = int(input("enter valid light value (1-10): "))
            if 1 <= light <= 10:
                valid = True
            else:
                print ("please enter valid light value")
        except ValueError, NameError:
            print ("please enter valid light value")
    valid = False
    while not valid:
        try:
            water = int(input("enter valid water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print ("please enter valid water value")
        except ValueError, NameError:
            print ("please enter valid water value")
    valid = False
    while not valid:
        try:
            food = int(input("enter valid food value (1-100): "))
            if 1 <= food <= 100:
                valid = True
            else:
                print ("please enter valid food value")
        except ValueError, NameError:
            print ("please enter valid food value")
    valid = False
    field.grow(light, water, food)


def display_crop_menu():
    print ""
    print ("Which Crop type would you like to create?")
    print ""
    print ("1. Potato")
    print ("2. Wheat")
    print ""
    print ("0. I don't want to add a crop - return me to main menu")
    print ""
    print ("Please select an option from above menu: ")

def display_animal_menu():
    print ""
    print ("Which Animal type would you like to create?")
    print ""
    print ("1. Cow")
    print ("2. Sheep")
    print ""
    print ("0. I don't want to add a animal - return me to main menu")
    print ""
    print ("Please select an option from above menu: ")

def display_main_menu():
    print ""
    print ("1. Plant a new crop")
    print ("2. Harvest a crop")
    print ""
    print ("3. Add an animal")
    print ("4. Remove an animal")
    print ""
    print ("5. Grow field manually over 1 day")
    print ("6. Grow field automatically over 30 days")
    print ""
    print ("7. Report a field status")
    print ""
    print ("8. Exit test program")
    print ""
    print ("Please select an option from above menu")
    print ""

def get_menu_choice(lower, upper):
    valid = False
    while not valid:
        try:
            choice = int(input("Option Selected: "))
            if lower <= choice <= upper:
                valid = True
            else:
                print ("Please enter a valid option")
        except ValueError, NameError:
            print ("Please enter avalid option")
    return choice

def plant_crop_in_field(field):
    display_crop_menu()
    choice = get_menu_choice(0,2)
    if choice == 1:
        if field.plant_crop(Potato()):
            print ""
            print ("Crop Planted")
            print ""
        else:
            print ""
            print ("Field is full - potato not planted")
            print ""
    elif choice == 2:
        if field.plant_crop(Wheat()):
            print ""
            print ("Crop Planted")
            print ""
        else:
            print ""
            print ("Field is full - wheat not planted")
            print ""

def add_animal_in_field(field):
    display_animal_menu()
    choice = get_menu_choice(0,2)
    if choice == 1:
        if field.add_animal(Cow("suresh")):
            print ""
            print ("Animal added")
            print ""
        else:
            print ""
            print ("Field is full - cow not added")
            print ""
    elif choice == 2:
        if field.add_animal(Sheep("suresh")):
            print ""
            print ("Animal added")
            print ""
        else:
            print ""
            print ("Field is full - sheep not added")
            print ""

def manage_field(field):
    print ("This is field managment program")
    print ""
    exit = False
    while not exit:
        display_main_menu()
        option = get_menu_choice(0,7)
        print ""
        if option == 1:
            plant_crop_in_field(field)
        elif option == 2:
            removed_crop = harvest_crop_from_field(field)
            print ("You removed the crop: {0}".format(removed_crop))
        elif option == 3:
            add_animal_in_field(field)
        elif option == 4:
            removed_animal = remove_animal_from_field(field)
            print ("You removed the animal: {0}".format(removed_animal))
        elif option == 5:
            manual_grow(field)
        elif option == 6:
            auto_grow(field, 30)
        elif option == 7:
            print (field.report_content())
            print ""
        elif option == 7:
            exit = True
            print ""
    print ("Thank you for using field managment program")


def main():
    new_field = Field(10, 5)
    manage_field(new_field)
    # new_field.plant_crop(Wheat())
    # new_field.plant_crop(Potato())
    # new_field.add_animal(Sheep("mc"))
    # new_field.add_animal(Cow("bc"))
    # manual_grow(new_field)
    # print new_field.report_content()
    # auto_grow(new_field, 30)
    # print new_field.report_content()
    # print new_field._crops
    # print type(new_field._crops)
    # print new_field._animals
    # print type(new_field._animals)
    # report = new_field.report_content()
    # print report["Crops"]
    # print ""
    # print report["Animals"]
    # print ""
    # report1 = new_field.report_needs()
    # print report1
    # print ""
    # new_field.grow(100,100,100)
    # harvest_crop_from_field(new_field)
    # remove_animal_from_field(new_field)
    # print(new_field._crops)
    # print(new_field._animals)


if __name__ == "__main__":
    main()
