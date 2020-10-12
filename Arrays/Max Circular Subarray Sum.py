# User function Template for python3
import math
# Complete this function

def circularSubarraySum(arr, n):
    normal_value = normalmaxsum(arr,n)
    if(normal_value < 0 ):
        return normal_value
    arr_sum = 0
    for i in range(n):
        arr_sum += arr[i] # in these two lines we are finding max sum and inverting the array.
        arr[i] = -arr[i]  #inverting the elements so that
    max_circular = arr_sum + normalmaxsum(arr,n) #normamaxsum(arr,n) should give minimum subarray sum.
    return max(max_circular,normal_value)

def normalmaxsum(arr,n):
    res = arr[0]
    maxEnd = arr[0]
    for i in range(1,n):
        maxEnd = max(arr[i],maxEnd+arr[i])
        res = max(maxEnd,res)
    return res
def main():
    T = int(input())
    while (T > 0):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends