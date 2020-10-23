

def firstRepeated(arr, n):
    ans = 9999999999999
    d = dict()

    for i,e in enumerate(arr):
        if e in d:
            if d[e]< ans and ans !=1:
                ans=d[e]
        else:
            d[e] = i

    if ans != 9999999999999:
        return (ans + 1)
    else:
        return (-1)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        print(firstRepeated(arr, n))
# } Driver Code Ends