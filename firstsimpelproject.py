class car:
    def __init__(self,speed,year,model,brand):
        self.s=speed
        self.y=year
        self.m=model
        self.b=brand
    def accelerate(self,amount):
        (self.s)+=amount
        print(self.s)
    def brake(self,amount):
        (self.s)-=amount
        print(self.s)
    def display_info(self):
        print(f"speed:{self.s} and year:{self.y} and model:{self.m} and brand:{self.b}")  
x4=car(0,2000,"a","bmw")
x4.accelerate(80)
x4.brake(40)
x4.display_info()     