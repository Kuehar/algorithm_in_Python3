def binarysearch(array,value):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high)//2
        lists = array[mid]
        if lists == value:
            return mid
        if lists > value:
            high = mid - 1
        else:
            low = mid + 1
    return None
