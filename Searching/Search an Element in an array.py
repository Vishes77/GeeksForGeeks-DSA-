# User function Template for python3
import math
# Complete the below function
def search(arr, N, X):
    low = 0
    high = N-1
    while(low <= high):
        mid = (low + high)//2 # // to get the round of value.
        if arr[mid] == X:
            return mid
        elif arr[mid] < X:
            low = mid + 1
        else:
            high = mid - 1
    return -1
    # return arr.insert

def main():
    T = int(input())
    while (T > 0):
        N = int(input())

        A = [int(x) for x in input().strip().split()]

        x = int(input())

        print(search(A, N, x))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends