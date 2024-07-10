# print true if the input string has any alphanumeric character
# print true if the input string has any alphabetical character
# print true if the input string has any lowercase letter
# print true if the input string has any uppercase letter
# print true if the input string has any numeric character
def main():
    s = input()

    has_alpha = False
    has_alpha_numeric = False
    has_digits = False
    has_lowercase = False
    has_uppercase = False

    for char in s:
        if (not has_alpha) and char.isalpha(): 
            has_alpha = True
        
        if (not has_alpha_numeric) and char.isalnum():
            has_alpha_numeric = True

        if (not has_digits) and char.isdigit():
            has_digits = True

        if (not has_lowercase) and char.islower():
            has_lowercase = True

        if (not has_uppercase) and char.isupper():
            has_uppercase = True

    print(has_alpha)
    print(has_alpha_numeric)
    print(has_digits)
    print(has_lowercase)
    print(has_uppercase)


if __name__ == '__main__':
    main()