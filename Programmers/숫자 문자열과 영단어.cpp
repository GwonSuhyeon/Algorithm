#include <string>
#include <vector>
#include <map>
#include <iostream>

#include <regex>

using namespace std;

int solution(string s) {
    int answer = 0;
    
    string text;
    vector<pair<int, string>> numbers;
    map<int, int> value;
    
    
    // 정규식으로 해결 가능함
    // 하지만 실행 시간이 조금 느려짐.
    
//     text = s;
    
//     text = regex_replace(text, regex("zero"), "0");
//     text = regex_replace(text, regex("one"), "1");
//     text = regex_replace(text, regex("two"), "2");
//     text = regex_replace(text, regex("three"), "3");
//     text = regex_replace(text, regex("four"), "4");
//     text = regex_replace(text, regex("five"), "5");
//     text = regex_replace(text, regex("six"), "6");
//     text = regex_replace(text, regex("seven"), "7");
//     text = regex_replace(text, regex("eight"), "8");
//     text = regex_replace(text, regex("nine"), "9");
    
    
    
    numbers.push_back(make_pair(0, "zero"));
    numbers.push_back(make_pair(1, "one"));
    numbers.push_back(make_pair(2, "two"));
    numbers.push_back(make_pair(3, "three"));
    numbers.push_back(make_pair(4, "four"));
    numbers.push_back(make_pair(5, "five"));
    numbers.push_back(make_pair(6, "six"));
    numbers.push_back(make_pair(7, "seven"));
    numbers.push_back(make_pair(8, "eight"));
    numbers.push_back(make_pair(9, "nine"));
    

    string temp = s;
    
    
    for(int i = 0; i < s.length(); i++)
    {
        if(s[i] < '0' || s[i] >'9')
        {
            temp = &s[i];
            int idx = 0;
            if((idx = temp.find(numbers[0].second)) == 0)
            {
                text += "0";
                i += numbers[0].second.length() - 1;
                continue;
            }
            
            if((idx = temp.find(numbers[1].second)) == 0)
            {
                text += "1";
                i += numbers[1].second.length() - 1;
                continue;
            }
            
            if((idx = temp.find(numbers[2].second)) == 0)
            {
                text += "2";
                i += numbers[2].second.length() - 1;
                continue;
            }
            
            if((idx = temp.find(numbers[3].second)) == 0)
            {
                text += "3";
                i += numbers[3].second.length() - 1;
                continue;
            }
            
            if((idx = temp.find(numbers[4].second)) == 0)
            {
                text += "4";
                i += numbers[4].second.length() - 1;
                continue;
            }
            
            if((idx = temp.find(numbers[5].second)) == 0)
            {
                text += "5";
                i += numbers[5].second.length() - 1;
                continue;
            }
            
            if((idx = temp.find(numbers[6].second)) == 0)
            {
                text += "6";
                i += numbers[6].second.length() - 1;
                continue;
            }
            
            if((idx = temp.find(numbers[7].second)) == 0)
            {
                text += "7";
                i += numbers[7].second.length() - 1;
                continue;
            }
            
            if((idx = temp.find(numbers[8].second)) == 0)
            {
                text += "8";
                i += numbers[8].second.length() - 1;
                continue;
            }
            
            if((idx = temp.find(numbers[9].second)) == 0)
            {
                text += "9";
                i += numbers[9].second.length() - 1;
                continue;
            }
        }
        else
        {
            text += s[i];
        }
    }
    
    
    
    answer = stoi(text);
    
    
    return answer;
}