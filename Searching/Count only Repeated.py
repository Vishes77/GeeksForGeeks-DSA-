

def findRepeating(arr, n):
    if(len(arr) == 0):
        return [0,0]
    s=0
    e=len(arr)-1
    while(s<e):
        m = (s+e)//2
        if(arr[m] >= m + arr[0]):
            s = m + 1
        else:
            e=m
    return [arr[s], len(arr) - (arr[len(arr) - 1] - arr[0])]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list((map(int, input().strip().split())))

        ans = findRepeating(arr, n)
        print(ans[0], ans[1])

# } Driver Code Ends