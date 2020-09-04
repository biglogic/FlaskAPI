class test:
    def __init__(self, x , y):
           self.x=x
           self.y=y

    def show(self , b):
        print(self.x  ,   self.y )
        print(b+1)

class testb(test):
    
    def __init__(self,x,y,z):
        self.z=z
        super().__init__(x , y)

    def show(self,b):
        print(self.z) 
        super().show(b+1)


value=testb(45,45,55)
print(value.x)        
print(value.show(3))