#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'staircase' function below.
 *
 * The function accepts INTEGER n as parameter.
 */

void staircase(int n) {
    
    for(int i = 0; i < n; i++)
    {
        for(int k = 0; k < (n - i - 1); k++)
        {
            printf(" ");
        }
        
        for(int k = (n - i - 1); k < n; k++)
        {
            printf("#");
        }
        
        printf("\n");
    }
}