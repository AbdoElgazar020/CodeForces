horseshoes = set({})
c = list(map(str, input().split()))
horseshoes.update(c)
print(4-len(horseshoes))