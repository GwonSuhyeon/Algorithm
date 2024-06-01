#include <bits/stdc++.h>

using namespace std;


int main(void)
{
    int N;
    int M;
    int a_idx;
    int b_idx;


    cin >> N >> M;


    vector<int> A(N);
    vector<int> B(M);

    
    for(int i = 0; i < N; i++)
    {
        cin >> A[i];
    }

    for(int i = 0; i < M; i++)
    {
        cin >> B[i];
    }

    a_idx = 0;
    b_idx = 0;

    while(a_idx < N && b_idx < M)
    {
        if(A[a_idx] < B[b_idx])
        {
            cout << A[a_idx] << endl;
            a_idx += 1;
        }
        else
        {
            cout << B[b_idx] << endl;
            b_idx += 1;
        }
    }

    while(a_idx < N)
    {
        cout << A[a_idx] << endl;
        a_idx += 1;
    }

    while(b_idx < M)
    {
        cout << B[b_idx] << endl;
        b_idx += 1;
    }


    return 0;
}