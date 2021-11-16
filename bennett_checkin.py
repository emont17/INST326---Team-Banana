def nike_store():
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

nike_store()
