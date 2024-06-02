def main():
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        last_two_terms = [1, 2]
        sum_even_terms = 2
        while sum(last_two_terms) < n:
            next_term = sum(last_two_terms)
            last_two_terms = [last_two_terms[1], next_term]
            if next_term % 2 == 0:
                sum_even_terms += next_term
        print(sum_even_terms)
        

if __name__ == '__main__':
    main()