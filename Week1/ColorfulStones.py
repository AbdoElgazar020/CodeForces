s = input()
t = input()

s = list(s)
t = list(t)

count = 1
state=0
back = 0
for i in range(len(t)):
    if s[back]==t[state]:
        count+=1
        back+=1
        state+=1
    else:
        state+=1
        
        
print(count)