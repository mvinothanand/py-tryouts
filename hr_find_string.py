# Given a string and a substring
# Find the number of occurences of the substring in string
def main():
    string = input('string: ')
    substring = input('substring: ')
    start_idx = 0
    no_of_occurences = 0

    while (True):
        index = string.find(substring, start_idx)
        if index > -1:
            no_of_occurences += 1
            start_idx = index + 1
        else:
            break

    print(no_of_occurences)
    return no_of_occurences


if __name__ == '__main__':
    main()