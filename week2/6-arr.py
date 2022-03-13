def maxMin(k, arr):
    sorted_array = sorted(arr)
    minimun = []
    k -= 1
    for i in range(len(sorted_array)- k):
        unfairness = sorted_array[i + k] - sorted_array[i]
        minimun.append(unfairness) 
    return min(minimun)
    
arr = [1,4,7,2]
k = 2

maxMin(k,arr)