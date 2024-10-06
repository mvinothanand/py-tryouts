# handle zerodivision exception

def main():
    for _ in range(int(input())):
        
        try:
            a, b = list(map(int, input().split()))
            print(a // b)
        except ZeroDivisionError as e:
            print(f'Error Code: {e}')
        except ValueError as e:
            print(f'Error Code: {e}')
    

if __name__ == '__main__':
    main()