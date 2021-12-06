"""These functions will set up a menu for user to shop at various store in the mall."""
class Mall:
    """Mall class creates mall for user to shop in"""

    def menu(self):
        """This method shows mall directory to user"""
        self.nike = 1
        self.dicks = 2
        self.bass_Pro_Shops = 3
        self.macys = 4
        self.american_Eagle = 5
        self.quit = 6
        
        print('     MALL DIRECTORY')
        print('1) Nike')
        print('2) Dicks')
        print('3) Bass Pro Shops')
        print('4) Macys')
        print('5) American Eagle')
        print('6) Leave Mall') 
        print()
        
    def user_choice(self):
        """This function allows user to select a store to shop in"""
        self.menu()
        choice = 0
        while choice != "QUIT":
            choice = int(input('Which store would you like to shop at? '))
            print()
            if choice == self.nike:
                print('You are now in Nike, shop away!')
                print()
            elif choice == self.dicks:
                print('You are now in Dicks, shop away!')
                print()
            elif choice == self.bass_Pro_Shops:
                print('You are now in Bass Pro Shops, shop away!')
                print()
            elif choice == self.macys:
                print('You are now in Macys, shop away!')
                print()
            elif choice == self.american_Eagle:
                print('You are now in American Eagle, shop away!')
                print()
            elif choice == self.quit:
                print('You have left the Mall, have a great day!')
                print()
                break
            else:
                print('ERROR: INVALID SELECTION, please try again:')
                print()

    
mall = Mall()
mall.user_choice()

