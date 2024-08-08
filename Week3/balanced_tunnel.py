n = int(input())

enter = list(map(int,input().split()))  #Entered cars in list
out = list(map(int,input().split()))    #Out cars in list


vis = [False] * (n + 9)

l = n-1
r = n-1
ans = 0

while l > -1 and r > -1:
    if enter[l] == out[r]:
        l -= 1
        r -= 1
    else:
        if vis[out[r]]:
            r -= 1
        else:
            ans += 1
            vis[enter[l]] = True
            l -= 1

print(ans)
