#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

int hourglassSum(vector<vector<int>> arr)
{
    int max = 0;
    int sum = 0;
    int isZero = 0;
    
    for(int i = 0; i < 4; i++)
    {
        for(int k = 0; k < 4; k++)
        {
            sum = 0;
            
            sum = arr[i][k] + arr[i][k + 1] + arr[i][k + 2] + 
            arr[i + 1][k + 1] + 
            arr[i + 2][k] + arr[i + 2][k + 1] + arr[i + 2][k + 2];
            
            if(sum == 0)
                isZero = 1;
            
            if((sum < 0) && (max < 0))
            {
                if((sum - max) > 0)
                {
                    max = sum;
                }
                else
                {
                    ;
                }
            }
            else
            {
                if(sum > max)
                {
                    max = sum;
                }
                else if((max == 0) && (sum < 0) && (isZero == 0))
                {
                    max = sum;
                }
                else if(sum == max)
                {
                    max = sum;
                }
            }
        }
    }
    
    return max;
}