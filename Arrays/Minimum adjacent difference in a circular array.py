# User function Template for python3

# Complete this function
def minAdjDiff(arr, n):
    temp = abs(arr[n-1]-arr[0])
    for i in range(1,n):
        if(abs(arr[i]-arr[i-1]) < temp):
            temp = abs(arr[i]-arr[i-1])
    return temp



def main():
    T = int(input())
    while (T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]

        print(minAdjDiff(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends