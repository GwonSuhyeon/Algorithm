#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

int score[8] = {0, 3, 2, 1, 0, 1, 2, 3};

string solution(vector<string> survey, vector<int> choices) {
    string answer = "";
    
    map<string, int> value;
    
    
    for(int i = 0; i < survey.size(); i++)
    {
        // iter 는 각 질문마다의 지표 ex. RT
        
        string positive; // 동의
        string negative; // 비동의
        
        string iter_survey = survey[i];
        int choice = choices[i];
        
        negative = iter_survey.substr(0, 1);
        positive = iter_survey.substr(1);
        
        if(choice >= 5)
        {
            // 동의 positive
            
            // if(value.find(positive) == value.end())
            //     value[positive] = score[choice];
            // else
            //     value[positive] += score[choice];
            
            value[positive] += score[choice];
        }
        else if(choice <= 3)
        {
            // 비동의 negative
            
            value[negative] += score[choice];
        }
        else
        {
            ;
        }
    }
    
    
    if(value["R"] > value["T"])
        answer += "R";
    else if(value["T"] > value["R"])
        answer += "T";
    else
    {
        // 점수가 같으면 사전순으로 결정
        
        answer += "R";
    }
    
    if(value["C"] > value["F"])
        answer += "C";
    else if(value["F"] > value["C"])
        answer += "F";
    else
    {
        // 점수가 같으면 사전순으로 결정
        
        answer += "C";
    }
    
    if(value["J"] > value["M"])
        answer += "J";
    else if(value["M"] > value["J"])
        answer += "M";
    else
    {
        // 점수가 같으면 사전순으로 결정
        
        answer += "J";
    }
    
    if(value["A"] > value["N"])
        answer += "A";
    else if(value["N"] > value["A"])
        answer += "N";
    else
    {
        // 점수가 같으면 사전순으로 결정
        
        answer += "A";
    }
    
    
    
    
    return answer;
}