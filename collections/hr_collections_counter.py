# collection.counter()
# stores the elements of a list as dictionary keys with values as their count
from collections import Counter

mylist = [1, 2, 3, 5, 2, 2, 1, 0, 3]
mylist_counter = Counter(mylist)

print(mylist_counter)
#Counter({2: 3, 1: 2, 3: 2, 5: 1, 0: 1})

print(mylist_counter.items())
#dict_items([(1, 2), (2, 3), (3, 2), (5, 1), (0, 1)])

print(mylist_counter.keys())
# dict_keys([1, 2, 3, 5, 0])

print(mylist_counter.values())
# dict_values([2, 3, 2, 1, 1])

print(mylist_counter[0])