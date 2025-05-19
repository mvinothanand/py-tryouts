var_1 = None
var_2 = None

def imported_func_in_main(one, two):
  global var_1, var_2
  var_1 = one
  var_2 = two


def local_func():
  print(f'{var_1}')
  print(f'{var_2}')

def modify_func():
  print(f'line 1: {var_1=}, {var_2=}')
  # var_1 = 101
  # var_2 = 102
  print(f'{var_1=}, {var_2=}')