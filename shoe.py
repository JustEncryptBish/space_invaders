class Shoe():
    """Holds Shoes"""

    def __init__(self, size, brand, has_fake_toe):
        self.size = size
        self.brand = brand
        self.has_fake_toe = has_fake_toe


    def update_shoe_size(self, size):
        self.size = size
        print('Shoe size changed!')