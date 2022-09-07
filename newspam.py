class Spam:
    numInstances = 0
    def count(cls): # Счётчики экземпляров по классам
        cls.numInstances += 1 # cls = самый нижний класс над экземпляром
    def __init__(self):
        self.count() # Передает self.__class__ методу count
    count = classmethod(count)

class Sub(Spam):
    numInstances = 0
    def __init__(self): # Переопределяет __init__
        Spam.__init__(self)

class Other(Spam): # Наследует __init__
    numInstances = 0

x = Spam()
y1, y2 = Sub(), Sub()
z1, z2, z3 = Other(), Other(), Other()
print(x.numInstances, y1.numInstances, z1.numInstances) # Данные для каждого класса!
print(Spam.numInstances, Sub.numInstances, Other.numInstances)
