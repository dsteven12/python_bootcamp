class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __repr__(self) -> str:
        return f"<Car {self.make} {self.model}"


class Garage:
    def __init__(self):
        self.cars=[]
    
    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car): #first parameter is variable, second is type (in this case Car Object)
            raise TypeError(f"Tried to add a `{car.__class__.__name__}` to the garage, but only `Car` objects can be added.")
        self.cars.append(car)

new_garage = Garage()
fiesta = Car("Ford", "Fiesta")
new_garage.add_car(fiesta)

cars_in_garage = len(new_garage)
end_comment = " in the garage."
if cars_in_garage == 1:
    print("There is one car" + end_comment)
else:
    print("There are {str(cars_in_garage)} " + end_comment)