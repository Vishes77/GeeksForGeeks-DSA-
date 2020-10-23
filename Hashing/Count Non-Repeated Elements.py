
def countNonRepeated(arr, n):
    dict = {}
    for i in arr:
        dict[i] = 0

    for i in arr:
        dict[i] += 1
    counter = 0

    for i in arr:
        if dict[i] == 1:
            counter += 1
    return counter

def main():
    T = int(input())
    while (T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        print(countNonRepeated(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends