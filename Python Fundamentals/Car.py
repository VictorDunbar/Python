# Create a class called Car. Create 6 instances of the class Car. (PRICE, SPEED, FUEL, MILEAGE, TAX).//
# Allow the user to specify the following attributes: price, speed, fuel, mileage. //
# If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.//
# In the class have a method called display_all() that returns all the information about the car as a string.//
# In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.//

class Car(object):

    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price < 10000:
            self.tax = 0.12
        else:
            self.tax = 0.15

    def displayAll(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed)
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage)
        print "Tax: " + str(self.tax)




car1 = Car("$2000","35mph","Full","15 mpg")
car2 = Car("$2000","5mph","Not Full","105 mpg")
car3 = Car("$2000","15mph","Kind of Full","95 mpg")
car4 = Car("$2000","25mph", "Full","25 mpg")
car5 = Car("$2000","45mph","Empty","25 mpg")
car6 = Car("$2000000","35mph","Empty","15 mpg")

car1.displayAll()

car2.displayAll()

car3.displayAll()

car4.displayAll()

car5.displayAll()

car6.displayAll()
        
