###############################################################################
# DONE: 1. (2 pts)
#
#   In this module, we are going to look at some familiar concepts that we have
#   seen before. You will notice that many of the things you have learned in
#   this course so far are objects. Each object has a class (or a blueprint
#   that helps to define it).
#   
#   Below this _todo_, I have provided a few different objects. Just as you
#   have done before, get the type of each object using its variable name and
#   the type() function. Make sure you print the type.
#
#   Notice how when the type is printed, it prints something like this:
#
#       <class str>
#
#   This is because the types that we have looked at before are classes. That
#   is, the type/class serves as the blueprint for that objects properties and
#   its methods.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
obj_1 = "The quick brown fox jumps over the lazy dog."
obj_2 = [1, 2, 3, 4, 5]
obj_3 = ("Red", "Blue", "Green")
obj_4 = {6, 7, 8, 9}

print(type(obj_1))
print(type(obj_2))
print(type(obj_3))
print(type(obj_4))
###############################################################################
# DONE: 2. (4 pts)
#
#   Also, remember that these objects have methods that we have used to perform
#   specific tasks on them.
#
#   Some examples of these were replace(), append(), pop(), etc.
#
#   For each of the objects above, use a method that is available to that
#   object to perform some sort of action on it. Feel free to look back at the
#   previous readings or exercises to remember which objects have which methods.
#
#   After you have performed an action on each object. Make sure you print the
#   changed version.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

print(obj_1.title())
print(obj_2.index(2))
print(obj_3.count("Red"))
print(obj_4.clear())