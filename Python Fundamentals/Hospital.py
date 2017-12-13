# create a program that contains patients. Create a Hospital class

class Patients(object):
    def __init__(self, ID, name, allergies, bed_number):
        self.ID = ID
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number

    def display(self):
        print "ID number:", self.ID
        print "Patient Name:",self.name
        print "Allergies:",self.allergies
        print "Bed Number:",self.bed_number
        return self
        

patient1 = Patients("200","Kanye West","Taylor Swift, fans, smiling","001")  
patient2 = Patients("210","Tiger Woods","Golf clubs, Grass, general golf things","002")
patient3 = Patients("203","Dumbo","Peanuts and Oreos","003")
patient4 = Patients("222","Dez Byrant","Receptions, Touchdowns, the ball","004")


class Hospital(object):
    def __init__(self, hosp_name, max_capacity):
        self.patients = []
        self.hosp_name = hosp_name
        self.max_capacity = max_capacity
        self.capacity = 0

    def admit(self,patient):
        if self.capacity > self.max_capacity:
            return self
        if self.capacity < self. max_capacity:
            self.patients.append(patient)
            self.capacity += 1
            return self

    def discharged(self,discharged):
        self.discharged = discharged
        self.patients.remove(discharged)
        return self

    def display(self):
        for i in self.patients:
            i.display()
            return self

hospital1 = Hospital("OOPs Hospital", 10)
hospital1.admit(patient1).admit(patient2).admit(patient3).admit(patient4).display()
hospital1.admit(patient1).admit(patient2).admit(patient3).discharged(patient4).display()



            

        
        
