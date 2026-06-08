def selection_sort(items):
    for i in range(len(items)):
        min = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min]:
                min = j
        x = items[i]
        items[i] = items[min]
        items[min] = x
    print(items)
def insertionSort(items):
    for i in range(1, len(items)):
        k = items[i]
        j = i - 1
        for j in range(i - 1, len(items)):
            if items[j] > k:
                items[j + 1] = items[j]
            else:
                items[j + 1] = k
                break
    print(items)
def printEvenTill10():
    i = 0
    while i <= 10:
        if i == 10:
            print(i)
        else:
            print(i, end = ", ")
        i+=2
def everyOther(items):
    for i in range(2, len(items)):
        if i + 2 <= len(items):
            print(items[i])
        else:
            print(items[i], end = ", ")


items = [2,4,3,6,5,1]
selection_sort(items)
insertionSort(items)
printEvenTill10()
everyOther(items)