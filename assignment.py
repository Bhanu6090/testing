class vehical :
    def __init__(self,name_of_vehicle,max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed 
        self.average_of_vehicle = average_of_vehicle
class car(vehical) :
    def seating_capacity(self,capacity):
        self.capacity = capacity
        return [ self.name_of_vehicle , self.capacity]
p1 = vehical("shine", 120, 50)
c1 = car("shine ",120,3)
print(c1.seating_capacity(5))

    
    