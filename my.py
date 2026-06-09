import random
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
    for i in range(0, len(items), 2):
        if i >= len(items) - 2:
            print(items[i])
        else:
            print(items[i], end = ", ")
def printMatrix(matrix):
    for row_index, row in enumerate(matrix):
        for item_index, item in enumerate(row):
            if item_index == len(row) - 1:
                print(item)
            else:
                print(item, end = ", ")
def createMatrix():
    zeros_matrix = [[0 for _ in range(3)] for _ in range(3)]
    return zeros_matrix
def fillMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = int(random.random() * 100)
    return matrix
def sortMatrix(matrix):
    for row in matrix:
        selection_sort(row)
    return matrix
def printRightTriangle(num):
    i = 0
    while i <= num:
        x = 0
        while x <= i:
            print("*", end = " ")
            x += 1
        print()
        i += 1
def readName():
    name = input("Enter your name: ")
    print(f"Hi, {name}")
def counToNumber(n):
    i = 0
    while i <= n:
        if i == n:
            print(i)
        else:
            print(i, end = ", ")
        i += 1
def countToN():
    n = int(input("Enter a number: "))
    counToNumber(n)
def guessingGame():
    num = int(random.random() * 100)
    print("Welcome to the number guessing game")
    found = False
    while found == False:
        guess = int(input("Guess a number 0-100 inclusive: "))
        if guess > num:
            print("Too high")
        if guess < num:
            print("Too low")
        if guess == num:
            print("You win")
            found = True
matrix = [
    [2,3,7],
    [5,9,1],
    [7,2,4]
]
items = [2,4,3,6,5,1]
selection_sort(items)
insertionSort(items)
printEvenTill10()
everyOther(items)
printMatrix(matrix)
printMatrix(createMatrix())
printMatrix(fillMatrix(createMatrix()))
printMatrix(sortMatrix(fillMatrix(createMatrix())))
printRightTriangle(4)
readName()
countToN()
guessingGame()