#with binary search
n, m = map(int, input().split())

xc, yc = map(int, input().split())

k = int(input())

total_steps = 0

for i_ in range(k):
    dx, dy = map(int, input().split())

    if dx > 0:
        max_steps_x = (n - xc) // dx
    elif dx < 0:
        max_steps_x = (1 - xc) // dx
    else:
        max_steps_x = float('inf') 

    if dy > 0:
        max_steps_y = (m - yc) // dy
    elif dy < 0:
        max_steps_y = (1 - yc) // dy
    else:
        max_steps_y = float('inf')  

    max_steps = min(max_steps_x, max_steps_y)
    
    xc += dx * max_steps
    yc += dy * max_steps
    
    
    total_steps += max_steps


    print(total_steps)

# with linear search but it have time limit error
'''
n,m = list(map(int,input().split()))
xc,yc = list(map(int,input().split()))
k = int(input())
maxSteps=0
for i in range(k):
    dx,dy = list(map(int,input().split()))
    while (1<=(xc+dx)<=n) and (1<(yc+dy)<m):
        xc = xc+dx
        yc = yc+dy
        maxSteps+=1
    else:
        continue
print(maxSteps)
'''