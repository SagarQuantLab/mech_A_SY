class mummy:

    def __init__(self, car, salary):
        self.car = car
        self.salary = salary

    def get_my_car_mummy(self):
        return f"You can drive my car - {self.car}"
class grandpa:

    def __init__(self, car, pension):
        self.car = car
        self.pension = pension

    def _get_my_car(self):
        return "You can drive my car - Grandpa"
    
    def __get_my_pension(self):
        return "You can't access my pension - Grandpa"
    

class papa(grandpa):

    def __init__(self, papa_car, papa_salary):
        grandpa.__init__(self, papa_car, papa_salary*0.5)

    def _get_fathers_car(self):
        return self._get_my_car()
    
    def _get_papa_pension(self):
        return self.__get_my_pension()
    
class son(papa, mummy):

    def __init__(self, car_name, papa_salary, mummy_car, mummy_salary):
        papa.__init__(self, car_name, papa_salary)
        mummy.__init__(self, mummy_car, mummy_salary)

    
    def get_grandpa_car(self):
        return self._get_my_car()
    
    def get_grandpa_pension(self):
        return self.__get_my_pension()
    
    def get_mummy_car(self):
        return self.get_my_car_mummy()

    

# grandpaIns = grandpa('Ambessador', 50000)
# print(grandpaIns._get_my_car())
# print(grandpaIns.__get_my_pension())

# papaIns = papa('Ambessador', 50000)
# print(papaIns._get_fathers_car())
# print(papaIns._get_papa_pension())

sonIns = son('Ambessador', 50000, 'Swift', 50000)
print(sonIns.get_grandpa_car())
print(sonIns.get_mummy_car())
# print(sonIns.get_grandpa_pension())
