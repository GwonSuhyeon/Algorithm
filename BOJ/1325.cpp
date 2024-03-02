#include <bits/stdc++.h>

using namespace std;

vector<int> graph[10001];
int visited[10001];

int bfs(int start)
{
    queue<int> bfs_q;
    int cnt = 0;

    bfs_q.push(start);
    visited[start] = 1;
    cnt += 1;

    while(bfs_q.size())
    {
        int node;
        
        node = bfs_q.front();
        bfs_q.pop();

        for(int i = 0; i < graph[node].size(); i++)
            if(visited[graph[node][i]] == 0)
            {
                bfs_q.push(graph[node][i]);
                visited[graph[node][i]] = 1;
                cnt += 1;
            }
    }

    return cnt;
}

int main(void)
{
    int n, m;
    int max = 0;
    vector<int> res;

    cin >> n >> m;

    for(int i = 1; i <= m; i++)
    {
        int a, b;

        cin >> a >> b;

        graph[b].push_back(a);
    }

    for(int i = 1; i <= n; i++)
    {
        int cnt;

        memset(visited, 0, sizeof(visited));

        cnt = bfs(i);

        res.push_back(cnt);

        if(max < cnt)
            max = cnt;
    }

    for(int i = 0; i < n; i++)
    {
        if(res[i] == max)
            cout << (i + 1) << " ";
    }
}