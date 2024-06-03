# Find the max absolute difference of the elements in a list
class Difference:
    def __init__(self, elements):
        self.__elements = elements

    def computeDifference(self):
        maxDifference = 0
        start_pos = 0
        for i in range(start_pos, len(self.__elements)):
            for j in range(i + 1, len(self.__elements)):
                if (diff := abs(self.__elements[i] - self.__elements[j])) > maxDifference:
                    maxDifference = diff
        self.maximumDifference = maxDifference

def main():
    elements = [100 ,2 ,300 ,4, 5, 19]
    d = Difference(elements)
    d.computeDifference()
    print(d.maximumDifference)
    print(d.__elements)


if __name__ == '__main__':
    main()