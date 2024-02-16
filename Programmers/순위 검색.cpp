#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>

using namespace std;

typedef enum E_language
{
    E_cpp = 1, //1, //3, //1,
    E_java = 2, //2, //5, //2,
    E_python = 4, //3, //7, //3,
    E_non_language = 0
} E_language;

typedef enum E_career
{
    E_junior = 10, //4, //11, //1,
    E_senior = 20, //5, //13, //2,
    E_non_career = 0
} E_career;

typedef enum E_work
{
    E_backend = 100, //6, //17, //1,
    E_frontend = 200, //7, //19, //2,
    E_non_work = 0
} E_work;

typedef enum E_food
{
    E_chicken = 1000, //8, //23, //1,
    E_pizza = 2000, //9, //29, //2,
    E_non_food = 0
} E_food;

int languageIdx[4] = {1, 2, 4, 0};
int careerIdx[3] = {10, 20, 0};
int workIdx[3] = {100, 200, 0};
int foodIdx[3] = {1000, 2000, 0};

E_language get_language(string data);
E_work get_work(string data);
E_career get_career(string data);
E_food get_food(string data);
int get_score(string data);

vector<int> solution(vector<string> info, vector<string> query) {
    vector<int> answer;
    map<int, map<int, int>> people;
    
    for(int i = 0; i < info.size(); i++)
    {
        int sum;
        
        string buf;
        vector<string> data;
        istringstream iss(info[i]);
        
        while(getline(iss, buf, ' '))
        {
            data.push_back(buf);
        }
        
        int language = get_language(data[0]);
        int work = get_work(data[1]);
        int career = get_career(data[2]);
        int food = get_food(data[3]);
        int score = get_score(data[4]);
        
        sum = language + work + career + food;
        
        people[sum][score] += 1;
    }
    
    for(auto iter = people.begin(); iter != people.end(); iter++)
    {
        int peopleSum = 0;
        
        for(auto iter_inner = iter->second.rbegin(); iter_inner != iter->second.rend(); iter_inner++)
        {
            peopleSum += iter_inner->second;
            
            iter_inner->second = peopleSum;
        }
    }
    
    
    for(int i = 0; i < query.size(); i++)
    {
        string str[5];
        string buf;
        int questionScore = 0;
        
        istringstream iss(query[i]);
        
        int cnt = 0;
        int sum = 0;
        
        int isLanguageNon = 3;
        int isWorkNon = 2;
        int isCareerNon = 2;
        int isFoodNon = 2;
        int isNon = 0;
        
        int idx = 0;
        while(getline(iss, buf, ' '))
        {
            if(buf != "and")
            {
                str[idx] = buf;
                idx++;
            }
        }
        
        if(get_language(str[0]) == E_non_language)
        {
            isNon = 1;
            isLanguageNon = 0;
        }
        else
            sum += get_language(str[0]);
        
        if(get_work(str[1]) == E_non_work)
        {
            isNon = 1;
            isWorkNon = 0;
        }
        else
            sum += get_work(str[1]);
        
        if(get_career(str[2]) == E_non_career)
        {
            isNon = 1;
            isCareerNon = 0;
        }
        else
            sum += get_career(str[2]);
        
        if(get_food(str[3]) == E_non_food)
        {
            isNon = 1;
            isFoodNon = 0;
        }
        else
            sum += get_food(str[3]);
        
        questionScore = stoi(str[4]);
        
        
        if(isLanguageNon + isCareerNon + isWorkNon + isFoodNon == 0)
        {
            for(auto iter = people.begin(); iter != people.end(); iter++)
            {
                cnt += iter->second.lower_bound(questionScore)->second;
            }
        }
        else if(isNon == 1)
        {
            for(int lang = isLanguageNon; lang < 4; lang++)
            {
                for(int work = isWorkNon; work < 3; work++)
                {
                    for(int carr = isCareerNon; carr < 3; carr++)
                    {
                        for(int food = isFoodNon; food < 3; food++)
                        {
                            int s = 0;
                            
                            s = sum + languageIdx[lang] + careerIdx[carr] +
                                workIdx[work] + foodIdx[food];
                            
                            cnt += people[s].lower_bound(questionScore)->second;
                        }
                    }
                }
            }
        }
        else
        {
            cnt += people[sum].lower_bound(questionScore)->second;
        }
        
        answer.push_back(cnt);
    }
    
    return answer;
}


E_language get_language(string data)
{
    if(data == "cpp")
        return E_cpp;
    else if(data == "java")
        return E_java;
    else if(data == "python")
        return E_python;
    
    return E_non_language;
}

E_work get_work(string data)
{
    if(data == "backend")
        return E_backend;
    else if(data == "frontend")
        return E_frontend;
    
    return E_non_work;
}

E_career get_career(string data)
{
    if(data == "junior")
        return E_junior;
    else if(data == "senior")
        return E_senior;
    
    return E_non_career;
}

E_food get_food(string data)
{
    if(data == "chicken")
        return E_chicken;
    else if(data == "pizza")
        return E_pizza;
    
    return E_non_food;
}

int get_score(string data)
{
    return stoi(data);
}

