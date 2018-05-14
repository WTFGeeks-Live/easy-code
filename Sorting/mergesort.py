def merge(a,b):
  
    """ Function to merge arrays """
  
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

# Code for merge sort

def mergeSort(s):
  
    """ Function to sort an array using merge sort """
  
    if len(s) == 0 or len(s) == 1:
        return s
    else:
        middle = len(s)//2
        a = mergeSort(s[:middle])
        b = mergeSort(s[middle:])
        return merge(a,b)

if __name__ == '__main__':
    List = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print('Sorted List:',mergeSort(List))
