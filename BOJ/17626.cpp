#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int n;
    vector<int> dp;
    
    cin >> n;

    for(int i = 0; i <= n; i++)
    {
        dp.push_back(0);
    }

    for(int i = 1; i <= n; i++)
    {
        dp[i] = dp[i - 1] + 1;

        for(int j = 1; j <= (int)sqrt(i); j++)
        {
            dp[i] = min(dp[i], dp[i - pow(j, 2)] + 1);
        }
    }

    cout << dp[n];
}



// python은 실행시간 0.5초 초과

// import math

// n = int(input())

// dp = [0 for _ in range(n + 1)]

// for i in range(1, n + 1):
//     dp[i] = dp[i - 1] + 1
    
//     for j in range(1, int(math.sqrt(i)) + 1):
//         dp[i] = min(dp[i], dp[i - (j**2)] + 1)

// print(dp[n])