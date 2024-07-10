# Create a generator function
def finite_generator(max_count):
    count = 1
    while count <= max_count:
        yield count
        count += 1


for i in finite_generator(10):
    print(i)