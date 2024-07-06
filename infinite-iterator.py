# Create a python infinite iterator class 
class Repeater:
    def __init__(self, value):
        self.value = value


    # required for a iterator class
    # returns the object itself
    def __iter__(self):
        return self
    

    # requried for a iterator class
    # returns a value upon call of the next() function
    def __next__(self):
        return self.value
    

# this step creates the iterator object
repeater = Repeater('Hello')

# set the iteration
iterator = iter(repeater)

# get the value from the iterator
print(next(iterator))
print(next(iterator))
print(next(iterator))


# Below code will print 'Hi Vinoth!' infinitely
# repeater_2 = Repeater('Hi Vinoth!')
# for item in repeater_2:
#     print(item)
