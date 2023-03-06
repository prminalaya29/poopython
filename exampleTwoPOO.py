# The __init__  function is called every time an object 
# is created from a class. The __init__ method lets the
# class initialize the object’s attributes and serves no other purpose. 
# It is only used within classes. 

# The self parameter is a reference to the current instance
# of the class, and is used to access variables that belongs
# to the class.

# __dict__: 
class Animal:

    # builder
    def __init__(self, name, age, color="white"):
        self.name = name
        self.age =age
        self.color = color

    def __str__(self):
        dato = f'El animal con nombre {self.name} tiene {self.age} años de edad'
        return dato
    
    def msj(self):
        if self.age > 1 and self.age <= 2:
            msj = "La mascota es carrocho"
        else:
            msj = "La mascota es adulta"
        
        return msj


dog = Animal("Milo", 2)
cat  = Animal("Lucho", 3, "rubio")

print(dog)
print("***************************")
print(dog.__dict__)
print("***************************")
print(dog.age)
print(dog.name)
print(dog.color)
print("***************************")
print(cat)
print("***************************")
print(cat.__dict__)
print("***************************")
print(cat.age)
print(cat.name)
print(cat.color)
print("***************************")
print(dog.msj())
print("***************************")
print(cat.msj())
