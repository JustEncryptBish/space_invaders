from shoe import Shoe


cody_shoe = Shoe(5, 'Sketchers', False)

print("The initial size is " + str(cody_shoe.size))

cody_shoe.update_shoe_size(10)

print("The size is now " + str(cody_shoe.size))


