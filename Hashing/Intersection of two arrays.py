
def NumberofElementsInIntersection(a, b, n, m):
    hs = set()
    c=0

    for i in range(0,n):
        hs.add(a[i])

    for i in range(0,m):
        if b[i] in hs:
            c+=1
            hs.remove(b[i])
    return c


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().strip().split()]

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]

        print(NumberofElementsInIntersection(a, b, n, m))

# } Driver Code Ends