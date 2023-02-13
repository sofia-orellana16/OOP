import random

# name of class will always start with a uppercase
class Insect:
   

    def __init__(self, n, w , l):
        self.name = n
        self.wings = w
        self.legs = l
        self.flight = 0
# self assures that it is only being used an not accesed

 

    def get_fly(self):
       self.flight = random.randint(1, 10)
  



    def get_flighttime(self):
            return self.flight
    
    def get_name(self):
         return self.name
#accesor methods: methods that return an