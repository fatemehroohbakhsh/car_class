class Car:
    def __init__(self,speed,year,model,brand):
        self.speed=speed
        self.year=year
        self.model=model
        self.brand=brand
    def accelerate(self,amount):
        self.speed+=amount
        print(self.speed)
    def brake(self,amount):
        self.speed-=amount
        if self.speed<0:
            print("it is not possible")   
            self.speed=0       #if speed is negtive speed=0
        else:
          print(self.speed)     
    def display_info(self):
        print(f"speed:{self.speed} and year:{self.year} and model:{self.model} and brand:{self.brand}")  
x4=Car(0,2000,"a","bmw")     #making an object
x4.accelerate(80)
x4.brake(40)
x4.display_info()     
