# User function Template for python3
import math
##Complete this function
def rearrange(arr, n):
    final = list()
    k = n-1
    for i in range(math.ceil(n/2)):
        if( k == i and i > k):
            break
        final.append(arr[k])
        final.append(arr[i])
        k -= 1
    for i in range(n):
        arr[i] = final[i]  # for this complexity is 3.33




def main():
    T = int(input())
    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        rearrange(arr, n)

        for i in arr:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends