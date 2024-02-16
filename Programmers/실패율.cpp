#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

bool compare(pair<int, float> a, pair<int, float> b)
{
    if(a.second == b.second)
    {
        return a.first < b.first;
    }
    else
    {
        return a.second > b.second;
    }
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    map<int, int> value; // 스테이지 번호, 실패중인 사람 수
    map<int, float> fail;
    
    int userSize = stages.size();
    
    
    for(auto stage : stages)
    {
        if(stage <= N)
            value[stage] += 1;
    }
    
    int notPass = 0;
    for(auto iter : value)
    {
        fail[iter.first] = (float)iter.second / (float)(userSize - notPass);
        
        notPass += iter.second;
    }
    
    for(int i = 1; i <= N; i++)
    {
        if(fail.find(i) == fail.end())
            fail[i] = 0;
    }
    
    
    vector<pair<int, float>> v(fail.begin(), fail.end());
    sort(v.begin(), v.end(), compare);
    
    
    for(auto iter : v)
         answer.push_back(iter.first);
    
    
    return answer;
}