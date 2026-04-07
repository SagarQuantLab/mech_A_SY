# class myClass:
#     pass

# a = myClass()
# print(type(a))

# print(isinstance(a, myClass))

class Car:

    def __init__(self, car, year):
        self._car = car
        self.__year = year

    def _get_my_car_details(self):
        return f"Here are my car details - {self.car} - {self.year}"
    
    def __get_registeration_details(self):
        return "Registeration details not found"


carIns = Car('Swift', '2026')
print(carIns._car)
# print(carIns.__year)
print(carIns._get_my_car_details())
# print(carIns.__get_registeration_details())