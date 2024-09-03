class Fraction(object):

    def __init__(self,numerator:int,denominator:int):
        self.numerator = numerator
        self.denominator = denominator
        

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Both numerator and denominator must be integers")
        
        if denominator==0:
            raise ValueError("Denominator cannot be zero.")

    def float(self):    
        return self.numerator/self.denominator

    def __str__(self):
        return "Fraction:  {}/{}".format(self.numerator,self.denominator)
    
    def __repr__(self):
        return f"The fraction is {self.numerator}/{self.denominator}"

    def __gt__(self,other):
        return self.float() > other.float()
    
    def __lt__(self,other):
        return self.float() < other.float()
    
    def __ge__(self,other):
        return self.float() > other.float() or self.float() == other.float()
            
    def __le__(self,other):
        return self.float() < other.float() or self.float() == other.float()
    
    def __eq__(self, other): 
        
        if not(isinstance(other, Fraction)):
            return False
        return self.float() == other.float() 
    
    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        if new_denominator == 0:
            raise ZeroDivisionError("Resulting denominator is zero.")
        return Fraction(new_numerator, new_denominator)
            

a= Fraction(1,3)

b = Fraction(1,4)

print(a-b)


