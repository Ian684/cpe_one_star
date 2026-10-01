def main():
    while True:
        n , k = map(int , input().split())
        if n == 0 and k == 0:
            break

        dp = [[0]*(n+1) for _ in range(k)]

        for j in range(n+1):
            dp[0][j] = 1

        for i in range(1 , k):
            dp[i][0] = 1
            for j in range(1 , n+1):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000

        print(dp[k-1][n])

if __name__ == "__main__":
    main()
