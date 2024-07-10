def main():
    N = int(input())

    mylist = []
    commands = []

    # _ avoids initializing an unwanted variable
    for _ in range(N):
        commands.append(input().strip())

    for command in commands:
        # Splits the content of command variable at space 
        # first element is assigned to operation var
        # rest of elements to a list args
        operation, *args = command.split()
        match operation:
            case 'insert':
                # inserts an element to the list at the specified index
                # insert(index, element)
                mylist.insert(int(args[0]),int(args[1]))
            case 'print':
                print(mylist)
            case 'remove':
                # removes the first occurence of the specified element
                mylist.remove(int(args[0]))
            case 'append':
                # appends the element to the end of the list
                mylist.append(int(args[0]))
            case 'sort':
                # sorts the list elements in ascending
                mylist.sort()
            case 'pop':
                # removes the last element in the list
                mylist.pop()
            case 'reverse':
                # reverses the contents of the list
                # note: this is not sorting in descending
                mylist = mylist[::-1]
            case _:
                print('Invalid Command')

if __name__ == '__main__':
    main()