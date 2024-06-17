# return the names that have '@gmail.com' as their email
# Inputs:
# N - number of inputs followed by N inputs of space separated name and emails
import re

def main():
    N = int(input().strip())
    names_with_gmail = []

    for _ in range(N):
        multi_input = input().strip().split()
        first_name, email = multi_input
        # print(f'{first_name},{email}')
        # Method 1: using endswith()
        # if email.endswith('@gmail.com'):
        #     names_with_gmail.append(first_name)

        #Method 2: using regex
        if re.search(r'.*@gmail.com$', email):
            names_with_gmail.append(first_name)
    
    for name in sorted(names_with_gmail):
        print(name)

if __name__ == '__main__':
    main()