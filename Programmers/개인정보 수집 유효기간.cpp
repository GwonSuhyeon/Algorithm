#include <string>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

vector<int> solution(string today, vector<string> terms, vector<string> privacies) {
    // today 는 오늘 날짜
    // terms 는 약관 종류별 개인정보 보관 기간
    // privacies 는 개인정보별 수집된 약관 종류, 날짜
    
    vector<int> answer;
    
    map<string, int> term;
    int todayDate = 0;
    string year;
    string month;
    string day;
    
    
    year = today.substr(0, 4);
    month = today.substr(5, 2);
    day = today.substr(8, 2);
    
    todayDate = ((stoi(year) - 2000) * 12 * 28) + (stoi(month) * 28) + stoi(day);
    
    
    
    for(auto iter : terms)
    {
        string str = iter.substr(0, 1);
        int num = stoi(iter.substr(2));
        
        term[str] = num;
    }
    
    
    int idx = 0;
    for(auto iter : privacies)
    {
        vector<string> tmp;
        istringstream iss(iter);
        string buf;
        int date = 0;
        
        idx++;
        
        while(getline(iss, buf, ' '))
            tmp.push_back(buf);
        
        year = tmp[0].substr(0, 4);
        month = tmp[0].substr(5, 2);
        day = tmp[0].substr(8, 2);
        
        date = ((stoi(year) - 2000) * 12 * 28) + (stoi(month) * 28) + stoi(day);
        
        if((todayDate - date) >= (term[tmp[1]] * 28))
        {
            answer.push_back(idx);
        }
    }
    
    
    return answer;
}