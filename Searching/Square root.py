# User function Template for python3

import math
# Complete this function
def floorSqrt(x):
    low = 1
    high = x
    ans = -1
    while(low<=high):
        mid = (low+high)//2
        msq = mid*mid
        if(msq == x):
            return mid
        elif(msq > x):
            high = mid - 1
        else:
            low = mid + 1
            ans = mid
    return ans





def main():
    T = int(input())
    while (T > 0):
        x = int(input())

        print(floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends