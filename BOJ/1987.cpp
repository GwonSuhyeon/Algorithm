#include <bits/stdc++.h>


using namespace std;


int R, C;
int res = 0;
int graph[20][20];
int visited[20][20];
vector<int> path;


void dfs(int row, int col)
{
    int direction[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    for(int i = 0; i < 4; i++)
    {
        int new_row = row + direction[i][0];
        int new_col = col + direction[i][1];

        if(0 <= new_row && new_row < R && 0 <= new_col && new_col < C)
        {
            if(find(path.begin(), path.end(), graph[new_row][new_col]) == path.end() && visited[new_row][new_col] == 0)
            {
                visited[new_row][new_col] = 1;
                path.push_back(graph[new_row][new_col]);
                res = max(res, (int)path.size());

                dfs(new_row, new_col);

                visited[new_row][new_col] = 0;
                path.pop_back();
            }
        }
    }
}


int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> R >> C;

    for(int i = 0; i < R; i++)
    {
        string input;

        cin >> input;

        for(int k = 0; k < input.length(); k++)
        {
            graph[i][k] = input[k];
            visited[i][k] = 0;
        }
    }

    path.push_back(graph[0][0]);
    res = (int)path.size();

    dfs(0, 0);

    cout << res;
}