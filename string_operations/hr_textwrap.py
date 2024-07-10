# textwrap module has two methods wrap() and fill() to work on wrapping
# long texts
import textwrap


def main():
    long_string = 'This is a very very long sentence, that is to be wrapped.'

    # wrap() method returns a list of strings
    # the long string is split up to the width provided as a list
    print(textwrap.wrap(long_string, 10))

    # fill() method returns a 'single' string with newlines after the
    # max width provided
    print(textwrap.fill(long_string, 10))


if __name__ == '__main__':
    main()