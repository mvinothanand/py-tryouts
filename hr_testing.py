def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

import random

class TestDataEmptyArray:
    def get_array():
        return []
        
class TestDataUniqueValues:
    array = None
    
    @classmethod
    def get_array(cls):
        cls.array = random.sample(range(0, 100), random.randrange(2, 30))
        return cls.array
    
    @classmethod
    def get_expected_result(cls):
        minimum_value = min(cls.array)
        return cls.array.index(minimum_value)

class TestDataExactlyTwoDifferentMinimums:
    indexes = []
    
    @classmethod
    def get_array(cls):
        minimum = random.randrange(0, 10)
        print(f'minimum value: {minimum}')
        array = TestDataUniqueValues.get_array()
        filtered_array = [element for element in array if element > minimum]
        
        cls.indexes = random.sample(range(0, len(filtered_array)-1), 2)
        print(cls.indexes)
        filtered_array.insert(cls.indexes[0], minimum)
        filtered_array.insert(cls.indexes[1], minimum)
        
        return filtered_array
        
    @classmethod
    def get_expected_result(cls):
        return min(cls.indexes)


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    print(seq)
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    print(TestDataUniqueValues.get_expected_result())
    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    print(result)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    print(tmp)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")

