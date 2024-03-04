#include <bits/stdc++.h>

using namespace std;

vector<int> graph[100001];
vector<int> visited(100001, 0);
int res[100001];
int digit = 1;

void dfs(int x)
{
    visited[x] = 1;

    res[x] = digit;

    for(auto i : graph[x])
    {
        if(visited[i] == 0)
        {
            digit += 1;
            dfs(i);
        }
    }
}

int main(void)
{
    int N, M, R;

    scanf("%d %d %d", &N, &M, &R);

    memset(res, 0, sizeof(res));

    for(int i = 0; i < M; i++)
    {
        int u, v;

        scanf("%d %d", &u, &v);

        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for(int i = 1; i <= N; i++)
    {
        sort(graph[i].begin(), graph[i].end(), greater<int>());
    }

    dfs(R);

    for(int i = 1; i <= N; i++)
    {
        printf("%d\n", res[i]);
    }
}