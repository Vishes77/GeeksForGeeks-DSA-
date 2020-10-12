# User function Template for python3
import math
##Complete this function
def maxSubArraySum(a, size):

        # res = a[0]
        # max_ending = a[0]
        # for i in range(1,size):
        #     max_ennding = max(max_ennding+a[i],a[i])
        #     res = max(res,max_ending)
        # return res
    max_so_far = -9999999 - 1
    max_ending_here = 0
    for i in range(0,size):
        max_ending_here =max_ending_here + a[i]

        if(max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here=0
    return max_so_far

def main():
    T = int(input())
    while (T > 0):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        print(maxSubArraySum(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends