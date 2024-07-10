# create a python boundd iterator class
class BoundedIterator:
    def __init__(self, value, max_repeats = 10):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0


    def __iter__(self):
        return self
    

    # implement the stop iteration control in the __next__ method
    # Raising StopIteration exception is must for a python iterator class
    def __next__(self):
        if self.count < self.max_repeats:
            self.count += 1
            return self.value
        else:
            raise StopIteration
        

bounded_iterator = BoundedIterator('Hello', 5)
for item in bounded_iterator:
    print(item)