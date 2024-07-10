# Given an integer N, build a rangoli
# example: N = 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

def main():
    alphabets = []
    n = 5
    width = (4 * n ) - 3
    for i in range(n):
        alphabets.append(chr(97 + i))

    print(alphabets)

    # top triangle
    for i in range(1, n):
        string = (
            '-'.join(reversed(alphabets[n + 1 - i : n])).rjust(width // 2 - 1, '-') +
            ''.center(1 if n > 1 else 0, '-') +
            '-'.join(alphabets[n - i : n]).ljust(width // 2 + 1, '-')
        )
        print(string, sep='')

    # center line
    print(
        '-'.join(reversed(alphabets[1:n])) +
        ''.center(1 if n > 1 else 0, '-') +
        '-'.join(alphabets[0:n])
    )

    # bottom triangle
    for i in range(1, n):
        string = (
            '-'.join(reversed(alphabets[i:n])) +
            '-' +
            '-'.join(alphabets[i + 1:n])
          )
        print(string.center(width, '-'))

if __name__ == '__main__':
    main()