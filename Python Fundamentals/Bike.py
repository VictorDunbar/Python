


class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self
    
    def ride(self):
        self.miles += 10
        print "Riding"
        return self

    def reverse(self):
        if self.miles >= 5:
            self.miles -= 5
        print "Reversing"
        return self


BMX = Bike("$150","30 mph")
MountainBike = Bike("$220","35 mph")
RoadBike = Bike("$450","45 mph")


BMX.ride()
BMX.ride()
BMX.ride()
BMX.reverse()
BMX.displayInfo()

MountainBike.ride()
MountainBike.ride()
MountainBike.reverse()
MountainBike.reverse()
MountainBike.displayInfo()

RoadBike.reverse()
RoadBike.reverse()
RoadBike.reverse()
RoadBike.displayInfo()


        



        
        