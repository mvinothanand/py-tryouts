def swap_case(s):
    case_swapped_string = ''
    # Method 1
    # Checking the ascii value of the character using the ord() method
    # for letter in s:
    #     if 65 <= ord(letter) <= 90:
    #         case_swapped_string += letter.lower()
    #     elif 97 <= ord(letter) <= 122:
    #         case_swapped_string += letter.upper()
    #     else:
    #         case_swapped_string += letter

    # Method 2
    # Using the inbuilt funcs islower() and isupper()
    for letter in s:
        if letter.isupper():
            case_swapped_string += letter.lower()
        elif letter.islower():
            case_swapped_string += letter.upper()
        else:
            case_swapped_string += letter
            
    return case_swapped_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)