from collections import defaultdict

lefts = defaultdict(int)
rights = defaultdict(int)

with open("../data/2024_1.txt") as f:
  for line in f:
    a, b = line.split()
    lefts[int(a)] += 1
    rights[int(b)] += 1

ans = 0
for l in lefts:
  ans += l * rights[l]
print(ans)