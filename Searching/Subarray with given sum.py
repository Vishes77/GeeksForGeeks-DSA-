# User function Template for python3

# Complete this function
def subArraySum(arr, n, sum):
    # Initialize curr_sum as
    # value of first element
    # and starting point as 0
    curr_sum = arr[0]
    start = 0

    # Add elements one by
    # one to curr_sum and
    # if the curr_sum exceeds
    # the sum, then remove
    # starting element
    i = 1
    while i <= n:

        # If curr_sum exceeds
        # the sum, then remove
        # the starting elements
        while curr_sum > sum and start < i - 1:
            curr_sum = curr_sum - arr[start]
            start += 1

        # If curr_sum becomes
        # equal to sum, then
        # return true
        if curr_sum == sum:
            print("%d %d" % (start + 1, i), end=" ")
            return 1

        # Add this element
        # to curr_sum
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1

    # If we reach here,
    # then no subarray
    print("-1", end=" ")


def main():
    T = int(input())
    while (T > 0):
        NS = input().strip().split()
        N = int(NS[0])
        S = int(NS[1])

        A = list(map(int, input().split()))

        subArraySum(A, N, S)

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends