import math

def leftIndex(arr, N, X):
    #First Occurance concept.
    low = 0
    high = N-1
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid] > X):
            high = mid - 1
        elif(arr[mid] < X):
            low = mid + 1
        else:
            if(mid == 0 or arr[mid-1]!= arr[mid]):
                return mid
            else:
                high = mid - 1
    return -1







def main():
    T = int(input())
    while (T > 0):
        N = int(input())

        A = [int(x) for x in input().strip().split()]

        x = int(input())

        print(leftIndex(A, N, x))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends