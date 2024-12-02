lefts = []
rights = []

with open("../data/2024_1.txt") as f:
  for line in f:
    a, b = line.split()
    lefts.append(int(a))
    rights.append(int(b))

lefts.sort()
rights.sort()

ans = 0
for l, r in zip(lefts, rights):
  ans += abs(l - r)

print(ans)