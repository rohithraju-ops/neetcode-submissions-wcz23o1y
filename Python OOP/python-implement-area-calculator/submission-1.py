import math

class AreaCalc:
    def calculate(self, length, width=None):
        self.length = length
        self.width = width
        if self.width is None:
            return round(math.pi * self.length ** 2 ,2)
        else:
            return self.length * self.width
        
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
