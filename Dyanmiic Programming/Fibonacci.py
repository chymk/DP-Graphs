def fibonacci(n):
    if n<2:
        return n
    for i in range(2,n+1):
        return fibonacci(i-1) + fibonacci(i-2)

#print(fibonacci(40))


def fibonacciDP(n):
    dp = [0,1]
    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])
    return dp[n]

print(fibonacciDP(10))
