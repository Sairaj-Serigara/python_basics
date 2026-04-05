#in static method we no need to write self
#we can write a method without using self key in static method

class Math:
    def __init__(self, n):
        self.n = n
    @staticmethod
    def add(a,b):
        print(a+b)

obj=Math(1)
obj.add(2,3)

print(Math.add(2,3))
