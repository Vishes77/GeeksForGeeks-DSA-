# Complete this function
import math
def trappingWater(arr, n):
    res = 0
    lmax = [0]*n
    rmax = [0]*n
    lmax[0] = arr[0]
    rmax[n-1] = arr[n-1]
    for i in range(1,n):
        lmax[i]=max(arr[i],lmax[i-1])
    for i in range(n-2,-1,-1):
        rmax[i]=max(arr[i],rmax[i+1])
    for i in range(n):
        res = res + (min(lmax[i],rmax[i])-arr[i])
    return res



def main():
    T = int(input())
    while (T > 0):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        print(trappingWater(arr, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends