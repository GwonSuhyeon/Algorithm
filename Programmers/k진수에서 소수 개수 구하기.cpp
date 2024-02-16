#include <string>
#include <vector>
#include <iostream>
#include <cmath>
#include <sstream>

using namespace std;

int solution(int n, int k) {
    int answer = -1;
    
    vector<int> value;
    vector<int> temp;
    
    string str;
    vector<string> splitString;
    
    
    int div = n;
    while(1)
    {
        if(div < k)
        {
            temp.push_back(div);
            break;
        }
        
        temp.push_back(div % k);
        
        div = div / k;
    }
    
    for(auto i = temp.rbegin(); i != temp.rend(); i++)
        value.push_back(*i);
    
    for(auto i : value)
        str += to_string(i);
    
    
    istringstream iss(str);
    string buf;
    
    while(getline(iss, buf, '0'))
    {
        splitString.push_back(buf);
    }
    
    if(splitString.empty() == true)
        splitString.push_back(str);
    
    
    int prime = 0;
    int cnt = 0;
    
    for(auto tmp : splitString)
    {
        long long p = 0;
        int idx = 0;
        
        for(int i = tmp.length() - 1; i >= 0; i--)
        {
            p += pow(10, i) * (tmp[idx] - '0');
            idx++;
        }
        
        prime = 1;
        
        if(p <= 1)
        {
            prime = 0;
        }
        else if(p == 2)
        {
            prime = 1;
        }
        else
        {
            for(int i = 2; i <= sqrt(p); i++)
            {
                if((p % i) == 0)
                {
                    prime = 0;
                    break;
                }
            }
        }
        
        if(prime == 1)
            cnt++;
    }
    
    answer = cnt;
    
    
    return answer;
}