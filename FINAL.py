import random

"""The Mall class will allow a user to shop at various stores"""
class Mall:
    """Mall class creates mall for user to shop in"""
    def totals(self):
        """This method creates totals for each store"""
        self.nike_total = 0
        self.dicks_total = 0
        self.bass_pro_total = 0
        self.macys_total = 0
        self.ae_total = 0
        self.beauty_total = 0
        self.fashion_total = 0
        
    def discounts(self):
	"""
	A method that allows discounts to be applied to cart depending on products purchased/amount spent.
	"""
        self.nike_discount = random.randint(5, 25)
        self.discount_amount_nike = self.nike_discount / 100
        
        self.dicks_discount = random.randint(10,30)
        self.discount_amount_dicks = self.dicks_discount / 100
        
        self.bass_pro_discount = random.randint(10,15)
        self.discount_amount_bass_pro = self.bass_pro_discount / 100
        
        self.macys_discount = random.randint(20,50)
        self.discount_amount_macys = self.macys_discount / 100
        
        self.ae_discount = random.randint(5,10)
        self.discount_amount_ae = self.ae_discount / 100

        self.beauty_discount = random.randint(10, 20)
        self.discount_amount_beauty = self.beauty_discount / 100

        self.fashion_discount = random.randint(7, 23)
        self.discount_amount_fashion = self.fashion_discount / 100
        
    def menu(self):
        """This method shows mall directory to user"""
        self.nike = 1
        self.dicks = 2
        self.bass_Pro_Shops = 3
        self.macys = 4
        self.american_Eagle = 5
        self.beauty = 6
        self.fashion_Nova = 7
        self.quit = 8
        
        print('     MALL DIRECTORY')
        print('1) Nike')
        print('2) Dicks')
        print('3) Bass Pro Shops')
        print('4) Macys')
        print('5) American Eagle')
        print('6) Beauty Store')
        print('7) Fashionnova')
        print('8) Leave Mall') 
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
            elif choice == self.beauty:
                print('You are now in the Beauty Store, shop away!')
                self.beauty_store()
                print()
            elif choice == self.fashion_Nova:
                print('You are now in FashionNova, shop away!')
                self.fashionnova_store()
                print()
            elif choice == self.quit:
                print('You have left the Mall, have a great day!')
                print()
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
                print()
                if shoe_choice == "Soccer cleats":
                    print("Congratulations! You have just recieved a discount of", self.nike_discount,"%, it will be applied at checkout.")
                    print()
                if shoe_choice != 'done':
                    shoe_purchases += shoe_prices[shoe_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(shoe_cart, '\n')
                    print('The amount you purchased on shoes is: $',round(shoe_purchases, 2),'\n''Your', self.nike_discount,'% discount will be applied at checkout.' '\n')
                    self.nike_total += shoe_purchases
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
                    print('The amount you purchased on outerwear is: $',round(outerwear_purchases, 2), '\n')
                    self.nike_total += outerwear_purchases
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
                    print('The amount you purchased on accessories is: $',round(accessories_purchases, 2), '\n')
                    self.nike_total += accessories_purchases
                    self.nike_store()
                accessories_cart.append(accessories_choice)
            
        self.discount_total_nike = self.discount_amount_nike * self.nike_total
        self.final_price_nike = self.nike_total - self.discount_total_nike  
         
        print('Thanks for shopping at Nike. Your total came out to be: $',round(self.final_price_nike, 2))
        print('You saved a total of: $',round(self.discount_total_nike, 2),'\n' 'Come again!' '\n')
        self.user_choice()
        
    def dicks_store(self):
        """
        A method to allow the shopper to shop in specific departements each store offers.
        
        Returns:
            Apparel_cart (str): the list of apparel products purchased
            Apparel_purchases (float): the total cost of apparel products purchased
            Sport_cart (str): the list of sport products purchased
            Sport_purchases (float): the total cost of sport products purchased
            Outdoor_cart (str): the list of outdoor products purchased
            Outdoor_purchases (float): the total cost of outdoor products purchased
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
                    print('The amount you purchased on apparel is: $',round(Apparel_purchases, 2), '\n')
                    self.dicks_total += Apparel_purchases
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
                    print('The amount you purchased on sport accessories is: $',round(Sport_purchases, 2), '\n')
                    self.dicks_total += Sport_purchases
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
                    print('The amount you purchased on outdoor gear is: $',round(Outdoors_purchases, 2), '\n')
                    self.dicks_total += Outdoors_purchases
                    self.dicks_store()
                Outdoors_cart.append(outdoors_choice)
        
        if self.dicks_total >= 100:
            self.discount_total_dicks = self.discount_amount__dicks * self.dicks_total
            self.final_price_dicks = self.dicks_total - self.discount_total_dicks 
        
        print('Thanks for shopping at Dicks. Your total came out to be: $',round(self.dicks_total, 2))
        print('You have spent over $100 at Dicks, you have been rewarded a discount of', self.dicks_discount,'%!')
        print('You saved a total of: $', round(self.discount_total_dicks, 2))
        print('Your new total is now: $', round(self.final_price_dicks, 2))
        print("Come again!")
        print()
        self.user_choice()
        
    def bps_store(self):
        """
        A method to allow the shopper to shop in specific departements each store offers.
        
        Returns:
            Fishing_cart (str): the list of fishing products purchased
            Fishing_purchases (float): the total cost of fishing products purchased
            Hunting_cart (str): the list of hunting products purchased
            Hunting_purchases (float): the total cost of hunting products purchased
            Camping_cart (str): the list of camping products purchased
            Camping_purchases (float): the total cost of camping products purchased 
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
                    print('The amount you purchased on fishing gear is: $',round(Fishing_purchases, 2), '\n')
                    self.bass_pro_total += Fishing_purchases
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
                    print('The amount you purchased on hunting gear is: $',round(Hunting_purchases, 2), '\n')
                    self.bass_pro_total += Hunting_purchases
                    self.bps_store()
                Hunting_cart.append(hunting_choice)
                
            elif user_choice == Camping:
                print(Camping_prices, '\n')
                camping_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                print()
                if camping_choice == "Tent":
                    print("Congratulations! You have just recieved a discount of ", self.bass_pro_discount,"%, it will be applied at checkout.")
                    print()
                if camping_choice != 'done':
                    Camping_purchases += Camping_prices[camping_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Camping_cart, '\n')
                    print('The amount you purchased on camping gear is: $',round(Camping_purchases, 2))
                    print('Your', self.bass_pro_discount,'% will be applied at checkout.')
                    print()
                    self.bass_pro_total += Camping_purchases
                    self.bps_store()
                Camping_cart.append(camping_choice)
        
        self.discount_total_bass_pro = self.discount_amount_bass_pro * self.bass_pro_total
        self.final_price_bass_pro = self.bass_pro_total - self.discount_total_bass_pro
         
        print('Thanks for shopping at Bass Pro Shops. Your total came out to be: $',round(self.final_price_bass_pro, 2))
        print('You saved a total of: $',round(self.discount_total_bass_pro, 2),'\n' 'Come again!' '\n')
        self.user_choice()

    def macys_store(self):
        """
        A method to allow the shopper to shop in specific departements each store offers.
        
        Returns:
            Footwear_cart (str): the list of footwear products purchased
            Footwear_purchases (float): the total cost of footwear products purchased
            Designer_cart (str): the list of designer products purchased
            Designer_purchases (float): the total cost of designer products purchased
            Jewelry_cart (str): the list of jewelry products purchased
            Jewelry_purchases (float): the total cost of jewelry products purchased 
            
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
                    print('The amount you purchased on footwear is: $',round(Footwear_purchases, 2), '\n')
                    self.macys_total += Footwear_purchases
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
                    print('The amount you purchased on designer accessories is: $',round(Designer_purchases, 2))
                    print()
                    self.macys_total += Designer_purchases
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
                    print('The amount you purchased on jewelry is: $',round(Jewelry_purchases, 2), '\n')
                    self.macys_total += Jewelry_purchases
                    self.macys_store()
                Jewelry_cart.append(jewelry_choice)
                
        if self.macys_total >= 200:
            self.discount_total_macys = self.discount_amount_macys * self.macys_total
            self.final_price_macys = self.macys_total - self.discount_total_macys 
        
        print('Thanks for shopping at Macys. Your total came out to be: $',round(self.macys_total, 2))
        print('You have spent over $200 at Macys, you have been rewarded a discount of', self.macys_discount,'%!')
        print('You saved a total of: $', round(self.discount_total_macys, 2))
        print('Your new total is now: $', round(self.final_price_macys, 2))
        print('Come again!')
        print()
        self.user_choice()
        
    def ae_store(self):
        """
        A method to allow the shopper to shop in specific departements each store offers.
        
        Returns:
            Tops_cart (str): the list of tops products purchased
            Tops_purchases (float): the total cost of tops products purchased
            Bottoms_cart (str): the list of bottoms products purchased
            Bottoms_purchases (float): the total cost of bottoms products purchased
            Accessories_cart (str): the list of accessory products purchased
            Accessories_purchases (float): the total cost of accessory products purchased 
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
                    print('The amount you purchased on tops is: $',round(Tops_purchases, 2), '\n')
                    self.ae_total += Tops_purchases
                    self.ae_store()
                Tops_cart.append(tops_choice)
            
            elif user_choice == Bottoms:
                print(Bottoms_prices, '\n')
                bottoms_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                print()
                if bottoms_choice == "Jeans":
                    print("Congratulations! You have just recieved a discount of ", self.ae_discount,"%, it will be applied at checkout.")
                    print()
                if bottoms_choice != 'done':
                    Bottoms_purchases += Bottoms_prices[bottoms_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Bottoms_cart, '\n')
                    print('The amount you purchased on bottoms is: $',round(Bottoms_purchases, 2))
                    print('Your',self.ae_discount,'% will be applied at checkout.')
                    self.ae_total += Bottoms_purchases
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
                    print('The amount you purchased on accessories is: $',round(Accessories_purchases, 2),'\n')
                    self.ae_total += Accessories_purchases
                    self.ae_store()
                Accessories_cart.append(accessories_choice)
        
        self.discount_total_ae = self.discount_amount_ae * self.ae_total
        self.final_price_ae = self.ae_total - self.discount_total_ae
         
        print('Thanks for shopping at American Eagle. Your total came out to be: $',round(self.final_price_ae, 2))
        print('You saved a total of: $',round(self.discount_total_ae, 2))
        print('Come again!')
        print()
        self.user_choice()

    def beauty_store(self):
        """
        A method to allow the shopper to shop in specific departements each store offers.
        
        Returns:
            Makeup_cart (str): the list of makeup products purchased
            Makeup_purchases (float): the total cost of makeup products purchased
            Fragrance_cart (str): the list of fragrance products purchased
            Fragrance_purchases (float): the total cost of fragrance products purchased
            Skincare_cart (str): the list of skincare products purchased
            Skincare_purchases (float): the total cost of skincare products purchased 
        """
        Makeup = 1
        Fragrance = 2
        Skincare = 3
        Exit = 4

        print('1) Makeup')
        print('2) Fragrance')
        print('3) Skincare')
        print('4) Exit')
        print()

        Makeup_prices = {'Foundation': 30.00, 'Concealer': 19.99, 'Powder': 7.99, 'Primer': 3.99}
        Makeup_purchases = 0
        Makeup_cart = []

        Fragrance_prices = {'oco channel noir': 135.00, 'tom ford soeil blanc': 365.00, 'tiffany & co Love': 118.00, 'lancome idol': 150.00}
        Fragrance_purchases = 0
        Fragrance_cart = []

        Skincare_prices = {'body exfoliator': 22.50, 'deodorant': 9.99, 'face cleanser': 14.99, 'face toner': 12.99}
        Skincare_purchases = 0
        Skincare_cart = []


        user_choice = int(input('Welcome to the Beauty Store! Which of our departments above would you like to shop in? '))
        print()

        while user_choice != Exit:
            if user_choice == Makeup:
                print(Makeup_prices, '\n')
                makeup_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if makeup_choice != 'done':
                    Makeup_purchases += Makeup_prices[makeup_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Makeup_cart, '\n')
                    print('The amount you purchased on makeup is: $',round(Makeup_purchases, 2), '\n')
                    self.beauty_total += Makeup_purchases
                    self.beauty_store()
                Makeup_cart.append(makeup_choice)
            
            elif user_choice == Fragrance:
                print(Fragrance_prices, '\n')
                fragrance_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                print()
                if fragrance_choice == "lancome idol":
                    print("Congratulations! You have just recieved a discount of ", self.beauty_discount,"%, it will be applied at checkout.")
                    print()
                if fragrance_choice != 'done':
                    Fragrance_purchases += Fragrance_prices[fragrance_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Fragrance_cart, '\n')
                    print('The amount you purchased on fragrance is: $',round(Fragrance_purchases, 2))
                    print('Your',self.beauty_discount,'% will be applied at checkout.')
                    self.beauty_total += Fragrance_purchases
                    self.beauty_store()
                Fragrance_cart.append(fragrance_choice)
                
            elif user_choice == Skincare:
                print(Skincare_prices, '\n')
                skincare_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if skincare_choice != 'done':
                    Skincare_purchases += Skincare_prices[skincare_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Skincare_cart, '\n')
                    print('The amount you purchased on skincare is: $',round(Skincare_purchases, 2),'\n')
                    self.beauty_total += Skincare_purchases
                    self.beauty_store()
                Skincare_cart.append(skincare_choice)
        
        self.discount_total_beauty = self.discount_amount_beauty * self.beauty_total
        self.final_price_beauty = self.beauty_total - self.discount_total_beauty
         
        print('Thanks for shopping at the Beauty Store. Your total came out to be: $',round(self.final_price_beauty, 2))
        print('You saved a total of: $',round(self.discount_total_beauty, 2))
        print('Come again!')
        print()
        self.user_choice()

    def fashionnova_store(self):
        """
        A method to allow the shopper to shop in specific departements each store offers.
        
        Returns:
            Dresses_cart (str): the list of dresses purchased
            Dresses_purchases (float): the total cost of dresses purchased
            Sweaters_cart (str): the list of sweaters purchased
            Sweaters_purchases (float): the total cost of sweaters purchased
            Coats_cart (str): the list of coats purchased
            Coats_purchases (float): the total cost of coats purchased 
            
        """
        Dresses = 1
        Sweaters = 2
        Coats = 3
        Exit = 4

        print('1) Dresses')
        print('2) Sweaters')
        print('3) Coats')
        print('4) Exit')
        print()

        Dresses_prices = {'Sundress': 35.00, 'Midi dress': 19.99, 'Maxi dress': 17.99, 'Mini dress': 13.49}
        Dresses_purchases = 0
        Dresses_cart = []

        Sweaters_prices = {'Cozy sweater': 54.00, 'Long sweater dress': 39.00, 'Christmas sweater': 30.00, 'Crop sweater': 15.00}
        Sweaters_purchases = 0
        Sweaters_cart = []

        Coats_prices = {'Trench coat': 49.50, 'Faux fur coat': 109.99, 'Blazer': 30.99, 'Double breasted coat': 120.49}
        Coats_purchases = 0
        Coats_cart = []


        user_choice = int(input('Welcome to FashionNova! Which of our departments above would you like to shop in? '))
        print()

        while user_choice != Exit:
            if user_choice == Dresses:
                print(Dresses_prices, '\n')
                dresses_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if dresses_choice != 'done':
                    Dresses_purchases += Dresses_prices[dresses_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Dresses_cart, '\n')
                    print('The amount you purchased on dresses is: $',round(Dresses_purchases, 2), '\n')
                    self.fashion_total += Dresses_purchases
                    self.fashionnova_store()
                Dresses_cart.append(dresses_choice)
            
            elif user_choice == Sweaters:
                print(Sweaters_prices, '\n')
                sweaters_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if sweaters_choice != 'done':
                    Sweaters_purchases += Sweaters_prices[sweaters_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Sweaters_cart, '\n')
                    print('The amount you purchased on sweaters is: $',round(Sweaters_purchases, 2))
                    print()
                    self.fashion_total += Sweaters_purchases
                    self.fashionnova_store()
                Sweaters_cart.append(sweaters_choice)
                
            elif user_choice == Coats:
                print(Coats_prices, '\n')
                coats_choice = input('Which items would you like to buy? Or are you "done"?' '\n')
                if coats_choice != 'done':
                    Coats_purchases += Coats_prices[coats_choice]
                else:
                    print('Your cart consists of the following items:' '\n')
                    print(Coats_cart, '\n')
                    print('The amount you purchased on coats is: $',round(Coats_purchases, 2), '\n')
                    self.fashion_total += Coats_purchases
                    self.fashionnova_store()
                Coats_cart.append(coats_choice)
                
        if self.fashion_total >= 150:
            self.discount_total_fashion = self.discount_amount_fashion * self.fashion_total
            self.final_price_fashion = self.fashion_total - self.discount_total_fashion 
        
        print('Thanks for shopping at FashionNova. Your total came out to be: $',round(self.fashion_total, 2))
        print('You have spent over $150 at FashionNova, you have been rewarded a discount of', self.fashion_discount,'%!')
        print('You saved a total of: $', round(self.discount_total_fashion, 2))
        print('Your new total is now: $', round(self.final_price_fashion, 2))
        print('Come again!')
        print()
        self.user_choice()



    
instance = Mall()
instance.totals()
instance.discounts()
instance.user_choice()
