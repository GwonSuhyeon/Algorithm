#include <bits/stdc++.h>

using namespace std;


int res = 0;
int Height, Width;
char graph[50][50];
int visited[50][50];


void bfs(int row, int col)
{
    int direction[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    deque<tuple<pair<int, int>, int>> bfs_q;
    bfs_q.push_back(make_tuple(make_pair(row, col), 0));
    visited[row][col] = 1;

    while(bfs_q.empty() == false)
    {
        int r, c, dist;

        auto temp = bfs_q.front();
        bfs_q.pop_front();

        r = get<0>(temp).first;
        c = get<0>(temp).second;
        dist = get<1>(temp);

        res = max(res, dist);

        for(int i = 0; i < 4; i++)
        {
            int new_row = direction[i][0] + r;
            int new_col = direction[i][1] + c;

            if(0 <= new_row && new_row < Height && 0 <= new_col && new_col < Width)
            {
                if(graph[new_row][new_col] == 'L' && visited[new_row][new_col] == 0)
                {
                    bfs_q.push_back(make_tuple(make_pair(new_row, new_col), dist + 1));
                    visited[new_row][new_col] = 1;
                }
            }
        }
    }
}


int main(void)
{
    cin >> Height >> Width;

    for(int i = 0; i < Height; i++)
    {
        string str;

        cin >> str;

        for(int k = 0; k < Width; k++)
        {
            graph[i][k] = str[k];
        }
    }

    for(int row = 0; row < Height; row++)
    {
        for(int col = 0; col < Width; col++)
        {
            if(graph[row][col] == 'L')
            {
                for(int i = 0; i < Height; i++)
                {
                    for(int k = 0; k < Width; k++)
                    {
                        visited[i][k] = 0;
                    }
                }

                bfs(row, col);
            }
        }
    }

    cout << res;
}