#5-m
class Car:
    def __init__(self, make, model):
        self.make = make
        self.__model = model
        
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_model):
        self.__model = new_model
        
c1 = Car('Ford', 'Mustang')
print(c1.model)

res = c1.model
print(res)

c1.model = res
print(c1.model)
