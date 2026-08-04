def mtable(n):
    for i in range(1,10):
        res = n * i
        print("{} * {} = {}".format(n, i, res))

n=int(input("Enter a Number  "))
mtable(n)