# User function Template for python3

def maxEvenOdd(arr, n):
    res = 1
    curr = 1
    for i in range(1,n):
        if((arr[i]%2 == 0 and arr[i-1]%2 != 0) or
                (arr[i]%2!=0 and arr[i-1]%2 == 0)):
            curr += 1
            res = max(res,curr)
        else:
            curr = 1
    return res

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))

        print(maxEvenOdd(arr, n))
# } Driver Code Ends