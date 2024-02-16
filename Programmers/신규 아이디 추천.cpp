#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string new_id) {
    string answer = "";
    
    int id_size = 0;
    
    string id;
    
    id = new_id;
    
    
    for(int i = 0; i < id.size(); i++)
    {
        if(id[i] >= 'A' && id[i] <= 'Z')
        {
            id[i] = id[i] + 32;
        }
    }
    
    for(int i = 0; i < id.length(); i++)
    {
        if((id[i] < 'a' || id[i] > 'z') && (id[i] < '0' || id[i] > '9') && id[i] != '-' && id[i] != '_' && id[i] != '.')
        {
            cout << id[i] << " ";
            id.erase(id.begin() + i);
            
            i--;
        }
    }
    cout << endl;
    cout << id << endl;
    
    int dot = 0;
    for(int i = 0; i < id.size(); i++)
    {
        if(id[i] == '.')
        {
            dot++;
        }
        else
        {
            dot = 0;
        }
        
        if(dot == 2)
        {
            dot = 1;
            
            id.erase(id.begin() + i);
            
            i--;
        }
    }
    
    if(id[0] == '.')
    {
        id.erase(id.begin() + 0);
    }
    
    if(id[id.length() - 1] == '.')
    {
        id.erase(id.begin() + (id.length() - 1));
    }
    
    if(id.empty() == true)
    {
        id = "a";
    }
    
    if(id.length() >= 16)
    {
        id.erase(id.begin() + 15, id.end());
        
        if(id[id.length() - 1] == '.')
        {
            id.erase(id.begin() + (id.length() - 1));
        }
    }
    
    if(id.length() <= 2)
    {
        while(id.length() != 3)
        {
            id += id[id.length() - 1];
        }
    }
    
    answer = id;
    
    
    return answer;
}