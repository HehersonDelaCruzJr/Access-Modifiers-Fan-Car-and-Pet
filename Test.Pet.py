from Acess import Pet 

myPet = Pet()

name = input("Enter the Pet's name: ")
myPet.setName(name)

animalType = input("Enter the of the Animal: ")
myPet.setAnimalType(animalType)

animalAge = int(input("Enter the Pet's Age: "))
myPet.setAge(animalAge)

print("Pet's Name: ", myPet.getName())
print("Type of Animal: ", myPet.getAnimalType())
print("Pet's Age: ", myPet.getAnimalAge())
