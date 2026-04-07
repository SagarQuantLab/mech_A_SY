class Mathematics:

    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def _addition(self):
        return self.first_num + self.second_num
    
class Physics(Mathematics):

    def __init__(self, first_num, second_num):
        Mathematics.__init__(self, first_num, second_num)

    def addition(self):
        return self.first_num * self.second_num

    

mIns = Mathematics(2, 3)
# print(mIns._addition())

pIns = Physics(2, 3)
print(pIns._addition())
print(pIns.addition())
