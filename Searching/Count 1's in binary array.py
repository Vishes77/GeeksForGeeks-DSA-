# User function Template for python3
import math
##Complete this code
def countOnes(arr, N):
    low = 0
    high = N-1
    while(low <= high):
        # we need to calc the first occurance of 1.
        # then we subtract that index form the array.
        mid = (low+high)//2
        if(arr[mid] == 0):
            high = mid - 1
        elif(mid == N-1 or (arr[mid +1] != arr[mid])):
            return mid+1
        else:
            low = mid + 1
    return 0



def main():
    T = int(input())
    while (T > 0):
        N = int(input())

        A = [int(x) for x in input().strip().split()]

        print(countOnes(A, N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends