from Acess import Fan

#creates class for test

class TestFan:
    def __init__(self):
        self.fan1 = Fan(Fan.FAST, 10, 'yellow', True)
        self.fan2 = Fan(Fan.MEDIUM, 5, 'blue', False)
        
    def displayFanProperties(self, fan):
        print("Fan Speed: ", fan.getSpeed())
        print("Fan Radius: ", fan.getRadius())
        print("Fan Color: ", fan.getColor())
        print("On: ", fan.is_O n())
        print()
    
    def run(self):
        print("Fan 1: ")
        self.displayFanProperties(self.fan1)
        
        print("Fan 2: ")
        self.displayFanProperties(self.fan2)
        
test_fan = TestFan()
test_fan.run()