#include <bits/stdc++.h>

using namespace std;


int et[10000];


int bfs(int A, int B)
{
    deque<pair<int, int>> bfs_q;
    int visited[10000];

    memset(visited, 0, sizeof(visited));

    bfs_q.push_back(make_pair(A, 0));
    visited[A] = 1;

    while(bfs_q.size())
    {
        auto item = bfs_q.front();
        int number = item.first;
        int cnt = item.second;

        bfs_q.pop_front();

        if(number == B)
            return cnt;
        
        for(int i = 0; i < 4; i++)
        {
            for(int k = 0; k < 10; k++)
            {
                if(i == 0 && k == 0)
                    continue;
                
                string str_number = to_string(number);
                
                if((k + '0') == str_number[i])
                    continue;
                
                str_number[i] = (k + '0');
                
                int temp = stoi(str_number);

                if(visited[temp] == 1)
                    continue;
                
                if(et[temp] == 0)
                    bfs_q.push_back(make_pair(temp, cnt + 1));
                
                visited[temp] = 1;
            }
        }
    }

    return -1;
}


int main(void)
{
    int T;

    cin >> T;

    memset(et, 0, sizeof(et));
    et[1] = 1;

    for(int i = 2; i < 10000; i++)
    {
        if(et[i] == 1)
            continue;
        
        for(int k = i * 2; k < 10000; k += i)
            et[k] = 1;
    }

    for(int i = 0; i < T; i++)
    {
        int A, B, res;

        cin >> A >> B;

        res = bfs(A, B);

        if(res > -1)
            cout << res << endl;
        
        else
            cout << "Impossible" << endl;
    }
}