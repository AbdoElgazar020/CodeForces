def numSeprates(number):
    count=0
    while number>9:
        numberStr = str(number)
        lst = list(numberStr)
        toNum=list(map(int,lst))
        number = sum(toNum)
        count+=1
    return count
    
n = int(input())
print(numSeprates(n))