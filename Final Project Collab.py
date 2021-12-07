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

    def nike():
        """
        A method to allow the shopper to shop in specific departements each store offers.

        Returns:
            shoe_cart (str): the list of shoe products purchased
            shoe_purchases (float): the total cost of shoe products purchased
            outerwear_cart (str): the list of outerwear products purchased
            outerwear_purchases (float): the total cost of outwear products purchased
            accessories_cart (str): the list of accessory products purchased
            accessories_purchases (float): the total cost of accessory products purchased
        """
        Footwear = 1
        Outerwear = 2
        Accessories = 3

        print('1) Footwear')
        print('2) Outerwear')
        print('3) Accessories' '\n')
    

        footwear_prices = {'Running shoes': 100, 'Soccer cleats': 200, 'Skateboard shoes': 75, 'Leisure shoes': 50}
        footwear_products = ['Running shoes', 'Soccer cleats', 'Skateboard shoes', 'Leisure shoes']
        shoe_purchases = 0
        shoe_cart = []

        outerwear_prices = {'Rain jacket': 125.00, 'Ski coat': 200.00, 'Hoodie': 30.00, '1/4 Fleece': 65.00}
        outerwear_products = ['Rain jacket', 'Ski coat', 'Hoodie', '1/4 Fleece']
        outerwear_purchases = 0
        outerwear_cart = []

        accessories_prices = {'Sunglasses': 105.00, 'Beanie': 20.00, 'Socks': 15.00, 'Running watch': 55.00}
        accessories_products = ['Sunglasses', 'Beanie', 'Socks', 'Running watch']
        accessories_purchases = 0
        accessories_cart = []

        total_purchases = 0

        user_choice = 0
        while user_choice != 'EXIT':
            user_choice = int(input('Welcome to Nike! Which of our departments above would you like to shop in? (or EXIT)' '\n'))
            if user_choice == Footwear:
                print(footwear_prices, '\n')
                print(footwear_products, '\n')
                shoe_choice = input('Which items would you like to buy? Or are you done?' '\n')
                if shoe_choice == 'done':
                    nike_store()
                shoe_cart.append(shoe_choice)
                shoe_purchases += footwear_prices[shoe_choice]
            
            
            elif user_choice == Outerwear:
                print(outerwear_products, '\n')
                input('Which items would you like to buy?' '\n')
                if user_choice == 'done':
                    nike_store()
                outerwear_cart.append(user_choice)
                outerwear_cart += outerwear_products[user_choice]
            
            elif user_choice == Accessories:
                print(accessories_products, '\n')
                input('Which items would you like to buy?' '\n')
                if user_choice == 'done':
                    nike_store()
                accessories_cart.append(user_choice)
                accessories_cart += accessories_products[user_choice]
            
            elif user_choice == 'EXIT':
                print('You have left the Nike store. Come again!' '\n')
            
            else:
                print('INVALID CHOICE' '\n')

        
    #def dicks():
    #def bass_pro_shops():
    #def macys():
    #def american_eagle():

    
instance = Mall()
instance.user_choice()
