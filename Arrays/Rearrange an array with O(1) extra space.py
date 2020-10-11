# User function Template for python3

##Complete this code
def arrange(arr, n):
    new = [0]*n
    for i in range(n):
        new[i] = arr[arr[i]]
    for i in range(n):
        arr[i] = new[i]
    return arr        #complexity os o(N) time = 0.03
                      #but space complexity is o(N).

#Alternavtive method with O(1) space and O(N) time complexity.
#complexity os o(N) time = 0.03
    # for i in range(0,n):
    #     arr[i] += (arr[arr[i]]%n)*n
    # for i in range(0,n):
    #     arr[i] = arr[i]//n

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