def BinarySearch(alist,data):
    left = 0
    right = len(alist)-1
    found = False
    while left <= right and not found:
        midPoint = (left + right)//2
        if alist[midPoint] == data:
            found = True
            break
        else:
            if data < alist[midPoint]:
                right = midPoint -1
            else:
                left = midPoint +1
    return found

a = [4, 12, 32, 32, 55, 67, 225, 97]
print(BinarySearch(a,225))

