#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<vector<string>> places) {
    
    vector<int> answer;
    
    for(int i = 0; i < 5; i++)
    {
        vector<string> room;
        int res = 1;
        
        room = places[i];
        
        for(int k = 0; k < 5; k++)
        {
            int x;
            int y;
            int windowX;
            int windowY;
            int p_idx = -1;
            
            // while((p_idx = room[k].find("P", p_idx + 1)) != string::npos)
            while(1)
            {
                p_idx = room[k].find("P", p_idx + 1);
                if(p_idx == string::npos)
                {
                    break;
                }

                x = k;
                y = p_idx;

                if((x - 2) >= 0)
                {
                    // 1
                    windowX = x - 2;
                    windowY = y;

                    if(room[windowX][windowY] == 'P')
                    {
                        if(room[windowX + 1][windowY] != 'X')
                        {
                            res = 0;

                            break;
                        }
                    }
                }

                if(x - 1 >= 0)
                {
                    // 2
                    windowX = x - 1;
                    windowY = y;

                    if(room[windowX][windowY] == 'P')
                    {
                        res = 0;

                        break;
                    }
                }

                if(x + 1 <= 4)
                {
                    // 3
                    windowX = x + 1;
                    windowY = y;

                    if(room[windowX][windowY] == 'P')
                    {
                        res = 0;

                        break;
                    }
                }

                if(x + 2 <= 4)
                {
                    // 4
                    windowX = x + 2;
                    windowY = y;

                    if(room[windowX][windowY] == 'P')
                    {
                        if(room[windowX - 1][windowY] != 'X')
                        {
                            res = 0;

                            break;
                        }
                    }
                }

                if(y - 2 >= 0)
                {
                    // 5
                    windowX = x;
                    windowY = y - 2;

                    if(room[windowX][windowY] == 'P')
                    {
                        if(room[windowX][windowY + 1] != 'X')
                        {
                            res = 0;

                            break;
                        }
                    }
                }

                if(y - 1 >= 0)
                {
                    // 6
                    windowX = x;
                    windowY = y - 1;

                    if(room[windowX][windowY] == 'P')
                    {
                        res = 0;

                        break;
                    }
                }

                if(y + 1 <= 4)
                {
                    // 7
                    windowX = x;
                    windowY = y + 1;

                    if(room[windowX][windowY] == 'P')
                    {
                        res = 0;

                        break;
                    }
                }

                if(y + 2 <= 4)
                {
                    // 8
                    windowX = x;
                    windowY = y + 2;

                    if(room[windowX][windowY] == 'P')
                    {
                        if(room[windowX][windowY - 1] != 'X')
                        {
                            res = 0;

                            break;
                        }
                    }
                }

                if(x - 1 >= 0 && y - 1 >= 0)
                {
                    // 9
                    windowX = x - 1;
                    windowY = y - 1;

                    if(room[windowX][windowY] == 'P')
                    {
                        if(room[windowX][windowY + 1] != 'X' || 
                          room[windowX + 1][windowY] != 'X')
                        {
                            res = 0;

                            break;
                        }
                    }
                }

                if(x - 1 >= 0 && y + 1 <= 4)
                {
                    // 10
                    windowX = x - 1;
                    windowY = y + 1;

                    if(room[windowX][windowY] == 'P')
                    {
                        if(room[windowX][windowY - 1] != 'X' || 
                          room[windowX + 1][windowY] != 'X')
                        {
                            res = 0;

                            break;
                        }
                    }
                }

                if(x + 1 <= 4 && y - 1 >= 0)
                {
                    // 11
                    windowX = x + 1;
                    windowY = y - 1;

                    if(room[windowX][windowY] == 'P')
                    {
                        if(room[windowX][windowY + 1] != 'X' || 
                          room[windowX - 1][windowY] != 'X')
                        {
                            res = 0;

                            break;
                        }
                    }
                }

                if(x + 1 <= 4 && y + 1 <= 4)
                {
                    // 12
                    windowX = x + 1;
                    windowY = y + 1;

                    if(room[windowX][windowY] == 'P')
                    {
                        if(room[windowX][windowY - 1] != 'X' || 
                          room[windowX - 1][windowY] != 'X')
                        {
                            res = 0;

                            break;
                        }
                    }
                }
            }
            
            if(res == 0)
            {
                break;
            }
        }
        
        answer.push_back(res);
    }
    
    return answer;
}