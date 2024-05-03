#include <bits/stdc++.h>

using namespace std;


int N;

int et[4000001];
vector<int> prefixSum;


int main(void)
{
    int front = 1;
    int back = 1;
    int res = 0;
    int num = 0;


    cin >> N;

    memset(et, 0, sizeof(et));
    et[1] = 1;

    for(int i = 2; i < 4000001; i++)
    {
        if(et[i] == 1)
        {
            continue;
        }

        for(int k = i * 2; k < 4000001; k += i)
        {
            et[k] = 1;
        }
    }

    prefixSum.push_back(0);

    for(int i = 1; i < 4000001; i++)
    {
        if(et[i] == 0)
        {
            if(prefixSum.size() > 1)
            {
                prefixSum.push_back(prefixSum.back() + i);
            }
            else
            {
                prefixSum.push_back(i);
            }
        }
    }

    while(true)
    {
        if(front > back || back == prefixSum.size())
        {
            break;
        }

        num = prefixSum[back] - prefixSum[front - 1];

        if(num == N)
        {
            front += 1;
            res += 1;
        }
        else if(num > N)
        {
            front += 1;
        }
        else if(num < N)
        {
            back += 1;
        }
    }

    cout << res;
}