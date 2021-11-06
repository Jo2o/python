arr = [3, 0, 3, 2, 0, 0, 0]
k = 3

occurrences = [0] * (k + 1)
sorted = []

for i in range(0, len(arr)):
  occurrences[arr[i]] += 1



print(occurrences)
