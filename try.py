import sys

n = int(sys.argv[1])

f = 1
for i in range(1, n+1):
    f *= i
print(f)