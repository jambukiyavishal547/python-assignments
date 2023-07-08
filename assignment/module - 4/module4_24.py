#Python class named Circle constructed by a radius and two 
#methods which will compute the area and the perimeter of a circle 

class circle:

    def __init__(self,r):
        self.radius=r

    def are(self):
        return self.radius**2*3.14
    
    def parimeter(self):
        return self.radius*3.14
    
obj=circle(6)
print(obj.are())
print(obj.parimeter())