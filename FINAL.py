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
                self.bps_store()
                print()
            elif choice == self.macys:
                print('You are now in Macys, shop away!')
                self.macys_store()
                print()
            elif choice == self.american_Eagle:
                print('You are now in American Eagle, shop away!')
                self.ae_store()
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
        
    def bps_store(self):
        """
        A method to allow the shopper to shop in specific departements each store offers.
        Returns:
            
        """
        Fishing = 1
        Hunting = 2
        Camping = 3
        Exit = 4

        print('1) Fishing')
        print('2) Hunting')
        print('3) Camping')
        print('4) Exit')
        print()

        Fishing_prices = {'Fly rod': 121.99, 'Senkos': 6.50, 'Dozen flies': 14.99, 'Net': 24.15}
        Fishing_purchases = 0
        Fishing_cart = []

        Hunting_prices = {'Duck blind': 429.99, 'Tree stand': 139.25, 'Trail cam': 79.99, 'Turkey call': 21.99}
        Hunting_purchases = 0
        Hunting_cart = []

        Camping_prices = {'Tent': 130.25, 'Sleeping bag': 69.95, 'Portable stove': 19.99, 'Deluxe tent': 500.00}
        Camping_purchases = 0
        Camping_cart = []


        user_choice = int(input('Welcome to Bass Pro Shops! Which of our departments above would you like to shop in? '))
        print()

        while user_choice != Exit:
            if user_choice == Fishing:
                print(Fishing_prices, '\n')
                fishing_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if fishing_choice != 'done':
                    Fishing_purchases += Fishing_prices[fishing_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Fishing_cart, '\n')
                    print('The amount you purchased on fishing gear is: $',Fishing_purchases, '\n')
                    self.total += Fishing_purchases
                    self.bps_store()
                Fishing_cart.append(fishing_choice)
            
            elif user_choice == Hunting:
                print(Hunting_prices, '\n')
                hunting_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if hunting_choice != 'done':
                    Hunting_purchases += Hunting_prices[hunting_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Hunting_cart, '\n')
                    print('The amount you purchased on hunting gear is: $',Hunting_purchases, '\n')
                    self.total += Hunting_purchases
                    self.dicks_store()
                Hunting_cart.append(hunting_choice)
                
            elif user_choice == Camping:
                print(Camping_prices, '\n')
                camping_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if camping_choice != 'done':
                    Camping_purchases += Camping_prices[camping_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Camping_cart, '\n')
                    print('The amount you purchased on camping gear is: $',Camping_purchases, '\n')
                    self.total += Camping_purchases
                    self.bps_store()
                Camping_cart.append(camping_choice)
        
        print('Thanks for shopping at Bass Pro Shops. Your total came out to be: $',self.total, 'Come again!' '\n')
        self.user_choice()

    def macys_store(self):
        """
        A method to allow the shopper to shop in specific departements each store offers.
        Returns:
            
        """
        Footwear = 1
        Designer = 2
        Jewelry = 3
        Exit = 4

        print('1) Footwear')
        print('2) Designer')
        print('3) Jewelry')
        print('4) Exit')
        print()

        Footwear_prices = {'Dress shoes': 79.50, 'Winter boots': 95.00, 'Ugg slippers':99.99, 'Sandals': 29.75}
        Footwear_purchases = 0
        Footwear_cart = []

        Designer_prices = {'Polo belt': 70.00, 'Michael Kors purse': 198.00, 'CK sweater': 89.50, 'Coach glasses': 173.00}
        Designer_purchases = 0
        Designer_cart = []

        Jewelry_prices = {'Fitbit': 129.95, 'Earrings': 19.95, 'Necklace': 39.99, 'Luxury watch': 1500.00}
        Jewelry_purchases = 0
        Jewelry_cart = []


        user_choice = int(input('Welcome to Macys! Which of our departments above would you like to shop in? '))
        print()

        while user_choice != Exit:
            if user_choice == Footwear:
                print(Footwear_prices, '\n')
                footwear_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if footwear_choice != 'done':
                    Footwear_purchases += Footwear_prices[footwear_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Footwear_cart, '\n')
                    print('The amount you purchased on footwear is: $',Footwear_purchases, '\n')
                    self.total += Footwear_purchases
                    self.macys_store()
                Footwear_cart.append(footwear_choice)
            
            elif user_choice == Designer:
                print(Designer_prices, '\n')
                designer_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if designer_choice != 'done':
                    Designer_purchases += Designer_prices[designer_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Designer_cart, '\n')
                    print('The amount you purchased on designer accessories is: $',Designer_purchases, '\n')
                    self.total += Designer_purchases
                    self.macys_store()
                Designer_cart.append(designer_choice)
                
            elif user_choice == Jewelry:
                print(Jewelry_prices, '\n')
                jewelry_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if jewelry_choice != 'done':
                    Jewelry_purchases += Jewelry_prices[jewelry_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Jewelry_cart, '\n')
                    print('The amount you purchased on jewelry is: $',Jewelry_purchases, '\n')
                    self.total += Jewelry_purchases
                    self.macys_store()
                Jewelry_cart.append(jewelry_choice)
        
        print('Thanks for shopping at Macys. Your total came out to be: $',self.total, 'Come again!' '\n')
        self.user_choice()
        
    def ae_store(self):
        """
        A method to allow the shopper to shop in specific departements each store offers.
        Returns:
            
        """
        Tops = 1
        Bottoms = 2
        Accessories = 3
        Exit = 4

        print('1) Tops')
        print('2) Bottoms')
        print('3) Accessories')
        print('4) Exit')
        print()

        Tops_prices = {'Sweatshirt': 37.50, 'Flannel': 59.95, 'T shirt': 22.99, 'Denim jacket': 49.75}
        Tops_purchases = 0
        Tops_cart = []

        Bottoms_prices = {'Jeans': 49.95, 'Chinos': 39.95, 'Sweatpants': 34.50, 'Camo joggers': 59.95}
        Bottoms_purchases = 0
        Bottoms_cart = []

        Accessories_prices = {'Wallet': 19.95, 'Socks': 15.95, 'Gloves': 11.96, 'Scarf': 14.96}
        Accessories_purchases = 0
        Accessories_cart = []


        user_choice = int(input('Welcome to American Eagle! Which of our departments above would you like to shop in? '))
        print()

        while user_choice != Exit:
            if user_choice == Tops:
                print(Tops_prices, '\n')
                tops_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if tops_choice != 'done':
                    Tops_purchases += Tops_prices[tops_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Tops_cart, '\n')
                    print('The amount you purchased on tops is: $',Tops_purchases, '\n')
                    self.total += Tops_purchases
                    self.ae_store()
                Tops_cart.append(tops_choice)
            
            elif user_choice == Bottoms:
                print(Bottoms_prices, '\n')
                bottoms_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if bottoms_choice != 'done':
                    Bottoms_purchases += Bottoms_prices[bottoms_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Bottoms_cart, '\n')
                    print('The amount you purchased on bottoms is: $',Bottoms_purchases, '\n')
                    self.total += Bottoms_purchases
                    self.ae_store()
                Bottoms_cart.append(bottoms_choice)
                
            elif user_choice == Accessories:
                print(Accessories_prices, '\n')
                accessories_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if accessories_choice != 'done':
                    Accessories_purchases += Accessories_prices[accessories_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Accessories_cart, '\n')
                    print('The amount you purchased on accessories is: $',Accessories_purchases, '\n')
                    self.total += Accessories_purchases
                    self.ae_store()
                Accessories_cart.append(accessories_choice)
        
        print('Thanks for shopping at American Eagle. Your total came out to be: $',self.total, 'Come again!' '\n')
        self.user_choice()        
            

instance = Mall()
instance.totals()
instance.user_choice()
