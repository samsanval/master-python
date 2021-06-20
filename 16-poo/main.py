from Car import Car
import Classes

car = Car('Lamborghini', 'Yellow', 'Diavolo', 250, 400, 2)
print(car.get_speed(), car.color)
car.speed_up()
print(car.get_speed())
print(car.get_info())

# Detect type
if type(car) == Car:
    print("It's a car")

print(car.get_engine())

person = Classes.Person()
person.setage(15)
person.setname('Sam')
person.setsurname('Sanchez')
person.setheight(1.76)

developer = Classes.Developer()
developer.setage(30)
developer.setname('Samuel')
developer.setsurname('Sanchez')
developer.setheight(1.75)
print(developer.program())
print(f"I am {developer.getname()} and {developer.walking()} and tomorrow {developer.program()} in {developer.getlanguages()}")

technician = Classes.Technician()
print(f"{technician.getlanguages()}")