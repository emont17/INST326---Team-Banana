class BeautyStore:
     """A store with various inventory items
    
    Attributes:
        inventory (list): the list containing the various products carried in the store
        cart (list): a list containing the items selceted by the shopper
       
    """
    
    inventory = ['Shower gel', 'body lotion', 'deodorant', 'perfume', 'makeup', 'hand sanitizer', 'hair dye']
    


    def add(self):
        """This function allows the shopper to add items to their cart
    
    Raises:
        ValueError: out of bound exception
       
    """
        print("Welcome to Beauty Store!!!!!!!!!!\nBelow are the products you will find here:")
        for i in range(0, len(self.inventory)):
            print("{id} {item}".format(id=i, item=self.inventory[i]))
        choice = int(input("Select an Item to add to the cart: "))
        self.cart.append(self.inventory[choice])
        print('Your shopping cart is: {}'.format(self.cart))

    def __init__(self):
        self.cart = []
        self.total = 0

        while True:
            self.add()
            print()


if __name__ == '__main__':
    beauty_store = BeautyStore()
