#include <string>
#include <vector>

using namespace std;

int solution(vector<int> queue1, vector<int> queue2) {
    int answer = -2;
    
    long mid = 0;
    long q1Total = 0;
    long q2Total = 0;
    int qSize = queue1.size();
    
    
    for(int i = 0; i < qSize; i++)
    {
        q1Total += queue1[i];
        q2Total += queue2[i];
    }
    
    if(((q2Total + q2Total) % 2) != 0)
        return -1;
    
    mid = (q1Total + q2Total) / 2;
    
    int cnt = 0;
    int q1Idx = 0;
    int q2Idx = 0;
    // int isQ1Zero = 0;
    // int isQ2Zero = 0;
    int isQ1End = 0;
    int isQ2End = 0;
    while(1)
    {
        if(q1Total > q2Total)
        {
            int tmp = queue1[q1Idx];
            
            queue2.push_back(tmp);
            
            q1Total -= (long)tmp;
            q2Total += (long)tmp;
            
            q1Idx++;
            cnt++;
        }
        else if(q1Total < q2Total)
        {
            int tmp = queue2[q2Idx];
            
            queue1.push_back(tmp);
            
            q2Total -= (long)tmp;
            q1Total += (long)tmp;
            
            q2Idx++;
            cnt++;
        }
        else
        {
            break;
        }
        
        if(q1Idx >= qSize)
            isQ1End = 1;
        
        if(q2Idx >= qSize)
            isQ2End = 1;
        
        if((isQ1End == 1) && (isQ2End == 1))
            return -1;
        
        
//         if(q1Total == 0)
//             isQ1Zero = 1;
//             // return -1;
        
//         if(q2Total == 0)
//             isQ2Zero = 1;
//             // return -1;
        
//         if((isQ1Zero == 1) && (isQ2Zero == 1))
//             return -1;
    }
    
    answer = cnt;
    
    
    return answer;
}