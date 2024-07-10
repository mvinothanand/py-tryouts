# design a doormat of size w * b
# the design should have 'WELCOME' at the center
# w is an odd number. b is 3 times w.
# use only, '|', '.' and '-'
import textwrap

def main():
    # #width = int(input('Provide width of the doormat: '))
    # width = 13
    # breadth = width * 3
    width, breadth = list(map(int, input().split(' ')))    
    
    midline = width // 2
    text = 'WELCOME'
    pattern = '|*|'
    filler = '-'

    for i in range(width):
        if i < midline:
        # prints the pattern above midline
          print((pattern * (i * 2 + 1)).center(breadth, filler))
        elif i == midline:
        # prints the pattern in midline
            print(
                (filler * ((breadth - len(text)) // 2)) + 
                text +
                (filler * ((breadth - len(text)) // 2)))
        else:
        # prints the pattern below midline
            print((pattern * (width - 2 * (i - midline))).center(breadth, filler))


if __name__ == '__main__':
    main()