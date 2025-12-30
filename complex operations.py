class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def shownumber(self):
        print(f"{self.real}i+{self.imag}j")
    def __add__(self,num2):
        newreal=self.real+num2.real   #+ or - or *
        newimag=self.imag+num2.imag   # + or - or *
        return Complex(newreal,newimag)
num1=Complex(1,6)
num1.shownumber()
num2=Complex(2,5)
num2.shownumber()
num3=num1+(num2)
num3.shownumber()