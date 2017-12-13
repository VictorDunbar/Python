# Product assignment
# The owner of a store wants a program to track products. Create a product class to fill the following requirements.


class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"

    def sell(self):
        self.status = "Sold"
        return self

    def addTax(self,tax):
        self.tax = round((self.price * tax),2)
        return self

    def Return(self,reason):
        if reason == reason1:
            self.status = "Defective"
            self.price = 0
        elif reason == reason2:
            self.status = "For Sale"
        elif reason == reason3:
            self.status = "Used"
            self.price = round((self.price * .8),2)
        return self

    def displayInfo(self):
        print "Item name: " + str(self.item_name)
        print "Brand: " + str(self.brand)
        print "Price: $" + str(self.price)
        print "Weight: " + str(self.weight) + "oz."
        print "Status: " + str(self.status)
        print "Cost: $" + str(self.cost)
        
        

        

reason1 = "defective"
reason2 = "in_box"
reason3 = "open_box"
Headphones = Product(199.99,"Headphones",16,"Beats by Dre",159.99)
Macbook = Product(899.99,"Macbook",112,"Apple",719.99)
Mouse = Product(39.99,"Mouse",3,"Apple",0.00)

Headphones.addTax(1.09).Return(reason2).displayInfo()
Macbook.addTax(1.09).Return(reason2).displayInfo()
Mouse.addTax(1.09).Return(reason1).displayInfo()
