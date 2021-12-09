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
                self.nike_store()
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

    def nike_store(self):
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
        Exit = 4

        print('1) Footwear')
        print('2) Outerwear')
        print('3) Accessories')
        print('4) Exit')
        print()
    

        shoe_prices = {'Running shoes': 99.99, 'Soccer cleats': 199.99, 'Skateboard shoes': 74.99, 'Leisure shoes': 49.99}
        shoe_purchases = 0
        shoe_cart = []

        outerwear_prices = {'Rain jacket': 124.99, 'Ski coat': 199.99, 'Hoodie': 49.99, '1/4 Fleece': 64.99}
        outerwear_purchases = 0
        outerwear_cart = []

        accessories_prices = {'Sunglasses': 104.99, 'Beanie': 19.99, 'Socks': 14.99, 'Running watch': 54.99}
        accessories_purchases = 0
        accessories_cart = []

        total = 0

        user_choice = int(input('Welcome to Nike! Which of our departments above would you like to shop in? '))
        print()

        while user_choice != Exit:
            """ if user_choice == Footwear:
                print(shoe_prices, '\n')
                shoe_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                shoe_purchases += shoe_prices[shoe_choice]
                if shoe_choice == 'done':
                    print('Your cart consists of the following items below:' '\n')
                    print(shoe_cart, '\n')
                    print('The amount you purchased on shoes is: $',shoe_purchases, '\n')
                    self.nike_store()
                shoe_cart.append(shoe_choice)
                #shoe_purchases += shoe_prices[shoe_choice]"""

            if user_choice == Footwear:
                print(shoe_prices, '\n')
                shoe_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if shoe_choice != 'done':
                    shoe_purchases += shoe_prices[shoe_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(shoe_cart, '\n')
                    print('The amount you purchased on shoes is: $',shoe_purchases, '\n')
                    self.nike_store()
                    total += shoe_purchases
                shoe_cart.append(shoe_choice)
            
            
            elif user_choice == Outerwear:
                print(outerwear_prices, '\n')
                outerwear_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if outerwear_choice != 'done':
                    outerwear_purchases += outerwear_prices[outerwear_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(outerwear_cart, '\n')
                    print('The amount you purchased on outerwear is: $',outerwear_purchases, '\n')
                    self.nike_store()
                    total += outerwear_purchases
                outerwear_cart.append(outerwear_choice)
                
                
            elif user_choice == Accessories:
                print(accessories_prices, '\n')
                accessories_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if accessories_choice != 'done':
                    accessories_purchases += accessories_prices[accessories_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(accessories_cart, '\n')
                    print('The amount you purchased on accessories is: $',accessories_purchases, '\n')
                    self.nike_store()
                    total += accessories_purchases
                accessories_cart.append(accessories_choice)
                
    
        
        
        print('Thanks for shopping at Nike. Your total came out to be: $',total, 'Come again!' '\n')
        self.user_choice()
            

instance = Mall()
instance.user_choice()
