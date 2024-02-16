#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <iostream>

using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer;
    
    map<string, vector<string>> user; // 모든 유저별 vector<이름, vector<신고한 id>>
    map<string, int> reportCnt; // 신고 받은 유저별 신고 누적 횟수
    
    for(auto iter_report : report)
    {
        istringstream iss(iter_report);
        string buf;
        vector<string> tmp;
        
        while(getline(iss, buf, ' '))
            tmp.push_back(buf);
        
        // tmp[0] : 신고를 한 유저 id
        // tmp[1] : 신고를 받은 유저 id
        
        user[tmp[0]].push_back(tmp[1]);
        
        int num = 0;
        for(auto id : user[tmp[0]])
        {
            if(id == tmp[1])
            {
                num++;
            }
            
            if(num >= 2)
            {
                user[tmp[0]].pop_back();
                break;
            }
        }
        
        if(num < 2)
        {
            if(reportCnt.find(tmp[1]) == reportCnt.end())
                reportCnt[tmp[1]] = 1;
            else
                reportCnt[tmp[1]] += 1;
        }
    }
    
//     for(auto iter : reportCnt)
//     {
//         cout << iter.first << " " << iter.second << endl;
//     }
    
//     for(auto iter : user)
//     {
//         for(auto inner : iter.second)
//         {
//             cout << inner << " ";
//         }
//         cout << endl;
//     }
    
    
    for(auto userId : id_list)
    {
        if(user.find(userId) != user.end())
        {
            int cnt = 0;
            for(auto iter : user[userId])
            {
                if(reportCnt[iter] >= k)
                    cnt++;
            }
            answer.push_back(cnt);
        }
        else
        {
            answer.push_back(0);
        }
    }
    
    
    
    
    
    
    return answer;
}