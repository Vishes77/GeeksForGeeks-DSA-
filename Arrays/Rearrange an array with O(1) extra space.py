# User function Template for python3

##Complete this code
def arrange(arr, n):
    new = list()
    for i in range(n):
        new[i] = arr[arr[i]]
    for i in range(n):
        arr[i] = new[i]
    return arr

import math


def main():
    T = int(input())
    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        arrange(arr, n)

        for i in arr:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends