#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int discounts[4] = {10, 20, 30, 40};

vector<int> solution(vector<vector<int>> users, vector<int> emoticons) {
    vector<int> answer;
    
    
    int dcMap[7][4] = {0};
    vector<vector<int>> prices;
    
    sort(emoticons.begin(), emoticons.end());
    
    for(int i = 0; i < emoticons.size(); i++)
    {
        for(int k = 0; k < 4; k++)
        {
            dcMap[i][k] = ((emoticons[i] * (100 - discounts[k])) / 100);
        }
    }
    
    
    for(int a = 0; a < 4; a++)
    {
        for(int b = 0; b < 4; b++)
        {   
            for(int c = 0; c < 4; c++)
            {
                for(int d = 0; d < 4; d++)
                {
                    for(int e = 0; e < 4; e++)
                    {
                        for(int f = 0; f < 4; f++)
                        {
                            for(int g = 0; g < 4; g++)
                            {
                                vector<int> v;

                                v.push_back(g);
                                v.push_back(f);
                                v.push_back(e);
                                v.push_back(d);
                                v.push_back(c);
                                v.push_back(b);
                                v.push_back(a);

                                prices.push_back(v);
                            }
                        }
                    }
                }
            }
        }
    }
    
    
    int plus = 0;
    int money = 0;
    
    for(int p = 0; p < pow(4, emoticons.size()); p++) // 실행 시간 빠름
    // for(auto iter_price : prices) // 실행 시간 느림
    {
        int plus_cnt = 0;
        int money_cnt = 0;
        
        for(auto iter_user : users)
        {
            int dc = iter_user[0];
            int maxPrice = iter_user[1];
            
            int sum = 0;
            int maxCheck = 0;
            
            for(int i = 0; i < emoticons.size(); i++)
            {
                if(discounts[prices[p][i]] >= dc) // 실행 시간 빠름
                // if(discounts[iter_price[i]] >= dc) // 실행 시간 느림
                {
                    sum += dcMap[i][prices[p][i]]; // 실행 시간 빠름
                    // sum += dcMap[i][iter_price[i]]; // 실행 시간 느림
                    
                    if(sum >= maxPrice)
                    {
                        maxCheck = 1;
                        //plus_cnt++;
                        break;
                    }
                }
            }
            
            if(maxCheck == 0)
                money_cnt += sum;
        }
        
        if(plus_cnt > plus)
        {
            plus = plus_cnt;
            money = money_cnt;
        }
        else if((plus_cnt == plus) && (money_cnt > money))
        {
            money = money_cnt;
        }
    }
    
    
    answer.push_back(plus);
    answer.push_back(money);
    
    
    return answer;
}