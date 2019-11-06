import collections

input =     [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
result = []
dd = collections.defaultdict(list)

for i in range(0, len(input)):
    for j in range(0, len(input[0])):
        dd[i+j].append(input[i][j])
print(dd)
for k in sorted(dd.keys()):

    if k%2 ==0:
        dd[k].reverse()
    print(dd[k])
    result+=dd[k]
print(result)
