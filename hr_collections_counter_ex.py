# A shoe shop has X number of shoes
# A list has the size of each shoe in the shop
#  N number of customers 
# How much money earned in total
# Input Format
# First line has X number of shoes
# 2nd line has list of all shoe sizes available
# 3rd line contains N - the number of customers
# Next N lines has the customer's size and price
from collections import Counter

def main():
    # get the number of shoes
    X = int(input())

    # sizes available
    sizes = list(map(int, input().split()))

    # number of customers
    N = int(input())

    # get customer demand
    customer_demand = []
    for _ in range(N):
        size, price = list(map(int, input().split()))
        customer_demand.append((size, price))

    print(f'no of shoes: {X}')
    print(f'sizes: {sizes}')
    print(f'no of customers: {N}')
    print(f'demand: \n{customer_demand}')

    init_avail_sizes_count = Counter(sizes)
    print(init_avail_sizes_count)

    avail_sizes_count = {**init_avail_sizes_count}

    print(avail_sizes_count)

    earnings = 0
    for demand in customer_demand:
        size, price = demand
        print(size, price)
        if avail_sizes_count.get(size) is not None and avail_sizes_count.get(size) > 0:
            earnings += price
            avail_sizes_count[size] -= 1

        print(f'updated availability: \n{avail_sizes_count}')
    
    print(f'earning: {earnings}')
        
if __name__ == '__main__':
    main()