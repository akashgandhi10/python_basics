from Cow_class import *
from Sheep_class import *

def display_menu():
    print ("which animal would you like to create? ")
    print ""
    print ("1. Cow")
    print ("2. Sheep")
    print ""
    print("Please select a option from above menu")


def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option Selected (1-2): "))
            if choice in (1, 2):
                valid_option = True
            else:
                print ("select valid option for animal")
        except ValueError and NameError:
                print ("select valid option for animal")
        return choice

def create_animal():
    display_menu()
    option = select_option()
    if option == 1:
        new_animal = Cow()
    elif option == 2:
        new_animal = Sheep()
    return new_animal

def main():
    new_animal = create_animal()
    manage_animal(new_animal)

if __name__== "__main__":
    main()

    # if choice == 1:
    #
    # print ""
    # print ("This is animal managment program")
    # noexit = True
    # while noexit:
    #     if choice == 1:
    #         option = int(input("Option Selected (1-2): "))
    #         if option == 1:
    #             manual_grow(cow_animal)
    #         elif option == 2:
    #             auto_grow(cow_animal)
    #         elif option == 3:
    #             print cow_animal.report()
    #         elif option == 0:
    #             noexit = False
    #     elif choice == 2:
    #         option = int(input("Option Selected (1-2): "))
    #         if option == 1:
    #             manual_grow(sheep_animal)
    #         elif option == 2:
    #             auto_grow(sheep_animal)
    #         elif option == 3:
    #             print sheep_animal.report()
    #         elif option == 0:
    #             noexit = False
    # print ("Thank you for using animal managment class")
