###############################################################################
# DONE: 1. (1 pt)
#
#   In this module, you will need the Pet class that you created in m2. Copy
#   and paste the class above this _todo_ for you to use in the rest of these
#   todos.
#
#   For this _todo_, create an object called myPet that is of the class Pet. It
#   should have a name and an age. You can choose whichever values you wish.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, Age:{self.age}"
    def speak(self):
        print(f"{self.name}: Bark! Bark! Bark!")

myPet = Pet("George", 3)
###############################################################################
# DONE: 2. (1 pt)
#
#   For this _todo_, print your object using it's variable name. Notice how it
#   prints according to your __str__() method definition.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
print(myPet)
###############################################################################
# DONE: 3. (1 pt)
#
#   For this _todo_, using the object you have defined in this todo, call the
#   speak() method on that object.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
myPet.speak()
###############################################################################
# DONE: 4. (1 pt)
#
#   For this _todo_, modify the age property of your object to be something
#   different than it was originally. Make sure you print your object again to
#   you can see the change.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
myPet.age = 10000
print(myPet)