import re

def capture_groups(input_str):
    matches = re.search(r"^(.+)\s*,\s*(.+)$", input_str)
    print(matches.group(2), matches.group(1))


def main():
    print("hello")
    capture_groups("vinoth , anand")


if __name__ == "__main__":
    main()