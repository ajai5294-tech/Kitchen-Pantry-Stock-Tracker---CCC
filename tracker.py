items = [2,4,3,6,5,1]
for i in range(len(items)):
    min = i
    for j in range(i + 1, len(items)):
        if items[j] < items[min]:
            min = j
    x = items[i]
    items[i] = items[min]
    items[min] = x
print(items)