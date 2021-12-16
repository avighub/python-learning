# Parent class 1
class Item():
    def __init__(self,sku):
        self.sku=sku
    def printSku(self):
        print("Item SKU code is : {} ".format(self.sku))

# Parent class 2
class Garment():
    def __init__(self,type):
        self.type=type
    def printGarment(self):
        print("Item is in {} section.".format(self.type))

# Child class
class Shirt(Item,Garment):
    def __init__(self,sku,type,size):
        self.sku=sku
        self.type=type
        self.size=size
item = Shirt("112","Casual","M")
item.printSku()
item.printGarment()

