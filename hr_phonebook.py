from sys import stdin

def main():
    phonebook = {}
    for i in range(int(input('n: '))):
        name, phone = input().strip().split()
        phonebook[name] = phone
    
    print(phonebook)

    while(True):
        try:
            search_name = input().strip()
            
            # works if end of inputs is indicated with an enter key
            if not search_name:
                break
            
            if phonebook.get(search_name):
                print(f'{search_name}={phonebook[search_name]}')
            else:
                print('Not Found')
        # works if an EOF indicates end of inputs
        except EOFError:
            break

        

if __name__ == '__main__':
    main()