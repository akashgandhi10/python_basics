from Potato_class import *
from Wheat_class import *

def display_menu():
    print ("which crop would you like to create? ")
    print ""
    print ("1. Potato")
    print ("2. Wheat")
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
                print ("select valid option for crop")
        except ValueError and NameError:
                print ("select valid option for crop")
        return choice

def create_crop():
    display_menu()
    option = select_option()
    if option == 1:
        new_crop = Potato()
    elif option == 2:
        new_crop = Wheat()
    return new_crop

def main():
    new_crop = create_crop()
    manage_crop(new_crop)

if __name__== "__main__":
    main()

    # if choice == 1:
    #
    # print ""
    # print ("This is crop managment program")
    # noexit = True
    # while noexit:
    #     if choice == 1:
    #         option = int(input("Option Selected (1-2): "))
    #         if option == 1:
    #             manual_grow(cow_crop)
    #         elif option == 2:
    #             auto_grow(cow_crop)
    #         elif option == 3:
    #             print cow_crop.report()
    #         elif option == 0:
    #             noexit = False
    #     elif choice == 2:
    #         option = int(input("Option Selected (1-2): "))
    #         if option == 1:
    #             manual_grow(sheep_crop)
    #         elif option == 2:
    #             auto_grow(sheep_crop)
    #         elif option == 3:
    #             print sheep_crop.report()
    #         elif option == 0:
    #             noexit = False
    # print ("Thank you for using crop managment class")
