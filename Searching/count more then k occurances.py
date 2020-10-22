
def countOccurence(arr, n, k):
    limit = n//k
    maxi = max(arr)
    l = [0]*(maxi+1)
    c = 0
    for i in range(n):
        l[arr[i]] += 1
    for i in range(maxi+1):
        if(l[i] > limit):
            c += 1
    return c





def main():
    T = int(input())
    while (T > 0):
        N = int(input())

        A = list(map(int, input().split()))

        K = int(input())

        print(countOccurence(A, N, K))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends