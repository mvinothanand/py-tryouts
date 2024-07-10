x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

n = int(input("n: "))

# Get the cordinates (i,j,k) where 0 <= i <= x, 0 <= j <= y, 0 <= k <= z 
# whose sum is not equal to n
# use list comprehension

result = [(i , j , k) for i in range(0, x+1) for j in range(0, y+1) for k in range(0,z+1) if i + j + k != n]
print("Result: ")
print(result)
print(len(result))
