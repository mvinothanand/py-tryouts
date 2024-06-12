# Change the first letter of a word to uppercase
# Note: title() can't be used on the entire input string.
# it doesn't work when:
# 1. apostrophes are present in a word
# 2. word starts with a number

def main():
    s = input()
     
    new_s = []
    for word in s.split(' '):
        if word:
            if word[0].isalpha():
                new_s.append(word.title())
            else:
                new_s.append(word)
        else:
            new_s.append('')
    print(' '.join(new_s))


if __name__ == '__main__':
    main()
