def split_and_join(input_str: str) -> str:
    split_string = input_str.split(' ')
    join_str = '-'.join(split_string)
    return join_str


def main():
    input_str = input().strip()
    print(split_and_join(input_str))


if __name__ == '__main__':
    main()