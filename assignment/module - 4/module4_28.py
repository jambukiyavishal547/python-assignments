#What is used to check whether an object o is an instance of class A?

'''
    Syntax of isinstance() function
    Return: true if the object is an instance or subclass of a class, or any element of the tuple false otherwise. 
    If class info is not a type or tuple of types, a TypeError exception is raised. 
    Example 1: In this example, we will see test isinstance() for the class object   
'''
class abc:

    print("Example of isinstance()")

obj=abc()
print(isinstance(obj,abc))