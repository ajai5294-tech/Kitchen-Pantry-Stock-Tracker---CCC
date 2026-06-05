items = [1,2,3,4,5,6]
for i in range(len(items)):
    min = i
    for j in range(len(items)):
        if items[i] > items[j]:
            min = j
    items[i] = items[min]
print(items)