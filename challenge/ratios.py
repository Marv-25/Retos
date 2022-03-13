
listOfNumbers = [8,9,-2,-8,-9]

def plusMinus(arr):
    # Write your code here
    positive, zero , negative  = 0, 0, 0
    for i in arr:
        if i == zero:
            zero += 1
        if i < 0:
            negative += 1
        if i > 0:
            positive += 1
    num = int(len(arr))
    
    zero = zero/num
    positive = positive/num
    negative= negative/num
    
    # zero = print(f"{zero:.6f}")
    # positive = f"{positive:.6f}"
    # negative = f"{zero:.6f}"

    print(zero)
    print(positive)
    print(negative)
    
    
plusMinus(listOfNumbers)
