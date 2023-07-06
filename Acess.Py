#Creating Class for Fan

class Fan:
    #creating Constants
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    
    def __init__(self, speed=1, radius=5, color='blue', on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on
        
    def getSpeed(self):
        return self.__speed
    
    def setSpeed(self, speed):
        self.__speed = speed
        
    def getRadius(self):
        return self.__radius
    
    def setRadius(self, radius):
        self.__radius = radius
        
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color
    
    def is_On(self):
        return self.__on
    
    def setOn(self, on):
        self.__on = on
        
    
        
# Creating Class for Car

class Car:
    def __init__(self, yearModel, make):
        self.__yearModel = yearModel
        self.__make = make
        self.__speed = 0
        
    def accelerate(self):
        self.__speed += 5
        
    def brale(self):
        self.__speed -= 5
        
    def getSpeed(self):
        return self.__speed
    
    def setSpeed(self, speedLevel):
        if speedLevel >= 1 and speedLevel <= 7:
            self.speed = speedLevel
            
    
        