
def task(n):
       # if n >= 1 and n <= 100:
        if n % 2 != 0:
            print("Weird")
        else:
            if (2 >= n <= 5):
                print("Not Weird")
            elif (6 >= n and n <= 20):
                print("Weird")
            elif (n > 20):
                print("Not Weird")


if __name__ == '__main__':
    n = int(input().strip())
    task(n)
