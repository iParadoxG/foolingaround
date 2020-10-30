print("Enter m: ")
m = int(input())
print("Enter n: ")
n = int(input())
for i in range(m):
    for j in range(n):
        print(f"({i}, {j})", end=" ")
    print()