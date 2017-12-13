# Create and animal class and give it the below attributes and methods. Extend the animal class to two child class, Dog and Dragon//

class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 1
        return self

    def displayHealth(self):
        print self.name, self.health
        return self

animal1 = Animal("Horse")
animal1.walk().walk().walk().run().run().displayHealth()



class Dog(Animal):
    def __init__(self,name):
        super(Dog, self). __init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

# dog1 = Dog("Bucky")
# dog1.walk().walk().walk().run().run().pet().displayHealth()
# dog1.fly().displayHealth()
# confirmed dog has no method fly

class Dragon(Animal):
    def __init__(self):
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        super(Dragon, self).displayHealth();
        print "I am a Dragon"

dragon1 = Dragon()
dragon1.walk().walk().walk().run().run().fly().displayHealth()

class KomodoDragon(Animal):
    def __init__(self):
        self.health = 150

    def fight(self):
        self.health -= 10
        return self

    def displayHealth(self):
        super(KomodoDragon, self).displayHealth();
        print "I am a Komodo Dragon"

KomodoDragon1 = KomodoDragon()

KomodoDragon1.walk().fight().run().run().displayHealth()
# confirmed new animal

KomodoDragon1.pet().displayHealth()
# confirmed Komodo Dragon has no pet method pet()

KomodoDragon1.fly().displayHealth()
# confimed Komodo Dragon has no fly method fly()
