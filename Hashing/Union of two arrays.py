
def doUnion(a, n, b, m):

    hs = set()
    for i in range(0,n):
        hs.add(a[i])
    for i in range(0,m):
        hs.add(b[i])

    return len(hs)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().strip().split()]

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]

        print(doUnion(a, n, b, m))
# } Driver Code Ends