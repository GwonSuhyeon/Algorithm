#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> graph;
vector<int> visited;

void dfs(int x)
{
    visited[x] = 1;

    for(int i = 0; i < graph[x].size(); i++)
    {
        if(visited[graph[x][i]] == 0)
        {
            dfs(graph[x][i]);
        }
    }
}
int main(void)
{
    int n, m;
    int cnt = 0;

    cin >> n >> m;

    for(int i = 0; i <= n; i++)
    {
        vector<int> v;

        graph.push_back(v);
        visited.push_back(0);
    }

    for(int i = 0; i < m; i++)
    {
        int a, b;

        cin >> a >> b;

        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for(int i = 1; i <= n; i++)
    {
        if(visited[i] == 0)
        {
            dfs(i);
            cnt += 1;
        }
    }

    cout << cnt;
}



// python 코드는 제출 시 시간초과

// import sys

// sys.setrecursionlimit(10000000)

// def dfs(x):
//     visited[x] = 1
    
//     for i in grape[x]:
//         if visited[i] == 0:
//             dfs(i)
    
// n, m = map(int, input().split())

// grape = [[] for _ in range(n + 1)]
// visited = [0 for _ in range(n + 1)]

// cnt = 0

// for _ in range(m):
//     a, b = map(int, input().split())
    
//     grape[a].append(b)
//     grape[b].append(a)

// for i in range(1, n + 1):
//     if visited[i] == 0:
//         dfs(i)
//         cnt += 1

// print(cnt)