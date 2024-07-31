def numProblems(n):
    nSummited=0
    for i in range(n):
        votes = list(map(int, input().split()))
        if sum(votes)>1:
            nSummited+=1
    return nSummited
    
n = int(input())
print(numProblems(n))