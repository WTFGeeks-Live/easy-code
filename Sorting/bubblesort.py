def bubbleSort(List):
    for i in range(len(List)):
        for j in range(len(List) - 1, i, -1):
            if List[j] < List[j - 1]:
                List[j], List[j - 1] = List[j - 1], List[j]
    return List

if __name__ == '__main__':
    List = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print('Sorted List:',bubbleSort(List))
