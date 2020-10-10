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
        arr[i] = final[i]  # for this complexity is 3.33 AND O(n) SPACE COMPLEXITY.

    #ALTERNATIVE OF THIS WITH O(1) SPACE COMPLEXITY AND O(N) TIME COMPLEXITY
    # def rearrange(arr, n):
    #
    #     # Initialize index of first minimum
    #     # and first maximum element
    #     max_idx = n - 1
    #     min_idx = 0
    #
    #     # Store maximum element of array
    #     max_elem = arr[n - 1] + 1
    #
    #     # Traverse array elements
    #     for i in range(0, n):
    #
    #         # At even index : we have to put maximum element
    #         if i % 2 == 0:
    #             arr[i] += (arr[max_idx] % max_elem) * max_elem
    #             max_idx -= 1
    #
    #         # At odd index : we have to put minimum element
    #         else:
    #             arr[i] += (arr[min_idx] % max_elem) * max_elem
    #             min_idx += 1
    #
    #     # array elements back to it's original form
    #     for i in range(0, n):
    #         arr[i] = arr[i] // max_elem


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