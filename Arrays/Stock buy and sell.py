import math

def stockBuySell(A, n):
    s=""
    if(n ==1):
        return
    sol = [] #create a emplty list.
    i=0 #initial value
    cnt=0
    while(i<n-1):
        #local seach
        while((i<n-1) and (A[i+1] <= A[i])):
            i +=1

        if(i == n-1):
            break

        e=[0,0]
        e[0] = i
        i += 1

        #local maxia
        while((i<n) and (A[i]>=A[i-1])):
            i = i+1
        e[1]=i-1
        sol.append(e[0],e[1])

        cnt = cnt + 1

    if(cnt == 0):
        s="No profit"
    else:
        s=""
        for i in sol:
            s1="("+str(i[0])+" "+str(i[1])+")"
            s = s + s1
            s = s + " "
    print(s)








def main():
    T = int(input())
    while (T > 0):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        stockBuySell(arr, n)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends