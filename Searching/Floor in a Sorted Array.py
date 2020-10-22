import math

def findFloor(A, N, X):
    low = 0
    high = N - 1
    if(X >= A[high]):
        return high
    while(low <= high):
        mid = (low + high) // 2
        if(X == A[mid]):
            return mid
        if(A[mid] > 0 and A[mid-1] <= X and x < A[mid] ):
            return mid - 1
        elif(X < A[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return -1








def main():
    T = int(input())
    while (T > 0):
        NX = [int(x) for x in input().strip().split()]
        N = NX[0]
        X = NX[1]

        A = [int(x) for x in input().strip().split()]

        print(findFloor(A, N, X))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends