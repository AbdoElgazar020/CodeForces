data = []
a,b= list(map(int,input().split()))
data.append(a)
data.append(b)
for i in range(b):
    x,y = list(map(int,input().split()))
    data.append(x)
    data.append(y)

if not data:
    raise ValueError("No input data provided")

n = int(data[0])
m = int(data[1])

if len(data) < 2 + 2 * m:
    raise ValueError("Insufficient input data for subarray ranges")

min_mex = float('inf')
index = 2

for _ in range(m):
    l = int(data[index]) - 1
    r = int(data[index + 1]) - 1
    min_mex = min(min_mex, r - l + 1)
    index += 2

print(min_mex)


result = [(i % min_mex) for i in range(n)]
print(' '.join(map(str, result)))