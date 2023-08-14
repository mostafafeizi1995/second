class Car:
    def __init__(self, car_name, model, color, car_capacity, gas_valume, initial_acceleration_from_0_100, gas_usage_per_100km ):
        self.car_name = car_name
        self.model = model
        self.color = color
        self.car_capacity = car_capacity
        self.gas_valume = gas_valume
        self.initial_acceleration_from_0_100 = initial_acceleration_from_0_100
        self.gas_usage_per_100km = gas_usage_per_100km
        self.distance_covered = 0 
    
    def __str__(self):
        # messege = "name car is {}, model is {}, color is {}, car_capacity {}, gas_valume {}, initial_acceleration_from_0_100 {}, gas_usage_per_100km {}, distance_covered {}". format(self.car_name, self.model, self.color, self.car_capacity, self.gas_valume, self.initial_acceleration_from_0_100, self.gas_usage_per_100km, self.distance_covered)
        messege = "gas_valume {}, gas_usage_per_100km {}, distance_covered {}". format(self.gas_valume, self.gas_usage_per_100km, self.distance_covered)
        return messege

    def drive(self, drive_distance):
        self.distance_covered += drive_distance
        self.gas_valume -= drive_distance * (self.gas_usage_per_100km / 100.0) 
        print("driving {} km".format(drive_distance))
        self.cheking_gas()


    def cheking_gas(self):
        if self.gas_valume <= 8:
            print("*"*5,"low fuel warning","*"*5)


    def fill_gas(self, valume):
        self.gas_valume += valume
        print("gas valume after filling {} ".format(self.gas_valume))




car = Car("pride", 1395, "white", 4, 40, "13s", 10)
print(car)

car.drive(450)
print(car)
car.fill_gas(30)
