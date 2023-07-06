# Acess Modifiers

# Class Fan
Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed.
1. A private int data field named speed that specifies the speed of the fan.
2. A private bool data field named on that specifies whether the fan is on (the default is False).
3. A private float data field named radius that specifies the radius of the fan.
4. A private string data field named color that specifies the color of the fan.
5. The accessor(getters)  and mutator(setters)  methods for all four data fields.
6. A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).
Write a test program named TestFan that creates two Fan objects. For the first object, assign the maximum speed, radius 10, color yellow, and turn it on. Assign medium speed, radius 5, color blue, and turn it off for the second object. Display each object’s speed, radius, color, and on properties.

# Class Car
1. Write a class named Car that has the following data attributes:
• _ _year_model (for the car’s year model)
• _ _make (for the make of the car)
• _ _speed (for the car’s current speed)

2. The Car class should have an _ _init_ _ method that accepts the car’s year model and make as arguments. These values should be assigned to the object’s _ _year_model and _ _make data attributes. It should also assign 0 to the _ _speed data attribute.

3. The class should also have the following methods:
• accelerate()
The accelerate method should add 5 to the speed data attribute each time it is called.
• brake()
The brake method should subtract 5 from the speed data attribute each time it is called.
• get_speed()
The get_speed method should return the current speed.

4. Next, design a program that creates a Car object then calls the accelerate method five times. After each call to the accelerate method, get the current speed of the car and display it. Then call the brake method five times. After each call to the brake method, get the current speed of the car and display it.
