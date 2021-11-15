###These functions will set up a menu for user to shop at various store in the mall."""

Nike = 1
Dicks = 2
Bass_Pro_Shops = 3
Macys = 4
American_Eagle = 5
QUIT = 6

def user():
    """This function allows user to select a store to shop in"""
    choice = 0
    while choice != QUIT:
        display()
        choice = int(input('Which store would you like to shop at first? '))
        print()
        if choice == Nike:
            print('You are now in Nike, shop away!')
            print()
        elif choice == Dicks:
            print('You are now in Dicks, shop away!')
            print()
        elif choice == Bass_Pro_Shops:
            print('You are now in Bass Pro Shops, shop away!')
            print()
        elif choice == Macys:
            print('You are now in Macys, shop away!')
            print()
        elif choice == American_Eagle:
            print('You are now in American Eagle, shop away!')
            print()
        elif choice == QUIT:
            print('You have left the Mall, have a great day!')
            print()
        else:
            print('ERROR: INVALID SELECTION')
            print()

def display():
    """This function displays stores oepn for shopping at the mall"""
    print('     MALL DIRECTORY')
    print('1) Nike')
    print('2) Dicks')
    print('3) Bass Pro Shops')
    print('4) Macys')
    print('5) American Eagle')
    print('6) Leave Mall')
    print()
    
    
user()
