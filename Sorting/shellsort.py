def shellSort(myList):
    dist = len(myList) // 2
    while dist > 0:
        for i in range(dist, len(myList)):
            currentItem = myList[i]
            j = i
            while j >= dist and myList[j - dist] > currentItem:
                myList[j] = myList[j - dist]
                j -= dist
            myList[j] = currentItem
        dist //= 2

    return myList

if __name__ == '__main__':
    myList = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print('Sorted List:',shellSort(myList))
