#include <bits/stdc++.h>

using namespace std;

int N;

void dfs(int start, int length)
{
    if(length == N)
    {
        cout << start << endl;
        return;
    }

    for(int i = 1; i < 10; i++)
    {
        int isPrime = 0;
        int value = (10 * start) + i;

        for(int k = 2; k < (value - 1); k++)
        {
            if(value % k == 0)
            {
                isPrime = 1;
                break;
            }
        }

        if(isPrime == 0)
        {
            dfs(value, length + 1);
        }
    }
}


int main(void)
{
    int prime[4] = {2, 3, 5, 7};

    cin >> N;

    for(int i = 0; i < 4; i++)
    {
        dfs(prime[i], 1);
    }
}