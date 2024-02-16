#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

typedef struct car
{
    string inTime;
    
    int money = 0;
    int time = 0;
    
    int notOut = 0;
}car;

int convert_time(string in, string out);

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    
    vector<pair<int, car*>> cars;
    
    for(int i = 0; i < records.size(); i++)
    {
        string tmp = records[i];
        string input[3];
        
        input[0] = tmp.substr(0, 5); // 시간
        input[1] = tmp.substr(6, 4); // 차량 번호
        input[2] = tmp.substr(11); // in, out
        
        if(input[2] == "IN")
        {
            int number = stoi(input[1]);
            int isFind = 0;
            int k;
            
            for(k = 0; k < cars.size(); k++)
            {
                if((cars[k].first) == number)
                {
                    isFind = 1;
                    break;
                }
            }
            
            if(isFind == 1)
            {
                cars[k].second->inTime = input[0];
                cars[k].second->notOut = 1;
            }
            else
            {
                car *c = new car();
            
                c->inTime = input[0];
                c->notOut = 1;

                cars.push_back(pair<int, car*>(stoi(input[1]), c));
            }
        }
        else
        {
            int k;
            int number = stoi(input[1]);
            int time;
            
            for(k = 0; k < cars.size(); k++)
            {
                if((cars[k].first) == number)
                    break;
            }
            
            (cars[k].second)->time += convert_time((cars[k].second)->inTime, input[0]);
            (cars[k].second)->notOut = 0;
        }
    }
    
    for(int i = 0; i < cars.size(); i++)
    {
        if((cars[i].second)->notOut == 1)
        {
            (cars[i].second)->time += convert_time((cars[i].second)->inTime, "23:59");
            
        }
        
        else
        {
            cout << (cars[i].second)->inTime << endl;
            cout << (cars[i].second)->time << endl;
        }
    }
    
    for(int i = 0; i < cars.size(); i++)
    {
        int money;
        
        int t = (((cars[i].second)->time - fees[0]) % fees[2]);
        
        if((cars[i].second)->time <= fees[0])
        {
            money = fees[1];
        }
        else if(t > 0)
        {
            money = fees[1] + ((((cars[i].second)->time - fees[0]) / fees[2]) + 1) * fees[3];
        }
        else
        {
            money = fees[1] + ceil((((cars[i].second)->time - fees[0]) / fees[2])) * fees[3];
        }
        
        (cars[i].second)->money = money;
    }
    
    sort(cars.begin(), cars.end());
    
    for(int i = 0; i < cars.size(); i++)
    {
        answer.push_back((cars[i].second)->money);
    }
    
    return answer;
}

int convert_time(string in, string out)
{
    int in_minute;
    int out_minute;
    
    string in_time[2];
    string out_time[2];
    
    in_time[0] = in.substr(0, 2);
    in_time[1] = in.substr(3, 2);
    
    out_time[0] = out.substr(0, 2);
    out_time[1] = out.substr(3, 2);
    
    
    out_minute = stoi(out_time[0]) * 60 + stoi(out_time[1]);
    in_minute = stoi(in_time[0]) * 60 + stoi(in_time[1]);
    
    return out_minute - in_minute;
}