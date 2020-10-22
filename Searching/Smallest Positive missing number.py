

def missingNumber(arr, n):
    m = max(arr)
    if ( m < 1):
        return  1
    if(n==1):
        return 2 if arr[0] == 1 else 1

    l = [0]*m
    for i in range(n):
        if(arr[i]>0):
            if(l[arr[i]-1] != 1):
                l[arr[i] - 1] = 1
    for i in range(len(l)):
        if(l[i] == 0):
            return i+1
    return i+2

def main():
    T = int(input())
    while (T > 0):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        print(missingNumber(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends