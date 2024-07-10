# Create the Hacker Rank Logo 
# using the text alingment methods ljust, rjust, center

def main():
    #thickness = int(input()) # this must be an odd number
    thickness = 5
    c = 'H'

    #Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Middle belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness*6))

    # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))    


if __name__ == '__main__':
    main()