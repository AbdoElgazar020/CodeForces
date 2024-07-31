numCoins = int(input())
c = list(map(int, input().split()))
coins = sorted(c,reverse=True)
half_amount = sum(coins)/2
x = 1
me = 0
numCoinsOFme=0
for coin in coins:
    me += coin
    numCoinsOFme += 1
    if me > half_amount:
        break
print(numCoinsOFme)
print(coins)