#include <bits/stdc++.h>

using namespace std;

int N = 0;
int res = 0;
vector<int> chess;

void back_tracking()
{
    if(chess.size() == N)
    {
        res += 1;

        return;
    }
    
    for(int col = 0; col < N; col++)
    {
        int row = chess.size();

        if(chess.size() == 0)
        {
            chess.push_back(col);

            back_tracking();

            chess.pop_back();
        }
        else
        {
            int check = 1;

            for(int r = 0; r < chess.size(); r++)
            {
                int c = chess[r];

                if(abs(c - col) == abs(r - row) || c == col)
                {
                    check = 0;

                    break;
                }
            }

            if(check == 1)
            {
                chess.push_back(col);

                back_tracking();

                chess.pop_back();
            }
        }
    }
}


int main(void)
{
    cin >> N;

    back_tracking();

    cout << res;
}