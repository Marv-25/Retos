def sockMerchant(n, ar):
    arr = list(set(ar))
    result = 0
    for i in arr:
        a = ar.count(i) // 2
        result += a
    return result

n = 7 
ar = [1,2,1,2,1,3,2]

sockMerchant(n,ar)