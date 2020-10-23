
def printNonRepeated(arr, n):
    dict = {}
    for i in arr:
        dict[i] = 0

    # iterating through the elements
    for i in arr:
        dict[i] += 1
    l = []
    for i in arr:
        if dict[i] == 1:
            l.append(i)
    return l

def main():
    T = int(input())
    while (T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        l = printNonRepeated(arr, n)
        print(*l)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends