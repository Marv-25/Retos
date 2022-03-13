
def pageCount(n, p):
    # Write your code here
    middle = n//2
    if p <= middle:
        return p // 2
    else: 
        return (n//2 - p//2)
        