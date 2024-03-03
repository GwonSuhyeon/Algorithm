#include <bits/stdc++.h>

using namespace std;

vector<int> graph[10001];
int visited[101][101];

int n, m, k;
int res;

int bfs(int row, int col)
{
    queue<pair<int, int>> bfs_q;
    int region = 0;
    int direction[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    bfs_q.push(pair<int, int>(row, col));
    visited[row][col] = 1;
    region += 1;

    while(!bfs_q.empty())
    {
        int r, c;

        r = bfs_q.front().first;
        c = bfs_q.front().second;
        bfs_q.pop();
        
        for(int i = 0; i < 4; i++)
        {
            int new_row, new_col;
            
            new_row = r + direction[i][0];
            new_col = c + direction[i][1];

            if(new_row >= 1 && new_row <= n && new_col >= 1 && new_col <= m)
            {
                if(graph[new_row][new_col] == 1 && visited[new_row][new_col] == 0)
                {
                    bfs_q.push(pair<int, int>(new_row, new_col));
                    visited[new_row][new_col] = 1;
                    region += 1;
                }
            }
        }
    }

    return region;
}

int main(void)
{
    cin >> n >> m >> k;

    for(int i = 0; i <= n; i++)
    {
        for(int k = 0; k <= m; k++)
            graph[i].push_back(0);
        
        memset(visited[i], 0, sizeof(visited[i]));
    }
    
    for(int i = 0; i < k; i++)
    {
        int r, c;

        cin >> r >> c;

        graph[r][c] = 1;
    }

    for(int i = 1; i <= n; i++)
    {
        for(int k = 1; k <= m; k++)
        {
            if(graph[i][k] == 1 && visited[i][k] == 0)
            {
                int region;

                region = bfs(i, k);

                if(res < region)
                    res = region;
            }
        }
    }

    cout << res;
}