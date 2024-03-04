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
    // ios_base::sync_with_stdio(0);
    // cin.tie(0);
    // cout.tie(0);

    int N, M, R;

    // cin >> N >> M >> R;
    scanf("%d %d %d", &N, &M, &R);

    memset(res, 0, sizeof(res));

    for(int i = 0; i < M; i++)
    {
        int u, v;

        // cin >> u >> v;
        scanf("%d %d", &u, &v);

        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for(int i = 1; i <= N; i++)
    {
        sort(graph[i].begin(), graph[i].end());
    }

    dfs(R);

    for(int i = 1; i <= N; i++)
    {
        // cout << res[i] << endl;
        printf("%d\n", res[i]);
    }
}