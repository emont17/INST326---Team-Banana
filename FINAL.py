"""These functions will set up a menu for user to shop at various store in the mall."""
class Mall:
    """Mall class creates mall for user to shop in"""
    def totals(self):
        self.total = 0
        
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
        while choice != self.quit:
            choice = int(input('Which store would you like to shop at? '))
            print()
            if choice == self.nike:
                print('You are now in Nike, shop away!')
                self.nike_store()
                print()
            elif choice == self.dicks:
                print('You are now in Dicks, shop away!')
                self.dicks_store()
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
                quit()
            else:
                print('ERROR INVALID SELECTION')
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


        user_choice = int(input('Welcome to Nike! Which of our departments above would you like to shop in? '))
        print()

        while user_choice != Exit:
            if user_choice == Footwear:
                print(shoe_prices, '\n')
                shoe_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if shoe_choice != 'done':
                    shoe_purchases += shoe_prices[shoe_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(shoe_cart, '\n')
                    print('The amount you purchased on shoes is: $',shoe_purchases, '\n')
                    self.total += shoe_purchases
                    self.nike_store()
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
                    self.total += outerwear_purchases
                    self.nike_store()
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
                    self.total += accessories_purchases
                    self.nike_store()
                accessories_cart.append(accessories_choice)
        
        print('Thanks for shopping at Nike. Your total came out to be: $',self.total, 'Come again!' '\n')
        self.user_choice()
        
    def dicks_store(self):
        """
        A method to allow the shopper to shop in specific departements each store offers.
        Returns:
            
        """
        Apparel = 1
        Sport = 2
        Outdoors = 3
        Exit = 4

        print('1) Apparel')
        print('2) Sport Accessories')
        print('3) Outdoors')
        print('4) Exit')
        print()
    

        Apparel_prices = {'Tank top': 30.99, 'Sweatshirt': 79.99, 'Sweatpants': 59.99, 'T-shirt': 34.25}
        Apparel_purchases = 0
        Apparel_cart = []

        Sport_prices = {'Soccer ball': 24.99, 'Football': 38.25, 'Lacrosse stick': 49.99, 'Basketball': 24.99}
        Sport_purchases = 0
        Sport_cart = []

        Outdoors_prices = {'Kayak': 999.99, 'Fishing rod': 100.50, 'Bike': 530.99, 'Crossbow': 350.00}
        Outdoors_purchases = 0
        Outdoors_cart = []


        user_choice = int(input('Welcome to Dicks! Which of our departments above would you like to shop in? '))
        print()

        while user_choice != Exit:
            if user_choice == Apparel:
                print(Apparel_prices, '\n')
                apparel_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if apparel_choice != 'done':
                    Apparel_purchases += Apparel_prices[apparel_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Apparel_cart, '\n')
                    print('The amount you purchased on apparel is: $',Apparel_purchases, '\n')
                    self.total += Apparel_purchases
                    self.dicks_store()
                Apparel_cart.append(apparel_choice)
            
            
            elif user_choice == Sport:
                print(Sport_prices, '\n')
                sport_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if sport_choice != 'done':
                    Sport_purchases += Sport_prices[sport_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Sport_cart, '\n')
                    print('The amount you purchased on sport accessories is: $',Sport_purchases, '\n')
                    self.total += Sport_purchases
                    self.dicks_store()
                Sport_cart.append(sport_choice)
                
                
            elif user_choice == Outdoors:
                print(Outdoors_prices, '\n')
                outdoors_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if outdoors_choice != 'done':
                    Outdoors_purchases += Outdoors_prices[outdoors_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Outdoors_cart, '\n')
                    print('The amount you purchased on outdoor gear is: $',Outdoors_purchases, '\n')
                    self.total += Outdoors_purchases
                    self.dicks_store()
                Outdoors_cart.append(outdoors_choice)
        
        print('Thanks for shopping at Dicks. Your total came out to be: $',self.total, 'Come again!' '\n')
        self.user_choice()
            

instance = Mall()
instance.totals()
instance.user_choice()
