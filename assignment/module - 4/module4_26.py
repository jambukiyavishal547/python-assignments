#Explain Inheritance in Python with an example? What is init? Or What 
#Is A Constructor In Python? 

'''
   (1) what is init?

    The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach. 
    The __init__ function is called every time an object is created from a class. 
    The __init__ method lets the class initialize the object's attributes and serves no other purpose. 
    It is only used within classes.

    (2) what is A Constructor In Python? 

        A constructor is a special method in a class used to create and initialize an object of a class. 
        There are different types of constructors in Python programming language. 
        Constructor is invoked automatically when an object of a class is created.

    (3) example of inharitance

        typr of Inharitance
            1.Single level
            2.multi level
            3.multipal 
            4.Hierarchical 
            5.Hybrid 
'''
#example of Single level 
class A:
    def a(self):
        print("This is the base class mathod")

class B(A):
    obj=A()
    obj.a()