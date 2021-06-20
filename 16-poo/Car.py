# Class
class Car:
    # Properties
    color = "Red"
    brand = "Ferrari"
    model = "Aventador"
    speed = 300
    power = 500
    seats = 2

    __engine = 'Mercedes'

    def __init__(self, brand, color, model, speed, power, seats):
        self.brand = brand
        self.color = color
        self.model = model
        self.speed = speed
        self. power = power
        self.seats = seats

    # Methods
    def speed_up(self):
        self.speed += 1

    def speed_down(self):
        self.speed -= 1

    def get_speed(self):
        return self.speed

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_engine(self):
        return self.__engine

    def get_info(self):
        info = "Car info ---"
        info += "\n Color : " + self.get_color()
        info += "\n Model : " + self.get_model()
        info += "\n Speed :" + str(self.get_speed())
        return info
# End