def findMedian(arr):
    arr = sorted(arr)
    arr_length =len(arr)
    median = int(arr_length/2)
    result = arr[median]
    return result 

arr = [5,3,1,2,4]
findMedian(arr)
