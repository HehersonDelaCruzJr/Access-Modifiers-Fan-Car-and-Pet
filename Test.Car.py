from Acess import Car

myCar = Car(2023, "Toyota")
myCar.setSpeed(0)

for _ in range(5):
    myCar.accelerate()
    print("Current Car Speed: ", myCar.getSpeed())
    
for _ in range(5):
    myCar.brake()
    print("Current Car Speed: ", myCar.getSpeed())