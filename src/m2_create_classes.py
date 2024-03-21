###############################################################################
# DONE: 1. (3 pts)
#
#   In m1 we looked at classes that you have seen before. Those are built-in
#   classes that are simply a part of Python.
#
#   We can actually create our own classes with their own properties and
#   methods.
#
#   For this _todo_, create a class called Pet. It should have an __init__()
#   function that sets two properties:
#       - name      <- str
#       - age       <- int
#
#   Remember that the __init__() function is what is used to create a new
#   object (a new instance of that class).
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age


###############################################################################
# DONE: 2. (2 pts)
#
#   For this _todo_, modify the class above to include a __str__() method. If
#   performed on a Pet object with these properties:
#
#       name: Fido
#       age: 4
#
#   this __str__() method should print the Pet object like so:
#
#       Name: Fido, Age: 4
#
#   In your reading, notice how the __str__() method uses a return (NOT a
#   print() ).
#
#   Feel free to create your own objects to test with. We will practice
#   creating objects in m3.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
    def __str__(self):
        return f"{self.name}, Age:{self.age}"
    
###############################################################################
# DONE: 3. (2 pts)
#
#   For this _todo_, modify the class in _todo_ 1 above to include a method
#   called speak() that, if given the same object described in _todo_ 2, would
#   print something like this:
#
#       Fido: Bark! Bark! Bark!
#
#   It is okay that the speak() method will print the same response for every
#   Pet for now (i.e. every Pet would say "Bark! Bark! Bark!" in this case).
#   This method should, however, always print the correct name of the pet.
#
#   We will learn how to have different sub-types within classes in the
#   materials for next class.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
    def speak(self):
        print(f"{self.name}: Bark! Bark! Bark!")

p1 = Pet("Fido", 4)
print(p1)
p1.speak()