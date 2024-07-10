def bubble_sort_1(input_list):
  sorted_list= [*input_list]
  print(f"no. of items in list: {len(input_list)}")
  
  swap_flg = True
  iterations = 0
  while (swap_flg):
    iterations += 1
    print(f"iteration: {iterations}")
    swap_flg = False
    for n, i in enumerate(sorted_list):
      if n < len(sorted_list) - 1:
        next_num = sorted_list[n+1]
        if i > next_num:
          sorted_list[n+1] = i
          sorted_list[n] = next_num
          swap_flg = True
  
  return sorted_list


def bubble_sort_2(input_list):
  n = len(input_list)
  for i in range(n):
    for j in range(0, n-i-1):
      #print(i, j)
      if input_list[j] > input_list[j+1]:
        tmp = input_list[j+1]
        input_list[j+1] = input_list[j]
        input_list[j] = tmp 
  return input_list


def main():
  input_list = [20,23, 13, 19, 20,21,  5,2,4,3,0,1,100,25, 14]
  print(bubble_sort_2(input_list))

if __name__ == "__main__":
  main()