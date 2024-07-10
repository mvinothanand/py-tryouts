# Example to show how a generator expression to be used

squares = (i*i for i in range(10))

print(next(squares))
print(next(squares))

# continues from the previous next call
for i in squares:
    print(i)

# stop iteration exception is raised beyond the range boundary
next(squares)